## Program untuk scan port yang terbuka ##

# Import port yang diperlukan
import socket
from typing import List

# Model
class Scanner:
    # Inisialisasi model dengan target IP dan daftar port terbuka
    def __init__(self, target_ip: str):
        self.target_ip = target_ip
        self.open_ports = []

    def scan_ports(self, start_port: int, end_port: int):
        # Melakukan pemindaian port dari port_awal hingga port_akhir
        for port in range(start_port, end_port + 1):
            # Memeriksa apakah port tersebut terbuka
            if self.is_port_open(port):
                # Jika terbuka, tambahkan ke daftar port_terbuka
                self.open_ports.append(port)

    def is_port_open(self, port: int) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((self.target_ip, port))
            # Jika koneksi berhasil, port terbuka
            return True
        except (socket.timeout, ConnectionRefusedError):
            # Jika koneksi gagal atau ditolak, port tertutup
            return False

    def get_open_ports(self) -> List[int]:
        # Mengembalikan daftar port terbuka setelah pemindaian
        return self.open_ports


# View
class InputView:
    def __init__(self, target_ip: str):
        self.target_ip = target_ip

    def get_target_ip(self) -> str:
        return self.target_ip


class OutputView:
    @staticmethod
    def display_open_ports(open_ports: List[int]):
        if not open_ports:
            # Jika tidak ada port terbuka, tampilkan pesan
            print("Tidak ada port terbuka ditemukan.")
        else:
            # Jika ada port yang terbuka, maka tampilkan
            print("Port terbuka:")
            for port in open_ports:
                print(f"[+] {port}")


# Controller
class PortScannerController:
    def __init__(
        self, scanner: Scanner, input_view: InputView, output_view: OutputView
    ):
        self.scanner = scanner
        self.input_view = input_view
        self.output_view = output_view

    def scan_ports(self, start_port: int, end_port: int):
        self.scanner.scan_ports(start_port, end_port)
        self.output_view.display_open_ports(self.scanner.get_open_ports())

# Fungsi utama
def main():
    target_ip = input("Masukkan IP: ")
    start_port = 1
    end_port = 1024

    scanner = Scanner(target_ip)
    input_view = InputView(target_ip)
    output_view = OutputView()
    controller = PortScannerController(scanner, input_view, output_view)

    controller.scan_ports(start_port, end_port)


if __name__ == "__main__":
    main()
