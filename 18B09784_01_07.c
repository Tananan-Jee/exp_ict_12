//プログラミング言語：C
//コンパイル方法：gcc version 4.2.1  gcc 18B09784_01_07.c
//実行方法：ターミナル上で ./a.out を実行

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define max_node 256

int arr[max_node][2]={{0}};
int arr_len=0;
                                            // first one get at first point , second one meet 8 so change the position to column+1
int make_tree(int i,int j){                 // 01234567 (column)
  int k;                                    // 80        length = 1 (row 0)
  for (k = 0; k < arr_len; k++){            // 0080      length = 2 (row 1)
    if (i==arr[k][0]&&j==arr[k][1])         // 00000088  length = 3 (row 2)
      return 8;                             // ex row 1 column 2 => 2 as binary is 10 so code is 10
    }
    return 0;
}


int main(void)
{
  int asize;
  printf("alphabet size> "); //get size of alphabet they will have
  scanf("%d", &asize);


  int *l;
  l = (int *)malloc(sizeof(int)*asize);
  for(int i = 0; i < asize; i++) {
    printf("l_%d> ", i + 1);
    scanf("%d", &l[i]); // length in each alphabet
  }

//make_tree
  int max;
  max = l[asize-1];
  long long int column;
  long long int *keep;
  int i;
  keep = (long long int*)malloc(sizeof(long long int)*asize);


  for (int i = 0; i < asize; i++) { //check from l_1 to l_asize
    column=0;
    for(int row = 0; row<l[i]; row++){ //check the row

      column = 2*column;
      if(make_tree(row,column) == 8){ //if on the way there are 8 move until not found 8 anymore
        column++;                     //8 is random number. just use as the flag to tell us that there are positions we can not pass
        while (make_tree(row,column) == 8) {
          column++;
        }
      }

      if (row == (l[i]-1)) { // we start array from row 0
        arr[arr_len][0]=row;
        arr[arr_len][1]=column;
        arr_len++;
        keep[i]=column; //column position is encode in base 10
      }
    }
  }


int a,b;
long long int con;
//change code in base 10 to base 2
  for(i = 0; i < asize; i++){
    int rmd[l[i]];
    con = keep[i];
    for(a = 0; a < l[i]; a++){  //get from back to front binary  ex 1101001
      rmd[a]=con%2;  //get remainder
      con=con/2; //do until we get the length we want (l[i])
    }
    printf("cw for l_%d: ", i + 1);
    for (b = l[i]-1; b >= 0 ; b--) { //reverse binary to get from front to back ex 1001011
      printf("%d",rmd[b]);
    }
    printf("\n");

  }

return 0;
}
