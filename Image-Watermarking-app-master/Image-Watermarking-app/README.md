# Watermarking Application

A Python-based watermarking application built using `CustomTkinter` and `PIL` that allows users to add text and logo watermarks to images. The application supports the customization of text, font, size, color, and the ability to drag and position the watermark on the image.

## Features

- **Text Watermark**: Add customizable text to your images.
  - Select font style, size, and color.
  - Drag and position the text watermark on the image.
- **Logo Watermark**: Add a logo or image as a watermark.
  - Resize and position the logo watermark.
  - Supports various image formats (JPG, PNG, BMP).
- **Mutual Exclusivity**: The application ensures that users can either add text or a logo as a watermark, not both simultaneously.
- **Image Saving**: Save the watermarked image in PNG format with an option to choose the file name and location.

## Installation

### Prerequisites

- Python 3.6 or higher
- `PIL` (Pillow)
- `CustomTkinter`

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jinku-06/Image-Watermarking-Desktop-app.git
   cd watermarking-app
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

## Usage

1. **Load an Image**: Start by loading an image onto the canvas.
2. **Add Text Watermark**:
   - Input your desired text.
   - Customize the font style, size, and color.
   - Drag and position the text on the image.
   - Note: Adding a text watermark disables the option to add a logo.
3. **Add Logo Watermark**:
   - Select and upload a logo or image to use as a watermark.
   - Resize and position the logo on the image.
   - Note: Adding a logo watermark disables the option to add text.
4. **Save the Image**: Once satisfied with the watermark, save the image to your desired location.

## Project Structure

```bash
watermarking-app/
│
├── fonts/                 # Custom fonts directory
├── app.py                 # Main application file
├── watermark.py           # Watermark functionality class
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

## Sample and look

Below are some sample images showcasing the application work:

UI:

<img src="https://github.com/user-attachments/assets/637200b2-6b88-4135-81fd-3c909aafbc4c" width ="500" height="350" alt='Userinterface image'>

Text Watermark :

<img src="https://github.com/user-attachments/assets/096e2675-d528-4ef7-aa98-b8483fb1c883" width="300" height="350" alt="text watermark demo image">

Logo Watermark:

<img src="https://github.com/user-attachments/assets/536675ae-a165-49b7-8294-0b599faa58f6" width="300" height="350" alt="logo watermark demo image">







  





