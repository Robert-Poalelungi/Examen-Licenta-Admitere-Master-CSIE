# THEORETICAL SUMMARY — Master Exam CSIE4
## Cybersecurity Master Program — Securitatea Informatică

> Ultra-detailed guide with real-life analogies, explained so that anyone can understand.

---

## TABLE OF CONTENTS

1. [C Programming Language](#1-c-programming-language)
2. [C++ Programming Language](#2-c-programming-language)
3. [Java Programming Language](#3-java-programming-language)

---

# 1. C PROGRAMMING LANGUAGE

## What is C?

**C** is a programming language created in 1972 by Dennis Ritchie at Bell Labs. It is the "mother" language of almost all modern languages — C++, Java, C#, Python all have roots in C.

**Real-life analogy**: C is like manual driving (manual transmission). You control EVERYTHING yourself — when to shift gears, how much to press the clutch. It's more effort, but you have maximum control and understand exactly what the car is doing. Higher-level languages (Java, Python) are like automatic transmission — simpler, but you give up some control.

Why study C?
- It's very close to hardware — you understand how a computer really works
- Extremely fast — operating systems (Windows, Linux, macOS) are written in C
- Forces you to understand memory, pointers, data structures at the fundamental level

---

## 1.1 Types, Operators, and Expressions

### Basic Data Types

```c
// Integer types (for whole numbers):
char    c = 'A';        // 1 byte: values -128 to 127 (or a character)
short   s = 1000;       // 2 bytes: values -32,768 to 32,767
int     n = 100000;     // 4 bytes: values ~-2 billion to +2 billion
long    l = 1000000L;   // 4 or 8 bytes (system dependent)
long long ll = 9876543210LL;  // 8 bytes: very large numbers

// Floating-point types (for decimal numbers):
float   f = 3.14f;      // 4 bytes: ~7 significant digits
double  d = 3.14159265; // 8 bytes: ~15 significant digits (DEFAULT for decimals)
long double ld = 3.14L; // 10-16 bytes: extra precision

// Unsigned variants (only positive values, double the max):
unsigned char  uc = 255;        // 0 to 255
unsigned int   ui = 4000000000U; // 0 to ~4 billion
unsigned short us = 60000;
unsigned long  ul = 1000000000UL;
```

**Real-life analogy for types**:
- `char` = a small mailbox (holds one letter)
- `int` = a regular drawer (holds normal numbers)
- `long long` = a warehouse (holds very large numbers)
- `float` = a calculator with 7 decimal digits
- `double` = a scientific calculator with 15 decimal digits

**IMPORTANT**: The size of types depends on the system! Use `sizeof()` to check:
```c
printf("int = %zu bytes\n", sizeof(int));      // usually 4
printf("double = %zu bytes\n", sizeof(double)); // usually 8
printf("pointer = %zu bytes\n", sizeof(int *)); // 4 on 32-bit, 8 on 64-bit
```

### Constants

```c
// Integer constants in different bases:
int decimal = 255;       // base 10 (normal)
int octal   = 0377;      // base 8  (starts with 0) — SAME value as 255!
int hex     = 0xFF;      // base 16 (starts with 0x) — SAME value as 255!

// Floating-point constants:
double d1 = 3.14;        // regular decimal
double d2 = 3.14e2;      // scientific: 314.0 (3.14 × 10²)
double d3 = 1.5e-3;      // 0.0015
float  f1 = 3.14f;       // 'f' suffix means float (not double)

// Character constants:
char cr = '\n';  // newline (Enter key)
char tab = '\t'; // tab
char null = '\0'; // null character (ASCII 0) — ends strings!
char quote = '\''; // single quote
char backslash = '\\'; // backslash

// String constants (arrays of char ending in '\0'):
// "hello" = {'h','e','l','l','o','\0'} — 6 bytes, not 5!

// Enum constants:
enum Days { MON=1, TUE, WED, THU, FRI, SAT, SUN };
// MON=1, TUE=2, WED=3, ... automatically
```

### Variable Declarations and Scope

```c
int global_var = 10;     // global: visible to all functions in file

void my_function() {
    int local_var = 5;   // local: exists only while function runs
    static int counter = 0;  // static: persists between function calls, init once
    counter++;

    {
        int block_var = 99;  // block scope: only within this { }
        printf("%d\n", block_var);  // OK
    }
    // printf("%d\n", block_var);  // ERROR: block_var doesn't exist here

    extern int another_global;  // declare that this exists in another file
}
```

### Operators

```c
int a = 10, b = 3;

// Arithmetic:
int sum  = a + b;    // 13
int diff = a - b;    // 7
int prod = a * b;    // 30
int quot = a / b;    // 3  ← INTEGER DIVISION! (not 3.333...)
int rem  = a % b;    // 1  ← remainder (10 = 3×3 + 1)

// IMPORTANT: integer division truncates toward zero!
printf("%d\n", 7 / 2);   // 3, not 3.5
printf("%d\n", -7 / 2);  // -3, not -3.5 (C99+)

// To get decimal result, cast to float first:
double real = (double)a / b;  // 3.333...

// Relational (return 0 or 1):
int r1 = (a == b);  // 0 (false) — are they equal?
int r2 = (a != b);  // 1 (true)  — are they different?
int r3 = (a > b);   // 1 (true)
int r4 = (a >= b);  // 1 (true)
int r5 = (a < b);   // 0 (false)
int r6 = (a <= b);  // 0 (false)

// Logical:
int p = 1, q = 0;
int l1 = p && q;    // 0 (AND: both must be true)
int l2 = p || q;    // 1 (OR: at least one must be true)
int l3 = !p;        // 0 (NOT: flips true/false)

// IMPORTANT: Short-circuit evaluation!
// In (expr1 && expr2): if expr1 is false, expr2 is NOT evaluated
// In (expr1 || expr2): if expr1 is true,  expr2 is NOT evaluated
int x = 0;
if (x != 0 && 10/x > 2) { ... }  // SAFE! Division not evaluated if x==0

// Assignment operators:
a += 5;    // a = a + 5   (same as a = a + 5)
a -= 3;    // a = a - 3
a *= 2;    // a = a * 2
a /= 4;    // a = a / 4
a %= 3;    // a = a % 3

// Increment / Decrement:
int x = 5;
int post = x++;  // post = 5, then x becomes 6 (post-increment)
int pre  = ++x;  // x becomes 7 first, then pre = 7 (pre-increment)
x--;             // x = 6
--x;             // x = 5

// Bitwise operators:
int b1 = 5 & 3;   // 1   (AND: 101 & 011 = 001)
int b2 = 5 | 3;   // 7   (OR:  101 | 011 = 111)
int b3 = 5 ^ 3;   // 6   (XOR: 101 ^ 011 = 110)
int b4 = ~5;       // -6  (NOT: inverts all bits)
int b5 = 5 << 1;  // 10  (shift left = multiply by 2)
int b6 = 5 >> 1;  // 2   (shift right = divide by 2)

// Conditional (ternary):
int max_val = (a > b) ? a : b;  // if a>b, result is a; else result is b

// Comma operator (evaluates left to right, returns last):
int y = (x = 3, x + 1);  // x=3, then y=4

// sizeof operator:
size_t sz = sizeof(int);        // size of int type in bytes
size_t sz2 = sizeof(a);         // size of variable a
size_t sz3 = sizeof("hello");   // 6 (5 chars + null terminator)

// Operator precedence (high to low — memorize this!):
// () [] -> .       (highest)
// ! ~ ++ -- (unary) + - * & (unary) (type) sizeof
// * / %
// + -
// << >>
// < <= > >=
// == !=
// &
// ^
// |
// &&
// ||
// ?:
// = += -= *= /= %= &= ^= |= <<= >>=
// ,                (lowest)
```

---

## 1.2 Control Flow

### If-else

```c
int score = 75;

if (score >= 90) {
    printf("A - Excellent\n");
} else if (score >= 80) {
    printf("B - Good\n");
} else if (score >= 70) {
    printf("C - Satisfactory\n");
} else if (score >= 60) {
    printf("D - Passing\n");
} else {
    printf("F - Failing\n");
}

// Single-statement if (no braces — DANGEROUS, easy to make mistakes):
if (score > 50) printf("Passed\n");
else printf("Failed\n");

// Nested if:
if (age >= 18) {
    if (has_id) {
        printf("You may enter\n");
    } else {
        printf("Please show ID\n");
    }
}
```

### Switch

```c
char grade = 'B';

switch (grade) {
    case 'A':
        printf("Excellent!\n");
        break;  // CRITICAL: without break, execution FALLS THROUGH to next case!
    case 'B':
        printf("Good!\n");
        break;
    case 'C':
        printf("Satisfactory\n");
        break;
    case 'D':
    case 'F':   // Two cases, same action (intentional fall-through)
        printf("You need to study more\n");
        break;
    default:
        printf("Invalid grade\n");
        break;
}

// What happens without break (fall-through):
switch (2) {
    case 1: printf("one\n");    // skipped
    case 2: printf("two\n");    // prints "two"
    case 3: printf("three\n");  // prints "three" too! (fell through)
    case 4: printf("four\n");   // prints "four" too!
    default: printf("done\n");  // prints "done" too!
}
// Output: two, three, four, done
```

### Loops

```c
// FOR loop — when you know the number of iterations:
for (int i = 0; i < 10; i++) {
    printf("%d ", i);   // 0 1 2 3 4 5 6 7 8 9
}

// For loop anatomy:
// for (initialization; condition; update)
// - initialization: runs ONCE at start
// - condition: checked BEFORE each iteration (if false, loop ends)
// - update: runs AFTER each iteration

// Infinite for loop:
// for (;;) { ... }  // no condition = always true

// WHILE loop — when you don't know how many iterations:
int n = 1;
while (n <= 100) {
    printf("%d\n", n);
    n *= 2;   // 1, 2, 4, 8, 16, 32, 64
}

// DO-WHILE — guarantees at least one execution:
int choice;
do {
    printf("Enter 1-5: ");
    scanf("%d", &choice);
} while (choice < 1 || choice > 5);  // repeat if invalid
// Useful for menus and input validation!

// BREAK — exits the loop immediately:
for (int i = 0; i < 100; i++) {
    if (i == 7) break;  // stops when i=7
    printf("%d ", i);   // prints 0 1 2 3 4 5 6
}

// CONTINUE — skips to next iteration:
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;  // skip even numbers
    printf("%d ", i);            // prints 1 3 5 7 9
}

// Nested loops:
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        printf("%d×%d=%d  ", i, j, i*j);
    }
    printf("\n");
}
// 1×1=1  1×2=2  1×3=3
// 2×1=2  2×2=4  2×3=6
// 3×1=3  3×2=6  3×3=9
```

---

## 1.3 Functions

**Real-life analogy**: A function is like a recipe. You give it ingredients (parameters), it does something, and returns a result (return value). You can use the same recipe multiple times without rewriting it.

```c
#include <stdio.h>
#include <math.h>

// Function DECLARATION (prototype) — tells compiler the function exists:
double circle_area(double radius);
void print_separator(int width, char ch);
int factorial(int n);

// Function DEFINITION — the actual implementation:
double circle_area(double radius) {
    const double PI = 3.14159265358979;
    return PI * radius * radius;  // return sends the value back to the caller
}

// void function — doesn't return a value:
void print_separator(int width, char ch) {
    for (int i = 0; i < width; i++) {
        putchar(ch);
    }
    putchar('\n');
    // No return statement needed (or just: return;)
}

// Recursive function — calls itself:
int factorial(int n) {
    if (n <= 1) return 1;        // base case: stop recursion
    return n * factorial(n - 1); // recursive case

    // How it works for n=4:
    // factorial(4) = 4 * factorial(3)
    //              = 4 * (3 * factorial(2))
    //              = 4 * (3 * (2 * factorial(1)))
    //              = 4 * (3 * (2 * 1))
    //              = 24
}

int main() {
    double area = circle_area(5.0);
    printf("Circle area with radius 5: %.2f\n", area);  // 78.54

    print_separator(20, '-');  // --------------------

    for (int i = 1; i <= 6; i++) {
        printf("%d! = %d\n", i, factorial(i));
    }
    return 0;
}
```

### Passing Arguments: By Value vs By Pointer

```c
// BY VALUE: function receives a COPY — original is unchanged:
void try_to_double_value(int n) {
    n = n * 2;  // only changes the local copy!
    printf("Inside function: %d\n", n);  // 20
}

// BY POINTER (reference): function receives the ADDRESS — original IS changed:
void actually_double_value(int *p) {
    *p = *p * 2;  // dereference: change the value AT that address
    printf("Inside function: %d\n", *p);  // 20
}

int main() {
    int x = 10;

    try_to_double_value(x);
    printf("After value call: %d\n", x);  // Still 10!

    actually_double_value(&x);            // pass ADDRESS of x with &
    printf("After pointer call: %d\n", x); // Now 20!

    return 0;
}
```

**IMPORTANT**: In C, ALL arguments are passed BY VALUE. To modify a variable, you must pass its address (pointer).

### Function Pointers

```c
// Pointer to a function that takes (int, int) and returns int:
int (*operation)(int, int);

int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }

void apply_op(int x, int y, int (*op)(int, int)) {
    printf("Result: %d\n", op(x, y));
}

int main() {
    operation = add;
    printf("%d\n", operation(5, 3));  // 8

    apply_op(10, 4, subtract);   // Result: 6
    apply_op(10, 4, multiply);   // Result: 40

    // Array of function pointers:
    int (*ops[3])(int, int) = {add, subtract, multiply};
    for (int i = 0; i < 3; i++) {
        printf("%d\n", ops[i](6, 2));  // 8, 4, 12
    }
    return 0;
}
```

---

## 1.4 Arrays

**Real-life analogy**: An array is like a row of numbered lockers at a gym. Locker 0 holds something, locker 1 holds something else, etc. They're all the same size, numbered consecutively.

```c
// 1D Array:
int scores[5] = {85, 90, 78, 92, 88};  // 5 elements, indices 0-4
double prices[] = {1.99, 2.49, 0.99};   // compiler counts: 3 elements
char vowels[5] = {'a', 'e', 'i', 'o', 'u'};

// Accessing elements (INDEX STARTS AT 0!):
printf("%d\n", scores[0]);   // 85 (first)
printf("%d\n", scores[4]);   // 88 (last)
scores[2] = 80;              // modify 3rd element

// DANGER: accessing out of bounds (undefined behavior!):
// scores[5] = 100;  // BUG! Index 5 doesn't exist

// Traversal:
int n = 5, sum = 0;
for (int i = 0; i < n; i++) {
    sum += scores[i];
}
printf("Average: %.1f\n", (double)sum / n);  // 87.0

// Uninitialized arrays contain garbage values!
int garbage[5];         // contains random values
int zeros[5] = {0};     // all elements = 0
int partial[5] = {1,2}; // {1, 2, 0, 0, 0} — rest initialized to 0

// 2D Array (matrix):
int matrix[3][4] = {
    {1,  2,  3,  4},
    {5,  6,  7,  8},
    {9, 10, 11, 12}
};

// Access: matrix[row][column]
printf("%d\n", matrix[1][2]);  // 7 (row 1, column 2)

// Traversal:
for (int row = 0; row < 3; row++) {
    for (int col = 0; col < 4; col++) {
        printf("%3d ", matrix[row][col]);
    }
    printf("\n");
}

// Arrays decay to pointers when passed to functions:
void fill_array(int *arr, int n, int value) {
    for (int i = 0; i < n; i++) arr[i] = value;
}
// or equivalently: void fill_array(int arr[], int n, int value)

int data[10];
fill_array(data, 10, 0);  // fills all elements with 0
```

---

## 1.5 Pointers — The Most Important (and Hardest) Concept

### The Pointer Mental Model

**The PERFECT real-life analogy**:

Imagine computer memory as a city with millions of houses (memory cells), each with a unique address (0, 1, 2, 3, ...).

- A regular variable (`int x = 5`) is like **house #4521** that contains the number **5**
- A pointer (`int *p = &x`) is like a **piece of paper that says "house #4521"** — it stores the ADDRESS, not the value
- Dereferencing (`*p`) is like saying "go to the address on that paper, and tell me what's inside"

```c
int x = 5;      // x lives at, say, address 1000
int *p = &x;    // p stores the value 1000 (address of x)
                // & = "address of" operator
                // * in DECLARATION means "this is a pointer"

printf("%d\n",  x);   // 5  — the value
printf("%p\n", &x);   // 0x3e8 or similar — the address (in hex)
printf("%p\n",  p);   // same as &x — what p contains
printf("%d\n", *p);   // 5  — value AT the address p points to
                       // * in EXPRESSION = "value at this address" (dereference)

*p = 99;              // change the value AT address p
printf("%d\n", x);   // 99 — x changed! (we modified it through the pointer)
```

### Pointer Arithmetic

```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr;  // p points to arr[0] (arrays decay to pointer to first element)

printf("%d\n", *p);       // 10  (arr[0])
printf("%d\n", *(p+1));   // 20  (arr[1])
printf("%d\n", *(p+2));   // 30  (arr[2])
printf("%d\n", p[3]);     // 40  (p[i] is EXACTLY the same as *(p+i))

// Incrementing a pointer:
p++;   // p now points to arr[1]
printf("%d\n", *p);  // 20

// Pointer arithmetic respects type size:
// If int is 4 bytes, p+1 advances by 4 bytes (one int)
// If double *q, q+1 advances by 8 bytes (one double)

// Pointer comparison:
int *first = arr;
int *last = arr + 4;  // points to arr[4]
while (first <= last) {
    printf("%d ", *first);  // 10 20 30 40 50
    first++;
}
```

### Pointers and Strings

```c
// String as array:
char greeting[] = "Hello";  // {'H','e','l','l','o','\0'} — 6 bytes
greeting[0] = 'h';          // CAN modify — it's in stack memory

// String as pointer:
char *msg = "Hello";   // points to string LITERAL in read-only memory
// msg[0] = 'h';       // UNDEFINED BEHAVIOR! Can't modify string literals

// Traversal with pointer:
char *p = greeting;
while (*p != '\0') {  // stop at null terminator
    putchar(*p);
    p++;
}
// Or: while (*p) putchar(*p++);  — more concise

// String functions from <string.h>:
char s1[50] = "Hello";
char s2[] = "World";

strlen(s1)                // 5 (not counting '\0')
strcpy(s1, s2)            // s1 = "World"  (copy s2 into s1 — DANGER: no bounds check)
strncpy(s1, s2, 49)       // safer: copy at most 49 chars
strcat(s1, " World")      // append " World" to s1 — DANGER: no bounds check
strncat(s1, " World", 49) // safer
strcmp(s1, s2)            // 0 if equal; <0 if s1<s2; >0 if s1>s2
strchr(s1, 'o')           // pointer to first 'o' in s1, or NULL
strstr(s1, "llo")         // pointer to first "llo" in s1, or NULL
```

### Dynamic Memory Allocation

```c
#include <stdlib.h>

// malloc: allocate n bytes (UNINITIALIZED — contains garbage!)
int *arr = (int *)malloc(5 * sizeof(int));
if (arr == NULL) {
    fprintf(stderr, "Memory allocation failed!\n");
    exit(1);
}

// calloc: allocate AND initialize to zero
int *zeros = (int *)calloc(5, sizeof(int));  // 5 ints, all = 0

// Use it:
for (int i = 0; i < 5; i++) arr[i] = i * 10;

// realloc: resize existing allocation
arr = (int *)realloc(arr, 10 * sizeof(int));  // now 10 ints
if (arr == NULL) { /* handle error */ }

// free: release memory (MANDATORY or you get a memory leak!)
free(arr);
arr = NULL;   // good practice: prevent use-after-free
free(zeros);
zeros = NULL;

// COMMON MISTAKES:
// 1. Memory leak: forget to free()
// 2. Double free: free() twice (crash!)
// 3. Use-after-free: access memory after freeing it
// 4. Buffer overflow: write beyond allocated size
```

### Pointers to Pointers

```c
int x = 5;
int *p = &x;    // p points to x
int **pp = &p;  // pp points to p (pointer to pointer)

printf("%d\n", x);     // 5
printf("%d\n", *p);    // 5
printf("%d\n", **pp);  // 5

**pp = 99;  // changes x through double indirection!
printf("%d\n", x);  // 99

// Common use: dynamic 2D arrays
int rows = 3, cols = 4;
int **matrix = (int **)malloc(rows * sizeof(int *));
for (int i = 0; i < rows; i++) {
    matrix[i] = (int *)malloc(cols * sizeof(int));
}

matrix[1][2] = 42;  // access like normal 2D array

// Free 2D array:
for (int i = 0; i < rows; i++) free(matrix[i]);
free(matrix);
```

---

## 1.6 Structures (struct)

**Real-life analogy**: A struct is like a form or record. An employee record has multiple fields (name, age, salary, department) all about one thing (the employee). A struct bundles these related pieces together.

```c
#include <stdio.h>
#include <string.h>

// Define the struct TYPE:
struct Point {
    double x;
    double y;
};

// typedef makes it easier to use (no need to write 'struct' every time):
typedef struct {
    int    id;
    char   name[50];
    double salary;
    int    age;
} Employee;

// Nested struct:
typedef struct {
    Employee manager;
    char     dept_name[30];
    int      employee_count;
} Department;

int main() {
    // Create and initialize:
    struct Point p1 = {3.0, 4.0};
    Employee e1 = {1, "John Smith", 75000.0, 35};
    Employee e2;   // uninitialized

    // Access with dot operator:
    e2.id = 2;
    strcpy(e2.name, "Jane Doe");
    e2.salary = 80000.0;
    e2.age = 28;

    printf("Employee: %s, Salary: $%.2f\n", e1.name, e1.salary);

    // Arrays of structs:
    Employee team[3] = {
        {1, "Alice", 70000.0, 30},
        {2, "Bob",   65000.0, 25},
        {3, "Carol", 90000.0, 40}
    };

    double total_salary = 0;
    for (int i = 0; i < 3; i++) {
        total_salary += team[i].salary;
        printf("%s earns $%.2f\n", team[i].name, team[i].salary);
    }
    printf("Total: $%.2f\n", total_salary);

    // Pointer to struct — use -> operator:
    Employee *ep = &e1;
    printf("Name: %s\n", ep->name);         // arrow operator
    printf("Same: %s\n", (*ep).name);        // equivalent, more verbose

    ep->salary *= 1.10;  // give 10% raise through pointer
    printf("New salary: $%.2f\n", e1.salary);  // original changed!

    return 0;
}
```

### Structs and Functions

```c
// Structs are passed BY VALUE (whole copy is made):
void print_employee(Employee e) {
    printf("%s: $%.2f\n", e.name, e.salary);
}

// Pass pointer to avoid copying (and to allow modification):
void give_raise(Employee *e, double percent) {
    e->salary *= (1.0 + percent / 100.0);
}

// Returning a struct:
Employee create_employee(int id, const char *name, double salary) {
    Employee e;
    e.id = id;
    strncpy(e.name, name, 49);
    e.name[49] = '\0';
    e.salary = salary;
    return e;  // returns a copy
}
```

---

## 1.7 Input / Output

```c
#include <stdio.h>

int main() {
    int n;
    double d;
    char name[50];

    // printf format specifiers:
    printf("%d\n",   42);          // integer
    printf("%f\n",   3.14);        // float/double (default 6 decimal places)
    printf("%.2f\n", 3.14159);     // 2 decimal places: 3.14
    printf("%e\n",   3.14);        // scientific: 3.140000e+00
    printf("%s\n",   "hello");     // string
    printf("%c\n",   'A');         // character
    printf("%p\n",   &n);          // pointer (address)
    printf("%5d\n",  42);          // right-aligned in 5-wide field: "   42"
    printf("%-5d|\n", 42);         // left-aligned: "42   |"
    printf("%05d\n", 42);          // zero-padded: "00042"
    printf("%+d\n",  42);          // show sign: "+42"

    // scanf reads from stdin:
    printf("Enter an integer: ");
    scanf("%d", &n);    // & is required! scanf needs the ADDRESS to store into

    printf("Enter a double: ");
    scanf("%lf", &d);   // %lf for double with scanf (not %f!)

    printf("Enter your name: ");
    scanf("%49s", name);  // reads one word (stops at whitespace)
    // or: fgets(name, 50, stdin);  // reads whole line including spaces

    // File I/O:
    FILE *file = fopen("data.txt", "w");   // open for writing
    if (file == NULL) {
        perror("Error opening file");  // prints system error message
        return 1;
    }
    fprintf(file, "Name: %s, Age: %d\n", name, n);
    fclose(file);   // ALWAYS close files!

    file = fopen("data.txt", "r");
    char buffer[200];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }
    fclose(file);

    return 0;
}
```

---

# 2. C++ PROGRAMMING LANGUAGE

## What is C++?

**C++** = C plus Object-Oriented Programming (and much more). Created by Bjarne Stroustrup in 1983, starting from C but adding classes, inheritance, polymorphism, templates, and the STL.

**Real-life analogy**:
- C is like building with raw materials (bricks, cement, boards)
- C++ is like building with LEGO bricks — you have pre-made components (classes) that you snap together, and you can create your own custom bricks (define new classes)

---

## 2.1 C++ vs C Basics

```cpp
// C++ includes and namespace:
#include <iostream>   // instead of <stdio.h>
#include <string>     // std::string type
#include <vector>     // dynamic arrays
using namespace std;  // so you can write cout instead of std::cout

// C++ uses cout/cin instead of printf/scanf:
cout << "Hello, World!" << endl;   // endl = newline and flush
cout << "Number: " << 42 << "\n";

int n;
cin >> n;    // read integer

string name;
cin >> name;         // read one word
getline(cin, name);  // read whole line

// C++ string (much better than char arrays!):
string greeting = "Hello";
greeting += " World";          // concatenation with +
cout << greeting.length() << endl;  // 11
cout << greeting.substr(0, 5) << endl;  // "Hello"
cout << greeting.find("World") << endl; // 6 (position)
if (greeting == "Hello World") { ... }  // comparison with ==

// C++ has bool type natively:
bool is_valid = true;
bool is_empty = false;

// References (alias for another variable):
int x = 10;
int &ref = x;   // ref is an alias for x (they share the same memory)
ref = 20;       // changes x to 20!
cout << x << endl;   // 20

// C++ allows declarations anywhere (not just at start of block):
for (int i = 0; i < 5; i++) { ... }  // i declared in for init

// new and delete (instead of malloc/free):
int *p = new int(42);      // allocate one int initialized to 42
int *arr = new int[10];    // allocate array of 10 ints
delete p;                  // free single object
delete[] arr;              // free array (MUST use delete[], not delete)
```

---

## 2.2 Classes and Objects — The Heart of C++

**Real-life analogy**:
- A **class** is the blueprint for a house
- An **object** is an actual house built from that blueprint
- You can build many different houses (objects) from the same blueprint (class)
- **Attributes** = the house's properties (color, number of rooms, size)
- **Methods** = what you can do with the house (open door, turn on lights, add a room)

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:   // only accessible inside the class (implementation details)
    string owner_name;
    string iban;
    double balance;
    int transaction_count;

public:    // accessible from anywhere (the interface)

    // Constructor — called automatically when object is created:
    BankAccount(string name, string iban_num, double initial_balance = 0.0)
        : owner_name(name), iban(iban_num),
          balance(initial_balance), transaction_count(0) {
        cout << "Account created for " << owner_name << endl;
    }

    // Copy constructor:
    BankAccount(const BankAccount &other)
        : owner_name(other.owner_name), iban(other.iban + "_COPY"),
          balance(other.balance), transaction_count(0) {
        cout << "Account copied" << endl;
    }

    // Destructor — called automatically when object is destroyed:
    ~BankAccount() {
        cout << "Account for " << owner_name << " closed. "
             << transaction_count << " transactions made." << endl;
    }

    // Methods:
    bool deposit(double amount) {
        if (amount <= 0) {
            cerr << "Error: deposit amount must be positive" << endl;
            return false;
        }
        balance += amount;
        transaction_count++;
        cout << "Deposited $" << amount << " | New balance: $" << balance << endl;
        return true;
    }

    bool withdraw(double amount) {
        if (amount <= 0) {
            cerr << "Error: invalid amount" << endl;
            return false;
        }
        if (amount > balance) {
            cerr << "Error: insufficient funds" << endl;
            return false;
        }
        balance -= amount;
        transaction_count++;
        cout << "Withdrew $" << amount << " | New balance: $" << balance << endl;
        return true;
    }

    bool transfer(BankAccount &target, double amount) {
        if (withdraw(amount)) {
            target.deposit(amount);
            return true;
        }
        return false;
    }

    // Getters (const — promise not to modify the object):
    double getBalance() const { return balance; }
    string getOwner() const { return owner_name; }
    string getIBAN() const { return iban; }

    // Display:
    void display() const {
        cout << "Account: " << iban
             << " | Owner: " << owner_name
             << " | Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount alice("Alice", "RO12INGB123456789", 1000.0);
    BankAccount bob("Bob", "RO12INGB987654321", 500.0);

    alice.deposit(500.0);    // Deposited $500 | New balance: $1500
    alice.withdraw(200.0);   // Withdrew $200 | New balance: $1300
    alice.transfer(bob, 300.0);  // Alice -300, Bob +300

    alice.display();  // Account: RO12... | Owner: Alice | Balance: $1000
    bob.display();    // Account: RO12... | Owner: Bob   | Balance: $800

    // Object on heap:
    BankAccount *vip = new BankAccount("VIP Client", "RO12INGB111", 50000.0);
    vip->deposit(5000.0);
    delete vip;  // destructor called here

    return 0;
    // alice and bob destructors called here automatically
}
```

---

## 2.3 Encapsulation

**Encapsulation** = hiding the internal details of a class and exposing only a clean interface.

Why? Because:
- The user of a class doesn't need to know HOW it works internally
- You can change the implementation without breaking anyone who uses the class
- You can enforce invariants (e.g., balance can never be negative)

```cpp
class Temperature {
private:
    double celsius;  // stored internally in Celsius

public:
    Temperature(double c = 0.0) : celsius(c) {}

    // Getters in multiple units — but only ONE private variable:
    double getCelsius() const    { return celsius; }
    double getFahrenheit() const { return celsius * 9.0/5.0 + 32.0; }
    double getKelvin() const     { return celsius + 273.15; }

    // Setters with validation:
    void setCelsius(double c) {
        if (c < -273.15) {
            throw invalid_argument("Temperature below absolute zero!");
        }
        celsius = c;
    }

    void setFahrenheit(double f) { setCelsius((f - 32.0) * 5.0/9.0); }
    void setKelvin(double k)     { setCelsius(k - 273.15); }

    void display() const {
        cout << getCelsius() << "°C = "
             << getFahrenheit() << "°F = "
             << getKelvin() << "K" << endl;
    }
};
```

---

## 2.4 Inheritance

**Inheritance** = a class can automatically inherit attributes and methods from another class.

**Real-life analogy**: Think about types of vehicles.
- `Vehicle` class: has wheels, can move, has a fuel level
- `Car` inherits from `Vehicle`: is a vehicle, PLUS has 4 doors, a trunk, air conditioning
- `ElectricCar` inherits from `Car`: is a car, PLUS has a battery, charging port

```cpp
// BASE CLASS (parent, superclass):
class Shape {
protected:  // accessible in derived classes, not from outside
    string color;
    string name;

public:
    Shape(string n, string c) : name(n), color(c) {}

    void setColor(string c) { color = c; }
    string getColor() const { return color; }
    string getName() const { return name; }

    // virtual = can be overridden by derived classes:
    virtual double area() const {
        return 0.0;  // base implementation (will be overridden)
    }

    virtual double perimeter() const {
        return 0.0;
    }

    // Pure virtual (= 0) means MUST be overridden:
    // virtual double area() const = 0;  // makes Shape abstract

    virtual void display() const {
        cout << name << " (" << color << "): "
             << "area=" << area() << ", perimeter=" << perimeter() << endl;
    }

    // IMPORTANT: virtual destructor when using polymorphism:
    virtual ~Shape() {}
};

// DERIVED CLASS (child, subclass):
class Circle : public Shape {
private:
    double radius;
    static const double PI;  // static: shared by all Circle objects

public:
    Circle(double r, string c = "blue")
        : Shape("Circle", c), radius(r) {}   // call base constructor

    // Override virtual methods:
    double area() const override {
        return PI * radius * radius;
    }

    double perimeter() const override {
        return 2 * PI * radius;
    }

    void display() const override {
        cout << "Circle: radius=" << radius << ", ";
        Shape::display();  // optionally call base class method
    }

    double getRadius() const { return radius; }
};

const double Circle::PI = 3.14159265358979;

class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(double w, double h, string c = "red")
        : Shape("Rectangle", c), width(w), height(h) {}

    double area() const override { return width * height; }
    double perimeter() const override { return 2 * (width + height); }

    double getWidth() const { return width; }
    double getHeight() const { return height; }
};

class Square : public Rectangle {  // inherits from Rectangle!
public:
    Square(double side, string c = "green")
        : Rectangle(side, side, c) {
        name = "Square";  // override the name
    }
};
```

**Access specifiers in inheritance**:

```cpp
class Base {
public:    int pub = 1;
protected: int prot = 2;
private:   int priv = 3;
};

class DerivedPublic    : public    Base { ... };  // pub→pub,  prot→prot, priv: no access
class DerivedProtected : protected Base { ... };  // pub→prot, prot→prot, priv: no access
class DerivedPrivate   : private   Base { ... };  // pub→priv, prot→priv, priv: no access
```

---

## 2.5 Polymorphism

**Polymorphism** = "many forms" — the same code works with objects of different types, and the correct behavior is chosen at runtime.

**Real-life analogy**: You have a remote control with a "Play" button. Press it on a DVD player and it plays a DVD. Press it on a music player and it plays music. Press it on a game console and it starts a game. Same button (same interface), different behaviors.

```cpp
int main() {
    // Polymorphism through base class POINTERS:
    Shape *shapes[4];
    shapes[0] = new Circle(5.0, "blue");
    shapes[1] = new Rectangle(4.0, 6.0, "red");
    shapes[2] = new Square(3.0, "green");
    shapes[3] = new Circle(2.5, "yellow");

    // Same code, different behaviors — THIS IS POLYMORPHISM:
    double total_area = 0;
    for (int i = 0; i < 4; i++) {
        shapes[i]->display();       // calls the RIGHT display() for each type
        total_area += shapes[i]->area();  // calls the RIGHT area() for each type
    }

    cout << "Total area: " << total_area << endl;

    // Clean up:
    for (int i = 0; i < 4; i++) delete shapes[i];

    // Polymorphism through REFERENCES:
    Circle c(3.0);
    Shape &ref = c;
    cout << ref.area() << endl;  // calls Circle::area(), not Shape::area()

    return 0;
}
```

### Why virtual is essential

```cpp
class Animal {
public:
    void sound_nonvirtual() { cout << "Generic animal sound" << endl; }
    virtual void sound_virtual() { cout << "Generic animal sound" << endl; }
    virtual ~Animal() {}
};

class Dog : public Animal {
public:
    void sound_nonvirtual() { cout << "Woof!" << endl; }
    void sound_virtual() override { cout << "Woof!" << endl; }
};

int main() {
    Dog d;
    Animal *ptr = &d;  // Base pointer, Derived object

    ptr->sound_nonvirtual();  // "Generic animal sound" — STATIC binding (wrong!)
    ptr->sound_virtual();     // "Woof!"                — DYNAMIC binding (correct!)

    // Without virtual: compiler looks at POINTER TYPE (Animal) at compile time
    // With virtual: runtime looks at OBJECT TYPE (Dog) at runtime
    return 0;
}
```

### Virtual Dispatch (vtable mechanism)

When a class has virtual functions, the compiler creates a **vtable** (virtual function table) for it — a table of function pointers. Each object has a hidden pointer to its class's vtable. When you call a virtual function through a pointer/reference, the runtime looks up the correct function in the vtable.

This is why:
1. Virtual functions have a small overhead (one extra pointer lookup)
2. You need a virtual destructor when using polymorphism (otherwise deleting through base pointer won't call the derived destructor)

---

## 2.6 Abstract Classes and Interfaces

An **abstract class** has at least one **pure virtual function** (`= 0`). You CANNOT create objects of an abstract class.

```cpp
class AbstractAnimal {
protected:
    string name;
    int age;

public:
    AbstractAnimal(string n, int a) : name(n), age(a) {}

    // Pure virtual = subclasses MUST implement:
    virtual void makeSound() const = 0;
    virtual void move() const = 0;
    virtual string describe() const = 0;

    // Non-pure virtual (has default, can override):
    virtual void breathe() const {
        cout << name << " breathes." << endl;
    }

    // Non-virtual (same for all):
    void eat(string food) const {
        cout << name << " eats " << food << "." << endl;
    }

    virtual ~AbstractAnimal() {}
};

class Dog : public AbstractAnimal {
private:
    string breed;

public:
    Dog(string n, int a, string b) : AbstractAnimal(n, a), breed(b) {}

    void makeSound() const override { cout << name << " says: Woof!" << endl; }
    void move() const override { cout << name << " runs on 4 legs." << endl; }
    string describe() const override {
        return name + " is a " + breed + " dog, " + to_string(age) + " years old.";
    }
};

class Bird : public AbstractAnimal {
private:
    bool can_fly;

public:
    Bird(string n, int a, bool fly) : AbstractAnimal(n, a), can_fly(fly) {}

    void makeSound() const override { cout << name << " tweets." << endl; }
    void move() const override {
        if (can_fly) cout << name << " flies." << endl;
        else cout << name << " walks." << endl;
    }
    string describe() const override {
        return name + ", a " + string(can_fly ? "flying" : "flightless") + " bird.";
    }
};

int main() {
    // AbstractAnimal a("x", 1);  // ERROR: can't instantiate abstract class

    AbstractAnimal *animals[] = {
        new Dog("Rex", 3, "Labrador"),
        new Bird("Tweety", 1, true),
        new Dog("Max", 5, "German Shepherd"),
        new Bird("Pingu", 10, false)
    };

    for (auto *a : animals) {
        cout << a->describe() << endl;
        a->makeSound();
        a->move();
        a->eat("food");
        a->breathe();
        cout << endl;
    }

    for (auto *a : animals) delete a;
    return 0;
}
```

---

## 2.7 Operator Overloading

C++ lets you redefine what operators (+, -, *, ==, <<, etc.) do for your classes.

```cpp
class Vector2D {
public:
    double x, y;

    Vector2D(double x = 0, double y = 0) : x(x), y(y) {}

    // Overload +: add two vectors
    Vector2D operator+(const Vector2D &other) const {
        return Vector2D(x + other.x, y + other.y);
    }

    // Overload -: subtract vectors
    Vector2D operator-(const Vector2D &other) const {
        return Vector2D(x - other.x, y - other.y);
    }

    // Overload * with scalar
    Vector2D operator*(double scalar) const {
        return Vector2D(x * scalar, y * scalar);
    }

    // Overload ==: equality
    bool operator==(const Vector2D &other) const {
        return x == other.x && y == other.y;
    }

    // Dot product (use *)
    double dot(const Vector2D &other) const {
        return x * other.x + y * other.y;
    }

    double magnitude() const {
        return sqrt(x*x + y*y);
    }

    // Overload << for output (must be friend to access private members if any):
    friend ostream& operator<<(ostream &os, const Vector2D &v) {
        os << "(" << v.x << ", " << v.y << ")";
        return os;
    }

    // Overload >>  for input:
    friend istream& operator>>(istream &is, Vector2D &v) {
        is >> v.x >> v.y;
        return is;
    }
};

int main() {
    Vector2D v1(3, 4), v2(1, 2);

    Vector2D sum = v1 + v2;       // (4, 6)
    Vector2D diff = v1 - v2;      // (2, 2)
    Vector2D scaled = v1 * 2.0;   // (6, 8)

    cout << "v1 = " << v1 << endl;       // (3, 4)
    cout << "v1 + v2 = " << sum << endl; // (4, 6)
    cout << "|v1| = " << v1.magnitude() << endl;  // 5
    cout << "v1 . v2 = " << v1.dot(v2) << endl;   // 11

    return 0;
}
```

---

## 2.8 Templates

**Templates** = write code that works with ANY data type.

**Real-life analogy**: A cookie cutter (template) works with any dough (data type). You define the shape once and use it with chocolate dough, sugar dough, or any other dough.

```cpp
// Function template:
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Works with int, double, char, string — any type with operator>:
cout << maximum(5, 8) << endl;           // 8 (int)
cout << maximum(3.14, 2.72) << endl;     // 3.14 (double)
cout << maximum('a', 'z') << endl;       // z (char)
cout << maximum(string("apple"), string("banana")) << endl;  // banana

// Multiple template parameters:
template <typename T, typename U>
void print_pair(T first, U second) {
    cout << first << " : " << second << endl;
}
print_pair("Age", 25);     // Age : 25
print_pair(3.14, "pi");    // 3.14 : pi

// Class template — generic container:
template <typename T>
class Stack {
private:
    T *data;
    int top_idx;
    int capacity;

public:
    Stack(int cap = 10) : top_idx(-1), capacity(cap) {
        data = new T[cap];
    }

    ~Stack() { delete[] data; }

    void push(const T &item) {
        if (top_idx < capacity - 1) data[++top_idx] = item;
        else throw overflow_error("Stack is full!");
    }

    T pop() {
        if (top_idx < 0) throw underflow_error("Stack is empty!");
        return data[top_idx--];
    }

    T peek() const {
        if (top_idx < 0) throw underflow_error("Stack is empty!");
        return data[top_idx];
    }

    bool empty() const { return top_idx == -1; }
    int size() const { return top_idx + 1; }
};

int main() {
    Stack<int> int_stack;
    int_stack.push(1); int_stack.push(2); int_stack.push(3);
    cout << int_stack.pop() << endl;   // 3
    cout << int_stack.peek() << endl;  // 2

    Stack<string> str_stack;
    str_stack.push("hello"); str_stack.push("world");
    while (!str_stack.empty()) {
        cout << str_stack.pop() << endl;  // world, hello
    }

    return 0;
}
```

---

## 2.9 STL — Standard Template Library

The STL provides ready-to-use data structures and algorithms.

### Containers

```cpp
#include <vector>     // dynamic array
#include <list>       // doubly-linked list
#include <deque>      // double-ended queue
#include <map>        // sorted key-value pairs (BST)
#include <unordered_map>  // unsorted key-value pairs (hash table)
#include <set>        // sorted unique values
#include <unordered_set>  // unsorted unique values (hash table)
#include <stack>      // LIFO stack
#include <queue>      // FIFO queue
#include <priority_queue>  // max-heap by default

// VECTOR — most commonly used:
vector<int> v = {5, 3, 8, 1, 9};
v.push_back(7);        // add to end: O(amortized 1)
v.pop_back();          // remove from end: O(1)
v.insert(v.begin(), 0); // insert at beginning: O(n)
v.erase(v.begin());    // erase first element: O(n)
cout << v[2] << endl;  // access by index: O(1)
cout << v.front() << endl;  // first element
cout << v.back() << endl;   // last element
cout << v.size() << endl;   // number of elements
v.clear();             // remove all elements
v.resize(10, 0);       // resize to 10 elements, new ones = 0

// MAP — key-value dictionary:
map<string, int> word_count;
word_count["apple"] = 3;
word_count["banana"]++;  // creates entry with 0, then increments to 1
word_count.insert({"cherry", 5});

// Iteration:
for (auto &[word, count] : word_count) {  // structured bindings (C++17)
    cout << word << ": " << count << endl;
}

// Lookup:
if (word_count.count("apple") > 0) {  // or: word_count.find() != word_count.end()
    cout << "apple count: " << word_count["apple"] << endl;
}

// SET — unique sorted values:
set<int> primes = {2, 3, 5, 7, 11};
primes.insert(13);   // O(log n)
primes.erase(5);     // O(log n)
bool found = primes.count(7) > 0;  // O(log n)
```

### Algorithms

```cpp
#include <algorithm>
#include <numeric>

vector<int> v = {5, 3, 8, 1, 9, 2, 7, 4, 6};

// Sorting:
sort(v.begin(), v.end());                          // ascending: 1 2 3 4 5 6 7 8 9
sort(v.begin(), v.end(), greater<int>());          // descending: 9 8 7 6 5 4 3 2 1
sort(v.begin(), v.end(), [](int a, int b) { return a > b; }); // lambda comparator

// Searching:
auto it = find(v.begin(), v.end(), 5);  // iterator to 5, or v.end() if not found
if (it != v.end()) cout << "Found at index: " << (it - v.begin()) << endl;

// Binary search (REQUIRES sorted vector!):
bool has_5 = binary_search(v.begin(), v.end(), 5);

// Count:
int count_3 = count(v.begin(), v.end(), 3);
int count_even = count_if(v.begin(), v.end(), [](int x){ return x % 2 == 0; });

// Min/Max:
auto min_it = min_element(v.begin(), v.end());
auto max_it = max_element(v.begin(), v.end());
cout << "Min: " << *min_it << ", Max: " << *max_it << endl;

// Numerical:
int total = accumulate(v.begin(), v.end(), 0);         // sum
int product = accumulate(v.begin(), v.end(), 1, multiplies<int>());

// Reverse:
reverse(v.begin(), v.end());

// Remove (doesn't actually remove, just moves to end — use with erase!):
auto new_end = remove(v.begin(), v.end(), 3);  // "remove" value 3
v.erase(new_end, v.end());  // actually erase them

// Fill:
fill(v.begin(), v.end(), 0);  // set all to 0

// Transform (apply function to each element):
vector<int> squares(v.size());
transform(v.begin(), v.end(), squares.begin(), [](int x){ return x * x; });
```

---

## 2.10 Exceptions in C++

```cpp
#include <stdexcept>
#include <iostream>
using namespace std;

double safe_divide(double a, double b) {
    if (b == 0.0) throw invalid_argument("Cannot divide by zero!");
    return a / b;
}

int get_element(vector<int> &v, int idx) {
    if (idx < 0 || idx >= (int)v.size())
        throw out_of_range("Index " + to_string(idx) + " is out of range [0, "
                           + to_string(v.size()-1) + "]");
    return v[idx];
}

// Custom exception:
class InsufficientFundsException : public runtime_error {
private:
    double amount_needed;
    double amount_available;
public:
    InsufficientFundsException(double needed, double available)
        : runtime_error("Insufficient funds"),
          amount_needed(needed), amount_available(available) {}

    double getNeeded() const { return amount_needed; }
    double getAvailable() const { return amount_available; }
};

int main() {
    try {
        cout << safe_divide(10.0, 2.0) << endl;   // 5.0 — OK
        cout << safe_divide(10.0, 0.0) << endl;   // throws exception!
        cout << "This line never runs" << endl;
    }
    catch (const invalid_argument &e) {
        cerr << "Invalid argument: " << e.what() << endl;
    }
    catch (const exception &e) {
        cerr << "Error: " << e.what() << endl;  // catches any std exception
    }
    catch (...) {
        cerr << "Unknown exception!" << endl;    // catches anything else
    }

    // Multiple exceptions:
    vector<int> data = {1, 2, 3, 4, 5};
    try {
        cout << get_element(data, 2) << endl;    // 3 — OK
        cout << get_element(data, 10) << endl;   // throws out_of_range
    }
    catch (const out_of_range &e) {
        cerr << "Out of range: " << e.what() << endl;
    }

    cout << "Program continues after exception handling" << endl;
    return 0;
}
```

---

# 3. JAVA PROGRAMMING LANGUAGE

## What is Java?

**Java** was created by James Gosling at Sun Microsystems in 1995. The key motto: **"Write once, run anywhere"** — Java code compiles to bytecode that runs on any machine with a Java Virtual Machine (JVM).

**Real-life analogy**:
- C is like a letter written in Romanian — you must translate it for each country separately
- Java is like a letter written in Esperanto (a universal language) — there's a translator (JVM) in every country that understands it

Key features:
- **Platform independent**: compile once, run on Windows/Linux/Mac/Android
- **Object-oriented**: everything is in classes
- **Automatic memory management**: garbage collector handles memory (no malloc/free!)
- **Strongly typed**: types must be declared, no implicit conversions between incompatible types
- **Rich standard library**: thousands of built-in classes

---

## 3.1 Java vs C++ Basics

```java
// Java program structure:
// - Everything is in a CLASS
// - File name MUST match class name: HelloWorld.java
// - Program starts at public static void main(String[] args)

public class HelloWorld {
    public static void main(String[] args) {
        // Print to console:
        System.out.println("Hello, World!");    // prints with newline
        System.out.print("No newline ");        // prints without newline
        System.out.printf("Formatted: %d\n", 42);  // like printf

        // Variables (must declare type):
        int number = 42;
        double pi = 3.14159;
        boolean isValid = true;
        String name = "Alice";         // String is a class, not primitive!

        // Strings:
        String s = "Hello";
        s += " World";                  // creates NEW string (strings are immutable!)
        System.out.println(s.length());           // 11
        System.out.println(s.toUpperCase());      // HELLO WORLD
        System.out.println(s.charAt(0));          // H
        System.out.println(s.substring(0, 5));    // Hello
        System.out.println(s.indexOf("World"));   // 6
        System.out.println(s.contains("World"));  // true
        System.out.println(s.replace("World", "Java")); // Hello Java

        // IMPORTANT: Use .equals() to compare strings, NOT ==!
        String a = "hello";
        String b = "hello";
        System.out.println(a == b);       // true (only by luck — same literal in pool)
        System.out.println(a.equals(b));  // true (CORRECT way to compare content)

        String c = new String("hello");
        System.out.println(a == c);       // FALSE! Different objects
        System.out.println(a.equals(c));  // true (same content)

        // User input:
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        int x = scanner.nextInt();
        double y = scanner.nextDouble();
        String line = scanner.nextLine();
        scanner.close();
    }
}
```

### Primitive Types vs Reference Types

```java
// PRIMITIVE types (stored directly, lowercase names):
byte    b  = 127;          // 1 byte, -128 to 127
short   s  = 32000;        // 2 bytes
int     i  = 2000000000;   // 4 bytes (most common)
long    l  = 9999999999L;  // 8 bytes (L suffix required)
float   f  = 3.14f;        // 4 bytes (f suffix required)
double  d  = 3.14159265;   // 8 bytes (default for decimals)
char    c  = 'A';          // 2 bytes (Unicode, not just ASCII!)
boolean bool = true;       // true or false

// REFERENCE types (stored as reference to object, uppercase):
String str = "hello";
int[] arr = {1, 2, 3};
Scanner scanner = new Scanner(System.in);
// Any class instance

// WRAPPER classes (objects for primitives):
Integer  intObj  = 42;        // auto-boxing: int → Integer
Double   dblObj  = 3.14;
Boolean  boolObj = true;
Character chrObj = 'A';

// Auto-boxing and unboxing:
Integer x = 5;      // autoboxing: int → Integer
int y = x;          // unboxing: Integer → int

// Wrapper methods:
int n = Integer.parseInt("123");   // "123" → 123
String s2 = Integer.toString(42);  // 42 → "42"
int max = Integer.MAX_VALUE;       // 2147483647
int min = Integer.MIN_VALUE;       // -2147483648
double sq = Math.sqrt(16.0);       // 4.0
int abs = Math.abs(-5);            // 5
double pow = Math.pow(2, 10);      // 1024.0
double rnd = Math.random();        // 0.0 to 1.0
```

---

## 3.2 Control Flow in Java

```java
// If-else (same syntax as C/C++):
int score = 85;
if (score >= 90) {
    System.out.println("A");
} else if (score >= 80) {
    System.out.println("B");
} else {
    System.out.println("F");
}

// Switch (traditional):
int day = 3;
switch (day) {
    case 1: System.out.println("Mon"); break;
    case 2: System.out.println("Tue"); break;
    case 3: System.out.println("Wed"); break;
    default: System.out.println("Other"); break;
}

// Switch expression (Java 14+):
String dayName = switch (day) {
    case 1 -> "Monday";
    case 2 -> "Tuesday";
    case 3 -> "Wednesday";
    default -> "Unknown";
};

// Loops (same as C/C++):
for (int i = 0; i < 5; i++) { ... }
while (condition) { ... }
do { ... } while (condition);

// Enhanced for (for-each) — Java's best loop for collections:
int[] arr = {1, 2, 3, 4, 5};
for (int element : arr) {
    System.out.println(element);
}

java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Carol");
for (String name : names) {
    System.out.println("Hello, " + name);
}
```

---

## 3.3 Arrays in Java

```java
// Declaration and creation:
int[] arr = new int[5];              // 5 ints, all initialized to 0
double[] values = {1.5, 2.5, 3.5}; // initialization with values
String[] names = new String[3];     // 3 Strings, all null initially

// Access:
arr[0] = 10;   // first element (index 0)
arr[4] = 50;   // last element (index 4)
// arr[5] = 60; // ArrayIndexOutOfBoundsException!

// Length:
System.out.println(arr.length);  // 5 (property, not method!)

// Traversal:
for (int i = 0; i < arr.length; i++) { ... }
for (int x : arr) { ... }  // for-each

// Useful methods from java.util.Arrays:
import java.util.Arrays;

int[] nums = {5, 3, 8, 1, 9, 2};
Arrays.sort(nums);               // sort in place: [1, 2, 3, 5, 8, 9]
System.out.println(Arrays.toString(nums));  // "[1, 2, 3, 5, 8, 9]"
int idx = Arrays.binarySearch(nums, 5);     // returns index of 5 (sorted required!)
int[] copy = Arrays.copyOf(nums, nums.length);  // create a copy
Arrays.fill(nums, 0);           // set all elements to 0

// 2D array:
int[][] matrix = new int[3][4];    // 3 rows, 4 columns
int[][] grid = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
System.out.println(grid[1][2]);   // 6 (row 1, col 2)
System.out.println(grid.length);      // 3 (number of rows)
System.out.println(grid[0].length);   // 3 (number of columns)
```

---

## 3.4 Object-Oriented Programming in Java

### Classes and Objects

```java
public class Student {
    // Instance fields (each object has its own):
    private String name;
    private int id;
    private double gpa;

    // Static field (shared by ALL Student objects):
    private static int totalStudents = 0;
    public static final double MAX_GPA = 4.0;  // constant

    // Constructor:
    public Student(String name, int id, double gpa) {
        this.name = name;   // 'this' distinguishes field from parameter
        this.id = id;
        this.gpa = gpa;
        totalStudents++;    // count every new student created
    }

    // Getters:
    public String getName() { return name; }
    public int getId() { return id; }
    public double getGpa() { return gpa; }
    public static int getTotalStudents() { return totalStudents; }

    // Setters with validation:
    public void setGpa(double gpa) {
        if (gpa < 0.0 || gpa > MAX_GPA) {
            throw new IllegalArgumentException("GPA must be 0-4: " + gpa);
        }
        this.gpa = gpa;
    }

    // Override toString() for nice printing:
    @Override
    public String toString() {
        return String.format("Student{id=%d, name='%s', gpa=%.2f}", id, name, gpa);
    }

    // Override equals() and hashCode():
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Student)) return false;
        Student other = (Student) obj;
        return id == other.id;  // two students are equal if same id
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(id);
    }
}

