from PIL import Image
import cv2
import numpy as np
import os

class Slika:
    def __init__(self, putanja=None):
        self.slika = None
        if putanja:
            self.ucitaj_sliku(putanja)
    
    def ucitaj_sliku(self, putanja):
        self.slika = np.array(Image.open(putanja))
    
    def sacuvaj_sliku(self, putanja):
        
        direktorijum = os.path.dirname(putanja)
        if not os.path.exists(direktorijum):
            os.makedirs(direktorijum, exist_ok=True)
        Image.fromarray(self.slika).save(putanja)
    
    def prikazi_sliku(self):
        Image.fromarray(self.slika).show()
    
    def pristupi_pikselu(self, x, y):
        return self.slika[x, y]
    
    def postavi_pixel(self, x, y, vrednost):
        self.slika[x, y] = vrednost


class Filtar:
    def primeni_filtar(self, slika):
        pass


class GausFiltar:
    def __init__(self, velicina_kernela, sigmaX, sigmaY):
        self.velicina_kernela = velicina_kernela
        self.sigmaX = sigmaX
        self.sigmaY = sigmaY
    def primeni_filtar(self, slika):
        if slika is None:
            print("Slika nije učitana.")
            return None
        
        if self.velicina_kernela % 2 == 0:
            print("Veličina kernela mora biti neparni broj.")
            return None

        
        isfiltrirana_slika = cv2.GaussianBlur(slika, (self.velicina_kernela, self.velicina_kernela), self.sigmaX, self.sigmaY)
        return isfiltrirana_slika

class CannyFiltar:
    def __init__(self, minimalna_vrednost, maksimalna_vrednost, velicina_otvora_blende=3):
        
        self.minimalna_vrednost = minimalna_vrednost
        self.maksimalna_vrednost = maksimalna_vrednost
        self.velicina_otvora_blende = velicina_otvora_blende

    def primeni_filtar(self, slika):

        if slika is None:
            print("Slika nije učitana.")
            return None

        if len(slika.shape) == 3:
            slika = cv2.cvtColor(slika, cv2.COLOR_BGR2GRAY)
        
        ivice = cv2.Canny(slika, self.minimalna_vrednost, self.maksimalna_vrednost, apertureSize=self.velicina_otvora_blende)
        return ivice


class LaplacianFiltar:
    def __init__(self, ddepth, ksize=1):
        """
        :param ddepth:Na primer, cv2.CV_8U, cv2.CV_16S, cv2.CV_32F, itd.
        :param ksize: Veličina kernela za Laplacian operator. Mora biti neparni broj.
        """
        self.ddepth = ddepth
        self.ksize = ksize

    def primeni_filtar(self, slika):

        if slika is None:
            print("Slika nije učitana.")
            return None
        if len(slika.shape) == 3:
            slika = cv2.cvtColor(slika, cv2.COLOR_BGR2GRAY)

        # Primena Laplacian filtra
        laplacian = cv2.Laplacian(slika, self.ddepth, ksize=self.ksize)
        return laplacian

class MedianFiltar:
    def __init__(self, velicina_kernela):
        

        # param velicina_kernela:mora biti neparni broj.
        
        self.velicina_kernela = velicina_kernela

    def primeni_filtar(self, slika):

        if slika is None:
            print("Slika nije učitana.")
            return None

        # Veličina kernela mora biti neparni broj.
        if self.velicina_kernela % 2 == 0:
            print("Veličina kernela za medijanski filter mora biti neparni broj.")
            return None


        isfiltrirana_slika = cv2.medianBlur(slika, self.velicina_kernela)
        return isfiltrirana_slika




# slika_obj = Slika("C:\\Users\\mihai\\Desktop\\zr-s-2024-filter-slike\\switz.png")
# slika = slika_obj.slika 


# laplacian_filtr = LaplacianFiltar(cv2.CV_8U, ksize=3)
# laplacian_ivice = laplacian_filtr.primeni_filtar(slika)


# if laplacian_ivice is not None:
#     cv2.imshow("Laplacian Ivice", laplacian_ivice)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
