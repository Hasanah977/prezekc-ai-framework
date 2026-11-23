
# PREZEKC AI — Workflow Protocol

**Version:** 0.1.0
**Status:** Draft Specification

## 1. Purpose

Workflow Protocol mendefinisikan
prosedur kerja PREZEKC AI dari
inisiasi proyek sampai pemeliharaan.

Workflow harus dapat digunakan
untuk berbagai jenis proyek.

## 2. Workflow Selection

Saat menerima proyek baru, AI harus
mengidentifikasi:

- Project name.
- Project type.
- Main objective.
- Stakeholders.
- Target platform.
- Existing system.
- Available evidence.
- Constraints.
- Expected deliverables.
- Approval requirements.

Project type dapat berupa:
- Software Development.
- Research.
- System Analysis.
- Documentation.
- Maintenance.
- Other.

Target platform dapat berupa:
- Web.
- Android.
- iOS.
- Cross-Platform.
- Backend/API.
- Not Applicable.

## 3. Standard Workflow

### PHASE 01 — Existing System Analysis

Input:
- Project brief.
- Informasi proses berjalan.
- Bukti observasi atau wawancara.
- Dokumen pendukung.

Activities:
1. Identifikasi aktor.
2. Petakan alur proses.
3. Identifikasi masalah.
4. Analisis penyebab dan dampak.
5. Dokumentasikan bukti.
6. Tandai asumsi yang belum tervalidasi.

Output:
Analisis Sistem Berjalan.

Exit Criteria:
- Aktor teridentifikasi.
- Proses berjalan tergambarkan.
- Masalah memiliki sumber atau label asumsi.
- Batasan data dijelaskan.

### PHASE 02 — Comparative Study

Input:
- Hasil analisis sistem berjalan.
- Referensi sistem atau solusi pembanding.

Activities:
1. Identifikasi sistem relevan.
2. Kumpulkan referensi terverifikasi.
3. Bandingkan fitur dan karakteristik.
4. Identifikasi kelebihan serta kekurangan.
5. Analisis kesenjangan kebutuhan.
6. Rumuskan peluang pengembangan.

Output:
Studi Komparasi.

Exit Criteria:
- Sistem pembanding relevan.
- Informasi memiliki sumber.
- Kelebihan dan kekurangan dijelaskan.
- Rekomendasi didasarkan pada temuan.

Jika sistem pembanding tidak ditemukan,
catat upaya pencarian dan keterbatasannya.
Jangan membuat sistem pembanding fiktif.

### PHASE 03 — Requirement Analysis

Input:
- Analisis Sistem Berjalan.
- Studi Komparasi.
- Masukan stakeholder.

Activities:
1. Identifikasi kebutuhan pengguna.
2. Identifikasi kebutuhan bisnis.
3. Identifikasi kebutuhan data.
4. Kelompokkan kebutuhan.
5. Tentukan prioritas.
6. Identifikasi batasan.
7. Periksa konflik kebutuhan.

Output:
Analisis Kebutuhan.

Exit Criteria:
- Kebutuhan memiliki sumber.
- Prioritas telah ditentukan.
- Kebutuhan ambigu ditandai.
- Kebutuhan penting siap dikembangkan.

### PHASE 04 — PRD Generation

Input:
- Hasil analisis kebutuhan.
- Tujuan produk.
- Ruang lingkup proyek.

Activities:
1. Susun product vision.
2. Definisikan problem statement.
3. Identifikasi target users.
4. Tentukan goals dan non-goals.
5. Susun fitur utama.
6. Tulis user stories.
7. Berikan ID kebutuhan.
8. Susun acceptance criteria produk.
9. Tentukan indikator keberhasilan.
10. Lakukan review kelengkapan.

Output:
Product Requirements Document (PRD).

Exit Criteria:
- Tujuan dan ruang lingkup jelas.
- Fitur memiliki alasan kebutuhan.
- Prioritas tersedia.
- Acceptance criteria dapat diperiksa.
- PRD memperoleh persetujuan manusia.

### PHASE 05 — PRD-to-SRS Engineering

Input:
- Approved PRD.
- Aturan bisnis.
- Kebutuhan integrasi dan data.

Activities:
1. Baca seluruh PRD.
2. Validasi status persetujuan.
3. Ekstrak setiap kebutuhan produk.
4. Pecah menjadi kebutuhan sistem.
5. Tentukan perilaku yang diharapkan.
6. Definisikan input dan output.
7. Definisikan validasi dan kondisi gagal.
8. Definisikan kebutuhan nonfungsional.
9. Tetapkan acceptance criteria terukur.
10. Bangun Requirement Traceability Matrix.
11. Periksa konsistensi dengan PRD.
12. Ajukan SRS untuk persetujuan.

Output:
- Software Requirements Specification.
- Requirement Traceability Matrix.

Contoh transformasi:

PRD-FR-001:
Pengguna dapat mendaftar akun.

SRS-FR-001.1:
Sistem menyediakan formulir pendaftaran.

SRS-FR-001.2:
Sistem memvalidasi format email.

SRS-FR-001.3:
Sistem menolak email yang telah digunakan.

SRS-FR-001.4:
Sistem menyimpan password secara aman.

Exit Criteria:
- Semua kebutuhan wajib PRD terpetakan.
- Kebutuhan SRS dapat diuji.
- Tidak ada konflik dengan PRD.
- Kebutuhan baru memiliki justifikasi.
- SRS memperoleh persetujuan manusia.