// Usage:
Student s1 = new Student("Alice", 1001, 3.8);
Student s2 = new Student("Bob", 1002, 3.5);

System.out.println(s1);             // Student{id=1001, name='Alice', gpa=3.80}
System.out.println(s1.getName());   // Alice
System.out.println(Student.getTotalStudents());  // 2 (static method)

s1.setGpa(4.0);
System.out.println(s1.getGpa());   // 4.0
```

### Inheritance in Java

```java
// Base class:
public class Vehicle {
    protected String brand;
    protected String model;
    protected int year;
    private int speed;  // private = not directly accessible in subclasses

    public Vehicle(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.speed = 0;
    }

    public void accelerate(int amount) {
        speed += amount;
        System.out.println(brand + " " + model + " accelerates to " + speed + " km/h");
    }

    public void brake(int amount) {
        speed = Math.max(0, speed - amount);
        System.out.println(brand + " slows to " + speed + " km/h");
    }

    public int getSpeed() { return speed; }

    // Method that CAN be overridden:
    public String describe() {
        return year + " " + brand + " " + model;
    }
}

// Derived class:
public class ElectricCar extends Vehicle {
    private double batteryLevel;  // 0-100%
    private double range;         // km per full charge

    public ElectricCar(String brand, String model, int year, double range) {
        super(brand, model, year);  // MUST call parent constructor first!
        this.batteryLevel = 100.0;
        this.range = range;
    }

