# Bài Tập Lớn Môn Mạng Máy Tính - Nhóm 11 - Đề 13
**Đề tài:** GIÁM SÁT VÀ PHÁT HIỆN TRUY CẬP BẤT THƯỜNG THÔNG QUA  
PHÂN TÍCH AUTH.LOG 


**Thành viên nhóm:**
1. Tạ Văn Sỹ - 23174600009 - DHKL17A1HN (Nhóm trưởng)
2. Nguyễn Huy Hoàng - 23174600010 - DHKL17A1HN
3. Phạm Hồng Ánh - 23174600040 - DHKL17A1HN

**Cấu trúc file:**
- `capture.py`, `analyze...`: Code chạy trên máy chủ Ubuntu.
- `*.csv`: Dữ liệu log và gói tin thu thập được.
- `Trucquanhoa.ipynb`: Code Pandas/Matplotlib vẽ biểu đồ.


**GV hướng dẫn:** [Cao Diệp Thắng]
**Nhóm:** 11 — Lớp DHKL17A1HN

---

### 📁 Cấu trúc thư mục nộp bài

```text
BTL13/
├── analyze_authlog.py       # Phân tích auth.log để bóc tách IP tấn công
├── capture.py               # Chạy nền TShark để bắt traffic mạng LAN ảo
├── collector.py             # Tổng hợp dữ liệu thành định dạng cấu trúc
├── Application_Data.csv     # Dataset tầng ứng dụng (Log đăng nhập SSH)
├── Packet_Network_Data.csv  # Dataset tầng mạng (Thông tin gói tin)
├── Trucquanhoa.ipynb        # Code Jupyter vẽ biểu đồ bằng Pandas/Matplotlib
└── Bao_cao_Nhom_11.pdf      # Báo cáo tổng kết hoàn chỉnh


### 👥 Phân công nhiệm vụ

| Thành viên | Vai trò | Nhiệm vụ chi tiết |
| :--- | :--- | :--- |
| **Tạ Văn Sỹ**<br>(Nhóm trưởng) | Thiết kế hệ thống, Quản lý Data | Triển khai và cấu hình máy chủ Ubuntu Server trên nền tảng VirtualBox. Lập trình `collector.py` — tổng hợp, làm sạch dữ liệu và trực tiếp trích xuất thành 2 bộ dataset chuẩn: `Application_Data.csv` và `Packet_Network_Data.csv`. Quản lý kho lưu trữ mã nguồn trên GitHub. Điều phối tiến độ nhóm. |
| **Nguyễn Huy Hoàng** | Lập trình Python, Trực quan hóa | Lập trình `analyze_authlog.py` — bóc tách nhật ký hệ thống `/var/log/auth.log` để trích xuất IP và trạng thái tấn công. Lập trình toàn bộ `Trucquanhoa.ipynb` — dùng Pandas và Matplotlib để tiền xử lý CSV và vẽ 5 biểu đồ thống kê. Đóng vai Client dùng CMD thực hiện kịch bản tấn công Brute-force. |
| **Phạm Hồng Ánh** | Quản trị mạng, Bắt gói tin & Báo cáo | Thiết kế và triển khai hạ tầng mạng LAN ảo bằng Tailscale (`100.75.21.72`). Lập trình thực thi `capture.py` — tích hợp công cụ TShark chạy ngầm để lắng nghe và bắt các gói tin giao thức TCP/SSH qua cổng 22, Phối hợp đóng vai Client tấn công sinh log. Phân tích kết quả biểu đồ, biên soạn và định dạng báo cáo hoàn chỉnh. |
