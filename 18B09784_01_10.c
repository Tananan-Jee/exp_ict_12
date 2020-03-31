//プログラミング言語：C
//コンパイル方法：gcc version 4.2.1  gcc 18B09784_01_10.c
//実行方法：ターミナル上で ./a.out を実行

#include<stdio.h>
#include <string.h>

int countzero(char *lstart,int i);

int main(void)
{

  int length;
  char keep[100];

  printf("codewords > ");
  scanf("%s",keep);
  printf("symbols : ");


  for(length=0;length<100;length++)
  {
    if (keep[length] == '1') { //1

      if (keep[length+1] == '1') { //11

        if(keep[length+2] == '0'){ //110
          if (keep[length+3] == '1') { //1101
            printf("d");
            length=length+2; //skip 3 position
          }
          else if (keep[length+3] != '1') { //1100

            if (countzero(keep,length+3) % 2 !=  0) { //110001 have odd number of 0 after 1 so it is d
              printf("d");                            //11001 have even number of 0 after 1 so it is c
              length=length+2;
            }
            else { //11 00 1
              printf("c");
              length=length+1;
            }

          }
          else break;
        }

        else if(keep[length+2] != '0'){ //111
          printf("c");
          length=length+1; //skip 2 position
        }
        else break;
      }
    else { //10

         //100,101
          printf("a");
          length=length+1;

    }

  }

    else if(keep[length] == '0') { //0
      if (keep[length+1] == '0') { //00
          printf("b");
          length=length+1;
        }
      else break;
    }

    else break;
  }

  printf("\n");
  return 0;

}

//count how many '0' after '1'
int countzero(char *lstart,int i){
  int count;
  count=1;
  while (lstart[i] == '0') {
    count++;
    i++;
  }

  return count;
}
