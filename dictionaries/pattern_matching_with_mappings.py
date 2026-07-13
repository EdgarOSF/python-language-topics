from collections import OrderedDict


def get_creators(record: dict):
    match record:

        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

def get_food_details(record: dict):
    match record:
        case {'category': 'ice cream', **details}:
            print(f'Ice cream details: {details}')



if __name__ == "__main__":
    b1 = dict(
        api=1, 
        author='Douglas', 
        type='book', 
        title='Godel, Escher, Bach'
    )

    print(get_creators(b1))

    b2 = OrderedDict(
        api=2,
        type='book',
        title='Python in a nutshell',
        authors='Martelli Ravenscroft Holden'.split()
    )

    print(get_creators(b2))

    # print(get_creators({'type': 'book', 'pages': 770}))

    food = dict(category='ice cream', flavor='vanilla', cost=199)

    get_food_details(food)

