# QR Code Generator

Generate QR codes with custom background images using Python and MyQR.

## About

QR Code Generator is a Python application for creating QR codes with image backgrounds.

The application accepts either a local image path or an online image URL as the background source. It uses MyQR to generate the QR code, Eel for the graphical interface, requests to retrieve remote images, and OpenCV to preview generated static images.

Animated GIF backgrounds are also supported. When the output file is a GIF, the generated result is saved without opening an OpenCV preview window.

## Features

- Generate QR codes with custom background images
- Use local images as QR code backgrounds
- Download and use background images from HTTP or HTTPS URLs
- Support animated GIF backgrounds
- Generate colorized QR codes with MyQR
- Preview generated non-GIF images with OpenCV
- Use a graphical interface built with Eel

## Getting Started

### Prerequisites

To run the application, you need:

- Python 3
- pip

The project uses the following Python packages:

- `myqr`
- `requests`
- `eel`
- `opencv-python`

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/sky9154/QRcode.git
cd QRcode
```

**2. Install the required packages**

```bash
pip install myqr
pip install requests
pip install eel
pip install opencv-python
```

### Usage

Run the application with:

```bash
python3 build.py
```

In the interface:

1. Enter the content or URL to encode in the QR code.
2. Enter the path or URL of the background image.
3. Enter the output file name.
4. Click **Build** to generate the QR code.

For animated GIF backgrounds, use `.gif` as the output file extension.

GIF output is saved without an OpenCV preview. Other generated image files are opened in a preview window after creation.

## Project Structure

```text
QRcode/
├── assets/
│   └── images/
├── gui/
├── build.py
└── README.md
```

- `build.py` contains the QR code generation logic and starts the Eel interface.
- `gui/` contains the files used by the Eel graphical interface.
- `assets/images/` contains image assets used by the project.

## Screenshots

![Demo](/assets/images/demo.gif)
