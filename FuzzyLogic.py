"""
TUBES PKB A

Kelompok 4:
Nama: Helmi 11211043 (Ketua)
Nama: Chyntia Putri Siregar 11211027 (Anggota)
"""

"""
Pada program ini meggunakan 2 library, yaitu numpy dan skfuzzy untuk memabntu membangun program logika fuzzy
dan 1 library matplotlib.pyplot untuk membantu menampilkan output
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

class fuzzyNilai: #Membuat Class FuzzyNilai untuk program Menentukan nilai Akhir Mahasiswa

    # Membuat Fungsi untuk pengkategorian penilain 
    def __init__(self): 
        # Variabel input nilai dengan nama: Quiz, UTS, UAS
        self.Quiz = ctrl.Antecedent(np.arange(0, 101, 1), 'Quiz')
        self.Uts = ctrl.Antecedent(np.arange(0, 101, 1), 'UTS')
        self.Uas = ctrl.Antecedent(np.arange(0, 101, 1), 'UAS')
        # Variabloutput nilai dengan nama: Nilai_Akhir
        self.NilaiAkhir = ctrl.Consequent(np.arange(0, 101, 1), 'Nilai_Akhir')
        
    def membership(self): 
        self.Quiz.automf(3)
        self.Uts.automf(3)
        self.Uas.automf(3)
        
    def customMembership(self): 
        self.membership() 
        # Mendeklarasikan variabel NilaiAkhir unutuk ketentuan batasan dari 3 pengkategorian nilai mulai dari nilai Kurang, Cukup, Tinggi
        self.NilaiAkhir['Kurang'] = fuzz.trimf(self.NilaiAkhir.universe, [0, 0, 50])
        self.NilaiAkhir['Cukup'] = fuzz.trimf(self.NilaiAkhir.universe, [51, 65, 80])  # Menyesuaikan rentang sedang
        self.NilaiAkhir['Tinggi'] = fuzz.trimf(self.NilaiAkhir.universe, [81, 100, 100]) 

    # Membuat fungsi untuk pengkategorian rule aturan fuzzifikasi
    def rule(self):
        self.membership()
        self.customMembership() 
        # Aturan 1
        self.rule1 = ctrl.Rule(self.Quiz['poor'] & self.Uts['poor'] & self.Uas['poor'], self.NilaiAkhir['Kurang'])
        # Aturan 2
        self.rule2 = ctrl.Rule(self.Quiz['average'] & self.Uts['average'] & self.Uas['average'], self.NilaiAkhir['Cukup'])
        # Aturan 3
        self.rule3 = ctrl.Rule(self.Quiz['good'] & self.Uts['good'] & self.Uas['good'], self.NilaiAkhir['Tinggi'])

    # Membuat fungsi untuk penginputan nilai mahasiswa
    def controlSystem(self):
        # Memanggil fungsi rule
        self.rule() 
        # Mendeklarasikan variabel nilai_ctrl
        nilai_ctrl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3])
        self.scoring = ctrl.ControlSystemSimulation(nilai_ctrl)

        # Mengambil input dari pengguna atau sesuai kebutuhan
        quiz_score = float(input("Masukkan nilai Quiz: "))
        uts_score = float(input("Masukkan nilai UTS: "))
        uas_score = float(input("Masukkan nilai UAS: "))

        # Perhitungan nilai akhir
        total_score = (quiz_score + uts_score + uas_score) / 2.83 #mengapa tidak dibagi 3 bilangan pas karena setalh dilakukan pengujian dengan 
                                                                    #kalkulator perhitungan pas berada diangka 2.83
        # Mengeset input fuzzy dengan nilai total
        self.scoring.input['Quiz'] = total_score
        self.scoring.input['UTS'] = total_score
        self.scoring.input['UAS'] = total_score

        # Melakukan perhitungan menggunakan sistem fuzzy
        self.scoring.compute()

        # Menampilkan Output untuk NilaiAkhir Mahasiswa
    def result(self):
        self.controlSystem() 
        nilai_akhir = self.scoring.output['Nilai_Akhir']
        print(f"Nilai Akhir Mahasiswa: {nilai_akhir:.2f}")

        # Menentukan kategori nilai
        if nilai_akhir <= 50:
            kategori = 'Kurang'
        elif 50 < nilai_akhir <= 80:
            kategori = 'Cukup'
        else:
            kategori = 'Tinggi'

        print(f"Kategori Nilai: {kategori}")
        self.NilaiAkhir.view(sim=self.scoring)

        # Menambahkan teks kategori nilai pada grafik
        plt.text(nilai_akhir + 2, 0.2, f'Kategori: {kategori}', rotation=0, verticalalignment='center')

        plt.show()

# Membuat objek fuzzyNilai
fuzzy_program = fuzzyNilai()

# Menjalankan metode result untuk menghitung dan menampilkan output
fuzzy_program.result()
