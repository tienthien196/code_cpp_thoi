import os
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Đường dẫn thư mục muốn chia sẻ
SHARE_FOLDER = r"C:\Users\ASUS\Downloads\cross"

# Cổng (có thể đổi nếu 8000 bị chiếm)
PORT = 8000

def get_local_ip():
    """Lấy địa chỉ IP LAN của máy (dạng 192.168.x.x hoặc 10.x.x.x)"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Không gửi dữ liệu thật, chỉ để lấy IP
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"

if __name__ == "__main__":
    # Chuyển đến thư mục cần chia sẻ
    if not os.path.exists(SHARE_FOLDER):
        print(f"[!] Thư mục không tồn tại: {SHARE_FOLDER}")
        exit(1)

    os.chdir(SHARE_FOLDER)
    print(f"📁 Đang chia sẻ thư mục: {SHARE_FOLDER}")
    
    ip = get_local_ip()
    print(f"🔗 Truy cập từ máy khác trong cùng mạng tại: http://{ip}:{PORT}")
    print("⚠️  ĐỪNG tắt cửa sổ này trong khi đang chia sẻ!")
    print("-" * 50)

    # Khởi động server
    try:
        server = HTTPServer(("", PORT), SimpleHTTPRequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️  Đã dừng chia sẻ.")