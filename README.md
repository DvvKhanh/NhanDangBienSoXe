# 📌 BÀI TIỂU LUẬN TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY
# 📌 XÂY DỰNG ỨNG DỤNG NHẬN DẠNG BIỂN SỐ XE (LICENSE PLATE RECOGNITION)

## Phương pháp nhận dạng biển số xe trong hệ thống được xây dựng gồm 4 bước chính:
- Phát hiện biển số: Sử dụng mô hình YOLOv3-Tiny để xác định vị trí biển số xe trong ảnh hoặc video.
- Tách ký tự: Áp dụng thuật toán segmentation để tách từng ký tự trên biển số.
- Nhận dạng ký tự: Sử dụng mô hình CNN để phân loại các chữ cái và chữ số.
- Định dạng biển số: Sắp xếp lại các ký tự và xác định biển số để tạo kết quả hoàn chỉnh.

## 📁 1. Cấu trúc thư mục
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

## ⚙️ 2. Cài đặt
### 1️⃣ Bước 1. Clone Repository
```
git clone <repository-url>
cd BTL_TTNT
```
### 2️⃣ Bước 2: Tạo môi trường ảo
Tạo môi trường Python:
```
python -m venv venv
```
Kích hoạt môi trường:
```
venv\Scripts\activate
```
### 3️⃣ Bước 3: Cài đặt thư viện cần thiết
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

### 4️⃣ Bước 4: Tạo dữ liệu ký tự

#### 1. Tạo dữ liệu ký tự từ ảnh

Chạy file:
```
python generate_dataset.py
```
Sau khi chạy xong, hệ thống sẽ tạo thư mục:
```
data/categorized/
```
Thư mục này chứa các ảnh ký tự đã được phân loại theo từng nhãn, bao gồm:

🔤 Chữ cái

🔢 Chữ số

#### 2. Chuyển dữ liệu sang định dạng NumPy

Sau khi có dữ liệu ký tự, cần chuyển dữ liệu sang định dạng NumPy (.npy) để phục vụ huấn luyện mô hình CNN.

Chạy file:
```
python src/CNN/create_data.py
```

Sau khi chạy xong sẽ tạo ra hai file dữ liệu:
```
alphas.npy   # dữ liệu ký tự chữ cái
digits.npy   # dữ liệu ký tự số
```

Các file này sẽ được lưu trong thư mục:
```
data/
```
### 5️⃣ Bước 5: Huấn luyện mô hình CNN
Trước khi nhận dạng biển số, cần huấn luyện mô hình CNN để nhận dạng ký tự.

Mở file:
```
src/CNN/train.ipynb
```

Sau đó chạy toàn bộ các cell để huấn luyện.

Sau khi train xong sẽ tạo file model:
```
CNN_model.h5
```

File này sẽ được lưu trong thư mục:
```
src/done/
```

### 🔍 Cách huấn luyện mô hình YOLOv3 Tiny có thể tham khảo tại đây: https://github.com/AlexeyAB/darknet?tab=readme-ov-file

### 6️⃣ Bước 6: Chạy chương trình nhận dạng
🚀 Chạy ứng dụng Streamlit:

Mở Terminal / Command Prompt trong thư mục project và chạy lệnh:
```
streamlit run app.py
```
🚀 Mở giao diện ứng dụng:

Sau khi chạy lệnh trên, Streamlit sẽ tự động khởi động server và hiển thị địa chỉ truy cập.

Mở trình duyệt và truy cập:
```
http://localhost:8501
```
🚀 Sử dụng hệ thống:

Tại giao diện web, người dùng có thể:
- 📤 Upload ảnh hoặc video chứa biển số xe.
- 🔍 Hệ thống sẽ tự động phát hiện biển số.
- 🔠 Tách ký tự và nhận dạng bằng mô hình CNN.
- ✅ Hiển thị kết quả biển số xe trên màn hình.

## ✅ Kết quả nhận dạng

