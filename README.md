Got it! Here's the updated README file with instructions for uploading a presentation using `PresentationTOPngConversion.py`:

---

# Hand Gesture-Based Presentation Controller

## Overview

The Hand Gesture-Based Presentation Controller is an innovative tool that allows users to control presentation slides using simple hand gestures. This controller utilizes a camera to detect and interpret specific hand gestures, providing a seamless and intuitive way to navigate through presentations.

## Features

- **Slide Navigation**: Move to the next or previous slide using hand gestures.
- **Pointer**: Use your finger as a pointer to highlight points on the slide.
- **Drawing**: Annotate slides in real-time using a single finger.
- **Zoom**: Zoom in and out of slides using pinch gestures.

## Gesture Guide

### 1. Slide Navigation
- **Left Slide Shift**: Use your thumb to shift to the previous slide.
- **Right Slide Shift**: Use your little finger to shift to the next slide.

### 2. Pointer
- **Activate Pointer**: Use two index fingers to activate the pointer mode. Move your hand to point at specific areas on the slide.

### 3. Drawing
- **Activate Drawing**: Use one index finger to activate drawing mode. Move your finger to draw on the slide.

### 4. Zoom
- **Zoom In/Out**: Use both hands, index fingers, and thumbs to perform pinch gestures to zoom in or out on the slide.

## Installation

1. Clone the repository:
   ```bash
    https://github.com/KRISH708048/Hand-Gestured-PPT.git
    ```
2. Navigate to the project directory:
   ```bash
   cd HandGesturedPresentation
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. Connect your camera and ensure it is working correctly.
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to calibrate the hand gestures.
4. Start your presentation and use the gestures as described in the Gesture Guide to control your slides.

### Uploading a Presentation

To upload a presentation and convert it to slide images, use the `PresentationTOPngConversion.py` script.

1. Place your presentation file (e.g., `presentation.pptx`) in the `presentations` directory.
2. Run the conversion script:
   ```bash
   python PresentationTOPngConversion.py 
   ```
3. The script will convert each slide in the presentation to a PNG image and save them in the `slides` directory.

## Contributing

I welcome contributions from the community. If you have any suggestions or improvements, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
