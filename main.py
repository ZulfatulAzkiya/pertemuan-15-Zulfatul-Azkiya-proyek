import os

from src.input_data import baca_data
from src.proses import hitung_statistik
from src.output import buat_laporan, tampilkan_laporan, simpan_laporan


def main():
    lokasi_folder = os.path.dirname(os.path.abspath(__file__))
    file_data = os.path.join(
        lokasi_folder,
        "data",
        "contoh_data.txt"
    )

    data = baca_data(file_data)

    statistik = hitung_statistik(data)

    if statistik is None:
        print("Tidak ada data nilai yang valid.")
        return

    laporan = buat_laporan(statistik)

    tampilkan_laporan(laporan)

    simpan_laporan(laporan)


if __name__ == "__main__":
    main()