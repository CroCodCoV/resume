import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Настройки
img = cv2.imread("Путь до файла")
mode = 1  # 1-Собель, 2-Лаплас, 3-Гаусс, 4-Эквализация

# Обработка изображения
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
if mode == 1:
    sx, sy = cv2.Sobel(gray, cv2.CV_64F, 1, 0, 3), cv2.Sobel(gray, cv2.CV_64F, 0, 1, 3)
    mask = cv2.normalize(cv2.magnitude(sx, sy), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    res = cv2.addWeighted(img, 1, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), 0.5, 0)
elif mode == 2:
    mask = cv2.normalize(cv2.Laplacian(gray, cv2.CV_64F), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    res = cv2.addWeighted(img, 1, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), 0.5, 0)
elif mode == 3:
    blur = cv2.GaussianBlur(gray, (15, 15), 0)
    mask = cv2.absdiff(gray, blur)
    res = cv2.GaussianBlur(img, (15, 15), 0)
else:
    eq = cv2.equalizeHist(gray)
    mask = cv2.absdiff(gray, eq)
    res = img.copy()
    for i in range(3): res[:,:,i] = cv2.equalizeHist(img[:,:,i])

# GUI
root = tk.Tk()
root.title("Обработка изображений")

# Масштабирование
h, w = img.shape[:2]
scale = min(300/h, 300/w) if max(h, w) > 700 else 1
size = (int(w*scale), int(h*scale))

# Отображение
images = []
titles = ["Оригинал", "Маска", "Результат"]
for i, (title, im) in enumerate(zip(titles, [img, mask, res])):
    if len(im.shape) == 2: im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
    else: im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = cv2.resize(im, size)
    tk_img = ImageTk.PhotoImage(Image.fromarray(im))
    images.append(tk_img)
    f = tk.Frame(root)
    f.grid(row=0, column=i, padx=5, pady=5)
    tk.Label(f, text=title).pack()
    tk.Label(f, image=tk_img).pack()

root.mainloop()
