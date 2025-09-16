from models.Containers_models import Containers
from models.Box_models import Box

class Automatizar:

    def __init__(self, contenedor: Containers, caja: Box):
        self.contenedor = contenedor
        self.caja = caja
    
    def calcular(self):
        cajas_altura = int(self.contenedor.altura / self.caja.altura)
        cajas_ancho = int(self.contenedor.ancho / self.caja.ancho)

        total_cajas = cajas_altura * cajas_ancho

        tamaño_contenedor = self.contenedor.altura * self.contenedor.ancho
        tamaño_caja = self.caja.altura * self.caja.ancho
        espacio_ocupado = total_cajas * tamaño_caja
    

        if tamaño_contenedor > 0:
            espacio_lleno = (espacio_ocupado / tamaño_contenedor) * 100
        else:
            espacio_lleno = 0

        return {
            "cajas_altura": cajas_altura,
            "cajas_ancho": cajas_ancho,
            "total_cajas": total_cajas,
            "porcentaje": espacio_lleno
        }


def main():

    contenedor_ropa = Containers(nombre="nombre", altura=278, ancho=150, tipo="ropa")
    contenedor_maquillaje = Containers(nombre="nombre", altura=170, ancho=110, tipo="maquillaje")
    contenedor_tenis = Containers(nombre="nombre", altura=350, ancho=210, tipo="tenis")
    contenedor_perfume = Containers(nombre="nombre", altura=250, ancho=120, tipo="perfume")
    contenedor_souvenirs = Containers(nombre="nombre", altura=320, ancho=130, tipo="souvernir")

    caja_ropa = Box(nombre="nombre", altura=78, ancho=50, tipo="ropa")
    caja_maquillaje = Box(nombre="nombre", altura=70, ancho=10, tipo="maquillaje")
    caja_tenis = Box(nombre="nombre", altura=50, ancho=10, tipo="tenis")
    caja_perfume = Box(nombre="nombre", altura=50, ancho=20, tipo="perfume")
    caja_souvenirs = Box(nombre="nombre", altura=20, ancho=10, tipo="souvernir")

    pares = [
    (contenedor_ropa, caja_ropa),
    (contenedor_maquillaje, caja_maquillaje),
    (contenedor_tenis, caja_tenis),
    (contenedor_perfume, caja_perfume),
    (contenedor_souvenirs, caja_souvenirs),
    ]


    for cont, caja in pares:
        auto = Automatizar(cont, caja)
        resultado = auto.calcular()
        print(f"Contenedor {cont.tipo}:")
        print(f" - Cajas por altura: {resultado['cajas_altura']}")
        print(f" - Cajas por ancho: {resultado['cajas_ancho']}")
        print(f" - Total de cajas que caben: {resultado['total_cajas']}")
        print(f" - Espacio lleno: {resultado['porcentaje']:.2f}%")
        print("-" * 40)

if __name__== "__main__":

    main()



