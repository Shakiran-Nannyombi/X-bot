class XGrowthBot {
    constructor() {
      this.savedPosts = JSON.parse(localStorage.getItem("savedPosts") || "[]")
      this.notificationSettings = JSON.parse(localStorage.getItem("notificationSettings") || "{}")
      this.notificationPermission = false
      this.scheduledNotifications = []
  
      this.init()
    }
  
    init() {
      this.setupEventListeners()
      this.loadSavedPosts()
      this.setupTabs()
      this.checkNotificationPermission()
      this.loadNotificationSettings()
      this.scheduleNotifications()
    }
  
    setupEventListeners() {
      // Generator events
      document.getElementById("generate-btn").addEventListener("click", () => this.generateContent())
      document.getElementById("copy-btn")?.addEventListener("click", () => this.copyToClipboard())
      document.getElementById("save-btn")?.addEventListener("click", () => this.savePost())
      document.getElementById("regenerate-btn")?.addEventListener("click", () => this.generateContent())
  
      // Scheduler events
      document
        .getElementById("enable-notifications")
        ?.addEventListener("click", () => this.requestNotificationPermission())
      document.getElementById("save-schedule")?.addEventListener("click", () => this.saveNotificationSettings())
  
      // Saved posts events
      document.getElementById("clear-saved")?.addEventListener("click", () => this.clearSavedPosts())
    }
  
    setupTabs() {
      const tabs = document.querySelectorAll(".tab-button")
      const contents = document.querySelectorAll(".tab-content")
  
      tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
          // Remove active class from all tabs and contents
          tabs.forEach((t) => t.classList.remove("active"))
          contents.forEach((c) => c.classList.add("hidden"))
  
          // Add active class to clicked tab
          tab.classList.add("active")
  
          // Show corresponding content
          const tabId = tab.id.replace("-tab", "-content")
          const content = document.getElementById(tabId)
          if (content) {
            content.classList.remove("hidden")
          }
  
          // Update analytics when analytics tab is clicked
          if (tabId === "analytics-content") {
            this.updateAnalytics()
          }
        })
      })
    }
  
    async generateContent() {
      const contentType = document.getElementById("content-type").value
      const topic = document.getElementById("topic").value
      const generateBtn = document.getElementById("generate-btn")
  
      generateBtn.textContent = "Generating..."
      generateBtn.disabled = true
  
      try {
        const response = await fetch("/generate", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ type: contentType, topic: topic }),
        })
  
        const data = await response.json()
  
        if (data.error) {
          throw new Error(data.error)
        }
  
        this.displayContent(data.content, data.length)
      } catch (error) {
        console.error("Error generating content:", error)
        alert("Error generating content. Please try again.")
      } finally {
        generateBtn.textContent = "Generate Content 🎯"
        generateBtn.disabled = false
      }
    }
  
    displayContent(content, length) {
      const generatedText = document.getElementById("generated-text")
      const charCount = document.getElementById("char-count")
      const contentOutput = document.getElementById("content-output")
  
      if (generatedText) generatedText.textContent = content
      if (charCount) {
        charCount.textContent = `${length}/280 characters`
  
        if (length > 280) {
          charCount.classList.add("text-red-500")
          charCount.classList.remove("text-gray-500")
        } else {
          charCount.classList.add("text-gray-500")
          charCount.classList.remove("text-red-500")
        }
      }
  
      if (contentOutput) contentOutput.classList.remove("hidden")
    }
  
    async copyToClipboard() {
      const text = document.getElementById("generated-text")?.textContent
      if (!text) return
  
      try {
        await navigator.clipboard.writeText(text)
        const btn = document.getElementById("copy-btn")
        if (btn) {
          const originalText = btn.textContent
          btn.textContent = "✅ Copied!"
          setTimeout(() => {
            btn.textContent = originalText
          }, 2000)
        }
      } catch (error) {
        console.error("Failed to copy:", error)
      }
    }
  
    savePost() {
      const content = document.getElementById("generated-text")?.textContent
      if (!content) return
  
      const contentType = document.getElementById("content-type").value
      const topic = document.getElementById("topic").value
  
      const post = {
        id: Date.now(),
        content: content,
        type: contentType,
        topic: topic,
        timestamp: new Date().toISOString(),
        used: false,
      }
  
      this.savedPosts.unshift(post)
      localStorage.setItem("savedPosts", JSON.stringify(this.savedPosts))
      this.loadSavedPosts()
  
      // Update analytics if on analytics tab
      const analyticsContent = document.getElementById("analytics-content")
      if (analyticsContent && !analyticsContent.classList.contains("hidden")) {
        this.updateAnalytics()
      }
  
      const btn = document.getElementById("save-btn")
      if (btn) {
        const originalText = btn.textContent
        btn.textContent = "✅ Saved!"
        setTimeout(() => {
          btn.textContent = originalText
        }, 2000)
      }
    }
  
    loadSavedPosts() {
      const container = document.getElementById("saved-posts")
      if (!container) return
  
      if (this.savedPosts.length === 0) {
        container.innerHTML =
          '<p class="text-gray-500 text-center py-8">No saved posts yet. Generate and save some content!</p>'
        return
      }
  
      container.innerHTML = this.savedPosts
        .map(
          (post) => `
              <div class="border rounded-lg p-4 ${post.used ? "bg-gray-50" : "bg-white"}">
                  <div class="flex justify-between items-start mb-2">
                      <div class="flex items-center gap-2">
                          <span class="text-xs px-2 py-1 rounded-full bg-blue-100 text-blue-800">${post.type}</span>
                          ${post.topic ? `<span class="text-xs px-2 py-1 rounded-full bg-green-100 text-green-800">${post.topic}</span>` : ""}
                          ${post.used ? '<span class="text-xs px-2 py-1 rounded-full bg-gray-100 text-gray-600">Used</span>' : ""}
                      </div>
                      <div class="flex gap-2">
                          <button onclick="bot.copyPost('${post.content.replace(/'/g, "\\'")}'))" class="text-blue-600 hover:text-blue-700 text-sm">Copy</button>
                          <button onclick="bot.toggleUsed(${post.id})" class="text-green-600 hover:text-green-700 text-sm">
                              ${post.used ? "Mark Unused" : "Mark Used"}
                          </button>
                          <button onclick="bot.deletePost(${post.id})" class="text-red-600 hover:text-red-700 text-sm">Delete</button>
                      </div>
                  </div>
                  <p class="text-gray-800 whitespace-pre-wrap text-sm">${post.content}</p>
                  <p class="text-xs text-gray-500 mt-2">${new Date(post.timestamp).toLocaleString()}</p>
              </div>
          `,
        )
        .join("")
    }
  
    async copyPost(content) {
      try {
        await navigator.clipboard.writeText(content)
        this.showNotification("✅ Post copied to clipboard!", "success")
      } catch (error) {
        console.error("Failed to copy:", error)
      }
    }
  
    toggleUsed(postId) {
      const post = this.savedPosts.find((p) => p.id === postId)
      if (post) {
        post.used = !post.used
        localStorage.setItem("savedPosts", JSON.stringify(this.savedPosts))
        this.loadSavedPosts()
  
        // Update analytics if on analytics tab
        const analyticsContent = document.getElementById("analytics-content")
        if (analyticsContent && !analyticsContent.classList.contains("hidden")) {
          this.updateAnalytics()
        }
      }
    }
  
    deletePost(postId) {
      if (confirm("Are you sure you want to delete this post?")) {
        this.savedPosts = this.savedPosts.filter((p) => p.id !== postId)
        localStorage.setItem("savedPosts", JSON.stringify(this.savedPosts))
        this.loadSavedPosts()
      }
    }
  
    clearSavedPosts() {
      if (confirm("Are you sure you want to clear all saved posts?")) {
        this.savedPosts = []
        localStorage.setItem("savedPosts", JSON.stringify(this.savedPosts))
        this.loadSavedPosts()
      }
    }
  
    // Notification System
    async requestNotificationPermission() {
      if (!("Notification" in window)) {
        alert("This browser does not support notifications")
        return
      }
  
      const permission = await Notification.requestPermission()
      this.notificationPermission = permission === "granted"
  
      if (this.notificationPermission) {
        this.showNotificationStatus("✅ Notifications enabled! You'll get reminders at optimal posting times.", "success")
        this.scheduleNotifications()
      } else {
        this.showNotificationStatus("❌ Notifications denied. Enable them in browser settings for reminders.", "error")
      }
    }
  
    checkNotificationPermission() {
      if ("Notification" in window) {
        this.notificationPermission = Notification.permission === "granted"
        if (this.notificationPermission) {
          this.showNotificationStatus("🔔 Notifications are enabled", "success")
        }
      }
    }
  
    showNotificationStatus(message, type) {
      const statusDiv = document.getElementById("notification-status")
      const iconSpan = document.getElementById("notification-icon")
      const textSpan = document.getElementById("notification-text")
  
      if (statusDiv && iconSpan && textSpan) {
        statusDiv.className = `mb-6 p-4 rounded-lg border ${type === "success" ? "bg-green-50 border-green-200" : "bg-red-50 border-red-200"}`
        iconSpan.textContent = type === "success" ? "✅" : "❌"
        textSpan.textContent = message
        statusDiv.classList.remove("hidden")
  
        setTimeout(() => {
          statusDiv.classList.add("hidden")
        }, 5000)
      }
    }
  
    saveNotificationSettings() {
      const settings = {
        morning: {
          enabled: document.getElementById("morning-enabled")?.checked || false,
          time: document.getElementById("morning-time")?.value || "09:00",
        },
        afternoon: {
          enabled: document.getElementById("afternoon-enabled")?.checked || false,
          time: document.getElementById("afternoon-time")?.value || "13:30",
        },
        evening: {
          enabled: document.getElementById("evening-enabled")?.checked || false,
          time: document.getElementById("evening-time")?.value || "20:00",
        },
      }
  
      this.notificationSettings = settings
      localStorage.setItem("notificationSettings", JSON.stringify(settings))
  
      this.scheduleNotifications()
      this.showNotification("✅ Notification settings saved!", "success")
    }
  
    loadNotificationSettings() {
      if (Object.keys(this.notificationSettings).length === 0) {
        // Set default settings
        this.notificationSettings = {
          morning: { enabled: true, time: "09:00" },
          afternoon: { enabled: true, time: "13:30" },
          evening: { enabled: true, time: "20:00" },
        }
      }
  
      // Load settings into form
      const morningEnabled = document.getElementById("morning-enabled")
      const morningTime = document.getElementById("morning-time")
      const afternoonEnabled = document.getElementById("afternoon-enabled")
      const afternoonTime = document.getElementById("afternoon-time")
      const eveningEnabled = document.getElementById("evening-enabled")
      const eveningTime = document.getElementById("evening-time")
  
      if (morningEnabled) morningEnabled.checked = this.notificationSettings.morning?.enabled ?? true
      if (morningTime) morningTime.value = this.notificationSettings.morning?.time ?? "09:00"
      if (afternoonEnabled) afternoonEnabled.checked = this.notificationSettings.afternoon?.enabled ?? true
      if (afternoonTime) afternoonTime.value = this.notificationSettings.afternoon?.time ?? "13:30"
      if (eveningEnabled) eveningEnabled.checked = this.notificationSettings.evening?.enabled ?? true
      if (eveningTime) eveningTime.value = this.notificationSettings.evening?.time ?? "20:00"
    }
  
    scheduleNotifications() {
      if (!this.notificationPermission) return
  
      // Clear existing timeouts
      this.scheduledNotifications.forEach((timeout) => clearTimeout(timeout))
      this.scheduledNotifications = []
  
      const now = new Date()
      const times = ["morning", "afternoon", "evening"]
      const nextNotifications = []
  
      times.forEach((period) => {
        const setting = this.notificationSettings[period]
        if (!setting?.enabled) return
  
        const [hours, minutes] = setting.time.split(":").map(Number)
        const notificationTime = new Date()
        notificationTime.setHours(hours, minutes, 0, 0)
  
        // If time has passed today, schedule for tomorrow
        if (notificationTime <= now) {
          notificationTime.setDate(notificationTime.getDate() + 1)
        }
  
        const timeUntilNotification = notificationTime.getTime() - now.getTime()
  
        const timeout = setTimeout(() => {
          this.showPostingNotification(period)
          // Reschedule for next day
          this.scheduleNotifications()
        }, timeUntilNotification)
  
        this.scheduledNotifications.push(timeout)
        nextNotifications.push({
          period: period,
          time: notificationTime.toLocaleString(),
        })
      })
  
      this.displayNextNotifications(nextNotifications)
    }
  
    displayNextNotifications(notifications) {
      const container = document.getElementById("next-notifications")
      const list = document.getElementById("notification-list")
  
      if (!container || !list) return
  
      if (notifications.length === 0) {
        container.classList.add("hidden")
        return
      }
  
      container.classList.remove("hidden")
      list.innerHTML = notifications
        .map(
          (notif) => `
              <div class="flex items-center justify-between p-2 bg-white rounded border">
                  <span class="text-sm">
                      ${notif.period.charAt(0).toUpperCase() + notif.period.slice(1)} posting reminder
                  </span>
                  <span class="text-xs text-gray-500">${notif.time}</span>
              </div>
          `,
        )
        .join("")
    }
  
    showPostingNotification(period) {
      const messages = {
        morning: "🌅 Good morning! Time to post your morning content and catch the early birds!",
        afternoon: "☀️ Afternoon posting time! Your audience is taking their lunch break.",
        evening: "🌆 Evening peak time! Perfect moment to engage with your community.",
      }
  
      if (this.notificationPermission) {
        new Notification("X Growth Bot - Time to Post! 🚀", {
          body: messages[period],
          tag: "posting-reminder",
          requireInteraction: true,
        })
      }
  
      // Also show in-app notification
      this.showNotification(messages[period], "info")
    }
  
    showNotification(message, type) {
      // Create a temporary notification element
      const notification = document.createElement("div")
      notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
        type === "success"
          ? "bg-green-500 text-white"
          : type === "error"
            ? "bg-red-500 text-white"
            : "bg-blue-500 text-white"
      }`
      notification.textContent = message
  
      document.body.appendChild(notification)
  
      setTimeout(() => {
        notification.remove()
      }, 5000)
    }
  
    updateAnalytics() {
      const contentTypes = {}
      const totalGenerated = this.savedPosts.length
      const postsUsed = this.savedPosts.filter((post) => post.used).length
  
      // Count content types
      this.savedPosts.forEach((post) => {
        contentTypes[post.type] = (contentTypes[post.type] || 0) + 1
      })
  
      // Update stats
      const totalGeneratedEl = document.getElementById("total-generated")
      const postsUsedEl = document.getElementById("posts-used")
      const successRateEl = document.getElementById("success-rate")
  
      if (totalGeneratedEl) totalGeneratedEl.textContent = totalGenerated
      if (postsUsedEl) postsUsedEl.textContent = postsUsed
      if (successRateEl) {
        successRateEl.textContent = totalGenerated > 0 ? Math.round((postsUsed / totalGenerated) * 100) + "%" : "0%"
      }
  
      // Update content distribution
      const distributionContainer = document.getElementById("content-distribution")
      if (distributionContainer) {
        distributionContainer.innerHTML = Object.entries(contentTypes)
          .sort(([, a], [, b]) => b - a)
          .map(
            ([type, count]) => `
            <div class="flex justify-between items-center p-2 bg-gray-50 rounded">
              <span class="capitalize">${type}</span>
              <div class="flex items-center">
                <div class="w-20 bg-gray-200 rounded-full h-2 mr-2">
                  <div class="bg-blue-600 h-2 rounded-full" style="width: ${(count / totalGenerated) * 100}%"></div>
                </div>
                <span class="text-sm text-gray-600">${count}</span>
              </div>
            </div>
          `,
          )
          .join("")
      }
  
      // Update top content types
      const topTypesContainer = document.getElementById("top-content-types")
      if (topTypesContainer) {
        const topTypes = Object.entries(contentTypes)
          .sort(([, a], [, b]) => b - a)
          .slice(0, 3)
  
        topTypesContainer.innerHTML =
          topTypes.length > 0
            ? topTypes
                .map(
                  ([type, count], index) => `
              <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                <div class="flex items-center">
                  <span class="w-6 h-6 rounded-full bg-blue-600 text-white text-xs flex items-center justify-center mr-2">
                    ${index + 1}
                  </span>
                  <span class="capitalize">${type}</span>
                </div>
                <span class="text-sm text-gray-600">${count} posts</span>
              </div>
            `,
                )
                .join("")
            : '<p class="text-gray-500 text-center py-4">No data yet</p>'
      }
  
      // Update recommendations
      this.updateRecommendations(contentTypes, totalGenerated, postsUsed)
    }
  
    updateRecommendations(contentTypes, totalGenerated, postsUsed) {
      const recommendationsContainer = document.getElementById("recommendations")
      if (!recommendationsContainer) return
  
      const recommendations = []
  
      if (totalGenerated === 0) {
        recommendations.push("Start by generating some content to get personalized insights!")
      } else {
        if (postsUsed / totalGenerated < 0.3) {
          recommendations.push("💡 Try using more of your generated content - you have great posts saved!")
        }
  
        if (!contentTypes["project"]) {
          recommendations.push("🚀 Consider sharing project highlights to showcase your work")
        }
  
        if (!contentTypes["career"]) {
          recommendations.push("💼 Career advice posts tend to get high engagement")
        }
  
        if (!contentTypes["challenge"]) {
          recommendations.push("🧩 Coding challenges encourage community interaction")
        }
  
        if (contentTypes["educational"] && contentTypes["educational"] > totalGenerated * 0.5) {
          recommendations.push("🎯 Mix in more motivational and engagement posts for variety")
        }
  
        if (totalGenerated > 10 && postsUsed > 5) {
          recommendations.push("🎉 Great job staying consistent! Keep up the momentum")
        }
      }
  
      recommendationsContainer.innerHTML =
        recommendations.length > 0
          ? recommendations.map((rec) => `<p class="mb-1">${rec}</p>`).join("")
          : "<p>You're doing great! Keep creating valuable content.</p>"
    }
  }
  
  // Initialize the bot when page loads
  let bot
  document.addEventListener("DOMContentLoaded", () => {
    bot = new XGrowthBot()
  })
  
  // AI-Powered Post Generation
  function generateAIPost() {
    const contentType = document.getElementById('content-type').value;
    const topic = document.getElementById('topic').value;
    const provider = document.getElementById('ai-provider').value;
    let prompt = `Write a Twitter post about ${topic || 'a trending topic'} as if you're a friendly, witty developer. The post should be a ${contentType} and sound human, engaging, and slightly imperfect.`;
    
    // Show loading state
    const outputDiv = document.getElementById('content-output');
    outputDiv.classList.remove('hidden');
    document.getElementById('generated-text').textContent = 'Generating with AI...';
    document.getElementById('char-count').textContent = '';

    fetch('/ai-generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, provider })
    })
    .then(res => res.json())
    .then(data => {
        if (data.content) {
            document.getElementById('generated-text').textContent = data.content;
            document.getElementById('char-count').textContent = `${data.content.length} chars`;
        } else {
            document.getElementById('generated-text').textContent = data.error || 'Error generating content.';
        }
    })
    .catch(() => {
        document.getElementById('generated-text').textContent = 'Error connecting to AI service.';
    });
  }

  // Add AI button to generator tab
  window.addEventListener('DOMContentLoaded', function() {
    const genBtn = document.getElementById('generate-btn');
    if (genBtn && !document.getElementById('ai-generate-btn')) {
        const aiBtn = document.createElement('button');
        aiBtn.id = 'ai-generate-btn';
        aiBtn.className = 'btn-primary w-full mt-2';
        aiBtn.textContent = 'AI-Powered Post 🤖';
        aiBtn.onclick = generateAIPost;
        genBtn.parentNode.insertBefore(aiBtn, genBtn.nextSibling);
    }
  });
  
  // Meme Generator Form Handler
  window.addEventListener('DOMContentLoaded', function() {
    const memeForm = document.getElementById('meme-form');
    if (memeForm) {
      memeForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const templateInput = document.getElementById('meme-template');
        const captionInput = document.getElementById('meme-caption');
        const resultDiv = document.getElementById('meme-result');
        resultDiv.innerHTML = 'Generating meme...';
        const formData = new FormData();
        formData.append('template', templateInput.files[0]);
        formData.append('caption', captionInput.value);
        fetch('/generate-meme', {
          method: 'POST',
          body: formData
        })
        .then(res => {
          if (!res.ok) throw new Error('Failed to generate meme');
          return res.blob();
        })
        .then(blob => {
          const url = URL.createObjectURL(blob);
          resultDiv.innerHTML = `<img src="${url}" alt="Generated Meme" class="mx-auto rounded shadow">`;
        })
        .catch(() => {
          resultDiv.textContent = 'Error generating meme.';
        });
      });
    }
  });
  
  // Tech News & Trends Handlers
  window.addEventListener('DOMContentLoaded', function() {
    const newsResults = document.getElementById('news-results');
    function renderNews(items) {
      if (!items || items.length === 0) {
        newsResults.innerHTML = '<p class="text-gray-500">No results found.</p>';
        return;
      }
      newsResults.innerHTML = '<ul class="space-y-2">' +
        items.map(item => `<li><a href="${item.url}" target="_blank" class="text-blue-600 hover:underline">${item.title}</a></li>`).join('') +
        '</ul>';
    }
    function fetchNews(endpoint) {
      newsResults.innerHTML = 'Loading...';
      fetch(endpoint)
        .then(res => res.json())
        .then(data => {
          if (data.results) renderNews(data.results);
          else newsResults.innerHTML = data.error || 'Error fetching news.';
        })
        .catch(() => {
          newsResults.innerHTML = 'Error fetching news.';
        });
    }
    const githubBtn = document.getElementById('fetch-github');
    if (githubBtn) githubBtn.onclick = () => fetchNews('/fetch-github-trending');
    const hnBtn = document.getElementById('fetch-hackernews');
    if (hnBtn) hnBtn.onclick = () => fetchNews('/fetch-hackernews');
    const devtoBtn = document.getElementById('fetch-devto');
    if (devtoBtn) devtoBtn.onclick = () => fetchNews('/fetch-devto');
  });
  
  // Sentiment Analysis Handler
  window.addEventListener('DOMContentLoaded', function() {
    const sentimentForm = document.getElementById('sentiment-form');
    if (sentimentForm) {
      sentimentForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const text = document.getElementById('sentiment-text').value;
        const resultDiv = document.getElementById('sentiment-result');
        resultDiv.textContent = 'Analyzing...';
        fetch('/analyze-sentiment', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text })
        })
        .then(res => res.json())
        .then(data => {
          if (data.polarity !== undefined && data.subjectivity !== undefined) {
            resultDiv.innerHTML = `<div class='mb-2'>Polarity: <b>${data.polarity.toFixed(3)}</b></div><div>Subjectivity: <b>${data.subjectivity.toFixed(3)}</b></div>`;
          } else {
            resultDiv.textContent = data.error || 'Error analyzing sentiment.';
          }
        })
        .catch(() => {
          resultDiv.textContent = 'Error analyzing sentiment.';
        });
      });
    }
  });
  
  // Save Post Handler
  window.addEventListener('DOMContentLoaded', function() {
    const saveBtn = document.getElementById('save-btn');
    if (saveBtn) {
      saveBtn.onclick = function() {
        const text = document.getElementById('generated-text').textContent;
        if (!text || text === 'Generating with AI...' || text === 'Error generating content.' || text === 'Error connecting to AI service.') {
          alert('No content to save!');
          return;
        }
        fetch('/save-content', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ content: text })
        })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            saveBtn.textContent = 'Saved!';
            setTimeout(() => { saveBtn.textContent = '💾 Save Post'; }, 1500);
          } else {
            alert(data.error || 'Error saving content.');
          }
        })
        .catch(() => {
          alert('Error saving content.');
        });
      };
    }
    // Export Content Handler
    const exportBtn = document.getElementById('export-content-btn');
    const exportResult = document.getElementById('export-content-result');
    if (exportBtn) {
      exportBtn.onclick = function() {
        exportResult.textContent = 'Preparing download...';
        fetch('/export-content')
          .then(res => {
            if (!res.ok) throw new Error('No content to export.');
            return res.blob();
          })
          .then(blob => {
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'generated_content.csv';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            exportResult.textContent = 'Download started!';
            setTimeout(() => { exportResult.textContent = ''; }, 2000);
          })
          .catch(() => {
            exportResult.textContent = 'No content to export.';
          });
      };
    }
  });
  