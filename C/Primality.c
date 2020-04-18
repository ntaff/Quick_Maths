/* Author : @ntaff */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#ifndef __bool_true_false_are_defined || __bool_true_false_are_defined == 0
  #define true(1 == 1)
  #define false(!true)
#endif

int primtest(int prim) {
  int i = 3;
  if ((prim % 2) == 0) return false; //Si divisible par deux alors non premier
  for (i = 3; i < ((int) sqrt(prim) + 1); i += 2) {
    if ((prim % i) == 0) return false; //si divisible par au moins un i (avec i allant de 3 à sqrt(prim) avec un pas de 2) alors nom premier
  }
  return true; //Sinon premier
}

int main(void) {
  float temps;
  clock_t t1, t2;
  t1 = clock();
  int n;

  for (n = 0; n < 20000; n++) {

    int x = primtest(n);
    fprintf(stdout, "%d", n);
    fputs(x ? " est un nombre premier" : " n'est pas un nombre premier", stdout);
    //fputs(x ? "true" : "false", stdout);
    fputs("\n", stdout);
  }

  t2 = clock();
  temps = (float)(t2 - t1) / CLOCKS_PER_SEC;
  printf("temps = %f\n", temps);
  getchar();

  return 0;
}
