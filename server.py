import socket
from generated_codec import TelemetryData

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen(1)
    print("Serwer TCP uruchomiony. Oczekiwanie na dane...")

    conn, addr = server_socket.accept()
    print(f"Połączono z: {addr}")

    try:
        while True:
            data = conn.recv(12)
            if not data:
                break
            
            received_packet = TelemetryData.deserialize(data)
            print(f"[Serwer odebrał]: {received_packet}")
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    run_server()