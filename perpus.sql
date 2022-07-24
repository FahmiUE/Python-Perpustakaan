create schema perpus;
use perpus;

CREATE TABLE buku(
nama_buku VARCHAR(80),
kode_buku INT NOT NULL PRIMARY KEY,
jumlah_buku INT,
kategori VARCHAR(30)
);


CREATE TABLE anggota(
no_id INT AUTO_INCREMENT PRIMARY KEY,
nama_anggota VARCHAR(60),
tgl_lahir DATE,
pekerjaan VARCHAR(40),
alamat VARCHAR(100)
);

CREATE TABLE pinjam(
nama_anggota VARCHAR(60),
no_id INT,
kode_buku INT,
tgl_pinjam DATE, 
tgl_kembali DATE,
PRIMARY KEY (no_id, kode_buku),
FOREIGN KEY (no_id) REFERENCES anggota(no_id) ON DELETE CASCADE,
FOREIGN KEY (kode_buku) REFERENCES buku(kode_buku) ON DELETE CASCADE
);