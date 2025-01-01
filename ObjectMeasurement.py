import cv2
import Utlis
import json
calibration_file = "calibration_data.json"
def load_calibration_data():
    try:
        with open(calibration_file, "r") as file:
            data = json.load(file)
        return data["scale"]
    except FileNotFoundError:
        return None

def save_calibration_data(scale):
    with open(calibration_file, "w") as file:
        json.dump({"scale": scale}, file)

webcam = True
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)
scale = load_calibration_data()
wP, hP = 210 * 3, 297 * 3
if scale is None:
    print("No calibration data found. Place an A4 sheet to calibrate.")
    scale = None
while True:
    if webcam:
        success, img = cap.read()
        if not success:
            print("Failed to read from webcam.")
            break
    else:
        img = cv2.imread('1.jpg')
    imgContours, conts = Utlis.getContours(img, minArea=50000, filter=4, draw=True)
    cv2.imshow('Contours', imgContours)
    if len(conts) != 0:
        biggest = conts[0][2]
        imgWarp = Utlis.warpImg(img, biggest, wP, hP)
        cv2.imshow('Warped A4 (Calibration)', imgWarp)
        if scale is None:
            scale = wP / 210 
            save_calibration_data(scale)
            print("Calibration complete. Scale saved.")
        imgContours2, conts2 = Utlis.getContours(imgWarp, minArea=2000, filter=4, cThr=[50, 50], draw=True)
        cv2.imshow('Contours on Warped Image', imgContours2)
        print(f"Number of contours detected: {len(conts2)}")
        if len(conts2) != 0:
            for obj in conts2:
                cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
                nPoints = Utlis.reorder(obj[2])
                nW = round(Utlis.findDis(nPoints[0][0], nPoints[1][0]) / scale, 1)
                nH = round(Utlis.findDis(nPoints[0][0], nPoints[2][0]) / scale, 1)
                x, y, w, h = obj[3]
                cv2.putText(imgContours2, f'{nW} cm', (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (255, 0, 255), 2)
                cv2.putText(imgContours2, f'{nH} cm', (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (255, 0, 255), 2)
        else:
            print("No objects detected.")
    else:
        print("A4 sheet not detected. Ensure proper placement.")
    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    cv2.imshow('Original', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
