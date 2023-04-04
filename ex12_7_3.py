per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
cl_per =[]
cl_per.append(per_cent.get('ТКБ'))
cl_per.append(per_cent.get('СКБ'))
cl_per.append(per_cent.get('ВТБ'))
cl_per.append(per_cent.get('СБЕР'))

print('Ставки в банках:')
print(cl_per)
money = int(input("Введите сумму средств к размещению:"));

deposit = []
for i in cl_per:
    deposit.append(i * money/100);
#deposit.append(cl_per[0] * money/100);
#deposit.append(cl_per[1] * money/100);
#deposit.append(cl_per[2] * money/100);
#deposit.append(cl_per[3] * money/100);
print("Сумма заработанных процентов в банках: ТКБ, СКБ, ВТБ, СБЕР (соответственно):")
print(deposit)
print()
print("Максимальную сумму, которую вы можете заработать: ", max(deposit))