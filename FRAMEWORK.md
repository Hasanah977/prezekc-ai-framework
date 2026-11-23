
# PREZEKC AI FRAMEWORK

> Universal AI-Assisted System Analysis & Software Development Framework

**Versi:** 0.1.0  
**Status:** Initial Development  
**Jenis:** Universal AI Governance & Project Lifecycle Framework

---

## 1. Pendahuluan

PREZEKC AI adalah framework universal berbantuan
kecerdasan buatan yang dirancang untuk mendukung
proses analisis, penelitian, rekayasa kebutuhan,
perancangan, implementasi, pengujian, deployment,
dan pemeliharaan proyek.

PREZEKC AI tidak terikat pada satu bahasa pemrograman,
platform, industri, atau teknologi tertentu.

Framework ini dapat digunakan untuk:
- Sistem informasi berbasis web.
- Aplikasi Android.
- Aplikasi iOS.
- Aplikasi mobile cross-platform.
- Sistem backend dan API.
- Penelitian dan dokumentasi akademik.
- Proyek perangkat lunak lainnya.

AI berperan sebagai asisten analisis dan pelaksanaan.
Manusia tetap bertanggung jawab atas keputusan
dan persetujuan akhir.

## 2. Tujuan Framework

PREZEKC AI dikembangkan untuk:

1. Membantu identifikasi masalah secara sistematis.
2. Menganalisis proses dan sistem yang sudah berjalan.
3. Melakukan studi komparasi berbasis bukti.
4. Mengidentifikasi kebutuhan pengguna.
5. Menghasilkan dokumen PRD yang terstruktur.
6. Mengembangkan PRD menjadi SRS yang terukur.
7. Menjaga keterlacakan kebutuhan antar dokumen.
8. Mendukung perancangan arsitektur dan UI/UX.
9. Membantu implementasi berbagai jenis aplikasi.
10. Menjamin setiap hasil melalui prosedur verifikasi.
11. Mendokumentasikan keputusan dan perubahan proyek.
12. Mendukung kolaborasi manusia dan AI.

## 3. Prinsip Utama

### 3.1 Analysis First

AI harus memahami permasalahan, tujuan, pengguna,
dan batasan proyek sebelum menyusun solusi.

### 3.2 Human-Centered Decision Making

Keputusan penting harus disetujui manusia,
terutama perubahan ruang lingkup, kebutuhan,
arsitektur kritis, dan penerimaan hasil akhir.

### 3.3 Evidence-Based Research

Informasi penelitian harus berasal dari
sumber yang dapat diperiksa.

AI dilarang mengarang:
- Hasil wawancara.
- Data observasi.
- Referensi ilmiah.
- Statistik.
- Hasil pengujian.
- Fakta tentang sistem pembanding.

### 3.4 Requirement Traceability

Setiap kebutuhan memiliki identitas yang
dapat ditelusuri dari analisis hingga pengujian.

### 3.5 PRD-to-SRS Transformation

SRS harus dikembangkan dari PRD yang
telah disetujui.

Kebutuhan SRS tidak boleh bertentangan
dengan ruang lingkup PRD.

### 3.6 Modular AI Workflow

Pekerjaan dibagi menjadi agents, skills,
rules, templates, dan workflows.

Modul dipilih berdasarkan jenis proyek.

### 3.7 Verified Implementation

AI tidak boleh menyatakan tugas selesai
tanpa memeriksa hasil sesuai kriteria
penerimaan yang relevan.

## 4. Arsitektur Framework

PREZEKC AI terdiri atas tujuh komponen.

### 4.1 Human Controller

Pengguna yang menentukan:
- Tujuan proyek.
- Ruang lingkup.
- Prioritas.
- Batasan.
- Persetujuan dokumen.
- Keputusan pengembangan.

### 4.2 Project Orchestrator

Komponen logis yang bertanggung jawab untuk:
- Memahami instruksi pengguna.
- Mengidentifikasi jenis proyek.
- Memilih workflow.
- Mengarahkan penggunaan skills.
- Memeriksa ketergantungan tugas.
- Memantau status pekerjaan.

Pada versi 0.1.0, orkestrasi dilakukan
melalui prosedur dan instruksi AI.

Orkestrasi otomatis belum diimplementasikan.

### 4.3 Governance Layer

Mengatur:
- Kewenangan AI.
- Persetujuan manusia.
- Keamanan.
- Batas perubahan.
- Manajemen risiko.
- Audit keputusan.