    // Override parent method:
    @Override
    public void accelerate(int amount) {
        batteryLevel -= amount * 0.1;  // uses more battery when accelerating fast
        super.accelerate(amount);       // call parent implementation
        System.out.printf("Battery: %.1f%%\n", batteryLevel);
    }

    public void charge(double hours) {
        batteryLevel = Math.min(100.0, batteryLevel + hours * 20);
        System.out.printf("Charged to %.1f%%\n", batteryLevel);
    }

    public double estimatedRange() {
        return range * (batteryLevel / 100.0);
    }

    @Override
    public String describe() {
        return super.describe() + " (Electric, range: " + range + " km)";
    }
}

// Interfaces (like abstract classes but more flexible — a class can implement multiple):
public interface Chargeable {
    void charge(double hours);      // abstract (must implement)
    double getBatteryLevel();       // abstract
    default void displayCharge() { // default implementation (Java 8+)
        System.out.println("Battery: " + getBatteryLevel() + "%");
    }
}

public interface GPS {
    void setDestination(String destination);
    double getDistanceToDestination();
}

// A class can implement multiple interfaces:
public class SmartCar extends ElectricCar implements GPS {
    private String destination;
    private double distance;

    public SmartCar(String brand, String model, int year, double range) {
        super(brand, model, year, range);
    }

