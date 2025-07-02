def main():
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    print(car)

def make_car(model, car_type, **car_info):
    car_info['model'] = model
    car_info['type'] = car_type
    return car_info


if __name__ == '__main__':
    main()