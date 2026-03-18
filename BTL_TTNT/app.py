import streamlit as st
import cv2
import numpy as np
import tempfile
import time
from PIL import Image
from src.license_plate_recognition import E2E

# =============================
# CẤU HÌNH TRANG
# =============================
st.set_page_config(
    page_title="Nhận dạng biển số xe",
    page_icon="🚗",
    layout="wide"
)

# =============================
# CSS GIAO DIỆN
# =============================
st.markdown("""
<style>
.main {
    background: linear-gradient(120deg, #1e3c72, #2a5298);
}
h1 {
    text-align: center;
    color: white;
}
h3 {
    color: #2a5298;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 8px;
    padding: 8px 18px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #ff0000;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #f0f2f6;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# TIÊU ĐỀ
# =============================
st.title("🚗 HỆ THỐNG NHẬN DẠNG BIỂN SỐ XE")
st.markdown("### Ứng dụng AI sử dụng YOLOv3 Tiny và CNN")

# =============================
# LOAD MODEL (CACHE)
# =============================
@st.cache_resource
def load_model():
    return E2E()

model = load_model()

# =============================
# SIDEBAR
# =============================
st.sidebar.header("⚙️ Chế độ hoạt động")

option = st.sidebar.selectbox(
    "Chọn chức năng:",
    (
        "📷 Nhận diện ảnh",
        "🎥 Nhận diện video",
        "📹 Webcam realtime"
    )
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Thông tin đề tài")
st.sidebar.markdown("""
- **Sinh viên:** Đậu Văn Khánh  
- **Lớp:** K58KTP  
- **Ngành:** Kỹ thuật phần mềm  
- **GVHD:** TS. Nguyễn Tuấn Linh  
- **Môn học:** Trí tuệ nhân tạo & Học máy  
""")

# =====================================================
# 1️⃣ NHẬN DIỆN ẢNH
# =====================================================
if option == "📷 Nhận diện ảnh":

    uploaded_file = st.file_uploader(
        "📤 Tải ảnh lên từ máy tính",
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Ảnh gốc")
            st.image(image, width=500)

        image_np = np.array(image)
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        if st.button("🔍 Bắt đầu nhận diện"):

            start = time.time()

            try:
                result = model.predict(image_np)
                detected = True
            except:
                result = image_np
                detected = False

            end = time.time()

            result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

            with col2:
                st.subheader("Kết quả nhận dạng")
                st.image(result, width=500)

                st.markdown(
                    f"""
                    <div class="result-box">
                    ⏱ Thời gian xử lý: <b>{end-start:.2f} giây</b><br>
                    {"✅ Phát hiện biển số thành công" if detected else "❌ Không phát hiện biển số"}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# =====================================================
# 2️⃣ NHẬN DIỆN VIDEO
# =====================================================
elif option == "🎥 Nhận diện video":

    uploaded_video = st.file_uploader(
        "📤 Tải video lên",
        type=["mp4", "avi", "mov"]
    )

    if uploaded_video is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        st.info("Đang xử lý video... Nhấn Stop để dừng.")
        stop = st.button("🛑 Stop")

        while cap.isOpened():
            if stop:
                break

            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (640, 480))

            try:
                frame = model.predict(frame)
            except:
                pass

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame)

        cap.release()
        st.success("Hoàn thành xử lý video.")

# =====================================================
# 3️⃣ WEBCAM REALTIME
# =====================================================
elif option == "📹 Webcam realtime":

    run = st.checkbox("▶️ Bật webcam")

    FRAME_WINDOW = st.image([])

    if run:
        camera = cv2.VideoCapture(0)

        while run:
            ret, frame = camera.read()
            if not ret:
                break

            frame = cv2.resize(frame, (640, 480))

            try:
                frame = model.predict(frame)
            except:
                pass

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)

        camera.release()