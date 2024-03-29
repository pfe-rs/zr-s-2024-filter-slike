import PIL
import numpy as np
import pytest
from PIL import Image
from main import Slika

PUTANJA_TEST_SLIKE = "switz.png"
PUTANJA_SACUVANE_SLIKE = "sacuvana_switz.png"

def test_ucitaj_sliku():
    slika = Slika(PUTANJA_TEST_SLIKE)
    assert slika.slika is not None
    assert isinstance(slika.slika, np.ndarray)

def test_sacuvaj_sliku():
    slika = Slika(PUTANJA_TEST_SLIKE)
    slika.sacuvaj_sliku(PUTANJA_SACUVANE_SLIKE)

    sacuvana_slika = Image.open(PUTANJA_SACUVANE_SLIKE)
    originalna_slika = Image.open(PUTANJA_TEST_SLIKE)
    assert list(sacuvana_slika.getdata()) == list(originalna_slika.getdata())




def test_prikazi_sliku(mocker):
    mocker.patch('PIL.Image.Image.show')
    slika = Slika(PUTANJA_TEST_SLIKE)
    slika.prikazi_sliku()
    assert PIL.Image.Image.show.call_count == 1



