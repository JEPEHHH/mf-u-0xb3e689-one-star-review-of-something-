# Rencana Kerja: One-Star Review of Something Essential

## Tujuan & Kriteria
Menghasilkan program `program/v1` yang menulis satu baris ulasan bintang satu (*deadpan*, 1–160 karakter UTF-8, tanpa baris baru/whitespace kosong) tentang hal esensial sehari-hari (matahari, gravitasi, tidur, air, oksigen, Senin, dsb.) ke `/output/entry.txt`.
Prioritas penilaian juri:
1. Jelas berupa ulasan 1-bintang atas hal esensial sehari-hari.
2. Menemukan keluhan nyata paling tajam yang akrab tapi jarang diucapkan.
3. Menjaga nada *deadpan* murni (tanpa kedipan, penjelasan, atau tanda seru).
4. Membalikkan ekspektasi (*turn/sting*) di beberapa kata terakhir.
5. Padat, spesifik, satu lelucon bersih (ukuran byte lebih kecil menguntungkan *tie-break*).

## Tahapan Kerja (Commit tiap Milestone)
1. **Eksplorasi & Seleksi Kandidat**: Menyusun daftar kandidat ulasan lintas topik esensial, lalu menyaringnya menggunakan rubrik 5 kriteria juri dan perbandingan berpasangan.
2. **Inisialisasi Lisensi & Entrypoint**: Membuat `LICENSE` (SPDX MIT) dan mengimplementasikan `main.py` untuk menulis teks terpilih ke `/output/entry.txt` (mendukung direktori output lokal/sandbox).
3. **Iterasi & Penyempurnaan Teks**: Melakukan minimal 2 siklus revisi pada teks di `main.py` guna menajamkan *turn* akhir, menghilangkan kata mubazir, dan memenuhi syarat *transcript gate* (`thinking_revised`).
4. **Pengujian & Verifikasi Gate**: Menjalankan uji otomatis lokal (UTF-8, panjang 1–160 karakter, satu baris, non-whitespace) dan pengecekan pra-submit melalui CLI kit.

## Daftar Berkas yang Akan Dibuat
- `PLAN.md` — Dokumen rencana kerja dan daftar berkas ini.
- `LICENSE` — Lisensi OSI-approved (`SPDX-License-Identifier: MIT`) sesuai syarat kompetisi.
- `main.py` — Entrypoint `program/v1` (Python 3.13) yang menulis ulasan final ke `/output/entry.txt`.
- `reviews.md` — Catatan eksplorasi kandidat ulasan dan evaluasi pairwise terhadap kriteria juri.
- `tests/test_entry.py` — Skrip validasi lokal untuk memastikan output lolos gate dan deterministik.
