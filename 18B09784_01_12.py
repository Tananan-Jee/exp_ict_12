# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784_01_12.py
#実行方法：ターミナル上で python3 18B09784_01_12.py を実行

size=int(input("alphabet size> "))
list = []

for i in range(size):
    ele =[input("symbol_" + str(i+1) + "> "),input("codeword_" + str(i+1) + "> ")]#get symbol and codeword
    list.append(ele)#make ex list=[['a',101],['b',1101],['c',0]]

codeword=input("codeword> ") # get codeword to decode

print("symbols: ", end="") # end="" is to make next element still be at the same line

start_position=0 #pointer
while start_position < len(codeword):  #ex code=10111011101

    for element in range(0,size):  #get codeword in the same length with each code length ex first one get 3 of them => 101
        count = 0                                                                          # second one get 4 of them => 1011
        keep = ""                                                                          # third one get 1 of them => 1
        while count<len(list[element][1]):
            keep = keep + codeword[start_position+count]
            count = count + 1

        if list[element][1] == keep: #then compair with the list number 101 = 101 , 1101 != 1011, 0 != 1
            print(list[element][0], end="") #if it is the same print out list alphabet 101 =a
            start_position=start_position+count #set the next position
            break

print(" ")
