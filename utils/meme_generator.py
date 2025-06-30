"""
Meme image generation utility using Pillow.
"""
from PIL import Image, ImageDraw, ImageFont
import os

def generate_meme(template_path, caption, output_path, font_path=None, font_size=40):
    """
    Overlay caption text on a meme template image.
    Args:
        template_path (str): Path to the meme template image.
        caption (str): Caption text to overlay.
        output_path (str): Path to save the generated meme image.
        font_path (str, optional): Path to a .ttf font file. Uses default if None.
        font_size (int, optional): Font size for the caption.
    """
    # Open the template image
    image = Image.open(template_path).convert('RGB')
    draw = ImageDraw.Draw(image)

    # Load font
    if font_path and os.path.exists(font_path):
        font = ImageFont.truetype(font_path, font_size)
    else:
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

    # Calculate text size and position
    text = caption
    image_width, image_height = image.size
    text_width, text_height = draw.textsize(text, font=font)
    x = (image_width - text_width) / 2
    y = image_height - text_height - 20  # 20px from bottom

    # Add outline for readability
    outline_range = 2
    for ox in range(-outline_range, outline_range+1):
        for oy in range(-outline_range, outline_range+1):
            draw.text((x+ox, y+oy), text, font=font, fill='black')

    # Draw the main text
    draw.text((x, y), text, font=font, fill='white')

    # Save the meme
    image.save(output_path) 