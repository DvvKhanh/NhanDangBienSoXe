# 📌 BÀI TIỂU LUẬN TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY
# 📌 XÂY DỰNG ỨNG DỤNG NHẬN DẠNG BIỂN SỐ XE (LICENSE PLATE RECOGNITION)

## Phương pháp nhận dạng biển số xe trong hệ thống được xây dựng gồm 4 bước chính:
- Phát hiện biển số: Sử dụng mô hình YOLOv3-Tiny để xác định vị trí biển số xe trong ảnh hoặc video.
- Tách ký tự: Áp dụng thuật toán segmentation để tách từng ký tự trên biển số.
- Nhận dạng ký tự: Sử dụng mô hình CNN để phân loại các chữ cái và chữ số.
- Định dạng biển số: Sắp xếp lại các ký tự và xác định biển số để tạo kết quả hoàn chỉnh.

## Cài đặt môi trường
