# 📌 BÀI TIỂU LUẬN TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY
# 📌 XÂY DỰNG ỨNG DỤNG NHẬN DẠNG BIỂN SỐ XE (LICENSE PLATE RECOGNITION)

## Phương pháp nhận dạng biển số xe trong hệ thống được xây dựng gồm 4 bước chính:
- Phát hiện biển số: Sử dụng mô hình YOLOv3-Tiny để xác định vị trí biển số xe trong ảnh hoặc video.
- Tách ký tự: Áp dụng thuật toán segmentation để tách từng ký tự trên biển số.
- Nhận dạng ký tự: Sử dụng mô hình CNN để phân loại các chữ cái và chữ số.
- Định dạng biển số: Sắp xếp lại các ký tự và xác định biển số để tạo kết quả hoàn chỉnh.

## Cấu trúc thư mục
```
BTL_TTNT/
│
├── data/                         # Dữ liệu phục vụ huấn luyện và nhận dạng
│   ├── categorized/              # Thư mục chứa dữ liệu ký tự đã phân loại
│   ├── alphas.npy                # Dataset ký tự chữ cái
│   └── digits.npy                # Dataset ký tự số
│
├── images/                       # Ảnh dùng để test nhận dạng
├── train/                        
│
├── src/                          # Mã nguồn chính của hệ thống
│
│   ├── CNN/                      # Module huấn luyện và nhận dạng ký tự bằng CNN
│   │   ├── config.py             # Cấu hình mô hình CNN
│   │   ├── create_data.py        # Tạo dữ liệu huấn luyện
│   │   ├── dulieu.py             # Xử lý và chuẩn bị dữ liệu
│   │   ├── mohinh.py             # Xây dựng kiến trúc mô hình CNN
│   │   └── train.ipynb           # Notebook huấn luyện mô hình
│
│   ├── done/                     # Các mô hình đã huấn luyện
│   │   ├── CNN_model.h5          # Model CNN dùng nhận dạng ký tự
│   │   └── yolov3-tiny.weights   # Trọng số YOLOv3-Tiny
│
│   ├── YOLO/                     # Module phát hiện biển số xe
│   │   ├── cfg/                  # File cấu hình YOLO
│   │   │   ├── yolo.names
│   │   │   ├── yolov3-tiny.cfg
│   │   │   
│   │   ├── YOLO_detect.py        # Phát hiện biển số bằng YOLO
│   │
│   ├── data_utils.py             # Các hàm xử lý dữ liệu
│   └── license_plate_recognition.py   # Pipeline nhận dạng biển số
│
├── video/                        # Video test nhận dạng
│
├── app.py                        # Ứng dụng Streamlit giao diện người dùng
├── main.py                       # Chạy nhận dạng với ảnh
├── main_video.py                 # Chạy nhận dạng với video
│
├── generate_dataset.py           # Tạo dataset huấn luyện
│
├── requirements.txt              # Danh sách thư viện cần cài đặt
```
## Cài đặt môi trường
Trước tiên cần cài đặt Python. Sau đó tiến hành cài đặt các thư viện cần thiết cho dự án bằng các lệnh sau:
```
pip install tensorflow
pip install numpy
pip install matplotlib
pip install opencv-contrib-python
pip install streamlit
pip install scikit-learn
pip install scikit-image
pip install imutils
```
Hoặc để cài đặt tất cả các thư viện cần thiết cho dự án, hãy chạy lệnh sau trong terminal:
```
pip install -r requirements.txt
```
