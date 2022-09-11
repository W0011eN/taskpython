#Задание 1 
#Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
#Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
#Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

import sys

def pay(kch,sch,p):
    zp = kch * sch
    return zp + p

ch=st=pr= ''
if __name__ == '__main__':
    if len(sys.argv) > 1:
        ch = sys.argv[1]
    if len(sys.argv) > 2:
        st = sys.argv[2]
    if len(sys.argv) > 3:
        pr = sys.argv[3]
print(f'Заработная плата {pay(float(ch),float(st),float(pr))}')
