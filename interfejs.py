from main import Slika, Filtar, GausFiltar, CannyFiltar, LaplacianFiltar, MedianFiltar
import cv2


def izaberi_filtar_i_parametre():
    print("Izaberite filter koji želite da primenite na sliku:")
    
    print("1. Gausov filter")
    
    print("2. Canny filter")
    
    print("3. Laplasov filter")
    
    print("4. Median filter")
    
    izbor = int(input("Unesite redni broj filtera: "))
    
    
    
    
    if izbor == 1:
        velicina_kernela = int(input("Unesite veličinu kernela: "))
        sigmaX = int(input("Unesite vrednost parametra sigmaX: "))
        sigmaY = int(input("Unesite vrednost parametra sigmaY: "))
        return GausFiltar(velicina_kernela, sigmaX, sigmaY)
    elif izbor == 2:
        minimalna_vrednost = int(input("Unesite minimalnu vrednost: "))
        maksimalna_vrednost = int(input("Unesite maksimalnu vrednost: "))
        velicina_otvora_blende = int(input("Unesite veličinu otvora blende: "))
        return CannyFiltar(minimalna_vrednost, maksimalna_vrednost, velicina_otvora_blende)
    elif izbor == 3:
        ddepth = int(input("Unesite vrednost parametra ddepth: "))
        ksize = int(input("Unesite veličinu kernela: "))
        return LaplacianFiltar(ddepth, ksize)
    elif izbor == 4:
        velicina_kernela = int(input("Unesite veličinu kernela: "))
        return MedianFiltar(velicina_kernela)
    else:
        print("Nepostojeći filter.")
        return None
    
def primeni_filtar_na_sliku(filtr):
    putanja = input("Unesite putanju do slike: ")
    slika = Slika(putanja)
    if slika.slika is None:
        print("Ne mogu učitati sliku.")
        return

    isfiltrirana_slika = filtr.primeni_filtar(slika.slika)
    if isfiltrirana_slika is not None:
        cv2.imshow("Isfiltrirana Slika", isfiltrirana_slika)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Nije moguće primeniti filtar.")

if __name__ == "__main__":
    filtr = izaberi_filtar_i_parametre()
    if filtr is not None:
        primeni_filtar_na_sliku(filtr)