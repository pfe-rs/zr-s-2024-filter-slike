from PIL import Image
import numpy as np

class Slika:
    def __init__(self, putanja=None):
        self.slika = None
        if putanja:
            self.ucitaj_sliku(putanja)
    
    def ucitaj_sliku(self, putanja):
        self.slika = np.array(Image.open(putanja))
    
    def sacuvaj_sliku(self, putanja):
        Image.fromarray(self.slika).save(putanja)
    
    def prikazi_sliku(self):
        Image.fromarray(self.slika).show()
    
    def pristupi_pikselu(self, x, y):
        return self.slika[x, y]
    
    def postavi_pixel(self, x, y, vrednost):
        self.slika[x, y] = vrednost


class Filtar:
    def primeni_filtar(self):
        pass


class GausFiltar:
    def primeni_filtar(self,velicina_kernela,sigmaX,sigmaY):
        pass

class CannyFiltar:
    def primeni_filtar(self, minimalna_vrednost, maksimalna_vrednost,velicina_otvora_blende):
        pass

class LaplacianFiltar:
    def primeni_filtar(self, velicina_kernela):
        pass

class MedianFiltar:
    def primeni_filtar(self, velicina_kernela):
        pass