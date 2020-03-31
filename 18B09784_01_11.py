# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784_01_11.py
#実行方法：ターミナル上で python3 18B09784_01_11.py を実行

size=int(input("alphabet size> "))
list = []

for i in range(size):

    ele =[input("symbol_" + str(i+1) + "> "),input("codeword_" + str(i+1) + "> ")] #get symbol and codeword
    list.append(ele) #make ex list=[['a',10],['b',11],['c',0]]


symbols=input("symbols> ") # get symbols to encode

print("codewords: ", end ="") # end="" is to make next element still be at the same line

#encode
for j in symbols:
    for x in range(size):
        if j == list[x][0]:  #if symbol=first character of sublist in list   ex b
            print(list[x][1], end="") # print second character of sublist in list ex 11

print(" ")
