//プログラミング言語：C
//コンパイル方法：gcc version 4.2.1  gcc 18B09784_01_06_a.c
//実行方法：ターミナル上で ./a.out を実行

#include<stdio.h>
int main(void)

{
  int length;
  char keep[30];

//store each number in array keep
  printf("codewords > ");
  scanf("%s",keep);

  printf("symbols : ");

//check that each set of number is a or b or else
  for(length=0;length<30;length++)
  {
    if (keep[length] == '0') { //a=0
      printf("a");
    }
    else if (keep[length] == '1') { //b=1
      printf("b");
    }
    else break;

  }
  printf("\n");
return 0;

}
