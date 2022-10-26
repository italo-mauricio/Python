from barcode import EAN13
from barcode.writer import ImageWriter

print("Testando biblioteca barcode")
with open(r'C:/Users/italo/OneDrive/Documentos/GitHub/Projetos-python/barcode.png', 'wb') as f:
    EAN13('111112222222', writer=ImageWriter()).write(f)