    @Override
    public void setDestination(String dest) { this.destination = dest; }

    @Override
    public double getDistanceToDestination() { return distance; }
}
```

### Polymorphism in Java

```java
// All Java method calls are virtual by default!
// To prevent overriding, use 'final':
// public final void cannotOverride() { ... }

Vehicle[] fleet = {
    new Vehicle("Toyota", "Corolla", 2020),
    new ElectricCar("Tesla", "Model 3", 2023, 500),
    new ElectricCar("BMW", "iX", 2023, 630)
};

for (Vehicle v : fleet) {
    System.out.println(v.describe());   // calls the RIGHT describe() for each type
    v.accelerate(50);                    // calls the RIGHT accelerate() for each type
}

// instanceof check:
for (Vehicle v : fleet) {
    if (v instanceof ElectricCar ec) {  // pattern matching (Java 16+)
        System.out.println("Range: " + ec.estimatedRange() + " km");
    }
}
```

---

## 3.5 Collections Framework

Java has a rich set of collection classes. Key ones:

```java
import java.util.*;
import java.util.stream.*;

// ArrayList (like vector<T> in C++):
List<String> list = new ArrayList<>();  // note: List interface, ArrayList implementation
list.add("Alice");          // add to end
list.add("Bob");
list.add(0, "Zara");        // insert at index 0
list.remove("Alice");       // remove by value
list.remove(0);             // remove by index
System.out.println(list.get(0));     // access by index
System.out.println(list.size());     // number of elements
System.out.println(list.contains("Bob")); // true/false
list.sort(Comparator.naturalOrder()); // sort
Collections.sort(list);              // alternative

