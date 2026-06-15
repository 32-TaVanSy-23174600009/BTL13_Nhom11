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
