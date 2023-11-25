"""
TUBES PKB (Pengantar Kecerdasan Buatan)
Kelompok 4:
Nama: Helmi 11211043 (Ketua)
Nama: Cynthia Putri Siregar 11211027 (Anggota)
"""

"""
Pada Program ini saya menggunakan 2 Librabry yaitu Numpy dan Scikit Fuzzy untuk membantu dalam membuat
Program Logika Fuzzy Menentukan nilai akhir mahasiswa, serta library dari matplotlib.pylot untuk menampilkan hasil berupa grafik
terlebih dahulu kita import ketiga library tersebut dan menggantikannya dengan kata yang lebih sederhana
untuk membantu programmer dalam menggunakan syntax yang sederhana dan tidak terlalu panjang
seperti numpy menjadi np dan lain sebagainya, untuk import library ini opsional tergantung programmer
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import matplotlib.pyplot as plt

class fuzzyNilai: #Membuat Class FuzzyNilai untuk program Menentukan nilai Akhir Mahasiswa

    def __init__(self): #Membuat fungsi untuk pengkategorian penilaian
        #Membuat beberapa variabel input nilai dengan nama variabel ; forum, disiplin, dan NilaiQuizUjian
        self.Quiz = ctrl.Antecedent(np.arange(0, 11, 1), 'Quiz')
        self.Uts = ctrl.Antecedent(np.arange(0, 11, 1), 'UTS')
        self.Uas = ctrl.Antecedent(np.arange(0, 11, 1), 'UAS')
        #Membuat beberapa variabel output nilai dengan nama variabel ; NilaiAkhir
        self.NilaiAkhir = ctrl.Consequent(np.arange(0, 101, 1), 'Nilai_Akhir')
        
    def membership(self): #Membuat fungsi untuk pengkategorian penilaian
        self.Quiz.automf(3)
        self.Uts.automf(3)
        self.Uas.automf(3)
        
    def customMembership(self): #Membuat fungsi untuk pengkategorian penilaian pada Nilai Akhir
        self.membership() #Memanggil Fungsi membership()
        #Mendeklarasikan variabel NilaiAkhir untuk ketentuan batasan dari 3 pengkategorian nilai mulai dari kecil,dedang dan tinggi
        self.NilaiAkhir['kecil'] = fuzz.trimf(self.NilaiAkhir.universe,[0,0,80])
        self.NilaiAkhir['sedang'] = fuzz.trimf(self.NilaiAkhir.universe,[60,80,100])
        self.NilaiAkhir['tinggi'] = fuzz.trimf(self.NilaiAkhir.universe,[80,100,100])
        
    def rule(self):#Membuat fungsi untuk pengkategorian Rule aturan fuzzifikasi
        self.membership()#Memanggil Fungsi membership()
        self.customMembership() #Memanggil Fungsi customMembership()
        #Mendeklarasikan variabel rule1,rule2,rule3 dan rule4 untuk program Rule sesuai pada studi kasus
        #Dengan ketentuan jika input[a] | input[b] maka hasil outputnya ,output[c]
        self.rule1 = ctrl.Rule(self.Quiz['poor'] | self.Uts['poor'] | self.Uas['poor'], self.NilaiAkhir['kecil'])
        self.rule2 = ctrl.Rule(self.Quiz['good'] | self.Uas['good'], self.NilaiAkhir['tinggi'])
        self.rule3 = ctrl.Rule(self.Quiz['average'] | self.Uts['average'], self.NilaiAkhir['sedang'])
        self.rule4 = ctrl.Rule(self.Uts['good'], self.NilaiAkhir['tinggi'])
        
    def controlSystem(self):#Membuat fungsi untuk penginputan nilai mahasiswa
        self.rule() #Memanggil Fungsi Rule
        #Mendeklarasikan variabel nilai_ctrl
        nilai_ctrl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3, self.rule4])
        self.scoring = ctrl.ControlSystemSimulation(nilai_ctrl)
        self.scoring.input['Quiz'] = 10 #Menginputkan nilai Forum mahasiswa
        self.scoring.input['UTS'] = 10 #Menginputkan nilai Disiplin mahasiswa
        self.scoring.input['UAS'] = 10 #Menginputkan nilai Nilai_Quiz mahasiswa
        self.scoring.compute()

    def result(self): #Membuat fungsi untuk menampilkan output
        self.controlSystem() #Memanggil Fungsi controlSystem()
        # Menampilkan hasil output program dengan memanggil variabel Nilai_Akhir
        print(self.scoring.output['Nilai_Akhir'])
        self.NilaiAkhir.view(sim=self.scoring)
        plt.show()  # Menampilkan plot


# Membuat objek fuzzyNilai
fuzzy_program = fuzzyNilai()

# Menjalankan metode result untuk menghitung dan menampilkan output
fuzzy_program.result()
