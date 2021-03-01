# Tugas-Kecil-2-Strategi-Algoritma
# Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)
Pada tugas kali ini, mahasiswa diminta membuat aplikasi sederhana yang dapat menyusun
rencana pengambilan kuliah, dengan memanfaatkan algoritma Decrease and Conquer. Penyusunan
Rencana Kuliah diimplementasikan dengan menggunakan pendekatan Topological Sorting. Berikut
akan dijelaskan tugas yang dikerjakan secara detail.

1. Aplikasi akan menerima daftar mata kuliah beserta prasyarat yang harus diambil seorang
mahasiswa sebelum mengambil mata kuliah tersebut. Daftar mata kuliah tersebut dituliskan
dalam suatu file teks dengan format:

<kode_kuliah_1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah
prasyarat - 3>.
<kode_kuliah_2>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.
<kode_kuliah_3>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah
prasyarat - 3>, <kode kuliah prasyarat - 4>.
<kode_kuliah_4>.
contoh 1

Sebuah kode_kuliah mungkin memiliki nol atau lebih prasyarat kuliah. Kode_kuliah bisa
diambil pada suatu semester jika semua prasyaratnya sudah pernah diambil di semester
sebelumnya (tidak harus 1 semester sebelumnya). Asumsi semua kuliah bisa diambil di
sembarang semester, baik semester ganjil maupun semester genap.
Sebagai contoh, terdapat 5 kuliah yang harus diambil seorang mahasiswa dengan daftar
prerequisite dalam file teks sebagai berikut. Dari contoh 1 terlihat bahwa kuliah C3 tidak
memiliki prerequisite.

C1, C3.
C2, C1, C4.
C3.
C4, C1, C3.
C5, C2, C4.
contoh 2

Asumsi untuk persoalan ini, kuliah dan prerequisite nya pasti berupa Directed Acyclic Graph
(DAG), dan untuk contoh pada contoh 1, dapat dilihat representasi DAG pada contoh 2.

2. Dari file teks yang telah diterima, ditentukan kuliah apa saja yang bisa diambil di semester 1,
semester 2, dan seterusnya. Sebuah kuliah tidak mungkin diambil pada semester yang sama
dengan prerequisitenya. Untuk menyederhanakan persoalan, tidak ada Batasan banyaknya
kuliah yang bisa diambil pada satu semester.
