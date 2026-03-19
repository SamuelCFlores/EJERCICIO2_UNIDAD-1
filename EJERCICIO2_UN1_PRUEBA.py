from EJERCICIO2_UN1 import *

### PRUEBA CLASES
# PRUEBA PERSONAS
 
Persona1 = Persona("001", "Samuel", "samueel@gmail.com" )
Persona2 = Persona("002", "Camila", "camilongo@gmail.com" )
Persona3 = Persona("003", "Carlos", "carlos10messi@gmail.com" )
Persona4 = Persona("004", "Alejandro", "alejandro12@gmail.com" )
Persona5 = Persona("005", "Paulina", "paulinaaa08@gmail.com" )
Persona6 = Persona("006", "Sara", "s41241@gmail.com" )
Persona7 = Persona("007", "Yuridia", "6y102@gmail.com" )
Persona8 = Persona("008", "Jesús", "jesus10201@gmail.com" )
Persona9 = Persona("009", "Josué", "josca412@gmail.com" )
Persona10 = Persona("010", "Vania", "ainav123@gmail.com" )

Personas = [Persona1, Persona2, Persona3, Persona4, Persona5, 
            Persona6, Persona7, Persona8, Persona9, Persona10]

for p in Personas:
    print(f"ID: {p.idPersona} // Nombre: {p.nombre} // Email: {p.email}")

# PRUEBA CLIENTE
# En esta parte la clase cliente hereda de "Persona(), por lo que en un escenario "realista", C1-5 hereda de persona es decir solo agrega datos faltantes
# en caso de ser necesario, de C6-10 son clientes nuevos para verificar que si funciona y que despúes se pueda dar continuidad a trabajadores, clientes etc
# según sea el caso

# PRUEBA CLIENTE

Cliente1 = Cliente("001", "Samuel", "samueel@gmail.com")
Cliente2 = Cliente("002", "Camila", "camilongo@gmail.com")
Cliente3 = Cliente("003", "Carlos", "carlos10messi@gmail.com")
Cliente4 = Cliente("004", "Alejandro", "alejandro12@gmail.com")
Cliente5 = Cliente("005", "Paulina", "paulinaaa08@gmail.com")

#NUEVOS
Cliente6 = Cliente("011", "Luis", "luis123@gmail.com")
Cliente7 = Cliente("012", "Fernanda", "fer_98@gmail.com")
Cliente8 = Cliente("013", "Diego", "diegoxd@gmail.com")
Cliente9 = Cliente("014", "Mariana", "mariana_22@gmail.com")
Cliente10 = Cliente("015", "Ricardo", "richi_pro@gmail.com")

Clientes = [Cliente1, Cliente2, Cliente3, Cliente4, Cliente5,
            Cliente6, Cliente7, Cliente8, Cliente9, Cliente10]

for c in Clientes:
    print(f"ID: {c.idPersona} // Nombre: {c.nombre} // Email: {c.email} // Puntos: {c.puntosFidelidad}")

# PRUEBA EMPLEADO
# En esta parte empleado hereda de Persona(), por lo que E1-5 son personas existentes
# E6-10 son empleados nuevos

# PERSONAS EXISTENTES
Empleado1 = Empleado("006", "Sara", "s41241@gmail.com", "E001", "BARISTA")
Empleado2 = Empleado("007", "Yuridia", "6y102@gmail.com", "E002", "MESERO")
Empleado3 = Empleado("008", "Jesús", "jesus10201@gmail.com", "E003", "GERENTE")
Empleado4 = Empleado("009", "Josué", "josca412@gmail.com", "E004", "BARISTA")
Empleado5 = Empleado("010", "Vania", "ainav123@gmail.com", "E005", "MESERO")

# NUEVOS
Empleado6 = Empleado("016", "Mario", "mario@gmail.com", "E006", "BARISTA")
Empleado7 = Empleado("017", "Lucia", "lucia@gmail.com", "E007", "GERENTE")
Empleado8 = Empleado("018", "Raul", "raul@gmail.com", "E008", "MESERO")
Empleado9 = Empleado("019", "Elena", "elena@gmail.com", "E009", "BARISTA")
Empleado10 = Empleado("020", "Pablo", "pablo@gmail.com", "E010", "MESERO")

Empleados = [Empleado1, Empleado2, Empleado3, Empleado4, Empleado5,
             Empleado6, Empleado7, Empleado8, Empleado9, Empleado10]

for e in Empleados:
    print(f"ID: {e.idPersona} // Nombre: {e.nombre} // Email: {e.email} // ID EMP: {e.idEmpleado} // ROL: {e.rol}")

