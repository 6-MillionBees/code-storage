// Arden Boettcher
// 1 - 8 - 25
// Mario

#include<stdio.h>
#include<stdlib.h>

int main(void) {
  int main_num = get_int("enter mario: ");
  printf("\n");

  for (int y = 0; y < main_num; y++) {

    for (int x = 0; x < main_num; x++) {
      printf("#");
    }

    printf("\n");
  }

}

//if

//elif

//else