# Nama : Ryan Kurnia Hidayatullah
# NIM : 13519212
# Kelas : K-04
# Deskripsi : Tucil 2 Stima - Decrease and Conquer Topological Sorting


daftar_matkul = input("Masukkan Input Daftar Matkul: ")  # Menerima input berupa nama file.txt
matkul = open(daftar_matkul, "r")  # Membuka file daftar_matkul
array_matkul = []  # deklarasi array matkul yang akan berisi matkul dan pre req nya
array_semester = []  # deklarasi array semester yang akan berisi rencana studi yang dapat diambil
for line in matkul:
    array_matkul.append(line.strip('\n.').split(', '))  # memasukkan isi file per baris menjadi array dalam array dan dipisah oleh tanda koma
matkul.close()


def decrease(array):  # fungsi decrease untuk menghapus matkul yang tidak memiliki prereq dan mengisinya ke dalam rencana studi
    test = [] # membuat array test untuk sementara menyimpan data rencana matkul tiap semester yang nantinya akan di
    for i in range(len(array)):
        for j in range(len(array[i])):
            if len(array[i]) == 1:          # jika ada matkul yang tidak memiliki prereq maka akan dimasukkan ke dalam array sementara test
                test.append(array[i][0])
    for i in range(len(array)):
        array[i] = list(filter(lambda x: x not in test, array[i])) # menghapus matkul yang tidak memiliki prereq
    kosong = []
    while kosong in array :
        array.remove(kosong) # menghapus array kosong di dalam array
    array_semester.append(test) # mamasukkan array test ke dalam array semester

while array_matkul != []:  # mendecrease satu per satu array matkul selama belum kosong
    decrease(array_matkul)

semester = 0
for row in array_semester: # mengeprint array semester yang berisi rencana studi yang dapat diambil pada setiap semester
    semester = semester + 1
    print("Semester "+ str(semester) + " : " ,*row)
    print()