# PRUEBA PRODUCTO BASE

Producto1 = ProductoBase("P001", "Cafe Americano", 30)
Producto2 = ProductoBase("P002", "Latte", 40)
Producto3 = ProductoBase("P003", "Capuccino", 45)
Producto4 = ProductoBase("P004", "Te", 25)
Producto5 = ProductoBase("P005", "Chocolate", 35)

Producto6 = ProductoBase("P006", "Pan", 20)
Producto7 = ProductoBase("P007", "Galleta", 15)
Producto8 = ProductoBase("P008", "Brownie", 28)
Producto9 = ProductoBase("P009", "Pastel", 50)
Producto10 = ProductoBase("P010", "Muffin", 22)

Productos = [Producto1, Producto2, Producto3, Producto4, Producto5,
             Producto6, Producto7, Producto8, Producto9, Producto10]

for p in Productos:
    print(f"ID: {p.idProducto} // Nombre: {p.nombre} // Precio: {p.precioBase}")

# PRUEBA BEBIDA

Bebida1 = Bebida("B001", "Latte", 40, "GRANDE", "CALIENTE")
Bebida2 = Bebida("B002", "Capuccino", 45, "MEDIANO", "CALIENTE")
Bebida3 = Bebida("B003", "Frappé", 50, "GRANDE", "FRIA")
Bebida4 = Bebida("B004", "Americano", 30, "CHICO", "CALIENTE")
Bebida5 = Bebida("B005", "Te Helado", 35, "MEDIANO", "FRIA")

Bebida6 = Bebida("B006", "Mocha", 48, "GRANDE", "CALIENTE")
Bebida7 = Bebida("B007", "Chocolate", 42, "MEDIANO", "CALIENTE")
Bebida8 = Bebida("B008", "Matcha", 55, "GRANDE", "FRIA")
Bebida9 = Bebida("B009", "Chai", 38, "MEDIANO", "CALIENTE")
Bebida10 = Bebida("B010", "Cold Brew", 60, "GRANDE", "FRIA")

Bebidas = [Bebida1, Bebida2, Bebida3, Bebida4, Bebida5,
           Bebida6, Bebida7, Bebida8, Bebida9, Bebida10]

for b in Bebidas:
    print(f"ID: {b.idProducto} // Nombre: {b.nombre} // Tamaño: {b.tamaño} // Temp: {b.temperatura} // Precio Base: {b.precioBase}")

# PRUEBA POSTRE

Postre1 = Postre("PO1", "Brownie", 25, False, False)
Postre2 = Postre("PO2", "Galleta", 15, False, False)
Postre3 = Postre("PO3", "Pastel", 50, False, False)
Postre4 = Postre("PO4", "Pan Vegano", 30, True, False)
Postre5 = Postre("PO5", "Pan Sin Gluten", 35, False, True)

Postre6 = Postre("PO6", "Cupcake", 28, False, False)
Postre7 = Postre("PO7", "Donut", 20, False, False)
Postre8 = Postre("PO8", "Pay", 45, False, False)
Postre9 = Postre("PO9", "Galleta Vegana", 18, True, False)
Postre10 = Postre("PO10", "Pastel Sin Gluten", 55, False, True)

Postres = [Postre1, Postre2, Postre3, Postre4, Postre5,
           Postre6, Postre7, Postre8, Postre9, Postre10]

for p in Postres:
    print(f"ID: {p.idProducto} // Nombre: {p.nombre} // Precio: {p.precioBase} // Vegano: {p.esVegano} // Gluten: {p.sinGluten}")

# PRUEBA PEDIDO

Pedido1 = Pedido("PED1")
Pedido2 = Pedido("PED2")
Pedido3 = Pedido("PED3")
Pedido4 = Pedido("PED4")
Pedido5 = Pedido("PED5")
Pedido6 = Pedido("PED6")
Pedido7 = Pedido("PED7")
Pedido8 = Pedido("PED8")
Pedido9 = Pedido("PED9")
Pedido10 = Pedido("PED10")

Pedidos = [Pedido1, Pedido2, Pedido3, Pedido4, Pedido5,
           Pedido6, Pedido7, Pedido8, Pedido9, Pedido10]

for p in Pedidos:
    print(f"ID: {p.idPedido} // Estado: {p.estado} // Total: {p.total}")

# PRUEBA INVENTARIO

inventario = Inventario()

inventario.agregarIngrediente("Cafe", 10)
inventario.agregarIngrediente("Leche", 8)
inventario.agregarIngrediente("Azucar", 15)
inventario.agregarIngrediente("Chocolate", 5)
inventario.agregarIngrediente("Harina", 7)
inventario.agregarIngrediente("Huevos", 12)
inventario.agregarIngrediente("Mantequilla", 6)
inventario.agregarIngrediente("Canela", 3)
inventario.agregarIngrediente("Vainilla", 2)
inventario.agregarIngrediente("Hielo", 20)

