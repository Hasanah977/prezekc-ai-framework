
# PREZEKC AI — Verification Protocol

**Version:** 0.1.0
**Status:** Draft Specification

## 1. Purpose

Verification Protocol menetapkan
standar pemeriksaan kualitas dan
konsistensi hasil pekerjaan.

AI harus membedakan antara:
- Hasil yang telah dibuat.
- Hasil yang telah diperiksa.
- Hasil yang disetujui manusia.
- Hasil yang berhasil diuji secara nyata.

## 2. Verification Principles

1. Evidence over assumptions.
2. Verify against defined criteria.
3. Never fabricate test results.
4. Report failures transparently.
5. Preserve requirement traceability.
6. Reverify affected outputs after changes.

## 3. Verification States

NOT_CHECKED:
Belum dilakukan pemeriksaan.

PASS:
Semua kriteria wajib pada pemeriksaan
tersebut telah terpenuhi.

PASS_WITH_NOTES:
Tidak ada kegagalan kriteria wajib,
tetapi terdapat catatan non-blocking.

FAIL:
Terdapat kriteria wajib yang gagal.

BLOCKED:
Pemeriksaan tidak dapat dilakukan
karena kendala atau data yang kurang.

NOT_APPLICABLE:
Pemeriksaan tidak relevan dan
alasannya sudah didokumentasikan.

## 4. System Analysis Verification

Periksa:
- Identitas sistem atau proses.
- Aktor yang terlibat.
- Alur kerja yang berjalan.
- Masalah yang teridentifikasi.
- Penyebab dan dampak.
- Sumber informasi.
- Asumsi dan keterbatasan.

FAIL jika data faktual utama dikarang
atau tidak dapat dibedakan dari asumsi.

## 5. Comparative Study Verification

Periksa:
- Identitas sistem pembanding.
- Relevansi pembanding.
- Sumber yang dapat diperiksa.
- Kelebihan dan kekurangan.
- Kriteria perbandingan yang konsisten.
- Kesimpulan yang didukung bukti.

FAIL jika referensi atau sistem
pembanding dibuat secara fiktif.

## 6. Requirement Analysis Verification

Periksa:
- Identifikasi stakeholder.
- Sumber kebutuhan.
- Kelengkapan kebutuhan utama.
- Prioritas kebutuhan.
- Konflik atau ambiguitas.
- Batasan proyek.
- Asumsi yang belum tervalidasi.

Kebutuhan yang belum tervalidasi
harus ditandai secara eksplisit.

## 7. PRD Verification

Minimum checklist:
- Product vision tersedia.
- Problem statement jelas.
- Target users teridentifikasi.
- Goals dan non-goals tersedia.
- Scope terdokumentasi.
- Fitur memiliki ID.
- Fitur memiliki alasan kebutuhan.
- Prioritas tersedia.
- Acceptance criteria tersedia.
- Indikator keberhasilan dijelaskan.
- Tidak terdapat konflik kebutuhan utama.

PRD dapat diajukan untuk persetujuan
jika pemeriksaan wajib PASS.

PRD tidak otomatis APPROVED
karena telah lolos pemeriksaan.

## 8. SRS Verification

Minimum checklist:
- SRS mengacu pada PRD yang disetujui.
- Kebutuhan fungsional memiliki ID.
- Kebutuhan nonfungsional terdefinisi.
- Aturan bisnis terdokumentasi.
- Aktor dan hak akses dijelaskan.
- Input dan output relevan dijelaskan.
- Validasi dan error handling tersedia.
- Batasan sistem dijelaskan.
- Acceptance criteria dapat diuji.
- Tidak bertentangan dengan PRD.
- RTM tersedia.

Setiap kebutuhan harus:
- Jelas.
- Konsisten.
- Dapat diuji.
- Dapat ditelusuri.
- Relevan dengan ruang lingkup.

Kebutuhan nonfungsional yang menyatakan
target numerik harus menjelaskan
kondisi dan metode pengukurannya.

## 9. Requirement Traceability

Format hubungan utama:

PRD Requirement
  -> SRS Requirement
  -> Design Component
  -> Test Case

Contoh:

PRD-FR-001
  -> SRS-FR-001.1
  -> DESIGN-001
  -> TEST-001

Verifikasi harus mengidentifikasi:
- PRD tanpa kebutuhan SRS terkait.
- SRS tanpa sumber kebutuhan yang sah.
- SRS tanpa komponen desain.
- Kebutuhan implementasi tanpa test case.
- Test case tanpa kebutuhan yang diuji.

