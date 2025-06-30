// Service worker for X-bot 
self.addEventListener("notificationclick", (event) => {
    event.notification.close()
  
    if (event.action === "generate") {
      // Open the app and focus on generator
      event.waitUntil(clients.openWindow("/?action=generate"))
    } else if (event.action === "dismiss") {
      // Just close the notification
      return
    } else {
      // Default action - open the app
      event.waitUntil(clients.openWindow("/"))
    }
  })
  
  self.addEventListener("push", (event) => {
    const options = {
      body: event.data ? event.data.text() : "Time to create engaging content!",
      tag: "posting-reminder",
      requireInteraction: true,
    }
  
    event.waitUntil(self.registration.showNotification("X Growth Bot 🚀", options))
  })
  