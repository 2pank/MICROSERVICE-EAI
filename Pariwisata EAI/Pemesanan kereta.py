class TiketKereta:
    def __init__(self, nama_penumpang, tujuan, tanggal_keberangkatan, jumlah_tiket):
        self.nama_penumpang = nama_penumpang
        self.tujuan = tujuan
        self.tanggal_keberangkatan = tanggal_keberangkatan
        self.jumlah_tiket = jumlah_tiket

class PemesananKereta:
    def __init__(self):
        self.daftar_tiket = []

    def pesan_tiket(self, nama_penumpang, tujuan, tanggal_keberangkatan, jumlah_tiket):
        tiket = TiketKereta(nama_penumpang, tujuan, tanggal_keberangkatan, jumlah_tiket)
        self.daftar_tiket.append(tiket)

    def tampilkan_daftar_tiket(self):
        if self.daftar_tiket:
            for i, tiket in enumerate(self.daftar_tiket, start=1):
                print(f"=== Tiket Kereta ke-{i} ===")
                print(f"Nama Penumpang: {tiket.nama_penumpang}")
                print(f"Tujuan: {tiket.tujuan}")
                print(f"Tanggal Keberangkatan: {tiket.tanggal_keberangkatan}")
                print(f"Jumlah Tiket: {tiket.jumlah_tiket}")
                print()
        else:
            print("Belum ada tiket kereta yang dipesan.")

# Contoh penggunaan aplikasi
if __name__ == "__main__":
    pesanan_kereta = PemesananKereta()
    
    pesanan_kereta.pesan_tiket("John Doe", "Jakarta - Surabaya", "2024-06-15", 2)
    pesanan_kereta.pesan_tiket("Jane Smith", "Yogyakarta - Bandung", "2024-07-20", 1)
    
    pesanan_kereta.tampilkan_daftar_tiket()
