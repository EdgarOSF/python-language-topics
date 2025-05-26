class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
    
    def __add__(self, other):
        return Polynomial(*(a + b for a, b in zip(self.coeffs, other.coeffs)))

    def __repr__(self):
        return "Polynimial(*{!r})".format(self.coeffs)
    
    def __len__(self):
        return len(self.coeffs)
    
p1 = Polynomial(1, 2, 3)  # Represents 1 + 2x + 3x^2
p2 = Polynomial(3, 4, 3) 