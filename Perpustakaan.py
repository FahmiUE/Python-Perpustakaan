import mysql.connector

# Fungsi koneksi ke MYSQL

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "perpus"
)

#Fungsi penambahan buku baru
def registerBuku():
    nama_buku = input("Tulis judul buku: ")
    kode_buku = input("Tulis kode buku: ")
    jumlah_buku = input("Jumlah buku: ")
    kategori = input("Kategori: ")
    data = (nama_buku,kode_buku,jumlah_buku,kategori)
    sql = "INSERT INTO buku(nama_buku,kode_buku,jumlah_buku,kategori) VALUES (%s,%s,%s,%s)"
    mycursor = mydb.cursor()
    mycursor.execute(sql,data)
    mydb.commit()
    print("Data sudah dimasukkan")
    main()

#Fungsi daftar anggota baru   
def registerAnggota():
    nama_anggota= input("Nama: ")
    tgl_lahir= input("Tanggal lahir(YYYY-MM-DD):")
    pekerjaan= input("Pekerjaan:")
    alamat= input("Alamat:")
    data = (nama_anggota,tgl_lahir,pekerjaan,alamat)
    sql = "INSERT INTO anggota (no_id,nama_anggota,tgl_lahir,pekerjaan,alamat) VALUES (%s,%s,%s,%s,)"
    mycursor = mydb.cursor()
    mycursor.execute(sql,data)
    mydb.commit()
    print("Data sudah dimasukkan")
    main()

#Fungsi list anggota yg terdaftar
def daftarAnggota():
    query = "SELECT * FROM anggota"
    mycursor= mydb.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
    
#Fungsi list buku yg tersedia    
def daftarBuku():
    query = "SELECT * FROM buku"
    mycursor= mydb.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
    
#Fungsi list peminjaman    
def daftarPinjam():
    query = "SELECT * FROM pinjam"
    mycursor= mydb.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
    
#Fungsi pencarian judul buku
def cariBuku():
    find = input("Tulis buku yg Anda inginkan: ")
    query = "SELECT nama_buku FROM buku where nama_buku = %s "
    mycursor= mydb.cursor()
    mycursor.execute(query,find)
    result = mycursor.fetchall()
    print(result)

#Fungsi edit stok dimana code=kode buku & pcs=jumlah buku
def editStok(code, pcs):
    query="SELECT jumlah_buku FROM buku WHERE kode_buku = %s "
    data = (code,)
    mycursor = mydb.cursor()
    mycursor.execute(query,data)
    result = mycursor.fetchone()
    jmlh = result[0] + pcs 
    query = "UPDATE buku SET jumlah_buku = %s WHERE kode_buku = %s"
    datanya = (jmlh,code)
    mycursor.execute(query,datanya)
    mydb.commit()
    main()
     
#Fungsi peminjaman buku    
def pinjam():
    nama_anggota = input("Tulis nama Anda : ")
    no_id = input("Tuliskan nomor ID : ")
    kode_buku = input("Tuliskan kode buku yg Anda pinjam: ")
    tgl = input("Tanggal peminjaman(YYYY-MM-DD): ")
    query ="INSERT INTO pinjam(nama_anggota, no_id,kode_buku,tgl_pinjam) VALUES (%s,%s,%s,%s,)"
    data = (nama_anggota,no_id,kode_buku,tgl)
    mycursor = mydb.cursor()
    mycursor.execute(query,data)
    mydb.commit()
    print("Buku telah berhasil dipinjam oleh:", nama_anggota)
    editStok(kode_buku,-1)

#Fungsi Pengembalian buku
def kembalikan():
    nama_anggota = input("Tulis nama Anda : ")
    no_id = input("Tuliskan nomor ID : ")
    kode_buku = input("Tuliskan kode buku yg Anda pinjam: ")
    tgl = input("Tanggal peminjaman(YYYY-MM-DD): ")
    query ="INSERT INTO pinjam(nama_anggota, no_id,kode_buku,tgl_kembali) VALUES (%s,%s,%s,%s,)"
    data = (nama_anggota,no_id,kode_buku,tgl)
    mycursor = mydb.cursor()
    mycursor.execute(query,data)
    mydb.commit()
    print("Buku telah dikembalikan oleh:", nama_anggota)
    editStok(kode_buku, 1)

    
#Fungsi Main
def main():
    print("""--------Perpustakaan WOW---------
      1. Pendaftaran Anggota Baru
      2. Pendaftaran Buku Baru
      3. Peminjaman
      4. Daftar Buku
      5. Daftar Anggota
      6. Daftar Pinjam
      7. Cari Buku
      8. Pengembalian
      9. Exit
      """)

pilihan = input("Masukan pilihan no:")
if(pilihan == '1'): 
    registerAnggota()
elif(pilihan =='2'):
    registerBuku()
elif(pilihan =='3'):
    pinjam()
elif(pilihan =='4'):
    daftarBuku()
elif(pilihan =='5'):
    daftarAnggota()
elif(pilihan =='6'):
    daftarPinjam()
elif(pilihan =='7'):
    cariBuku()
elif(pilihan =='8'):
    kembalikan()
else :
    exit        