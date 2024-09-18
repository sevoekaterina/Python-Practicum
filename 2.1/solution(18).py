good = input()
price = int(input())
weight = int(input())
cash = int(input())

price_string = str(weight) + 'кг * ' + str(price) + 'руб/кг'
sum_string = str(price * weight) + 'руб'
cash_string = str(cash) + 'руб'
change_string = str(cash - price * weight) + 'руб'

print('================Чек================')
print(f'Товар: {good:>28}')
print(f'Цена: {price_string:>29}')
print(f'Итого: {sum_string:>28}')
print(f'Внесено: {cash_string:>26}')
print(f'Сдача: {change_string:>28}')
print('===================================')