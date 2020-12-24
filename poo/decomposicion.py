class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
            self._motor.temperaturas(260)
        elif tipo == "frena":
            self._motor.bolsas("activar")
            self._motor.temperaturas(90)
        else:
            self._motor.inyecta_gasolina(3)
            self._motor.temperaturas(130)

        self._estado = 'en_movimiento'


class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self.litros = 550

    def inyecta_gasolina(self, cantidad):
        self.litros -= cantidad

    def temperaturas(self, grados):
        if grados > 250:
            self.ventidaores("on")
        else:
            self.ventidaores("off")

        print(f'La temperatura actual es: {grados}°')

    def ventidaores(self, estado):
        if estado == "on":
            print('Se ha prendido el ventilador para regular la temperatura')
        else:
            print('Temperatura estable: no requiere de ventilación')

    def bolsas(self, estado):
        if estado == "activar":
            print("ACTIVANDO AIRBG")


if __name__ == '__main__':
    auto = Automovil("RS5", "Audi", "Plata")
    auto.acelerar("rapida")
    auto.acelerar("frena")
