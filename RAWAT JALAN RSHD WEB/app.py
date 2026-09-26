from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ganti-dengan-secret-key-anda"

# Data contoh. Ganti dengan data resmi RSUD H. Damanhuri.
POLI = [
    {"nama": "Poli Penyakit Dalam", "dokter": "dr. Nama Dokter, Sp.PD", "jadwal": "Senin–Jumat, 08.00–12.00"},
    {"nama": "Popy ppli Anak", "dokter": "dr. Nama Dokter, Sp.A", "jadwal": "Senin–Kamis, 08.00–12.00"},
    {"nama": "Poli Bedah", "dokter": "dr. Nama Dokter, Sp.B", "jadwal": "Senin, Rabu, Jumat, 08.00–12.00"},
    {"nama": "Poli Kebidanan & Kandungan", "dokter": "dr. Nama Dokter, Sp.OG", "jadwal": "Senin–Jumat, 08.00–12.00"},
    {"nama": "Poli Saraf", "dokter": "dr. Nama Dokter, Sp.N", "jadwal": "Selasa dan Kamis, 08.00–12.00"},
    {"nama": "Poli Gigi", "dokter": "drg. Nama Dokter", "jadwal": "Senin–Jumat, 08.00–12.00"},
]

@app.route("/")
def beranda():
    return render_template("index.html", title="Beranda", poli=POLI[:4])

@app.route("/informasi")
def informasi():
    return render_template("informasi.html", title="Informasi")

@app.route("/poliklinik")
def poliklinik():
    return render_template("poliklinik.html", title="Poliklinik", poli=POLI)

@app.route("/jadwal-dokter")
def jadwal_dokter():
    return render_template("jadwal.html", title="Jadwal Dokter", poli=POLI)

@app.route("/alur-pelayanan")
def alur_pelayanan():
    return render_template("alur.html", title="Alur Pelayanan")

@app.route("/kontak")
def kontak():
    return render_template("kontak.html", title="Kontak")

@app.route("/daftar-online", methods=["GET", "POST"])
def daftar_online():
    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        nik = request.form.get("nik", "").strip()
        telepon = request.form.get("telepon", "").strip()
        poli_pilihan = request.form.get("poli", "").strip()
        tanggal = request.form.get("tanggal", "").strip()
        no_rm = request.form.get("no_rm", "").strip()

        if not all([nama, nik, telepon, poli_pilihan, tanggal]):
            flash("Mohon lengkapi seluruh kolom wajib.", "error")
        else:
            # DEMO: belum menyimpan ke database dan belum menghasilkan nomor antrean resmi.
            flash("Formulir demo berhasil dikirim. Ini belum merupakan pendaftaran resmi; silakan konfirmasi ke petugas RSUD.", "success")
            return redirect(url_for("daftar_online"))
    return render_template("daftar.html", title="Daftar Online", poli=POLI)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Login belum diaktifkan. Hubungkan dengan sistem autentikasi dan database sebelum digunakan.", "error")
    return render_template("login.html", title="Login")

@app.route("/health")
def health():
    return {
    "status": "ok",
    "app": "RSUD H. Damanhuri Barabai"
}

if __name__ == "__main__":
    app.run(debug=True)
