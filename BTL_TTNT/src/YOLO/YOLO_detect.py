import cv2
import numpy as np
from src.data_utils import get_labels, get_output_layers, draw_labels_and_boxes

class detectNumberPlate(object):
    def __init__(self, classes_path, config_path, weight_path, threshold=0.5):
        self.weight_path = weight_path
        self.cfg_path = config_path
        self.labels = get_labels(classes_path)
        self.threshold = threshold

        # Load model YOLO
        self.model = cv2.dnn.readNet(model=self.weight_path, config=self.cfg_path)

    def detect(self, image):
        boxes = []
        classes_id = []
        confidences = []
        scale = 0.00392

        blob = cv2.dnn.blobFromImage(image, scalefactor=scale, size=(416, 416),
                                     mean=(0, 0, 0), swapRB=True, crop=False)
        height, width = image.shape[:2]

        # input image vào model
        self.model.setInput(blob)

        # forward
        outputs = self.model.forward(get_output_layers(self.model))

        for output in outputs:
            for i in range(len(output)):
                scores = output[i][5:]
                class_id = np.argmax(scores)
                confidence = float(scores[class_id])

                if confidence > self.threshold:
                    center_x = int(output[i][0] * width)
                    center_y = int(output[i][1] * height)
                    detected_width = int(output[i][2] * width)
                    detected_height = int(output[i][3] * height)
                    x_min = center_x - detected_width / 2
                    y_min = center_y - detected_height / 2

                    boxes.append([x_min, y_min, detected_width, detected_height])
                    classes_id.append(class_id)
                    confidences.append(confidence)

        # Non-max suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=self.threshold, nms_threshold=0.4)

        coordinates = []
        for i in indices:
            # i có thể là 1D hoặc 2D, xử lý cho mọi trường hợp
            index = i[0] if isinstance(i, (list, tuple, np.ndarray)) else i
            x_min, y_min, width_box, height_box = boxes[index]
            x_min = round(x_min)
            y_min = round(y_min)
            coordinates.append((x_min, y_min, width_box, height_box))

        return coordinates
