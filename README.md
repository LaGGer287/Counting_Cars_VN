# Dự án Đếm Lưu Lượng Xe

Dự án này sử dụng Python để nhận diện và đếm các phương tiện như xe máy, ô tô, xe bus với bộ dữ liệu tự huấn luyện.

## Tính năng

- Nhận diện các loại phương tiện giao thông: xe máy, ô tô, xe bus
- Đếm số lượng phương tiện di chuyển qua một khu vực cụ thể
- Hiển thị kết quả theo thời gian thực
- Ghi lại dữ liệu lưu lượng xe cho phân tích sau này

## Công nghệ sử dụng

- Python cho xử lý dữ liệu và nhận diện hình ảnh
- OpenCV cho xử lý hình ảnh
- Ultralytics YOLOv8 cho mô hình nhận diện
- Roboflow cho việc huấn luyện dữ liệu
- Matplotlib cho hiển thị kết quả
- Pandas cho xử lý và lưu trữ dữ liệu

## Phần cứng và yêu cầu hệ thống

- Máy tính có GPU để tăng tốc quá trình huấn luyện và dự đoán (khuyến nghị)
- Camera để thu thập dữ liệu video hoặc hình ảnh

## Cách sử dụng

1. Clone lại repository:
    ```sh
    git clone https://github.com/LaGGer287/Vehicle_Count.git
    ```

2. Di chuyển đến thư mục dự án:
    ```sh
    cd Vehicle_Count
    ```

3. Cài đặt các thư viện cần thiết:
    ```sh
    pip install -r requirements.txt
    ```

4. Chuẩn bị bộ dữ liệu:
    - Thu thập và gán nhãn dữ liệu hình ảnh/video các phương tiện (xe máy, ô tô, xe bus)
    - Có thể sử dụng file video để ở trong link drive

5. Huấn luyện mô hình:
    - Nếu bạn sử dụng dữ liệu của mình, hãy chuẩn bị dữ liệu và huấn luyện mô hình trên Roboflow
    - Nếu bạn không có dữ liệu của mình, bạn có thể sử dụng mô hình đã được huấn luyện sẵn trong file `best2.pt`.

6. Sử dụng mô hình để đếm lưu lượng xe:
    - 1: Sử dụng file GUI.py để tiến hành chạy chương trình 
    - 2: Kết nối camera và bắt đầu nhận diện và đếm phương tiện theo thời gian thực

Chúc bạn sử dụng dự án thành công!
