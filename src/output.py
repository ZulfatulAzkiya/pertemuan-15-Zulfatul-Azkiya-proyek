import os


def buat_laporan(statistik):
    laporan = (
        "HASIL ANALISIS NILAI MATEMATIKA\n"
        "================================\n"
        f"Jumlah siswa: {statistik['jumlah']}\n"
        f"Rata-rata: {statistik['rata_rata']:.2f}\n"
        f"Nilai tertinggi: {statistik['tertinggi']}\n"
        f"Nilai terendah: {statistik['terendah']}\n"
        f"Siswa tuntas: {statistik['tuntas']}\n"
        f"Siswa belum tuntas: {statistik['belum_tuntas']}\n"
    )

    return laporan


def tampilkan_laporan(teks):
    print(teks)


def simpan_laporan(teks):
    os.makedirs("output", exist_ok=True)

    nama_file = "output/hasil_analisis.txt"

    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write(teks)

        print(f"Laporan berhasil disimpan di {nama_file}.")

    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")