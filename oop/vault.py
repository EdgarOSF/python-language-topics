class Vault:
    def __init__(self, galeons=0, sickles=0, knuts=0) -> None:
        self.galeons = galeons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self) -> str:
        return f'Galeons: {self.galeons}, Sickles: {self.sickles}, Knuts: {self.knuts}'

    # Operator OVerloading 
    def __add__(self, other):
        galeons = self.galeons + other.galeons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galeons, sickles, knuts)
    

harry = Vault(100, 50, 25)
ron = Vault(25, 50, 100)
total = harry + ron # Use of Operator Overloading

print('Harry: ', harry)
print('Ron: ', ron)
print('Total: ', total)