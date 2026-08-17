import collections

elementos = {"cursos": 9.99, "playeras": 11.99, "stickers": 3.99}

carrito = collections.Counter(cursos=2, playeras=4, stickers=10)
total = collections.Counter()

for articulo, cantidad in carrito.items():
    subtotal = cantidad * elementos[articulo]
    precio = elementos[articulo]
    total.update({articulo: subtotal})

    print(f"{articulo:8}: $ {precio:7.2f} x {cantidad:2} subtotal: $ {subtotal:7.2f}")

print(" " * 27, f"total: $ {total.total():7}")