### PHASE 06 — System Design

Input:
- Approved SRS.
- RTM.
- Batasan teknologi.

Activities:
1. Rancang arsitektur.
2. Identifikasi komponen sistem.
3. Rancang alur interaksi.
4. Buat diagram UML yang relevan.
5. Rancang struktur database.
6. Definisikan API jika diperlukan.
7. Rancang UI/UX.
8. Periksa kesesuaian dengan SRS.

Output:
Dokumen Perancangan Sistem.

Exit Criteria:
- Komponen utama terdefinisi.
- Desain dapat ditelusuri ke SRS.
- Keputusan teknologi dijelaskan.
- Risiko desain dicatat.
- Desain utama disetujui.

### PHASE 07 — Implementation

Input:
- Approved SRS.
- Approved design.
- Selected technology stack.

Activities:
1. Susun rencana implementasi.
2. Siapkan struktur proyek.
3. Konfigurasi environment.
4. Implementasikan fitur berdasarkan prioritas.
5. Hubungkan frontend, backend, dan database.
6. Lakukan pemeriksaan kode.
7. Catat perubahan.

Output:
Source code dan artefak aplikasi.

Platform-specific activities:

WEB:
- Frontend.
- Backend.
- Database.
- API.
- Browser compatibility.
- Responsive design.

ANDROID:
- Android build configuration.
- Device permissions.
- Device compatibility.
- Testing on Android.

IOS:
- iOS build configuration.
- Platform permissions.
- Apple platform requirements.
- Testing on iOS.

CROSS-PLATFORM:
- Shared application code.
- Android-specific verification.
- iOS-specific verification.
- Device compatibility assessment.

Exit Criteria:
- Fitur sesuai kebutuhan.
- Tidak ada kegagalan kritis yang diketahui.
- Hasil build dilaporkan secara akurat.
- Perubahan terdokumentasi.

### PHASE 08 — Testing and Verification

Input:
- Source code.
- SRS.
- RTM.
- Test cases.

Activities:
1. Unit testing.
2. Integration testing.
3. Functional testing.
4. Nonfunctional testing.
5. Security review.
6. Regression testing.
7. User acceptance testing jika diperlukan.
8. Catat hasil serta kegagalan.

Output:
Verification and Test Report.

Exit Criteria:
- Kriteria penerimaan diperiksa.
- Hasil pengujian tercatat.
- Kegagalan kritis ditangani.
- Risiko tersisa dikomunikasikan.
- Persetujuan penerimaan diperoleh.

### PHASE 09 — Deployment and Maintenance

Input:
- Verified application.
- Deployment plan.
- Release approval.

Activities:
1. Periksa environment.
2. Buat backup bila relevan.
3. Jalankan deployment.
4. Verifikasi sistem setelah rilis.
5. Siapkan rollback plan.
6. Monitor masalah operasional.
7. Catat perbaikan dan perubahan.

Output:
- Released application.
- Deployment report.
- Maintenance log.

Exit Criteria:
- Deployment terverifikasi.
- Risiko tersisa dicatat.
- Dokumentasi diperbarui.
- Pemilik sistem menerima hasil.

## 4. Workflow States

Setiap tugas dapat memiliki status:

- TODO
- IN_PROGRESS
- IN_REVIEW
- CHANGES_REQUESTED
- APPROVED
- VERIFIED
- BLOCKED
- DONE

APPROVED menandakan persetujuan manusia.
VERIFIED menandakan lulus pemeriksaan.
DONE menandakan seluruh syarat tugas terpenuhi.

## 5. Dependency Management

Aturan dependensi utama:

- Requirement Analysis bergantung pada
  bukti kebutuhan yang memadai.
- PRD bergantung pada Requirement Analysis.
- SRS bergantung pada Approved PRD.
- Final System Design bergantung pada Approved SRS.
- Production Implementation bergantung pada
  approved requirements dan design.
- Deployment bergantung pada verifikasi dan
  persetujuan rilis.

Eksperimen atau prototipe awal diperbolehkan,
tetapi tidak boleh dinyatakan sebagai
implementasi final tanpa baseline persyaratan.

## 6. Iteration and Change

Jika ditemukan masalah:
1. Identifikasi fase asal.
2. Catat masalah.
3. Analisis dampak.
4. Kembali ke fase terkait.
5. Perbarui dokumen turunan.
6. Jalankan verifikasi ulang.

Perubahan PRD harus memicu pemeriksaan
pada SRS, design, code, dan tests.

## 7. Workflow Adaptation

Untuk proyek non-software:
- Fase implementasi dapat berupa
  pelaksanaan penelitian atau pekerjaan.
- Fase desain dapat berupa metode penelitian.
- Fase SRS dapat dinyatakan tidak berlaku.

Pengecualian harus dijelaskan dan
disetujui sesuai tingkat risikonya.

Untuk proyek software baru, PRD dan SRS
tetap menjadi baseline kebutuhan.

## 8. Reporting Format

Setiap fase harus dilaporkan dengan:

Phase:
Status:
Inputs:
Outputs:
Verification:
Open Issues:
Next Phase:
Human Approval:

AI tidak boleh melaporkan fase sebagai
selesai jika exit criteria belum terpenuhi.

---

PREZEKC AI Workflow Protocol
