from EJERCICIO2_UN1 import *

# PRUEBA GENERAL DEL SISTEMA

print("INICIO DE PRUEBAS DEL SISTEMA")


# CREAR INVENTARIO
inventario = Inventario()
inventario.agregarIngrediente("Cafe", 10)
inventario.agregarIngrediente("Leche", 8)
inventario.agregarIngrediente("Azucar", 5)

print("Inventario inicial:")
print(inventario.ingredientes)


# CREAR CLIENTE
cliente1 = Cliente(1, "Carlos", "carlos@email.com")

print("Intentando hacer pedido sin login")
pedido_fallido = Pedido(100)
cliente1.realizarPedido(pedido_fallido)


# LOGIN
print("Login del cliente")
cliente1.login()


# ACTUALIZAR PERFIL
print("Actualizar perfil")
cliente1.actualizarPerfil()


# CREAR PRODUCTOS
cafe = Bebida(1, "Latte", 4.5, "Grande", "CALIENTE")
cafe.agregarExtra("Leche de almendra")
cafe.agregarExtra("Caramelo")

te = Bebida(2, "Té Verde", 3.0, "Mediano", "CALIENTE")

pastel = Postre(3, "Cheesecake", 5.5, False, False)


# CREAR PEDIDO
pedido1 = Pedido(101)

pedido1.agregarProducto(cafe)
pedido1.agregarProducto(te)
pedido1.agregarProducto(pastel)

print("Calculando total del pedido")
total = pedido1.calcularTotal()
print("Total:", total)


# VALIDAR STOCK
pedido1.validarStock()


# CLIENTE REALIZA PEDIDO
cliente1.realizarPedido(pedido1)


# CONSULTAR HISTORIAL
print("Historial del cliente")
cliente1.consultarHistorial()


# CANJEAR PUNTOS
print("Intentando canjear puntos")
cliente1.canjearPuntos(5)


# CREAR EMPLEADO
empleado1 = Empleado(2, "Ana", "ana@cafe.com", 501, "BARISTA")

print("Empleado actualizando inventario")
empleado1.actualizarInventario("Cafe", 20)


# REDUCIR INVENTARIO
inventario.reducirStock("Cafe", 3)
inventario.reducirStock("Leche", 6)

inventario.notificarFaltante("Leche")


# CAMBIAR ESTADO DEL PEDIDO
print("Cambio de estado del pedido")
empleado1.cambiarEstadoPedido(pedido1.idPedido, "PREPARANDO")

pedido1.estado = "PREPARANDO"

empleado1.cambiarEstadoPedido(pedido1.idPedido, "ENTREGADO")

pedido1.estado = "ENTREGADO"

print("Estado final del pedido:", pedido1.estado)

print("FIN DE PRUEBAS")
