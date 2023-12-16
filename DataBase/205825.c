To print "Hello, World!" in C, you can use the following program:

```c
#include <stdio.h>

int main() {
  printf("Hello, World!\n");
  return 0;
}
```

This program is very simple, but it demonstrates some important concepts in C programming.

* The `#include <stdio.h>` statement tells the compiler to include the contents of the `stdio.h` header file in the program. This header file contains declarations for functions such as `printf()`, which is used to print output to the console.
* The `main()` function is the entry point for all C programs. This is where the program execution begins.
* The `printf()` function takes a format string as its argument and prints the formatted output to the console. The format string can contain plain text, as well as format specifiers that indicate how to print specific data types. In this case, the format specifier `%s` is used to print a string.
* The `\n` character at the end of the format string represents a newline character. This will cause the cursor to move to the next line after the message has been printed.
* The `return 0` statement at the end of the `main()` function tells the operating system that the program has completed successfully.

To compile and run this program, you can use the following steps:

1. Save the program in a file with the `.c` extension, such as `helloworld.c`.
2. Open a terminal window and navigate to the directory where the program is saved.
3. Compile the program using the following command:

```
gcc hello_world.c
```

This will create an executable file called `a.out`.
4. Run the program using the following command:

```
./a.out
```

This will print the message "Hello, World!" to the console.

Congratulations! You have now written and executed your first C program.