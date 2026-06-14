import subprocess

OUTPUT_FILE = "Packet_Network_Data.csv"

# Lệnh TShark bắt cổng 22 trên tất cả card mạng (bao gồm cả Tailscale)
cmd = f'tshark -i any -f "tcp port 22" -T fields -e frame.time_epoch -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e tcp.len -e frame.len -E header=y -E separator=, > {OUTPUT_FILE}'

print(f"[*] Đang rình bắt gói tin SSH. Dữ liệu ghi vào: {OUTPUT_FILE}")
print("[*] Chờ anh em bắn dữ liệu xong thì bấm Ctrl + C để dừng...")

try:
    subprocess.run(cmd, shell=True)
except KeyboardInterrupt:
    print("\n[*] Đã ngắt bắt gói tin và lưu file thành công!")