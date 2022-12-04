###Proc1. Описать функцию powerA3(A), вычисляющую третью степень числа A и возвращающую ее (параметр вещественный). С помощью этой функции найти третьи степени пяти случайных чисел.
##import random
##def power_a3(a):
##    cube=a*a*a
##    return cube
##for i in range(5):
##    x= random.randint(-10,10)
##    print("x=",x,"x^3=", power_a3(x))
###Proc2. Описать 2 функции PowerA2(А), PowerA4(A), вычисляющие вторую и четвертую степень числа A и возвращающие эти степени (параметры являются вещественными). С помощью этих функций найти вторую и четвертую степень пяти случайных чисел
##import random
##def power_a2(a):
##    kv=a*a
##    return kv
##def power_a4(a):
##    fa=a*a*a*a
##    return fa
##for i in range(5):
##    x=random.randint(1,20)
##    print("x=",x,"x^2=",power_a2(x))
##print( )
##for i in range(5):
##    x=random.randint(1,20)
##    print("x=",x,"x^4=",power_a4(x))
###Proc3. Описать 2 функции aMean(X, Y), gMean(X,Y), вычисляющие среднее арифметическое aMean = (X+Y)/2 и среднее геометрическое gMean = √ X·Y двух положительных чисел X и Y (X и Y — входные параметры вещественного типа).
###С помощью этих функций найти среднее арифметическое и среднее геометрическое для 10 пар случайных чисел.
##import random
##import math
##def a_mean(x,y):
##    amean=(x+y)/2
##    return amean
##def g_mean(x,y):
##    gmean=math.sqrt(x*y)
##    return gmean
##for i in range(10):
##    x=random.randint(1,50)
##    y=random.randint(1,50)
##    print("x=",x,"y=",y,"(x+y)/2)=",a_mean(x,y))
##print( )
##for i in range(10):
##    x=random.randint(1,50)
##    y=random.randint(1,50)
##    print("x=",x,"y=",y,"(√x*y)=",g_mean(x,y))
###Proc4. Описать 2 функции triangleP(a) и triangleS(a), вычисляющие по стороне a равностороннего треугольника его периметр P = 3·a и площадь S = a 2 · √ 3/4 (параметры являются вещественными).
###С помощью этих функций найти периметры и площади трех равносторонних треугольников с данными сторонами (стороны ввести с клавиатуры).
##import random
##import math
##def triangle_p(a):
##    p=3*a
##    return p
##def triangle_s(a):
##    s=((a*a)*math.sqrt(3))/4
##    return s
##for i in range(3):
##    a=int(input())
##    print("a=",a,"P=", triangle_p(a))
##    print("a=",a,"S=", triangle_s(a))
###Proc5. Описать 2 функции rectP(x1, y1, x2, y2) и rectS(x1, y1, x2, y2), вычисляющие периметр P и площадь S прямоугольника со сторонами, параллельными осям координат, по координатам (x1, y1), (x2, y2) его противоположных вершин.
###С помощью этих функций найти периметры и площади трех прямоугольников с данными противоположными вершинами
##import random
##import math
##def rect_p(x1,y1,x2,y2):
##    p=(abs(x2-x1)+abs(y2-y1))*2
##    return p
##def rect_s(x1,y1,x2,y2):
##    s=abs(x2-x1)*abs(y2-y1)
##    return s
##for i in range(3):
##    x1=random.randint(-10,10)
##    y1=random.randint(-10,10)
##    x2=random.randint(-10,10)
##    y2=random.randint(-10,10)
##    print("(x1,y1)=",(x1,y1),"(x2,y2)=",(x2,y2),"P=",rect_p(x1,y1,x2,y2))
##    print("(x1,y1)=",(x1,y1),"(x2,y2)=",(x2,y2),"S=",rect_s(x1,y1,x2,y2))
#Proc6. Описать функцию digitSum(K), находящую сумму цифр целого положительного числа K (K входной параметр целого типа). С помощью этой функции найти сумму цифр для каждого из пяти данных целых чисел.
import random
def digit_sum(k):
    s=0
    while k!=0:
        cifr=k%10
        k=k//10
        s+=cifr
    return s

for i in range(5):
    a=random.randint(1,1000)
    print("a=",a,"digitsum=",digit_sum(a))
