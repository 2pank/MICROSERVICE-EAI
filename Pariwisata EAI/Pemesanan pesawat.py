class TiketPesawat:
    def __init__(self, maskapai, tujuan, tanggal, jumlah_penumpang):
        self.maskapai = maskapai
        self.tujuan = tujuan
        self.tanggal = tanggal
        self.jumlah_penumpang = jumlah_penumpang

class PemesananPesawat:
    def __init__(self):
        self.daftar_tiket = []

    def pesan_tiket(self, maskapai, tujuan, tanggal, jumlah_penumpang):
        tiket = TiketPesawat(maskapai, tujuan, tanggal, jumlah_penumpang)
        self.daftar_tiket.append(tiket)

    def tampilkan_daftar_tiket(self):
        if self.daftar_tiket:
            for i, tiket in enumerate(self.daftar_tiket, start=1):
                print(f"=== Tiket Pesawat ke-{i} ===")
                print(f"Maskapai: {tiket.maskapai}")
                print(f"Tujuan: {tiket.tujuan}")
                print(f"Tanggal: {tiket.tanggal}")
                print(f"Jumlah Penumpang: {tiket.jumlah_penumpang}")
                print()
        else:
            print("Belum ada tiket pesawat yang dipesan.")

# Contoh penggunaan aplikasi
if __name__ == "__main__":
    pesanan_pesawat = PemesananPesawat()
    
    pesanan_pesawat.pesan_tiket("Garuda Indonesia", "Jakarta - Bali", "2024-06-15", 2)
    pesanan_pesawat.pesan_tiket("Lion Air", "Surabaya - Jakarta", "2024-07-20", 1)
    
    pesanan_pesawat.tampilkan_daftar_tiket()