// LinkedList (doubly-linked, also implements Queue and Deque):
LinkedList<Integer> linked = new LinkedList<>();
linked.addFirst(1);
linked.addLast(2);
linked.addFirst(0);   // [0, 1, 2]
linked.removeFirst(); // [1, 2]

// HashMap (like unordered_map<K,V> in C++):
Map<String, Integer> map = new HashMap<>();
map.put("apple", 3);
map.put("banana", 5);
map.put("cherry", 2);
int count = map.get("apple");              // 3
int defaultVal = map.getOrDefault("date", 0);  // 0 (key doesn't exist)
map.putIfAbsent("elderberry", 1);          // only if not already there
boolean hasKey = map.containsKey("banana"); // true
map.remove("cherry");

// Iterate map:
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + " -> " + entry.getValue());
}
// Or with forEach:
map.forEach((k, v) -> System.out.println(k + " -> " + v));

// HashSet (unordered unique values):
Set<String> set = new HashSet<>(Arrays.asList("a", "b", "c", "a", "b"));
// set = {a, b, c}  (duplicates removed, ORDER NOT GUARANTEED)

// TreeSet (sorted unique values):
Set<Integer> treeSet = new TreeSet<>(Arrays.asList(5, 3, 8, 1, 9));
// iterates in order: 1, 3, 5, 8, 9

