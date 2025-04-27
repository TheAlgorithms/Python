import customtkinter as ctk
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from watermark import Watermark
import pyglet
from tkinter import colorchooser


# ------------------- Create Window -----------------
pyglet.font.add_directory("fonts")


window = ctk.CTk()
window.geometry("810x525")
window.title("Grenze")

text_label = None
loaded_image = False
logo = None
img = None
user_text = None
logo_path = None
color_code = "white"
font_values = ["Decorative", "MartianMono", "DancingScript", "AkayaKanadaka"]


# -------------------------- LOAD IMAGE AND CHECK FILE TYPE ON IMAGE CANVAS (use Frame) --------------
def load_image():
    global img, loaded_image, image_canvas

    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if not file_path:
        return

    img = Image.open(file_path)
    max_width, max_height = 800, 600
    if img.width > max_width or img.height > max_height:
        ratio = min(max_width / img.width, max_height / img.height)
        resize_img = img.resize(
            (int(img.width * ratio), int(img.height * ratio)), Image.Resampling.LANCZOS
        )
        loaded_image = ImageTk.PhotoImage(resize_img)

        window.geometry(f"{resize_img.width + 300 + 30}x{resize_img.height + 50}")
        image_canvas.config(width=resize_img.width, height=resize_img.height)
        image_canvas.grid(row=0, column=1, padx=20, pady=20, columnspan=2)
        image_canvas.create_image(0, 0, anchor="nw", image=loaded_image)
    else:
        loaded_image = ImageTk.PhotoImage(img)
        window.geometry(f"{img.width + 300}x{img.height + 50}")
        image_canvas.config(width=img.width, height=img.height)
        image_canvas.grid(row=0, column=1, padx=20, pady=20, columnspan=2)
        image_canvas.create_image(0, 0, anchor="nw", image=loaded_image)


# ------------------------------------- DRAG AND DROP FEATURE --------

start_x = 0
start_y = 0

new_x = 0
new_y = 0


def move_logo(e):
    global logo, new_x, new_y
    canvas_width = image_canvas.winfo_width()
    canvas_height = image_canvas.winfo_height()
    label_width = image_canvas.bbox(logo)[2] - image_canvas.bbox(logo)[0]
    label_height = image_canvas.bbox(logo)[3] - image_canvas.bbox(logo)[1]

    new_x = e.x
    new_y = e.y

    if new_x < 0:
        new_x = 0
    elif new_x + label_width > canvas_width:
        new_x = canvas_width - label_width

    if new_y < 0:
        new_y = 0
    elif new_y + label_height > canvas_height:
        new_y = canvas_height - label_height
    image_canvas.coords(logo, new_x, new_y)


def move_text(e):
    global text_label, new_x, new_y
    canvas_width = image_canvas.winfo_width()
    canvas_height = image_canvas.winfo_height()
    label_width = image_canvas.bbox(text_label)[2] - image_canvas.bbox(text_label)[0]
    label_height = image_canvas.bbox(text_label)[3] - image_canvas.bbox(text_label)[1]

    new_x = e.x
    new_y = e.y

    if new_x < 0:
        new_x = 0
    elif new_x + label_width > canvas_width:
        new_x = canvas_width - label_width

    if new_y < 0:
        new_y = 0
    elif new_y + label_height > canvas_height:
        new_y = canvas_height - label_height
    image_canvas.coords(text_label, new_x, new_y)


def choose_color():
    global color_code
    choose_color = colorchooser.askcolor(title="Choose Color")
    color_code = choose_color[1]


# ----------------- ADD TEXT ON CANVAS-----------------


def add_text_on_canvas():
    global text_label, loaded_image, user_text, img, font_values
    user_text = text.get()
    font_key = font_style.get()
    if font_key not in font_values:
        CTkMessagebox(
            title="Font Not Available",
            message=f"{font_key} FileNotFoundError.",
        )
        return

    if logo is not None:
        CTkMessagebox(title="Logo Use", message="Logo is in use.")
        return

    if text_label is not None:
        image_canvas.delete(text_label)  # Delete previous text_label

    if loaded_image:
        if user_text:
            selected_size = int(font_size.get())
            pyglet.font.add_file(f"fonts/{font_key}.ttf")
            text_label = image_canvas.create_text(
                10,
                10,
                text=user_text,
                font=(font_key, selected_size),
                fill=color_code,
                anchor="nw",
            )

            image_canvas.tag_bind(text_label, "<B1-Motion>", move_text)
        else:
            CTkMessagebox(title="Error", message="Text Filed Empty.", icon="cancel")
    else:
        CTkMessagebox(title="Error", message="Image Not Found. Upload Image.")


# ----------------------TODO UPLOAD LOGO -----------


