import math

while True:
    print("Введите номер задачи: 1-5")
    i = int(input())

    # task1
    if (i == 1):
        nameSurname = input("Ваши фамилия, имя? ")
        age = input("Сколько вам лет? ")
        location = input("Где вы живёте? ")
        print("Ваши фамилия, имя " + nameSurname)
        print("Ваш возраст " + age)
        print("Вы живёте в " + location)


    #task2
    if(i == 2):
        x = 10
        t = 1
        print("z = " +
              str((9*math.pi*t + 10*math.cos(x)/(math.sqrt(t) - abs(math.sin(t))))*math.pow(math.e,x))
        )


    #task3
    if(i == 3):
        print("Введите число 1")
        number1 = int(input())

        print("Введите число 2")
        number2 = int(input())

        print("Введите число 3")
        number3 = int(input())

        count = 0

        print("Принадлежат интервалу [1, 3] числа: ")
        if(number1 <= 3 and number1 >= 1):
            print(str(number1))
            count = count + 1
        if(number2 <= 3 and number2 >= 1):
            print(str(number2))
            count = count + 1
        if(number3 <= 3 and number3 >= 1):
            print(str(number3))
            count = count + 1
        if(count == 0):
            print("Нет таких чисел!")


    #task4
    if(i == 4):

        print("Задание 4.6: По данному натуральному n вычислите n!")
        n = int(input("Введите n > 0: "))
        proizv = 1
        if (n == 1):
            print("Сумма " + str(n) + "= " + str(sum))
        else:
            while(n > 1):
                proizv = proizv * n
                n = n - 1
        print(str(proizv))



        print("Задание 4.7: по данному натуральном n вычислите сумму 1! + 2! + ... + n!")
        print("Введите n > 0: ")
        n = int(input())
        k = 1
        sum = 0

        for i in range(1, n + 1):
            k *= i
            sum += k
        print(sum)



        print("Задание 4.8: По данному натуральному n <= 9 вывести лесенку из n ступенек")
        print("Введите n: ")
        n = int(input())
        k = 0
        chislo = ""

        while(k != n):
            if(n == 1):
                print("1")
                break

            while(k + 1 <= n):
                k = k + 1
                chislo = chislo + str(k)
                print(chislo)


    # task5
    if (i == 5):
        print("Вариант 8: посчитать сколько слов в строке до точки")

        stroka = "Ветер подул, листья упали! Хорошо в деревне."
        print(len(stroka.partition(".")[0].split()))


