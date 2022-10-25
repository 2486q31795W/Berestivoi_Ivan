print ('Введите свой возраст')
age = int (input())
print ('Введите свое имя')
name = str (input())
if name !='Иван':
    if age > 0 and age < 75:
        if age >= 16:
            print ('Поздравляем, Вы поступили в ВГУИТ')   
        else:           
             print ('Сначала надо окончить школу')
             print ('Вам осталось учиться', 16 - age, 'лет') 
else:
    print('Извините, но вас зовут Иван')
