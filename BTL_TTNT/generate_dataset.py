import os
import cv2
import numpy as np
import random

# =============================
# Cấu hình
# =============================
IMG_SIZE = 28
SAMPLES_PER_CLASS = 300  # số ảnh mỗi ký tự
OUTPUT_DIR = "data/categorized"

# Font OpenCV
FONTS = [
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_TRIPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
]

# =============================
# Tạo thư mục
# =============================
digits = [str(i) for i in range(10)]
alphas = list("ABCDEFGHKLMNPRSTUVXYZ") 

for d in digits:
    os.makedirs(f"{OUTPUT_DIR}/digits/{d}", exist_ok=True)

for a in alphas:
    os.makedirs(f"{OUTPUT_DIR}/alphas/{a}", exist_ok=True)

# =============================
# Hàm tạo ảnh ký tự
# =============================
def generate_char_image(char):
    img = np.ones((IMG_SIZE, IMG_SIZE), dtype=np.uint8) * 255

    font = random.choice(FONTS)
    scale = random.uniform(0.7, 1.2)
    thickness = random.randint(1, 2)

    text_size = cv2.getTextSize(char, font, scale, thickness)[0]

    x = (IMG_SIZE - text_size[0]) // 2
    y = (IMG_SIZE + text_size[1]) // 2

    cv2.putText(img, char, (x, y),
                font, scale, (0,), thickness)

    # xoay nhẹ để đa dạng
    angle = random.uniform(-15, 15)
    M = cv2.getRotationMatrix2D((IMG_SIZE/2, IMG_SIZE/2), angle, 1)
    img = cv2.warpAffine(img, M, (IMG_SIZE, IMG_SIZE),
                         borderValue=255)

    img = img.reshape((28, 28, 1))
    return img

# =============================
# Tạo ảnh digits
# =============================
for d in digits:
    for i in range(SAMPLES_PER_CLASS):
        img = generate_char_image(d)
        cv2.imwrite(f"{OUTPUT_DIR}/digits/{d}/{d}_{i}.png", img)

# =============================
# Tạo ảnh alphas
# =============================
for a in alphas:
    for i in range(SAMPLES_PER_CLASS):
        img = generate_char_image(a)
        cv2.imwrite(f"{OUTPUT_DIR}/alphas/{a}/{a}_{i}.png", img)

print("✅ Đã tạo dataset thành công!")