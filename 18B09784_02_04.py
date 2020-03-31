# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784_02_04.c
#実行方法：ターミナル上で python3 18B09784_02_04.c を実行

import math

def decimalToBinary(num, k) : #change decimal fraction to binary
    binary = ""
    Integral = int(num)
    fractional = num - Integral
    while (Integral) :
        rem = Integral % 2
        binary += str(rem);
        Integral //= 2
    binary = binary[ : : -1]
    binary += '.'

    while (k) :
        fractional *= 2
        fract_bit = int(fractional)
        if (fract_bit == 1) :
            fractional -= fract_bit
            binary += '1'
        else :
            binary += '0'
        k -= 1
    return binary


def binaryToDecimal(binary,bi_length) : #change binary to decimal fraction
    two = 2
    fracDecimal = 0
    for i in range(bi_length):
        fracDecimal += (ord(binary[i]) - ord('0')) / two
        two *= 2.0
    return fracDecimal


size=int(input("alphabet size> "))
list = [("",0)]

for i in range(size):
    ele =[input("symbol_" + str(i+1) + "> "),float(input("p_" + str(i+1) + "> "))]
    list.append(ele) #list = [["",0],['a',0.3],['b',0.2],['c',0.5]]

keep = []
add = 0.0

for i in range(size):
    add = add + list[i][1]
    keep_ele = [list[i+1][0],add,add+list[i+1][1]]
    keep.append(keep_ele) #keep = [['a',small,large],['b',small,large],['c',small,large]]
                          #keep = [['a',0,0.3],['b',0.3,0.3+0.2],['c',0.5,1.0]]

keep_full=keep[:]
del list[0]#list = [['a',0.3],['b',0.2],['c',0.5]] list can consider as ratio in each character

symbols=input("symbols> ")

keep_2 = []

#find range
for alphabet in symbols:
    for i in range(size):
        if alphabet == keep[i][0]: #keep_2=[(alphabet,the largest of the one before,(our large-small)*ratio + the largest of the one before )]
            keep_2 = [[keep[0][0],keep[i][1],((keep[i][2]-keep[i][1])*list[0][1])+keep[i][1]]]
            for j in range(size-1):
                keep_2_ele = [keep[j+1][0],keep_2[j][2],((keep[i][2]-keep[i][1])*list[j+1][1])+keep_2[j][2]]
                keep_2.append(keep_2_ele)
            keep=keep_2[:]
#find m,l
print("range: [" + str(round(keep_2[0][1],12)) + "," + str(round(keep_2[size-1][2],12)) + ")")
m = float((keep_2[0][1]+keep_2[size-1][2])/2)
l = math.ceil(-math.log2(keep_2[size-1][2]-keep_2[0][1])) + 1

#change to binary
m_bi = decimalToBinary(m,l+1)
#get code
print("encoded: ", end="")
for i in range(l):
    print(m_bi[i+1], end="")

print(" ")

code = input("codewords> ")
#change to decimal
code_gen = binaryToDecimal(code,len(code))
length = int(input("length> "))

print("decode: ", end="")
for i in range(length):
    for j in range(size):
        if code_gen < keep_full[j][2]: # p2=(p1-the largest of x)/(interval of x)
            code_gen = (code_gen-keep_full[j][1])/(keep_full[j][2]-keep_full[j][1])
            print(keep_full[j][0], end="")
            break

print(" ")
