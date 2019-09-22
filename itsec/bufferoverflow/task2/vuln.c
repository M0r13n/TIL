#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int
main (int argc, char *argv[])
{
  char buf[128];
  char x;
  char *px = &x;

  *px = 100;

  if (argc != 2) {
    printf ("Braucht ein Argument!\n");
    exit (1);
  }

  printf (argv[1]);
  putchar('\n');

  printf ("x = %d\n", x);
  printf ("Eingabe: ");
  fflush (stdout);

  if (fgets (buf, sizeof buf, stdin))
    printf (buf);
    
  printf ("x = %d\n", x);

  return 0;
}