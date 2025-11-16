import cv2
import numpy as np

IMG_NAME = "motor.jpg"  # si tenés recorte del aro: "motor_crop.jpg"
img = cv2.imread(IMG_NAME)
assert img is not None, f"No se pudo cargar {IMG_NAME}"

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(
    gray, cv2.HOUGH_GRADIENT,
    dp=1.2, minDist=100,
    param1=100, param2=38,
    minRadius=40, maxRadius=70
)

out = img.copy()
if circles is not None:
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv2.circle(out, (x, y), r, (0, 255, 0), 2)
        cv2.circle(out, (x, y), 2, (0, 0, 255), 3)

cv2.imwrite("resultado_circulos.jpg", out)
print("OK -> resultado_circulos.jpg")
