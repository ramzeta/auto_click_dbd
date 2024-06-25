import time
import pytesseract
import pyautogui
import cv2
import numpy as np

# Configurar la ruta de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # Ajusta esta ruta según tu instalación

# Cargar la imagen objetivo
target_image_path = 'image.png'
target_image = cv2.imread(target_image_path)

# Convertir la imagen a escala de grises
target_image_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

# Obtener las dimensiones de la imagen objetivo
w, h = target_image_gray.shape[::-1]

while True:
    # Tomar una captura de pantalla
    screenshot = pyautogui.screenshot()

    # Convertir la captura de pantalla a un array de numpy
    screenshot_np = np.array(screenshot)

    # Convertir la captura de pantalla a escala de grises
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    # Buscar la imagen objetivo en la captura de pantalla
    res = cv2.matchTemplate(screenshot_gray, target_image_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # Si se encuentra la imagen objetivo, hacer clic en su posición
    for pt in zip(*loc[::-1]):
        pyautogui.mouseDown(pt[0] + w / 2, pt[1] + h / 2)
        time.sleep(.7)
        pyautogui.mouseUp(pt[0] + w / 2, pt[1] + h / 2)
        break

    # Esperar un segundo antes de la próxima iteración
    time.sleep(.5)
