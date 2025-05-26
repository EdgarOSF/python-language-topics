from dataclasses import dataclass, asdict, astuple, fields


@dataclass
class InventoryItem:
    """Class for keeping of a item in enventory"""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self):
        return self.unit_price * self.quantity_on_hand


itm = InventoryItem('Casco', 220, 20)

print(itm)
print(itm.name)
print(type(itm.name))
print(itm.unit_price)
print(type(itm.unit_price))
itm.name = 'moto'
print(itm)
print(type(itm))

print(asdict(InventoryItem('Chamarra', 550.0, 10)) )
print(astuple(InventoryItem('Chamarra', 550.0, 10)) )

print(tuple(getattr(itm, field.name) for field in fields(itm)))