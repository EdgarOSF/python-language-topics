import asyncio

class FlujoNumeros:

    def __init__(self, numeros):
        self.numeros = iter(list(numeros))
        self.cerrado = False
        self._abierto = False

    async def __aenter__(self):
        self.cerrado = False
        self._abierto = True
        return self

    async def __aexit__(self, exc_type, value, tb):
        self.cerrado = True
        self._abierto = False

        return False

    def __aiter__(self):
        if not self._abierto:
            raise RuntimeError
        return self

    async def __anext__(self):
        if self._abierto is False:
            raise RuntimeError
        try:
            value = next(self.numeros)
        except StopIteration:
            raise StopAsyncIteration
        await asyncio.sleep(0)
        return value



async def main():
    flujo = FlujoNumeros([10, 20, 30])

    async with flujo:
        async for numero in flujo:
            print(numero)

    print(flujo.cerrado)  # True

asyncio.run(main())
