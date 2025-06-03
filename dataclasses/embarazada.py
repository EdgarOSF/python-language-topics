from dataclasses import dataclass, field
from datetime import date


@dataclass
class Embarazada:
    """Clase que representa a una embarazada"""
    nombre: str
    fecha_nacimiento: str
    edad: int
    derechohabiencia: str
    peso: float
    altura: float
    imc: float = field(init=False)
    religion: str
    es_indigena: str
    ocupacion: str

    def __post_init__(self):
        self.imc = self.peso / (self.altura / 100)



if __name__ == '__main__':
    emb1 = Embarazada(
        'Erika Lissete Reyes Morales', 
        '12-05-2000',
        25,
        'Imss Bienestar',
        87,
        150,
        'Catolica',
        'No',
        'Ama de casa'
    )

    print(emb1)