// TreeMap (sorted by key):
Map<String, Integer> sortedMap = new TreeMap<>();
sortedMap.put("banana", 2); sortedMap.put("apple", 1); sortedMap.put("cherry", 3);
// iterates: apple→1, banana→2, cherry→3
```

---

## 3.6 Java Streams API

Streams provide a functional programming style for processing collections. Very powerful and elegant.

```java
import java.util.*;
import java.util.stream.*;

List<Integer> numbers = Arrays.asList(5, 3, 8, 1, 9, 2, 7, 4, 6);
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "Anna", "Brian");

// Pipeline: source → intermediate operations → terminal operation

// filter: keep elements matching predicate
List<Integer> evens = numbers.stream()
    .filter(n -> n % 2 == 0)    // keep only even numbers
    .collect(Collectors.toList());  // [8, 2, 4, 6]

// map: transform each element
List<Integer> doubled = numbers.stream()
    .map(n -> n * 2)
    .collect(Collectors.toList());  // [10, 6, 16, 2, 18, 4, 14, 8, 12]

// sorted:
List<Integer> sorted = numbers.stream()
    .sorted()                       // natural order
    .collect(Collectors.toList());  // [1, 2, 3, 4, 5, 6, 7, 8, 9]

// Chain operations:
List<String> result = names.stream()
    .filter(n -> n.startsWith("A"))     // keep names starting with A
    .map(String::toUpperCase)           // convert to uppercase
    .sorted()                           // sort
    .collect(Collectors.toList());      // ["ALICE", "ANNA"]

