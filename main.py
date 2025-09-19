from models.Containers_models import Containers
from models.Box_models import Box

class Automatizar:
    def __init__(self):
        ...

    def calcular_cantidad_cajas(self, contenedor, caja):
        if caja.altura <= 0 or caja.ancho <= 0:
            return 0, 0
        cajas_altura = int(contenedor.altura / caja.altura)
        cajas_ancho = int(contenedor.ancho / caja.ancho)
        return cajas_altura, cajas_ancho

    def calcular_espacio_ocupado(self, contenedor, caja, total_cajas):
        tamaño_contenedor = contenedor.altura * contenedor.ancho
        tamaño_caja = caja.altura * caja.ancho
        espacio_ocupado = total_cajas * tamaño_caja

        if tamaño_contenedor > 0:
            return (espacio_ocupado / tamaño_contenedor) * 100
        return 0

    def calcular(self, contenedor, caja):
        cajas_altura, cajas_ancho = self.calcular_cantidad_cajas(contenedor, caja)
        total_cajas = cajas_altura * cajas_ancho
        porcentaje = self.calcular_espacio_ocupado(contenedor, caja, total_cajas)

        return {
            "cajas_altura": cajas_altura,
            "cajas_ancho": cajas_ancho,
            "total_cajas": total_cajas,
            "porcentaje": porcentaje
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

    auto = Automatizar()


    for cont, caja in pares:
        resultado = auto.calcular(cont, caja)
        print(f"Contenedor {cont.tipo}:")
        print(f" - Cajas por altura: {resultado['cajas_altura']}")
        print(f" - Cajas por ancho: {resultado['cajas_ancho']}")
        print(f" - Total de cajas que caben: {resultado['total_cajas']}")
        print(f" - Espacio lleno: {resultado['porcentaje']:.2f}%")
        print("-" * 40)

if __name__== "__main__":

    main()



