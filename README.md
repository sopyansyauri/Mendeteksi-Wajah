Program Mendeteksi Wajah
=====

Pengguna Linux:


1. Masuk Terminal `CTRL+Alt+t`:

2. Masukan perintah `git clone`:
```
git clone https://github.com/sopyansyauri/Mendeteksi-Wajah.git
```

3. Masuk directory:
```
cd Mendeteksi-Wajah/
```

4. Membuat `Virtual-Environment` Python:
```
python3 -m venv nama-env
```

5. Aktifkan Virtual Environment:
```
source nama-env/bin/activate
```

6. Setelah itu install library yang di butuhkan:
```
pip install -r requirement.txt
```

7. Ganti kata `env` di file main.py, Sesuai dengan nama Virtual Environment yang dibuat:
<img src="gambar/edit.png">

8. Masukan `File Gambar` ke folder gambar

9. Lalu, jalankan program nya:
```
python3 main.py gambar/<path-file>
```