import asyncio

class FlujoNumeros:

    def __init__(self, numeros):
        self.numeros = list(numeros)
        self.cerrado = None

    async def __aenter__(self):
        self.cerrado = False
        return self

    async def __aexit__(self, exc_type, value, tb):
        self.cerrado = True

        # if exc_type is None:
        #     return self.cerrado
        return False

    def __aiter__(self):
        if self.cerrado is True:
            raise RuntimeError
        return iter(self.numeros)

    async def __anext__(self):
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
