Hand Gesture Controlled LED Brightness

Introduction:
This project demonstrates controlling the brightness of an LED using hand gestures captured by a webcam. The system detects hand gestures in real-time, calculates the distance between two specific points on the hand (finger tips), and adjusts the LED brightness accordingly.

Dependencies:

tkinter
time
pyfirmata
opencv-python
math
numpy

Installation:
Install Python (if not already installed).
Install required libraries using pip:
Copy code
pip install pyfirmata opencv-python numpy
Clone the repository or download the project files.

Usage:
Connect an Arduino board to your computer.
Connect an LED to pin 9 of the Arduino board.
Run the provided Python script in a Python environment.
Ensure that the webcam is connected and functional.
Perform hand gestures in front of the webcam to control the LED brightness.
Adjust the distance between two fingers to change the brightness level.


Note:
This project is for educational and experimental purposes.
Additional features and optimizations can be added, such as gesture recognition for different commands or controlling multiple LEDs.
