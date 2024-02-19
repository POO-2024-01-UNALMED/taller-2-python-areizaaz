class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self,colorNuevo):
        if(colorNuevo == "rojo" or colorNuevo == "verde" or colorNuevo == "amarillo" or colorNuevo == "negro" or colorNuevo == "blanco"):
            self.color = colorNuevo

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registroNuevo):
        self.registro = registroNuevo
        
    def asignarTipo(self, tipoNuevo):
        if(tipoNuevo == "electrico" or tipoNuevo == "gasolina"):
            self.tipo = tipoNuevo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        contadorAsientos = 0
        for asiento in self.asientos:
            if(type(asiento) == Asiento):
                contadorAsientos += 1
        return contadorAsientos

    def verificarIntegridad(self):
        if(self.registro == self.motor.registro):
            for asiento in self.asientos:
                if asiento != None:
                    if(asiento.registro != self.registro):
                        return "Las piezas no son originales"
                    break
            return "Auto original"
        else:
            return "Las piezas no son originales"