// Terminal operations:
long count = numbers.stream().filter(n -> n > 5).count();  // 4
int sum = numbers.stream().mapToInt(Integer::intValue).sum();  // 45
OptionalInt max = numbers.stream().mapToInt(Integer::intValue).max();  // 9
boolean anyAbove8 = numbers.stream().anyMatch(n -> n > 8);    // true
boolean allPositive = numbers.stream().allMatch(n -> n > 0);  // true

// Grouping:
Map<Boolean, List<Integer>> partitioned = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
// {false=[5,3,1,9,7], true=[8,2,4,6]}

Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length));
// {3=[Bob], 5=[Alice, Brian], 7=[Charlie]}

// String joining:
String joined = names.stream()
    .collect(Collectors.joining(", ", "[", "]"));
// "[Alice, Bob, Charlie, Anna, Brian]"
```

---

## 3.7 Exception Handling in Java

**Real-life analogy**: Exception handling is like a safety net below a tightrope walker. Normal execution goes across the rope. If something goes wrong (an exception is thrown), the safety net (catch block) catches it, handles the situation, and life continues.

```java
// Exception hierarchy:
// Throwable
// ├── Error (JVM errors — don't catch these normally)
// │   ├── OutOfMemoryError
// │   └── StackOverflowError
// └── Exception
//     ├── RuntimeException (unchecked — compiler doesn't force you to handle)
//     │   ├── NullPointerException
//     │   ├── ArrayIndexOutOfBoundsException
//     │   ├── ClassCastException
//     │   ├── IllegalArgumentException
//     │   ├── NumberFormatException
//     │   └── ArithmeticException
//     └── Checked exceptions (compiler FORCES you to handle or declare)
//         ├── IOException
//         ├── SQLException
//         └── FileNotFoundException

