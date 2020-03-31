# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784_02_01.py
#実行方法：ターミナル上で python3 18B09784_02_01.py を実行

asize=int(input("alphabet size> "))
length=int(input("length> "))

list = []

for i in range(asize):
    ele = [input("symbol_" + str(i+1) + "> "),float(input("p_" + str(i+1) + "> "))]
    list.append(ele)#list = [['a',0.3],['b',0.2],['c',0.7]]

#make shift ex. (a,b,c)->(b,c,a)->(c,a,b)
shift=[]
shift_ele=[]

for i in range(asize):
    for j in range(asize):
        shift_ele.append(list[(j+i)%asize])
    shift.append(shift_ele) #ex shift = [[['a',0.3],['b',0.2],['c',0.7]],[['b',0.2],['c',0.7],['a',0.3]],[['c',0.7],['a',0.3],['b',0.2]]]
    shift_ele=[]            #         (simple way to look) = [[a,b,c],[b,c,a],[c,a,b]]


keep = list[:]
keep_2 = []
keep_3_1 = ""
keep_3_2 = 0
value = []
count = 0

#list * shift[0] -> aa,bb,cc  also the same way with p
#list * shift[1] -> ab,bc,ca...
while count<length-1:
    for j in range(len(keep)):
        for k in range(len(shift)):
            keep_3_1 = keep[j][0] + shift[j%2][k][0]
            keep_3_2 = keep[j][1] * shift[j%2][k][1]
            value = [keep_3_1,keep_3_2]
            keep_2.append(value)
    count = count + 1
    keep = keep_2[:]

for i in range(len(keep)): #print only the one that have the size we want
    if len(keep[i][0])==length:
        print("P(" + keep[i][0] + "):" + str(round(keep[i][1],6)))