Spesifikasi: core/governance.md

### 4.4 Context Management

Mengelola:
- Informasi proyek.
- Kebutuhan.
- Keputusan.
- Riwayat perubahan.
- Tugas aktif.
- Masalah yang belum terselesaikan.

Konteks penting harus tersimpan dalam
dokumen proyek, bukan hanya percakapan AI.

### 4.5 Agent & Skill Layer

Agents menentukan tanggung jawab pekerjaan.

Skills menentukan prosedur khusus
untuk menyelesaikan pekerjaan tersebut.

Contoh agents:
- Research Agent.
- System Analyst.
- Requirements Engineer.
- System Architect.
- Development Engineer.
- Quality Assurance Engineer.

Agent merupakan definisi peran logis,
bukan jaminan adanya proses AI terpisah.

### 4.6 Workflow Engine

Mengatur urutan pekerjaan dan
ketergantungan antar tahapan.

Spesifikasi: core/workflow.md

### 4.7 Verification Engine

Menentukan apakah pekerjaan sudah
memenuhi kriteria penerimaan.

Spesifikasi: core/verification.md

## 5. Project Lifecycle

PREZEKC AI menggunakan sembilan fase utama.

| Fase | Nama | Hasil |
|---|---|---|
| 01 | Existing System Analysis | Analisis Sistem Berjalan |
| 02 | Comparative Study | Studi Komparasi |
| 03 | Requirement Analysis | Analisis Kebutuhan |
| 04 | Product Requirements | PRD |
| 05 | Software Requirements | SRS |
| 06 | System Design | Dokumen Perancangan |
| 07 | Implementation | Sistem atau aplikasi |
| 08 | Testing & Verification | Laporan Pengujian |
| 09 | Deployment & Maintenance | Rilis dan dokumentasi |

Setiap fase memiliki:
- Input.
- Aktivitas.
- Output.
- Kriteria penerimaan.
- Status verifikasi.

Fase dapat disesuaikan dengan jenis proyek,
tetapi fase yang dilewati harus disertai alasan.

## 6. Standar Enam Dokumen Utama

### 6.1 Analisis Sistem Berjalan

Minimal berisi:
- Gambaran organisasi atau proses.
- Aktor yang terlibat.
- Alur proses saat ini.
- Teknologi yang digunakan.
- Masalah dan kendala.
- Penyebab dan dampak masalah.
- Bukti dan batasan temuan.

### 6.2 Studi Komparasi

Minimal berisi:
- Sistem atau solusi pembanding.
- Sumber referensi.
- Fitur dan karakteristik.
- Kelebihan.
- Kekurangan.
- Relevansi terhadap proyek.
- Peluang pengembangan.

### 6.3 Analisis Kebutuhan

Minimal berisi:
- Stakeholder.
- Kebutuhan pengguna.
- Kebutuhan bisnis.
- Kebutuhan data.
- Prioritas kebutuhan.
- Batasan dan asumsi.
- Risiko yang teridentifikasi.

### 6.4 Product Requirements Document (PRD)

Minimal berisi:
- Ringkasan produk.
- Latar belakang masalah.
- Tujuan produk.
- Target pengguna.
- Ruang lingkup.
- Fitur utama.
- User stories.
- Prioritas.
- Indikator keberhasilan.
- Acceptance criteria tingkat produk.

### 6.5 Software Requirements Specification (SRS)

Minimal berisi:
- Pendahuluan dan ruang lingkup.
- Deskripsi umum sistem.
- Kebutuhan fungsional.
- Kebutuhan nonfungsional.
- Aktor dan hak akses.
- Aturan bisnis.
- Kebutuhan data.
- Integrasi eksternal.
- Batasan sistem.
- Acceptance criteria yang dapat diuji.

### 6.6 Dokumen Perancangan

Minimal berisi elemen yang relevan:
- Arsitektur sistem.
- Use Case Diagram.
- Activity Diagram.
- Sequence Diagram.
- Entity Relationship Diagram.
- Desain database.
- Rancangan API.
- UI/UX.
- Rancangan keamanan.
- Keputusan teknologi.

Diagram yang tidak relevan dengan
jenis proyek dapat dikecualikan
dengan alasan yang didokumentasikan.

## 7. PRD-to-SRS Transformation

PRD merupakan sumber kebutuhan tingkat produk.

SRS menjelaskan perilaku sistem secara
lebih rinci dan dapat diuji.

### Prosedur

