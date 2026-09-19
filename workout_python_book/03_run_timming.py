from decimal import Decimal


def run_timing():
    number_of_runs = 0
    total_time = 0.0

    while True:
        run_time = input('Enter 10k run time: ').strip()
        
        if not run_time:
            break
        
        try:
            run_time = float(run_time)
        except ValueError:
            print('Please enter a valid number')
            continue
        
        total_time += run_time
        number_of_runs += 1

    if number_of_runs:
        average_time = total_time / number_of_runs
        print(f'Average of {average_time:.1f}, over {number_of_runs} runs')

# run_timing()

# minireto 1
def partial_float(number, before, after):
    if before < 0 or after < 0:
        raise ValueError('Before and after must not be negative')

    before_number, after_number = str(number).split('.')

    before_number = before_number[-before:]
    after_number = after_number[:after]
    new_float = before_number + '.' + after_number

    return float(new_float)

# print(partial_float(1234.5678, 2, 3))

# minireto 2
def sum_decimal():
    first_number = Decimal(input('First number: '))
    second_number = Decimal(input('Second number: '))

    return first_number + second_number

print(sum_decimal())

