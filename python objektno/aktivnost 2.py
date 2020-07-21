"""Vaš prijatelj Marko vodi trgovinu DDD u zamišljenoj državi naziva CCC.
U trgovini se može kupiti sok, čokolada, jabuka ili kruh. Svaki proizvod ima svoj jedinstveni naziv i
osnovnu cijenu.
Poreznim izmjenama na početku ove godine porez na sve proizvode je 25% osim na sok gdje je ostao
20%, a na jabuku 10%.
Vaš zadatak je pomoći Marku u vođenju inventure na način da izračunate ukupnu cijenu svih proizvoda
pri čemu je ukupna cijena proizvoda jednaka osnovnoj povećanoj za vrijednost poreza na dodanu
vrijednost proizvoda. """

"""1. korak"""
"""Napiši klasu proizvod koja sadrži ime proizvoda, cijena i količina.(broj proizvoda koje posjeduje jedna trgovina)
primjer poziva konstruktora => proizvod("Vindija", 5, 3), """
class proizvod:

  def __init__ (self, x, y, z):

    self.ime = x
    self.cijena = y
    self.kolicina = z
  def pdv(self):
    return 0.25

  def uk_cijena(self):
    return self.pdv()*self.cijena + self.cijena

class sok(proizvod):
  def pdv(self):
    return 0.2

class kruh(proizvod):
  pass

class coko(proizvod):
  pass

class jabuka(proizvod):
  def pdv(self):
    return 0.1

lista = [ jabuka("jabuka1", 5, 2), kruh("Vindija", 5, 3), sok("Pago", 7, 2)]
br = 0.0
for item in lista:
  #print(item.uk_cijena())

  br = br + item.kolicina*item.uk_cijena()

print(br)
