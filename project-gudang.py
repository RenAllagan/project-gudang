class Barang:
    def __init__(self, nama, kategori, harga, jumlah):
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.jumlah = jumlah

    def cetak(self):
        print(f"Nama : {self.nama}")
        print(f"kategori: {self.kategori}")
        print(f"Harga: {self.harga}")
        print(f"Jumlah: {self.jumlah}")


class GudangABC:
    def __init__(self, nama):
        self.nama = nama
        self.data_barang = []

    def tambah_barang(self, barang):
        self.data_barang.append(barang)

    # Pencarian barang berdasarkan nama dan kategori
    def cari_barang(self, namabarang):
        for barang in self.data_barang:
            if barang.nama == namabarang:
                return barang
        return None

    def keluarkan_barang(self, nama, jumlah):
        barang = self.cari_barang(nama)
        if barang:
            if barang.jumlah >= jumlah:
                total_harga = barang.harga * jumlah
                barang.jumlah -= jumlah
                print(
                    f"\nBarang {barang.nama} sejumlah {jumlah} telah dikeluarkan dengan total harga {total_harga}."
                )
            else:
                print("Jumlah barang tidak mencukupi.")
        else:
            print("Barang tidak ditemukan.")

    def simpan_barang(self):
        print("\nSimpan data barang baru:")
        nama_barang = input("Masukkan nama barang: ")
        kategori_barang = input("Masukkan kategori barang: ")
        harga_barang = int(input("Masukkan harga barang: "))
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        barang_baru = Barang(nama_barang, kategori_barang, harga_barang, jumlah_barang)
        self.tambah_barang(barang_baru)
        print(f"\nBarang {nama_barang} berhasil disimpan di gudang {self.nama}.")

    def penutup(self):
        print("\nTerimakasi Sudah Memakai Program kami!")


gudang = GudangABC("Gudang PT ABC")

# Menambahkan barang ke gudang
gudang.tambah_barang(Barang("Komputer ABC", "Komputer", 10000000, 10))
gudang.tambah_barang(Barang("Switch ABC", "Switch", 5000000, 20))
gudang.tambah_barang(Barang("Kabel Jaringan ABC", "Kabel Jaringan", 1000000, 50))
gudang.tambah_barang(Barang("Access Point ABC", "Access Point", 2000000, 30))
gudang.tambah_barang(Barang("Router ABC", "Router", 3000000, 15))

print("\nDaftar Barang di Gudang:\n")
for barang in gudang.data_barang:
    barang.cetak()
    print()

barang_cari = gudang.cari_barang("Kabel Jaringan ABC")
if barang_cari:
    print(f"Barang {barang_cari.nama} ditemukan.")
    print("\nData barang yang telah ditemukan:")
    barang_cari.cetak()

else:
    print("Barang tidak ditemukan.")

# Mengeluarkan barang
gudang.keluarkan_barang("Kabel Jaringan ABC", 20)

# Menyimpan barang baru
gudang.simpan_barang()
