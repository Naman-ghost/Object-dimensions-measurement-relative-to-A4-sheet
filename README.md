# 📏 A4 Object Measurement with Webcam

This Python project enables users to measure the dimensions of objects placed on an A4 sheet using a webcam. It utilizes **OpenCV** for contour detection and image warping to ensure precise dimension calculations. The program includes a calibration step to map pixel measurements to real-world units (centimeters) using a standard A4 sheet.

---
## ✨ Features
- **Webcam Integration** - Captures live video feed for real-time measurement.
- **A4 Sheet Calibration** - Automatically detects an A4 sheet to calibrate pixel-to-centimeter conversion.
- **Real-time Object Measurement** - Measures objects placed on an A4 sheet and displays dimensions in centimeters.
- **Contours Detection** - Detects and highlights object contours.
- **Scale Storage** - Saves pixel-to-centimeter ratio for future use.

---
## 📌 Requirements
Ensure you have the following installed:
- **Python 3.0+**
- **OpenCV** (`pip install opencv-python`)
- **JSON** (built-in module for storing calibration data)
- **Utils Module** (Custom utility module for contour detection, image warping, and distance calculations)

---
## ⚙️ How It Works
### 1️⃣ **Calibration Step**
- When the program starts, it checks for `calibration_data.json`.
- If missing, it prompts you to place an **A4 sheet** in front of the webcam.
- The program detects the sheet and stores calibration data.

### 2️⃣ **Measuring Objects**
- Place any object on the A4 sheet.
- The program detects the object's contours and calculates its **width and height in centimeters**.
- Measurements are displayed in real time on the screen.

### 3️⃣ **Exit the Program**
- Press **'q'** to exit.

---
## 🚀 Running the Project
```bash
python object_measurement.py
```
Ensure your webcam is connected before running the script.

---
## 🛠 Troubleshooting
- **Calibration Issues?** Ensure proper lighting and a clear A4 sheet.
- **Contours Not Detected?** Adjust contrast or background to improve visibility.
- **Webcam Not Working?** Check permissions and ensure OpenCV is correctly installed.

---
🚀 **Happy Measuring!** 🎉