import java.io.*;

public class ExceptionExample {

    // Checked exception: MUST declare with 'throws' or catch it:
    public static String readFile(String path) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(path));
        StringBuilder content = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            content.append(line).append("\n");
        }
        reader.close();
        return content.toString();
    }

    // Custom exception:
    static class InsufficientBalanceException extends RuntimeException {
        private double amount;
        public InsufficientBalanceException(double amount) {
            super("Insufficient balance: need $" + amount + " more");
            this.amount = amount;
        }
        public double getAmount() { return amount; }
    }

    public static void main(String[] args) {
        // Basic try-catch:
        try {
            int result = 10 / 0;              // ArithmeticException
        } catch (ArithmeticException e) {
            System.err.println("Math error: " + e.getMessage()); // "/ by zero"
        }

        // Multiple catch blocks:
        try {
            String s = null;
            System.out.println(s.length());   // NullPointerException!
        } catch (NullPointerException e) {
            System.err.println("Null reference: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Other error: " + e.getMessage());
        } finally {
            System.out.println("This ALWAYS runs (finally block)");
        }

        // Multi-catch (Java 7+):
        try {
            // some code
        } catch (NullPointerException | ArrayIndexOutOfBoundsException e) {
            System.err.println("NPE or AIOOBE: " + e.getMessage());
        }

        // Try-with-resources (auto-closes the resource):
        try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
            String line = reader.readLine();
            System.out.println(line);
        } catch (IOException e) {
            System.err.println("File error: " + e.getMessage());
        }
        // reader.close() is called automatically!

        // Throwing exceptions:
        try {
            if (args.length == 0)
                throw new IllegalArgumentException("No arguments provided!");
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }

        // Chaining exceptions (wrap one exception in another):
        try {
            try {
                int n = Integer.parseInt("not a number");  // NumberFormatException
            } catch (NumberFormatException e) {
                throw new RuntimeException("Invalid configuration file", e);
            }
        } catch (RuntimeException e) {
            System.err.println(e.getMessage());
            System.err.println("Caused by: " + e.getCause().getMessage());
        }
    }
}
```

---

## 3.8 Generics in Java

```java
// Generic class (like templates in C++):
public class Pair<A, B> {
    private A first;
    private B second;

    public Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }

    public A getFirst() { return first; }
    public B getSecond() { return second; }

    @Override
    public String toString() {
        return "(" + first + ", " + second + ")";
    }
}

// Generic method:
public static <T extends Comparable<T>> T maximum(T a, T b) {
    return a.compareTo(b) >= 0 ? a : b;
}

// Wildcards:
// List<?>        — unknown type (read-only, can't add)
// List<? extends Number> — any Number subtype (can read as Number, can't add)
// List<? super Integer>  — Integer or its supertypes (can add Integer)

public static double sumList(List<? extends Number> list) {
    double sum = 0;
    for (Number n : list) sum += n.doubleValue();
    return sum;
}

// Usage:
Pair<String, Integer> nameAge = new Pair<>("Alice", 30);
System.out.println(nameAge);  // (Alice, 30)

System.out.println(maximum(5, 8));        // 8
System.out.println(maximum("apple", "banana"));  // banana

List<Integer> ints = Arrays.asList(1, 2, 3, 4, 5);
List<Double> doubles = Arrays.asList(1.5, 2.5, 3.5);
System.out.println(sumList(ints));     // 15.0
System.out.println(sumList(doubles));  // 7.5
```

---

## 3.9 Lambda Expressions and Functional Interfaces

Java 8 introduced lambda expressions — anonymous functions.

```java
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

// Traditional anonymous class:
Comparator<String> byLength_old = new Comparator<String>() {
    @Override
    public int compare(String a, String b) {
        return Integer.compare(a.length(), b.length());
    }
};

// Lambda equivalent:
Comparator<String> byLength = (a, b) -> Integer.compare(a.length(), b.length());
// or: Comparator.comparingInt(String::length)

List<String> words = new ArrayList<>(Arrays.asList("banana", "apple", "cherry", "date"));
words.sort(byLength);
System.out.println(words);  // [date, apple, banana, cherry]

// Functional interfaces from java.util.function:
Function<String, Integer> strToInt = Integer::parseInt;  // method reference
System.out.println(strToInt.apply("42"));  // 42

Predicate<Integer> isEven = n -> n % 2 == 0;
System.out.println(isEven.test(4));   // true
System.out.println(isEven.test(7));   // false

// Combine predicates:
Predicate<Integer> isPositive = n -> n > 0;
Predicate<Integer> isEvenAndPositive = isEven.and(isPositive);
Predicate<Integer> isEvenOrPositive  = isEven.or(isPositive);
Predicate<Integer> isOdd = isEven.negate();

Consumer<String> print = s -> System.out.println(">>> " + s);
print.accept("Hello");  // >>> Hello

Supplier<List<String>> listFactory = ArrayList::new;  // creates new ArrayList each time
List<String> newList = listFactory.get();

BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
System.out.println(add.apply(3, 4));  // 7

// Lambdas with streams (very common in modern Java):
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Sum of squares of even numbers:
int result = nums.stream()
    .filter(isEven)
    .map(n -> n * n)
    .reduce(0, Integer::sum);
System.out.println(result);  // 220  (4+16+36+64+100)
```

---

## Quick Reference Summary

### C vs C++ vs Java

| Feature | C | C++ | Java |
|---------|---|-----|------|
| Memory mgmt | manual (malloc/free) | manual (new/delete) | automatic (GC) |
| Strings | char arrays | std::string | String class |
| OOP | none | yes | yes (everything!) |
| Generics | none | templates | generics |
| Exception handling | none (setjmp) | try/catch | try/catch (checked!) |
| Collections | arrays only | STL | Collections Framework |
| Platform | machine-specific | machine-specific | cross-platform (JVM) |
| Performance | fastest | very fast | fast (JIT compiled) |

### Key Rules to Remember

**C**:
- Arrays start at index 0
- Strings end with `\0`
- Pass pointers to modify variables
- Always `free()` what you `malloc()`
- `==` for numbers, `strcmp()` for strings

**C++**:
- Always use `virtual` destructor in base classes with virtual methods
- Use `override` keyword when overriding (helps catch typos)
- The Rule of Three: if you define one of {destructor, copy constructor, copy assignment}, define all three
- `delete[]` for arrays, `delete` for single objects

**Java**:
- Use `.equals()` not `==` to compare Strings (and objects in general)
- Checked exceptions MUST be caught or declared with `throws`
- All method calls are virtual by default (use `final` to prevent override)
- `null` causes `NullPointerException` — always check before using
- Strings are immutable — use `StringBuilder` for many concatenations