for nombre, cantidad in inventario.ingredientes.items():
    print(f"Ingrediente: {nombre} // Cantidad: {cantidad}")

# PRUEBA METODOS 
# PRUEBA MÉTODOS PERSONA

p1 = Persona("001", "Samuel", "samueel@gmail.com")

p1.login()
p1.actualizarPerfil()

# PRUEBA MÉTODOS CLIENTE

c1 = Cliente("001", "Samuel", "samueel@gmail.com")

# intentar sin login
pedido_temp = Pedido("P1")
c1.realizarPedido(pedido_temp)

# login
c1.login()

# crear pedido
pedido1 = Pedido("PED1")
bebida1 = Bebida("B001", "Latte", 40, "GRANDE", "CALIENTE")
bebida1.agregarExtra("Leche de almendra")

pedido1.agregarProducto(bebida1)
pedido1.calcularTotal()

# realizar pedido
c1.realizarPedido(pedido1)

# consultar historial
c1.consultarHistorial()

# canjear puntos
c1.canjearPuntos(10)

# PRUEBA MÉTODOS EMPLEADO

e1 = Empleado("006", "Sara", "s41241@gmail.com", "E001", "BARISTA")

# actualizar inventario
e1.actualizarInventario("Cafe", 20)

# cambiar estado pedido
pedido1 = Pedido("PED1")
e1.cambiarEstadoPedido(pedido1.idPedido, "PREPARANDO")

# PRUEBA MÉTODOS BEBIDA

b1 = Bebida("B001", "Latte", 40, "GRANDE", "CALIENTE")

b1.agregarExtra("Shot extra")
b1.agregarExtra("Leche deslactosada")

precio_final = b1.calcularPrecioFinal()
print(f"Precio final: {precio_final}")

# PRUEBA MÉTODOS PEDIDO

pedido1 = Pedido("PED1")

b1 = Bebida("B001", "Latte", 40, "GRANDE", "CALIENTE")
b1.agregarExtra("Shot")

p1 = Postre("PO1", "Brownie", 25, False, False)

pedido1.agregarProducto(b1)
pedido1.agregarProducto(p1)

pedido1.validarStock()

total = pedido1.calcularTotal()
print(f"Total del pedido: {total}")

puntos = pedido1.calcularPuntos()
print(f"Puntos generados: {puntos}")

# PRUEBA MÉTODOS INVENTARIO

inv = Inventario()

inv.agregarIngrediente("Cafe", 5)
inv.agregarIngrediente("Leche", 2)

inv.reducirStock("Cafe", 2)
inv.reducirStock("Leche", 1)

inv.notificarFaltante("Leche")
inv.notificarFaltante("Cafe")

### PRUEBA DE LÓGICA

# PRUEBA DE RETOS - FLUJO COMPLETO DEL SISTEMA

# CREAR CLIENTE
cliente1 = Cliente("001", "Samuel", "samueel@gmail.com")
cliente1.login()

# CREAR INVENTARIO
inventario = Inventario()
inventario.agregarIngrediente("Cafe", 10)
inventario.agregarIngrediente("Leche", 10)

# CREAR PRODUCTOS
bebida1 = Bebida("B001", "Latte", 40, "GRANDE", "CALIENTE")
bebida1.agregarExtra("Leche de almendra")

postre1 = Postre("P001", "Brownie", 25, False, False)

# CREAR PEDIDO
pedido1 = Pedido("PED1")
pedido1.agregarProducto(bebida1)
pedido1.agregarProducto(postre1)

pedido1.validarStock()

# CALCULAR TOTAL
total = pedido1.calcularTotal()
print(f"Total del pedido: {total}")

# CLIENTE REALIZA PEDIDO
cliente1.realizarPedido(pedido1)

# CREAR EMPLEADO
empleado1 = Empleado("006", "Sara", "s41241@gmail.com", "E001", "BARISTA")

# EMPLEADO INTERACTÚA
empleado1.actualizarInventario("Cafe", 8)
empleado1.cambiarEstadoPedido(pedido1.idPedido, "PREPARANDO")

# CAMBIAR ESTADO FINAL
empleado1.cambiarEstadoPedido(pedido1.idPedido, "ENTREGADO")

# CONSULTAR HISTORIAL
cliente1.consultarHistorial()

# CANJEAR PUNTOS
cliente1.canjearPuntos(10)