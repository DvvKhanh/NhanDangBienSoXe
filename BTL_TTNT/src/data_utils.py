import numpy as np
import cv2

def get_digits_data(path):
    data = np.load(path, allow_pickle=True)
    total_nb_data = len(data)
    np.random.shuffle(data)
    data_train = []

    for i in range(total_nb_data):
        data_train.append(data[i])

    print("-------------DONE------------")
    print('The number of train digits data: ', len(data_train))

    return data_train


def get_alphas_data(path):
    data = np.load(path, allow_pickle=True)
    total_nb_data = len(data)

    np.random.shuffle(data)
    data_train = []

    for i in range(total_nb_data):
        data_train.append(data[i])

    print("-------------DONE------------")
    print('The number of train alphas data: ', len(data_train))

    return data_train

def get_labels(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    return [line.strip() for line in lines]

def draw_labels_and_boxes(image, labels, boxes):

    x_min = int(round(boxes[0]))
    y_min = int(round(boxes[1]))
    x_max = int(round(boxes[0] + boxes[2]))
    y_max = int(round(boxes[1] + boxes[3]))

    # 1️⃣ Vẽ bounding box
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max),
                  (255, 0, 255), 2)

    # 2️⃣ Chuẩn bị text
    text = str(labels)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    thickness = 2

    (w, h), _ = cv2.getTextSize(text, font, font_scale, thickness)

    # 3️⃣ Tính vị trí text (trên box nếu đủ chỗ)
    text_x = x_min
    text_y = y_min - 10

    # Nếu không đủ chỗ phía trên thì vẽ xuống dưới
    if text_y - h < 0:
        text_y = y_min + h + 10

    # 4️⃣ Vẽ nền chữ
    cv2.rectangle(image,
                  (text_x, text_y - h - 5),
                  (text_x + w, text_y + 5),
                  (0, 0, 0),
                  -1)

    # 5️⃣ Vẽ chữ
    cv2.putText(image,
                text,
                (text_x, text_y),
                font,
                font_scale,
                (0, 0, 255),
                thickness,
                cv2.LINE_AA)

    return image

def get_output_layers(model):
    layers_name = model.getLayerNames()
    out_layers_idx = model.getUnconnectedOutLayers()

    # Đảm bảo out_layers_idx là mảng 1D
    if isinstance(out_layers_idx, np.ndarray):
        out_layers_idx = out_layers_idx.flatten()
    elif isinstance(out_layers_idx, list):
        out_layers_idx = np.array(out_layers_idx).flatten()
    else:
        out_layers_idx = np.array([out_layers_idx])

    # Chỉ số trong OpenCV là 1-based, trừ 1 để dùng trong Python
    output_layers = [layers_name[i - 1] for i in out_layers_idx]

    return output_layers

def order_points(coordinates):
    rect = np.zeros((4, 2), dtype="float32")
    x_min, y_min, width, height = coordinates

    # top left - top right - bottom left - bottom right
    rect[0] = np.array([round(x_min), round(y_min)])
    rect[1] = np.array([round(x_min + width), round(y_min)])
    rect[2] = np.array([round(x_min), round(y_min + height)])
    rect[3] = np.array([round(x_min + width), round(y_min + height)])

    return rect

def convert2Square(image):
    """
    Resize non-square image (height != width) to square one (height == width)
    :param image: input images
    :return: numpy array
    """

    img_h = image.shape[0]
    img_w = image.shape[1]

    # if height > width
    if img_h > img_w:
        diff = img_h - img_w
        if diff % 2 == 0:
            x1 = np.zeros(shape=(img_h, diff // 2), dtype=image.dtype)
            x2 = x1
        else:
            x1 = np.zeros(shape=(img_h, diff // 2), dtype=image.dtype)
            x2 = np.zeros(shape=(img_h, (diff // 2) + 1), dtype=image.dtype)

        squared_image = np.concatenate((x1, image, x2), axis=1)
    elif img_w > img_h:
        diff = img_w - img_h
        if diff % 2 == 0:
            x1 = np.zeros(shape=(diff // 2, img_w), dtype=image.dtype)
            x2 = x1
        else:
            x1 = np.zeros(shape=(diff // 2, img_w), dtype=image.dtype)
            x2 = np.zeros(shape=(diff // 2, img_w), dtype=image.dtype)

        squared_image = np.concatenate((x1, image, x2), axis=0)
    else:
        squared_image = image

    return squared_image
