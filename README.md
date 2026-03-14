# 📌 Bài tiểu luận Trí tuệ nhân tạo và học máy
# 📌 Xây dựng ứng dụng nhận dạng biển số xe (License Plate Recognition)
## Phương pháp nhận dạng biển số xe được sử dụng trong đề tài này được xây dựng theo một quy trình gồm 4 bước chính, kết hợp giữa các kỹ thuật phát hiện đối tượng, xử lý ảnh và học sâu nhằm đảm bảo độ chính xác và hiệu quả trong quá trình nhận dạng:
## Bước 1: Xác định vùng chứa biển số xe.
- Ở bước đầu tiên, mô hình YOLOv3-Tiny được sử dụng để phát hiện vị trí của biển số trong ảnh hoặc khung hình video. Đây là một mô hình phát hiện đối tượng có tốc độ xử lý nhanh, phù hợp với các hệ thống yêu cầu xử lý gần thời gian thực.
## Bước 2: Tách các ký tự trên biển số xe.
- Sau khi xác định được vùng biển số, hệ thống tiến hành áp dụng các kỹ thuật xử lý ảnh và thuật toán segmentation để tách riêng từng ký tự trên biển số. Quá trình này giúp chuẩn bị dữ liệu đầu vào cho bước nhận dạng ký tự ở giai đoạn tiếp theo.
## Bước 3: Nhận dạng ký tự bằng mô hình CNN.
- Các ký tự sau khi được tách ra sẽ được đưa vào mô hình Convolutional Neural Network (CNN) để phân loại. Mô hình CNN được huấn luyện để nhận dạng các chữ cái và chữ số trên biển số xe, từ đó xác định chính xác từng ký tự.
## Bước 4: Chuẩn hóa và định dạng biển số xe.
- Ở bước cuối cùng, hệ thống tiến hành sắp xếp và định dạng lại các ký tự đã nhận dạng để tạo thành chuỗi biển số hoàn chỉnh. Đồng thời, hệ thống cũng xác định cấu trúc biển số là một dòng hoặc hai dòng nhằm hiển thị kết quả chính xác theo đúng định dạng thực tế.
