//プログラミング言語：C
//コンパイル方法：gcc version 4.2.1  gcc 18B09784_01_06_c.c
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

//check that each set of number is a or b or c or d or else
  for(length=0;length<30;length++)
  {
    if (keep[length] == '0') printf("a"); //a=0

    else if (keep[length] == '1') {
      if (keep[length+1] == '0') { //b=10
        printf("b");
        length++; //skip 2 position
      }
      else if (keep[length+1] == '1'){ //c=110
        if(keep[length+2] == '0'){
          printf("c");
          length=length+2; //skip 3 position
        }
        else if(keep[length+2] == '1'){ //d=111
          printf("d");
          length=length+2; //skip 3 position
        }
        else break;
      }
    }
      else break;
  }

  printf("\n");
  return 0;

}