Pada fase awal, kolom desain dan test
dapat berstatus PENDING.

Sebelum penerimaan akhir, setiap
kebutuhan wajib harus memiliki
bukti implementasi dan verifikasi
atau pengecualian yang disetujui.

## 10. System Design Verification

Periksa:
- Desain memenuhi kebutuhan SRS.
- Arsitektur terdokumentasi.
- Komponen utama teridentifikasi.
- Struktur data konsisten.
- Hak akses diperhitungkan.
- Integrasi sesuai kebutuhan.
- UI/UX mempertimbangkan pengguna.
- Keputusan teknologi memiliki alasan.
- Risiko utama diidentifikasi.

Diagram harus sesuai dengan sistem
yang benar-benar direncanakan.

## 11. Implementation Verification

Periksa:
- Kode sesuai kebutuhan.
- Tidak ada perubahan di luar ruang lingkup.
- Konfigurasi tidak mengekspos rahasia.
- Fitur utama dapat dijalankan.
- Error handling relevan tersedia.
- Build dan test telah diperiksa.
- Hasil pemeriksaan terdokumentasi.

Jika kode tidak dapat dijalankan,
jangan menyatakan implementasi berhasil.

## 12. Platform Verification

### WEB

Periksa sesuai kebutuhan:
- Build aplikasi.
- Alur frontend dan backend.
- Responsivitas.
- Browser compatibility.
- Authentication.
- API integration.
- Error handling.
- Security checks.

### ANDROID

Periksa sesuai kebutuhan:
- Android build.
- Install pada perangkat atau emulator.
- Navigasi.
- Permissions.
- API integration.
- Device compatibility.
- Crash dan error handling.

### IOS

Periksa sesuai kebutuhan:
- iOS build.
- Instalasi pada simulator atau perangkat.
- Navigasi.
- Permissions.
- API integration.
- Device compatibility.
- Crash dan error handling.

### CROSS-PLATFORM

Hasil pengujian Android tidak otomatis
membuktikan aplikasi berhasil di iOS.

Kedua platform harus memiliki
bukti pemeriksaan masing-masing.

## 13. Test Evidence

Setiap hasil pengujian harus mencatat:

Test ID:
Requirement ID:
Test Objective:
Environment:
Test Steps:
Expected Result:
Actual Result:
Status:
Evidence:
Executed By:
Execution Date:

Jika pengujian tidak dijalankan,
status harus NOT_CHECKED atau BLOCKED,
bukan PASS.

## 14. Severity Classification

CRITICAL:
Berisiko menyebabkan kebocoran data,
kerusakan data serius, atau kegagalan
fungsi inti yang tidak dapat diterima.

HIGH:
Fungsi utama gagal atau kebutuhan
wajib tidak terpenuhi.

MEDIUM:
Sebagian fungsi terganggu,
tetapi tersedia penanganan sementara.

LOW:
Masalah kecil yang tidak
menghambat fungsi utama.

Kegagalan CRITICAL atau HIGH yang masih
terbuka harus menghalangi penerimaan
rilis produksi, kecuali terdapat proses
penanganan risiko yang sah dan terdokumentasi
sesuai kebijakan organisasi.

## 15. Final Verification Gate

Sebelum fase dinyatakan selesai:

1. Semua output wajib tersedia.
2. Kriteria wajib telah diperiksa.
3. Tidak ada konflik kebutuhan kritis.
4. Masalah yang diketahui telah dicatat.
5. Bukti pemeriksaan tersedia.
6. Status pemeriksaan ditetapkan.
7. Persetujuan manusia diperoleh
   jika fase mensyaratkannya.

## 16. Verification Report Format

Verification ID:
Project:
Phase:
Deliverable:
Requirement References:
Criteria:
Methods:
Evidence:
Results:
Issues:
Risk Level:
Overall Status:
Reviewed By:
Review Date:

## 17. Honest Completion Reporting

AI wajib menggunakan pernyataan
yang sesuai bukti.

Contoh:
- "Dokumen berhasil disusun."
- "Struktur telah diperiksa."
- "Pengujian belum dijalankan."
- "Build Android berhasil."
- "Build iOS belum diverifikasi."
- "PRD menunggu persetujuan pengguna."

Tidak boleh menyatakan:
- Semua fitur berhasil jika belum diuji.
- Aplikasi siap produksi tanpa verifikasi.
- Dokumen sudah disetujui tanpa keputusan manusia.

---

PREZEKC AI Verification Protocol
