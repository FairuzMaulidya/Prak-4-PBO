# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:53:37 2024

@author: 
"""

class Student:
    # Deklarasi variabel class
    data_pribadi = "--- Data Pribadi ---"

    def __init__(self, nama):
        # Inisialisasi atribut nama
        self.nama = nama
        # Inisialisasi atribut nim dan nilai dengan nilai awal None
        self.nim = None
        self.nilai = None

    def set_nim(self, nim):
        # Method untuk mengatur NIM
        self.nim = nim

    def set_nilai(self, nilai):
        # Method untuk mengatur nilai
        self.nilai = nilai

    def print_data(self):
        # Method untuk mencetak data siswa
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Nilai:", self.nilai)

    @staticmethod
    def print_data_teman(nomor_teman, teman):
        # Method untuk mencetak data teman dengan nomor tertentu
        print("--- Data Teman---", nomor_teman)
        teman.print_data()


# Pembuatan objek Student
siswa = Student("Fairuz Maulidya")
teman1 = Student("Zahwa Nur Azkia")
teman2 = Student("Calissta Azzahra")
teman3 = Student("Noval Susanto")

# Mengatur data siswa dan teman
siswa.set_nim("064002100018")
siswa.set_nilai(100)

teman1.set_nim("064002100038")
teman1.set_nilai(99)

teman2.set_nim("064002100008")
teman2.set_nilai(95)

teman3.set_nim("064002100001")
teman3.set_nilai(80)

# Menampilkan data
print(Student.data_pribadi)
siswa.print_data()
print()
Student.print_data_teman(1, teman1)
print()
Student.print_data_teman(2, teman2)
print()
Student.print_data_teman(3, teman3)
