# EJERCICIO 2: GESTIÓN DE PEDIDOS DE UNA CAFETERÍA

# 1. MÓDULO DE PERSONAS (HERENCIA)

# PERSONA (CLASE BASE - ABSTRACTA) , CLASE FUNDAMENTAL PARA IDENTIFICAR A CUALQUIER INDIVIDIO EN EL SISTEMA
# ATRIBUTOS: idPersona: int, nombre: String, email: String
# MÉTODOS: login(), actualizarPerifil()

class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
        self.logueado = False  # Estado de sesión

    def login(self):
        usuario = input("Ingrese su nombre de usuario: ")

        if usuario == self.nombre:
            self.logueado = True
            print(f"{self.nombre} ha iniciado sesión.")
        else:
            print("Usuario incorrecto.")

    def actualizarPerfil(self, nuevo_nombre=None, nuevo_email=None):
        
        nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
        nuevo_email = input("Ingrese el nuevo email (deje en blanco para no cambiar): ")

        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_email:
            self.email = nuevo_email

        print(f"{self.nombre} ha actualizado su perfil.")

# CLIENTE (HEREDA DE PERSONA) , USUARIO QUE REALIZA EL CONSUMO
# ATRIBUTOS: puntosFidelidad: int, historialPedidos: List<Pedido>, 
# METODOS: realizarPedido(), consultarHistorial(), canjearPuntos()

class Cliente(Persona):
    def __init__(self, idPersona, nombre, email):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad = 0
        self.historialPedidos = []

    def realizarPedido(self, pedido):
        if self.logueado:
            self.historialPedidos.append(pedido)
            self.puntosFidelidad += pedido.calcularPuntos()
            print(f"{self.nombre} ha realizado un pedido. Puntos acumulados: {self.puntosFidelidad}")
        else:
            print("Debe iniciar sesión para realizar un pedido.")

    def consultarHistorial(self):
        if self.logueado:
            print(f"Historial de pedidos de {self.nombre}:")
            for pedido in self.historialPedidos:
                print(pedido)
        else:
            print("Debe iniciar sesión para consultar el historial.")

    def canjearPuntos(self, puntos):
        if self.logueado:
            if puntos <= self.puntosFidelidad:
                self.puntosFidelidad -= puntos
                print(f"{self.nombre} ha canjeado {puntos} puntos. Puntos restantes: {self.puntosFidelidad}")
            else:
                print("No tiene suficientes puntos para canjear.")
        else:
            print("Debe iniciar sesión para canjear puntos.")   

# EMPLEADO (HEREDA DE PERSONA), PERSONAL QUE OPERA LA CAFETERÍA
# ATRIBUTOS: idEmpleado: int, rol: Enum (BARISTA, MESERO, GERENTE) .
# MÉTODOS: actualizarInventario(), cambiarEstadoPedido()

class Empleado(Persona): 
    def __init__(self, idPersona, nombre, email, idEmpleado, rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol

    def actualizarInventario(self, producto, cantidad):
        if self.rol in ["BARISTA", "GERENTE"]:
            print(f"{self.nombre} ha actualizado el inventario: {producto}  Cantidad: {cantidad}")
        else:
            print(f"{self.nombre} no tiene permisos para actualizar el inventario.")

    def cambiarEstadoPedido(self, pedido, nuevo_estado):
        print(f"{self.nombre} ha cambiado el estado del pedido {pedido} a {nuevo_estado}")

# 2. MÓDULO DE PRODUCTOS

# PRODUCTOBASE (CLASE BASE) , DEFINE LAS PROPIEDADES GENERALES DE LO QUE SE VENDE
# ATRIBUTOS: idProducto: int, nombre: String, precioBase: float

class ProductoBase:
    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase

    def mostrarInfo(self):
        print(f"Producto: {self.nombre} | Precio base: {self.precioBase}")

# BEBIDA (HEREDA DE PRODUCTOBASE) , PRODUCTOS LÍQUIDOS PERSONALIZABLES
# ATRIBUTOS: tamaño: String, temperatura: Enum(FRIA, CALIENTE), modificadores: List<String>
# MÉTODOS: agregarExtra(), calcularPrecioFinal()

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño = tamaño
        self.temperatura = temperatura
        self.modificadores = []

    def agregarExtra(self, extra):
        self.modificadores.append(extra)
        print(f"Se agregó el extra: {extra}")

    def calcularPrecioFinal(self):
        precio = self.precioBase + (len(self.modificadores) * 0.5)
        return precio

# POSTRE (HEREDA DE PRODUCTOBASE) , PRODUCTOS DE REPOSTERÍA
# ATRIBUTOS: esVegano: boolean, sinGluten: boolean

class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, esVegano, sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten

# 3. LOGISTICA Y VENTAS 
# PEDIDO , GESTIÓN DE LA TRANSACCIÓN ACTUAL
# ATRIBUTOS: idPedido: int, productos: List<ProductoBase>, estado: Enum(PENDIENTE, PREPARANDO, ENTREGADO), total: float
# MÉTODOS: calcularTotal(), validarStock()

class Pedido:
    def __init__(self, idPedido):
        self.idPedido = idPedido
        self.productos = []
        self.estado = "PENDIENTE"
        self.total = 0

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self.productos:
            if hasattr(producto, "calcularPrecioFinal"):
                total += producto.calcularPrecioFinal()
            else:
                total += producto.precioBase
        self.total = total
        return total

    def validarStock(self):
        print("Stock validado para el pedido.")

    def calcularPuntos(self):
        return int(self.total)
    
# INVENTARIO , CONTROL DE SUMINISTROS
# ATRIBUTOS: ingredientes: Map<String, Integer>
# MÉTODOS: reducirStock(), notificarFaltante()

class Inventario:
    def __init__(self):
        self.ingredientes = {}

    def agregarIngrediente(self, nombre, cantidad):
        self.ingredientes[nombre] = cantidad

    def reducirStock(self, nombre, cantidad):
        if nombre in self.ingredientes:
            self.ingredientes[nombre] -= cantidad
            print(f"Stock actualizado: {nombre} ahora tiene {self.ingredientes[nombre]}")
        else:
            print("Ingrediente no encontrado.")

    def notificarFaltante(self, nombre):
        if self.ingredientes.get(nombre, 0) <= 2:
            print(f"⚠ Falta inventario de {nombre}")