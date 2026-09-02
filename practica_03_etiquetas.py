from dataclasses import dataclass

@dataclass(frozen=True)
class Etiqueta:
    texto: str

    def __eq__(self, other):
        
        if not isinstance(other, Etiqueta):
            return NotImplemented
        
        return self.texto.lower() == other.texto.lower()

    def __repr__(self):
         
        return f"Etiqueta({self.texto!r})"

    def __hash__(self):
        return hash(self.texto.lower())

backend = Etiqueta("Backend")
otra = Etiqueta("backend")

print(backend == otra)       # True
print({backend, otra})       # {Etiqueta('Backend')}  (solo un elemento)
print(backend.texto)         # Backend

backend.texto = "Python"     # Debe lanzar AttributeError

