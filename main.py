from fractions import Fraction
import re

def main():
    pattern = r'^[+-]?\d*[.,]?\d+$'
    user_input = input('informe a dizima periodica (por exemplo 0.111) para descobrir sua fração: ')
    if re.match(pattern, user_input):
        fraction = transform_to_fraction(user_input)
        print(f'a fração geratriz é: { fraction}')
    else:
        print('input no formato inválido')   
    ...
  
    
def transform_to_fraction(number):
    if ',' in number:
       number = number.replace(',', '.')
        
    integer, period, not_period = search_integer_period_and_not_period(number)
    numerator = int(integer+not_period+period) - int(integer+not_period)
    denominator = int('9'*len(period) +'0'*len(not_period))
    fraction = Fraction(numerator=numerator, denominator=denominator)
    fraction = fraction.limit_denominator()
    
    return str(fraction)
    ...


def search_integer_period_and_not_period(number):
    integer, decimal = number.split('.')
    integer = integer

    decimal_length = len(decimal)

    if decimal_length <= 2:
        return (integer,decimal, '')
    else:
        max_length = 0

        for i in range(decimal_length):
            for j in range(i + 1, decimal_length + 1):
                sub_number = decimal[i:j]
                if decimal.count(sub_number) > 1 and len(sub_number) > max_length:
                    max_length = len(sub_number)
                    period = sub_number

        not_period = decimal.replace(period, '')
        if not_period:

            return (integer,period, not_period)
        else:
            return (integer,period, '')
        ...


if __name__ == "__main__":
    main()
