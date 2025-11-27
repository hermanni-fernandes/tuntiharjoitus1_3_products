# models.py

class Tuote:
    def __init__(self, nimi, kuvaus, hinta, _id=None):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.hinta = hinta
        self._id = _id

    @property
    def id(self):
        return self._id
