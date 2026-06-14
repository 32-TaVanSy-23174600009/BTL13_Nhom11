import csv
import os

FILE_NAME = "Application_Data.csv"

def save_to_csv(data_row):
    # Tạo header đúng chuẩn yêu cầu của BTL13
    file_exists = os.path.isfile(FILE_NAME)
    header = ["record_id", "timestamp", "username", "ip_address", "login_status", 
              "failed_success_ratio", "login_frequency", "send_time", "receive_time", "delay_ms"]
    
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(data_row)