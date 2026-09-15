# Website ucapan ulang tahun — versi Streamlit

## Struktur folder
```
birthday-streamlit/
├── app.py              <- jalanin ini
├── template.html       <- desain asli (jangan diubah kecuali emang mau ubah desain)
├── requirements.txt
└── assets/
    ├── videos/         <- taruh video kenangan di sini (.mp4/.webm/.mov)
    └── photos/         <- taruh foto di sini (.jpg/.png/.webp), khusus buat kartu memory match
```

## Cara jalanin
```
pip install -r requirements.txt
streamlit run app.py
```

## Taruh video / foto di mana

**assets/videos/** — isi galeri "Kenangan dalam video".
- Format `.mp4`, `.webm`, atau `.mov`.
- Tiap file otomatis jadi satu kartu di galeri, urut sesuai nama file (kasih nama `01-....mp4`, `02-....mp4` kalau mau urutan tertentu).
- Kosongin folder ini → galeri tetap tampil pakai video contoh (placeholder), bukan error.
- Klip pendek (10–30 detik) dan sudah dikompres. File di-encode base64 dan ikut ditempel ke halaman, jadi makin besar total ukuran video makin berat/lambat halaman dibuka.

**assets/photos/** — isi pasangan kartu di minigame Memory Match.
- Format `.jpg`, `.jpeg`, `.png`, atau `.webp`.
- Minimal 2 foto biar aktif; kalau kurang dari itu, game tetap jalan pakai ikon emoji (default, gak berubah).
- Maksimal 8 foto dipakai (lebih dari itu dipotong ke 8 pertama secara urutan nama file).
- Disarankan foto persegi (crop 1:1) biar rapi di kartu.

Bagian lain (surat, timeline, pesan scratch card, nama pasangan) masih teks placeholder di `template.html` — edit langsung di file itu, cari tanda kurung siku `[...]`.
