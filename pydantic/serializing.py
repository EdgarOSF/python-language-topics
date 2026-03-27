from enum import Enum
from pydantic import BaseModel, PositiveInt, Field


class RolJugador(Enum):
    basico = "basico"
    premium = "premium"


class Jugador(BaseModel):
    id: PositiveInt
    name: str = Field(max_length=20)
    rol: RolJugador
    friends: list[int] = []


dic_jugador = {
    'id': 1,
    'name': 'Edgar',
    'rol': 'basico',
    'friends': ['1', '2', '3']
}

jugador = Jugador(**dic_jugador)

print(jugador)
print(jugador.model_dump_json())
# print(jugador.model_json_schema())