1. Periksa status persetujuan PRD.
2. Identifikasi setiap kebutuhan PRD.
3. Berikan ID unik pada kebutuhan.
4. Uraikan kebutuhan menjadi spesifikasi sistem.
5. Identifikasi aturan bisnis dan validasi.
6. Tetapkan kebutuhan nonfungsional.
7. Definisikan acceptance criteria.
8. Bangun Requirement Traceability Matrix (RTM).
9. Periksa kelengkapan dan konsistensi.
10. Ajukan SRS untuk persetujuan manusia.

### Contoh Keterlacakan

PRD-FR-001
  -> SRS-FR-001.1
  -> DESIGN-001
  -> TEST-001

Setiap SRS harus memiliki sumber PRD
atau justifikasi kebutuhan yang disetujui.

Kebutuhan baru yang ditemukan ketika
menyusun SRS harus diajukan sebagai
perubahan PRD apabila mengubah cakupan produk.

## 8. Technology-Agnostic Development

Framework tidak memaksakan satu
teknologi tertentu.

Pemilihan teknologi harus berdasarkan:
- Kebutuhan pengguna.
- Target platform.
- Kompleksitas aplikasi.
- Kompetensi tim.
- Biaya operasional.
- Keamanan.
- Performa.
- Pemeliharaan.
- Kemudahan deployment.

### 8.1 Web

Dapat menggunakan teknologi frontend,
backend, database, dan API yang sesuai.

### 8.2 Android

Dapat menggunakan pengembangan native
atau cross-platform.

### 8.3 iOS

Dapat menggunakan pengembangan native
atau cross-platform.

### 8.4 Cross-Platform

Dapat menggunakan shared codebase
jika memenuhi kebutuhan kedua platform.

Kompilasi, pengujian, dan distribusi
Android serta iOS harus diverifikasi
secara terpisah.

## 9. Human Approval Gates

Persetujuan manusia wajib untuk:
- Penetapan ruang lingkup.
- Penerimaan PRD.
- Penerimaan SRS.
- Persetujuan desain utama.
- Perubahan kebutuhan signifikan.
- Deployment produksi.
- Operasi yang merusak data.

Persetujuan harus terdokumentasi.

## 10. Change Management

Setiap perubahan signifikan dicatat
dengan informasi:
- ID perubahan.
- Alasan.
- Dokumen atau komponen terdampak.
- Risiko.
- Keputusan.
- Status verifikasi.

Jika PRD berubah, evaluasi dampak pada:
- SRS.
- Dokumen perancangan.
- Implementasi.
- Pengujian.
- Dokumentasi pengguna.

## 11. Verification

Status hasil pekerjaan:

- DRAFT: Masih dalam penyusunan.
- IN_REVIEW: Sedang diperiksa.
- CHANGES_REQUESTED: Memerlukan revisi.
- APPROVED: Disetujui manusia.
- VERIFIED: Lulus pemeriksaan yang relevan.
- BLOCKED: Tidak dapat dilanjutkan.

APPROVED dan VERIFIED memiliki arti berbeda.

APPROVED menandakan persetujuan manusia.
VERIFIED menandakan hasil pemeriksaan
berdasarkan kriteria yang ditentukan.

Keduanya dapat diperlukan sebelum
melanjutkan fase tertentu.

## 12. Keamanan dan Privasi

PREZEKC AI harus:
- Melindungi informasi rahasia.
- Menghindari paparan kredensial.
- Membatasi akses berdasarkan kebutuhan.
- Meminimalkan data pribadi.
- Tidak mempublikasikan data sensitif.
- Meminta persetujuan untuk operasi berisiko.
- Mencatat risiko keamanan yang relevan.

Untuk sistem yang menangani informasi sensitif,
terapkan pemeriksaan keamanan tambahan.

## 13. Status Implementasi

Versi 0.1.0 berfokus pada:
- Definisi arsitektur framework.
- Governance.
- Workflow.
- Verification.
- Aturan dasar AI.

Kemampuan berikut masih direncanakan:
- Skills operasional.
- Template dokumen lengkap.
- Validasi otomatis PRD-to-SRS.
- Generator proyek.
- Integrasi development tools.
- Pengujian framework otomatis.

Dokumen ini merupakan spesifikasi rancangan,
bukan bukti seluruh kemampuan sudah berjalan.

## 14. Referensi Internal

- README.md
- AGENTS.md
- core/governance.md
- core/workflow.md
- core/verification.md

---

PREZEKC AI Framework
Version 0.1.0
