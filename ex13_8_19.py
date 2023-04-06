col_ticket = int(input("Введите число билетов к покупке:"))
if col_ticket < 1 or col_ticket > 100:
   print("Неверное количество билетов. Попробуйте еще раз.")
else:
    list_vizitors = []
    i = 0
    while i < col_ticket:
        list_vizitors.append(int(input(f"Введите возраст посетителя {i+1}:")))
        i += 1
    Final_check = 0
    element = 0
    for element in range(len(list_vizitors)):
        if list_vizitors[element] > 25:
            Final_check += 1390
        elif list_vizitors[element] > 18:
            Final_check += 990
    print("Стоимость билетов составляет:")
    print(Final_check)
    if col_ticket > 3:
        Final_check *= 0.9
        print("Но... Вам положена скидка за опт!")
    print(f"Итого к оплате: {Final_check} рублей")

#int_list = []
#for element in input(f"Введите возраст посетителей через пробел:").split():
#    int_list.append(int(element))
#print(int_list)