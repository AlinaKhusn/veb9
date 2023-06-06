# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
#f = open('test_file/task_3.txt', 'r', encoding="utf8")
#while f.readline().isdigit():

file = open("test_file/task_3.txt", "r", encoding="utf-8")
total = 0
buy = []
for i in file.readlines():
    if i != '\n':
        total += int(i)
    else:
        buy.append(total)
        total = 0
buy.sort()
three_most_expensive_purchases = sum(buy[-3::])
file.close

assert three_most_expensive_purchases == 202346