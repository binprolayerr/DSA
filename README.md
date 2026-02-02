# DSA - Thực Nghiệm Các Giải Thuật Sắp Xếp Nội

## 1. Giới thiệu
Thực nghiệm tập trung vào việc so sánh hiệu năng của các thuật toán sắp xếp phổ biến trên Python với bộ dữ liệu lớn.

Mục tiêu là đánh giá tốc độ xử lý của các thuật toán với các dạng dữ liệu đầu vào khác nhau (tăng dần, giảm dần, ngẫu nhiên) và các kiểu dữ liệu khác nhau (số thực, số nguyên).

## 2. Thông tin sinh viên
* **Họ và tên:** Nguyễn Phúc Bình Minh
* **MSSV:** 25521120
* **Bài báo cáo:** [25521120-Nguyễn Phúc Bình Minh-Thực nghiệm các giải thuật sắp xếp nội.pdf]

## 3. Các thuật toán được kiểm thử
Chương trình thực hiện so sánh thời gian chạy của các thuật toán sau:
1.  **Quick Sort**
2.  **Heap Sort**
3.  **Merge Sort**
4.  **NumPy Sort** (Thư viện của Python)

## 4. Cấu trúc thư mục
* `main.py`: File mã nguồn chính để thực thi các thuật toán và đo đạc thời gian.
* `sinhtest.py`: Script dùng để sinh bộ dữ liệu thử nghiệm.
* `input.zip`: Bộ dữ liệu thử nghiệm chuẩn đã được nén. **Cần giải nén trước khi chạy**.
* `25521120-Nguyễn Phúc Bình Minh-Thực nghiệm các giải thuật sắp xếp nội.pdf`: Báo cáo chi tiết kết quả thực nghiệm và phân tích.

## 5. Mô tả bộ dữ liệu (Dataset)
Bộ dữ liệu bao gồm **10 dãy số**, mỗi dãy chứa **1 triệu phần tử**, được chia thành các trường hợp sau:

* **Dãy 1:** Số thực (Float) - Sắp xếp tăng dần.
* **Dãy 2:** Số thực (Float) - Sắp xếp giảm dần.
* **Dãy 3 – 5:** Số thực (Float) - Ngẫu nhiên.
* **Dãy 6 – 10:** Số nguyên (Int) - Ngẫu nhiên.
