def validasi_nilai(nilai):
    try:
        nilai = float(nilai)

        if 0 <= nilai <= 100:
            return True

        return False

    except (ValueError, TypeError):
        return False


def baca_data(nama_file):
    data_siswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):

                if not baris.strip():
                    continue

                bagian = baris.strip().split(",")

                if len(bagian) != 2:
                    print(f"Baris {nomor} tidak valid.")
                    continue

                nama = bagian[0].strip()
                nilai = bagian[1].strip()

                if not nama:
                    print(f"Nama pada baris {nomor} kosong.")
                    continue

                if not validasi_nilai(nilai):
                    print(f"Nilai pada baris {nomor} tidak valid.")
                    continue

                data_siswa.append({
                    "nama": nama,
                    "nilai": float(nilai)
                })

    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

    except OSError as error:
        print(f"Terjadi kesalahan saat membaca file: {error}")

    return data_siswa