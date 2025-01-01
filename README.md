A4 Object Measurement with Webcam
This Python project allows users to measure the dimensions of objects placed on an A4 sheet using a webcam. The program uses OpenCV to detect contours and warp the image for accurate dimension calculation. It also includes a calibration step to map pixel measurements to real-world units (centimeters) using a standard A4 sheet.


Features:
Webcam integration: Uses a webcam to capture live video feed.
A4 sheet calibration: Automatically calibrates the system based on the A4 sheet dimensions to provide accurate measurements.
Real-time object measurement: Measures objects placed on an A4 sheet and displays their dimensions in centimeters.
Contours detection: Detects and displays contours of objects on the A4 sheet.
Scale storage: Saves the calculated scale (pixel-to-centimeter ratio) for future use.


Requirements:
Python 3.x: Make sure Python 3.x is installed on your system.
OpenCV: For computer vision operations (contour detection, image warping, etc.).
JSON: For storing and loading calibration data.
Utlis: A custom utility module (presumed to be part of the project) that includes functions for contour detection, image warping, and distance calculations.


How It Works:
Calibration Step:
When you run the program, it will check if a calibration file (calibration_data.json) exists.
If the file is not found, the program will prompt you to place an A4 sheet in front of the webcam. The program will automatically detect the A4 sheet, and the calibration data will be saved to a file.
Measurement of Objects:

After calibration, place any object on the A4 sheet.
The program will detect the contours of the objects and measure their dimensions (width and height) in centimeters, which will be displayed on the screen in real-time.

Exit:
To exit the program, press the q key.
