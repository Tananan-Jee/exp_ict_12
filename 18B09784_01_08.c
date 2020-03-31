//プログラミング言語：C
//コンパイル方法：gcc version 4.2.1  gcc 18B09784_01_08.c
//実行方法：ターミナル上で ./a.out を実行

//same idea with 18B09784_01_07 just change p to l

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main(void)
{
  int asize;
  printf("alphabet size> ");
  scanf("%d", &asize);


  float *p;
  int *l;
  p = (float *)malloc(sizeof(int)*asize);
  l = (int *)malloc(sizeof(int)*asize);
  for(int i = 0; i < asize; i++) {
    printf("p_%d> ", i + 1);
    scanf("%f", &p[i]); // length in each
    l[i]=ceil(-log2(p[i]));
  }

  //make_tree
  int max;
  max = l[asize-1];
  long long int power;
  power = pow(2,max);
  long long int **tree;
  long long int column;
  long long int *keep;

  keep = (long long int*)malloc(sizeof(long long int)*asize);
  tree = (long long int**)malloc(sizeof(long long int*)*max);
  //cler matrix (filled with 0)
  for (int i = 0; i < max; i++){
    tree[i]=(long long int*)malloc(sizeof(long long int)*power);
    for (int j = 0; j < power; j++){
      tree[i][j]=0;
    }
  }



  for (int i = 0; i < asize; i++) { //check from l_1 to l_asize
    column=0;
    for(int row = 0; row<l[i]; row++){ //check the row

      column = 2*column;
      if(tree[row][column] == 8){ //if on the way there are 8 move until not found 8 anymore
        column++;                 ////8 is random number. just use as the flag to tell us that there are positions we can not pass
        while (tree[row][column] == 8) {
          column++;
        }
      }
      if (row == (l[i]-1)) { // we start array from row 0
        tree[row][column] = 8;
        keep[i]=column; //column position is encode in base 10
      }
    }
  }

  //符号語の作成
int i,a,b;
long long int con;
//change code in base 10 to base 2
  for(i = 0; i < asize; i++){
    int rmd[l[i]];
    con = keep[i];
    for(a = 0; a < l[i]; a++){  //get binary from last to first ex 54321
      rmd[a]=con%2;//get remainder
      con=con/2; //do until we get the length we want (l[i])
    }
    printf("cw for l_%d: ", i + 1);
    for (b = l[i]-1; b >= 0 ; b--) { //change 54321 to 12345
      printf("%d",rmd[b]);
    }
    printf("\n");

  }

//entropy
  float H=0;
  for(i = 0; i < asize; i++){
      H = H - (p[i]*log2(p[i]));
  }
  printf("entropy: %f\n",H);

//avg_length
  float L=0;
  for(i = 0; i < asize; i++){
    L = L + (p[i]*l[i]);
  }
  printf("average length: %f\n",L);

  free(l);
  free(p);
  free(tree);
  free(keep);

return 0;
}
