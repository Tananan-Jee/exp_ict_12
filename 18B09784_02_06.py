# -*- coding: utf-8 -*-
#プログラミング言語：Python version 3.8.0
#コンパイル方法：python3 18B09784_02_06.c
#実行方法：ターミナル上で python3 18B09784_02_06.c を実行


#remove same element
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

size=int(input("alphabet size> "))
length=int(input("length> "))

list = []

for i in range(size):
    ele =[input("symbol_" + str(i+1) + "> "),float(input("p_" + str(i+1) + "> "))]
    list.append(ele) #list = [["",0],['a',0.3],['b',0.2],['c',0.5]]

pp=[]
pp_1=[]
pp_ele=[]
pp_ele_1=[]
count=0
for i in range(size):
    for j in range(size):
        cp = float(input("cp_" + str(i+1) + str(j+1) + "> "))
        pp_ele_1 = [list[i][0],list[j][0],cp]
        pp_1.append(pp_ele_1)  #pp_1=[['a', 'a', 0.2], ['a', 'b', 0.3], ['b', 'a', 0.4], ['b', 'b', 0.5]]
        pp_ele = [list[i][0]+list[j][0],cp,list[j][0]]
        pp.append(pp_ele) #make pp=[['aa', 0.2,'a'], ['ab', 0.3,'b'], ['ba', 0.4,'a'], ['bb', 0.5,'b']]
        count += 1                  #           | represent the last alphabet
                                    #we know last alphabet of previous on so we can think as use at p(aa),p(ab),p(ba),p(bb)
shift=[]
shift_ele=[]
for i in range(size):
    for j in range(size):
        shift_ele.append(list[(j+i)%size])
    shift.append(shift_ele) #ex shift = [[['a',0.3],['b',0.2],['c',0.7]],[['b',0.2],['c',0.7],['a',0.3]],[['c',0.7],['a',0.3],['b',0.2]]]
    shift_ele=[]            #   (simple way to look) = [[a,b,c],[b,c,a],[c,a,b]]


keep = list[:]
keep_2 = []
keep_3_1 = ""
keep_3_2 = 0
value = []

#keep * shift[0] -> aa,bb,cc  also the same way with p
#keep * shift[1] -> ab,bc,ca...
for j in range(len(keep)):
    for k in range(len(shift)):
        keep_3_1 = keep[j][0] + shift[j%2][k][0]
        for m in range(len(pp)):
            if pp_1[m][0]==keep[j][0]: # find that when new element is added how which pp we should use
                if pp_1[m][1]==shift[j%2][k][0]:
                    keep_3_2 = keep[j][1] * pp_1[m][2]
        value = [keep_3_1,keep_3_2,shift[j%2][k][0]]
        keep_2.append(value)



keep = list[:]
keep_3_1 = ""
keep_3_2 = 0
value = []
count = 1
#length more than 2 kind of same with above
while count<length:
    for j in range(1,len(keep)+1):
        for k in range(len(shift)):
            keep_3_1 = keep_2[j-1][0] + shift[(j-1)%2][k][0]
            for m in range(len(pp)):
                if pp[m][0]==keep_2[j-1][2]+shift[(j-1)%2][k][0]:
                    keep_3_2 = keep_2[j-1][1] * pp[m][1]
            value = [keep_3_1,keep_3_2,shift[(j-1)%2][k][0]]
            keep_2.append(value)
    count = count + 1
    keep = keep_2[:]

for i in range(len(keep)):
    del keep[i][2] # get lit of the one that represent last alphabet

keep = Remove(keep) #delete the same element

for i in range(len(keep)):
    if len(keep[i][0])==length:
        print("P(" + keep[i][0] + "):" + str(round(keep[i][1],6)))
