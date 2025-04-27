from PIL import Image, ImageDraw, ImageFont
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk


class Watermark:
    def __init__(self):
        pass

    def add_text_watermark(
        self, image, text, text_color, font_style, font_size, position=(0, 0)
    ):

        font = ImageFont.truetype(font_style, font_size)
        draw = ImageDraw.Draw(image)
        draw.text(position, text, fill=text_color, font=font)
        return image

    def add_logo(self, image, logo, position=(0, 0)):
        if logo.mode != "RGBA":
            logo = logo.convert("RGBA")
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        if (position[0] + logo.width > image.width) or (
            position[1] + logo.height > image.height
        ):
            CTkMessagebox(title="Logo position", message="Logo position out of bounds.")

        image.paste(logo, position, mask=logo)
        return image

    def save_image(self, image):
        save_path = filedialog.asksaveasfilename(
            defaultextension="*.png",
            title="Save as",
            filetypes=[
                ("PNG files", "*.png"),
                ("All files", "*.*"),
            ],
        )
        if save_path:
            try:
                image.save(save_path)
            except Exception as e:
                print("Failed to save image: {e}")
