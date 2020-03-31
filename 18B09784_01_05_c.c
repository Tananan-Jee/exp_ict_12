//プログラミング言語：C
//コンパイル方法：gcc version 4.2.1  gcc 18B09784_01_05_c.c
//実行方法：ターミナル上で ./a.out を実行


#include<stdio.h>
int main(void)

{
  char keep[100];
  int length=0;

//store each symbols in array keep
  printf("symbols> ");
  scanf("%s",keep);

  printf("codewords : ");

//check that each symbols is a or b or c or else
  while(keep[length] != '\0') //check until no symbols anymore
  {
    if (keep[length] == 'a') { // a=0
      printf("0");
    }
    else if (keep[length] == 'b') { // b=10
      printf("10");
    }
    else if (keep[length] == 'c') { // c=110
      printf("110");
    }
    else if (keep[length] == 'd') { // d=111
      printf("111");
    }
    else {
      printf("error");
      break;
    }
    length++;
  }
  printf("\n");
return 0;

}
