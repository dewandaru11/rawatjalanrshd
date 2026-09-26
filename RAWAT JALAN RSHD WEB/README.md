# Website Rawat Jalan RSHD

Starter project Flask berdasarkan desain referensi yang diberikan.

## Isi fitur
- Beranda responsif
- Informasi, Poliklinik, Jadwal Dokter, Alur Pelayanan, Kontak
- Formulir pendaftaran online (demo, belum tersambung database)
- Halaman login (placeholder)
- Data poli contoh yang mudah diganti di `app.py`

## Menjalankan di komputer
1. Install Python 3.10 atau lebih baru.
2. Buka terminal pada folder proyek.
3. Buat virtual environment:
   - Windows: `py -m venv venv`
   - Aktifkan: `venv\\Scripts\\activate`
4. Install: `pip install -r requirements.txt`
5. Jalankan: `python app.py`
6. Buka `http://127.0.0.1:5000`

## Penting sebelum dipublikasikan
- Ganti nama/alamat/telepon/email dan seluruh jadwal/dokter contoh dengan data resmi.
- Form pendaftaran saat ini hanya demo, belum menyimpan data dan belum memberi nomor antrean resmi.
- Jangan mengumpulkan NIK atau data kesehatan melalui website publik sebelum database, HTTPS, persetujuan privasi, kontrol akses, dan perlindungan data disiapkan.
- Ganti `app.secret_key` dengan nilai acak yang aman dan simpan sebagai environment variable.
- Aktifkan autentikasi admin, validasi server, CSRF protection, pembatasan percobaan login, dan audit log sebelum produksi.
