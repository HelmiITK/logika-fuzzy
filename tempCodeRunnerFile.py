def result(self): #Membuat fungsi untuk menampilkan output
    self.controlSystem() #Memanggil Fungsi controlSystem()
        #Menampilkan hasil output program dengan memanggil variabel Nilai_Akhir
    print(self.scoring.output['Nilai_Akhir']) 
    self.NilaiAkhir.view(sim=self.scoring)