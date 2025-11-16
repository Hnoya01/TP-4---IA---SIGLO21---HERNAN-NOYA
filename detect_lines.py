import cv2
import numpy as np

# --- 1) Cargar imagen ---
img = cv2.imread("motor.jpg")  # reemplazá si usás otro nombre
assert img is not None, "No se pudo cargar motor.jpg (¿está en la carpeta?)"

# --- 2) Gris + suavizado ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 1.2)

# --- 3) Bordes (Canny) ---
low_thr, high_thr = 80, 160     # Ajustables
edges = cv2.Canny(gray, low_thr, high_thr)

# --- 4) Hough Lines (probabilística) ---
rho = 1                         # px
theta = np.pi / 180             # 1 grado
threshold = 60                  # votos mínimos
min_line_len = 60               # px
max_line_gap = 10               # px

lines = cv2.HoughLinesP(edges, rho, theta, threshold,
                        minLineLength=min_line_len, maxLineGap=max_line_gap)

# --- 5) Dibujar y guardar ---
out = img.copy()
if lines is not None:
    for (x1, y1, x2, y2) in lines[:, 0]:
        cv2.line(out, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite("edges_rectas.jpg", edges)
cv2.imwrite("resultado_rectas.jpg", out)
print("OK -> edges_rectas.jpg / resultado_rectas.jpg")
