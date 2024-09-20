# Aplikasi Cipher (Vigenere, Playfair, Hill)

Aplikasi ini adalah program Python yang mengimplementasikan tiga jenis cipher: Vigenere, Playfair, dan Hill. Program ini menggunakan antarmuka grafis Tkinter untuk interaksi pengguna.

## Persyaratan

Sebelum menjalankan program, pastikan Anda telah menginstal:

1. Python 3.x (Program ini dikembangkan menggunakan Python 3.8+)
2. Library NumPy

## Cara Instalasi

1. Pastikan Python sudah terinstal di komputer Anda. Anda bisa mengunduhnya dari [python.org](https://www.python.org/downloads/).

2. Instal NumPy dengan menjalankan perintah berikut di terminal atau command prompt:
   ```
   pip install numpy
   ```

## Cara Menjalankan Program

1. Unduh file `cipher_app.py` dari repositori ini.

2. Buka terminal atau command prompt.

3. Navigasikan ke direktori tempat Anda menyimpan `cipher_app.py`.

4. Jalankan program dengan perintah:
   ```
   python cipher_app.py
   ```

5. Antarmuka grafis aplikasi akan muncul.

## Penggunaan

1. Pilih jenis cipher yang ingin Anda gunakan (Vigenere, Playfair, atau Hill) dari dropdown menu.

2. Pilih mode "Enkripsi" atau "Dekripsi".

3. Masukkan kunci (minimal 12 karakter) pada kolom yang tersedia.

4. Masukkan pesan yang ingin dienkripsi atau didekripsi pada area teks.

5. Jika Anda ingin menggunakan file teks sebagai input, klik tombol "Pilih File" dan pilih file .txt yang diinginkan.

6. Klik tombol "Proses" untuk melakukan enkripsi atau dekripsi.

7. Hasil akan ditampilkan pada area teks di bagian bawah aplikasi.

## Catatan Penting

- Untuk Playfair Cipher, huruf 'J' akan otomatis diubah menjadi 'I'.
- Untuk Hill Cipher, program menggunakan matriks 3x3, jadi panjang kunci harus minimal 9 karakter.
- Program hanya akan memproses karakter alfabet dan akan mengabaikan karakter lainnya.

Jika Anda mengalami masalah atau memiliki pertanyaan, silakan buat issue di repositori GitHub ini.

Selamat menggunakan Aplikasi Cipher!