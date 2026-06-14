import time
import re
import random
from datetime import datetime, timedelta
from collector import save_to_csv

log_file = "/var/log/auth.log"
stats = {'failed': 0, 'success': 0, 'freq': 0}
record_id = 1

print(f"[*] Đang giám sát {log_file}...")
with open(log_file, "r") as f:
    # Nhảy đến cuối file để chỉ đọc log mới từ bây giờ
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue

        # Dùng Regex tóm sự kiện Failed hoặc Accepted
        match = re.search(r'(Failed|Accepted) password for (?:invalid user )?(.*?) from (.*?) port', line)
        if match:
            status = "Failed" if match.group(1) == "Failed" else "Success"
            username = match.group(2)
            ip_address = match.group(3)
            
            if status == "Failed": stats['failed'] += 1
            else: stats['success'] += 1
            stats['freq'] += 1
            
            # Tính tỉ lệ Failed/Success
            ratio = round(stats['failed'] / (stats['success'] if stats['success'] > 0 else 1), 2)
            
            # Giả lập tham số mạng để khớp với log ứng dụng
            now = datetime.now()
            delay_ms = random.randint(40, 90)
            receive_time = now
            send_time = receive_time - timedelta(milliseconds=delay_ms)
            
            row = [
                record_id,
                now.strftime("%Y-%m-%d %H:%M:%S"),
                username, ip_address, status, f"{ratio:.2f}", stats['freq'],
                send_time.strftime("%H:%M:%S.%f")[:-3],
                receive_time.strftime("%H:%M:%S.%f")[:-3],
                delay_ms
            ]
            
            save_to_csv(row)
            print(f"[{record_id}] Bắt được: {status} | IP: {ip_address} | User: {username}")
            record_id += 1