def upload_logo():
    global loaded_image, logo, logo_path, text_label

    if text_label is not None:
        CTkMessagebox(
            title="Text In Use", message="You are using text. Can't use logo."
        )
        return

    if logo is not None:
        image_canvas.delete(logo)
    if loaded_image:
        logo_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")],
        )
        if logo_path:
            logo_image = Image.open(logo_path).convert("RGBA")
            resize = logo_image.resize((160, 150))
            logo_photo = ImageTk.PhotoImage(resize)
            logo = image_canvas.create_image(0, 0, anchor="nw", image=logo_photo)
            image_canvas.tag_bind(logo, "<B1-Motion>", move_logo)

            image_canvas.logo_photo = logo_photo

    else:
        CTkMessagebox(
            title="Image Field Empty",
            message="Image field empty. Click on the open image button to add the image to the canvas.",
            icon="cancel",
        )


# ---------------------------- TODO SAVE FUNCTION ---------------
watermark = Watermark()


def save_image():
    global text_label, loaded_image, file_path, user_text, img, new_x, new_y, logo
    if loaded_image and text_label:
        width, height = img.size
        canvas_width = image_canvas.winfo_width()
        canvas_height = image_canvas.winfo_height()

        scale_x = width / canvas_width
        scale_y = height / canvas_height

        image_x = int(new_x * scale_x) - 10
        image_y = int(new_y * scale_y) - 10

        adjusted_font_size = int(int(font_size.get()) * min(scale_x, scale_y)) + 6
        watermarked_image = watermark.add_text_watermark(
            image=img,
            text=user_text,
            position=(image_x, image_y),
            text_color=color_code,
            font_style=f"fonts/{font_style.get()}.ttf",
            font_size=adjusted_font_size,
        )

        watermark.save_image(watermarked_image)

    elif loaded_image and logo_path is not None:
        original_image = img.convert("RGBA")
        canvas_width = image_canvas.winfo_width()
        canvas_height = image_canvas.winfo_height()

        logo_image = Image.open(logo_path)
        logo_resized = logo_image.resize(
            (
                int(original_image.width * 0.2) + 50,
                int(original_image.height * 0.2),
            )
        )

        image_width, image_height = original_image.size
        logo_position = (
            int(new_x * image_width / canvas_width),
            int(new_y * image_height / canvas_height),
        )

        watermark.add_logo(
            image=original_image, logo=logo_resized, position=logo_position
        )

        watermark.save_image(original_image)


# -------------------Tab View AND OPEN IMAGE-----------

tabview = ctk.CTkTabview(window, corner_radius=10, height=400)
tabview.grid(row=0, column=0, padx=10)


tab_1 = tabview.add("Text Watermark")
tab_2 = tabview.add("Logo Watermark")


# --------------- TEXT WATERMARK TAB_1 VIEW ----------
tab_1.grid_columnconfigure(0, weight=1)
tab_1.grid_columnconfigure(1, weight=1)

text = ctk.CTkEntry(master=tab_1, placeholder_text="Entry Text", width=200)
text.grid(row=2, column=0, padx=20, pady=10)


font_style = ctk.CTkComboBox(
    master=tab_1,
    values=font_values,
    width=200,
)
font_style.grid(row=3, column=0, pady=10)


font_size = ctk.CTkComboBox(
    master=tab_1,
    values=[
        "10",
        "12",
        "14",
        "20",
    ],
    width=200,
)
font_size.grid(row=4, column=0, pady=10)
font_size.set("10")

add_text = ctk.CTkButton(
    master=tab_1, text="Add Text", width=200, command=add_text_on_canvas
)
add_text.grid(row=5, column=0, pady=10)


open_image = ctk.CTkButton(
    master=tab_1, text="Open Image", width=200, corner_radius=10, command=load_image
)
open_image.grid(row=7, column=0, pady=10)

open_image2 = ctk.CTkButton(
    master=tab_2, text="Open Image", width=200, corner_radius=10, command=load_image
)
open_image2.grid(row=2, column=0, padx=20, pady=10)

pick_color = ctk.CTkButton(
    master=tab_1, text="Pick Color", width=200, corner_radius=10, command=choose_color
)
pick_color.grid(row=6, column=0, padx=10, pady=10)


# ------------- LOGO WATERMARK SESSION TAB_2 ---------------

logo_upload = ctk.CTkButton(
    master=tab_2, text="Upload Logo", width=200, corner_radius=10, command=upload_logo
)
logo_upload.grid(row=3, column=0, pady=10)


# ----------------- ImageFrame ---------------------
image_canvas = ctk.CTkCanvas(
    width=500,
    height=360,
)
image_canvas.config(bg="gray24", highlightthickness=0, borderwidth=0)
image_canvas.grid(row=0, column=1, columnspan=2)


# -------- SAVE BUTTON --------

save_image_button = ctk.CTkButton(window, text="Save Image", command=save_image)
save_image_button.grid(pady=10)

window.mainloop()
