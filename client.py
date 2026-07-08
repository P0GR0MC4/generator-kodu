import socket
import time
from generated_codec import TelemetryData

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65432))
    print("Połączono z serwerem TCP.")

    packets = [
        TelemetryData(device_id=101, temperature=24.5, status_code=200),
        TelemetryData(device_id=102, temperature=89.2, status_code=500),
        TelemetryData(device_id=103, temperature=15.0, status_code=200)
    ]

    try:
        for packet in packets:
            print(f"[Klient wysyła]: {packet}")
            binary_data = packet.serialize()
            client_socket.sendall(binary_data)
            time.sleep(1)
    finally:
        client_socket.close()
        print("Połączenie zamknięte.")

if __name__ == "__main__":
    run_client()