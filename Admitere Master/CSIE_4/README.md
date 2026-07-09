# 📚 THEORETICAL SUMMARY — Master Exam CSIE4
## Cybersecurity Master Program — *Securitatea Informatică* (English)

> Extracted from the exact pages specified in the bibliography.

---

## TABLE OF CONTENTS
1. [C Programming Language](#1-c-programming-language) — [1] Kernighan & Ritchie, pp. 35–190
2. [C++ Programming Language](#2-c-programming-language) — [2] Stroustrup, pp. 59–132, 255–410
3. [Java Programming Language](#3-java-programming-language) — [3] OCP Java SE 17 Study Guide, pp. 1–623

---

# 1. C PROGRAMMING LANGUAGE
**Source: [1] Kernighan & Ritchie — The C Programming Language, 2nd Edition**

## 1.1 Types, Operators, and Expressions (pp. 35–54)

### Variable Names
- Names are made up of letters and digits; the first character must be a letter
- Underscore `_` counts as a letter; don't begin names with underscore (library routines use it)
- Upper case and lower case are distinct: `x` and `X` are different names
- Keywords (`if`, `else`, `int`, `float`, etc.) are reserved, cannot be used as variable names
- Convention: lower case for variable names, all upper case for symbolic constants

### Data Types and Sizes (§2.2)
Basic data types in C:

| Type | Description |
|------|-------------|
| `char` | Single byte, holds one character |
| `int` | Integer, typically reflecting the natural size on the host machine |
| `float` | Single-precision floating point |
| `double` | Double-precision floating point |

Qualifiers: `short`, `long`, `signed`, `unsigned`.
- `short` is often 16 bits; `long` is at least 32 bits; `short` ≤ `int` ≤ `long`
- `signed` or `unsigned` may be applied to `char` or any integer type
- `unsigned char`: 0 to 255; `signed char`: −128 to 127
- `long double`: extended-precision floating point
- Header `<limits.h>` defines symbolic constants for sizes; `<float.h>` for floating-point

### Constants (§2.3)
- **Integer constants**: `1234` (decimal), `0666` (octal prefix `0`), `0x1F` (hex prefix `0x`)
- **Long constants**: suffix `l` or `L` (e.g., `123L`); unsigned: `u` or `U`
- **Floating-point**: `123.4`, `1e-2`; suffix `f`/`F` for `float`, `l`/`L` for `long double`
- **Character constants**: `'a'`, `'\n'`, `'\t'`, `'\0'`, `'\\'`, `'\''`, `'\xhh'` (hex), `'\ooo'` (octal)
- **String constants**: `"hello\n"` — array of characters terminated by `'\0'`; `"hello"` has length 6 in memory
- **Enumeration constants**: `enum boolean { NO, YES };` — values start at 0 by default

### Declarations (§2.4)
```c
int lower, upper, step;
char c, line[1000];
int i = 0;              /* initialized */
const double e = 2.71828;  /* const: value cannot be changed */
```
`const` can also qualify array arguments: `int strlen(const char[]);`

### Arithmetic Operators (§2.5)
Binary: `+`, `-`, `*`, `/`, `%` (modulus).
- Integer division truncates towards zero
- `%` cannot be applied to `float` or `double`
- Unary minus: `-x`
- Precedence: `*`, `/`, `%` higher than `+`, `-`; arithmetic operators associate left to right

### Relational and Logical Operators (§2.6)
- Relational: `>`, `>=`, `<`, `<=` — all have the same precedence
- Equality: `==`, `!=` — lower precedence than relational
- Logical: `&&` (AND), `||` (OR) — evaluated left to right; evaluation stops as soon as truth/falsehood is known (**short-circuit evaluation**)
- `!` (logical NOT) — unary, converts non-zero to 0 and zero to 1

### Type Conversions (§2.7)
- Automatic widening conversions: `char`/`short` → `int` → `long` → `float` → `double` → `long double`
- `char` is just a small integer; arithmetic is done on it freely
- Explicit cast: `(type) expression` — e.g., `(int) sqrt(n)` converts result to int
- `atoi`, `atof` — standard library string to number conversions

### Increment and Decrement Operators (§2.8)
- `++n` — prefix: increment before use; `n++` — postfix: use then increment
- `--n` / `n--` — decrement variants
- Can only be applied to variables, not expressions

### Bitwise Operators (§2.9)
Applied only to integer types (`char`, `short`, `int`, `long`):

| Operator | Meaning |
|----------|---------|
| `&` | AND |
| `\|` | OR (inclusive) |
| `^` | XOR (exclusive OR) |
| `<<` | Left shift |
| `>>` | Right shift |
| `~` | One's complement (unary) |

- `x & 0177` — mask off all but the low-order 7 bits
- `x |= SET_ON` — set bits in x that are set in SET_ON
- `x &= ~MASK` — turn off bits in x set in MASK
- `x ^= y` — XOR (flip bits)
- `x >> 2` — right shift by 2 (division by 4 for unsigned; sign bit propagation for signed is machine-dependent)

### Assignment Operators and Expressions (§2.10)
- `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=`
- `x += 2` is equivalent to `x = x + 2`

### Conditional Expressions (§2.11)
- Ternary operator: `expr1 ? expr2 : expr3`
- `z = (a > b) ? a : b;` — z = maximum of a and b

### Precedence and Order of Evaluation (§2.12)
From highest to lowest:
```
() [] -> .                    left to right
! ~ ++ -- + - * & (type) sizeof  right to left (unary)
* / %                         left to right
+ -                           left to right
<< >>                         left to right
< <= > >=                     left to right
== !=                         left to right
&                             left to right
^                             left to right
|                             left to right
&&                            left to right
||                            left to right
?:                            right to left
= += -= etc.                  right to left
,                             left to right
```

---

## 1.2 Control Flow (pp. 55–66)

### Statements and Blocks (§3.1)
- An expression followed by `;` is a statement
- Braces `{ }` group declarations and statements into a **compound statement** (block)

### If-Else (§3.2)
```c
if (expression)
    statement1
else
    statement2
```
The `else` part is optional. The `else` associates with the **closest** preceding `else-less if`. Use braces to override:
```c
if (n > 0) {
    if (a > b)
        z = a;
} else        /* associates with outer if */
    z = b;
```

### Else-If (§3.3)
```c
if (expr1)   stmt1;
else if (expr2) stmt2;
else if (expr3) stmt3;
else    stmt_default;
```

### Switch (§3.4)
```c
switch (expression) {
    case const1:
        statements;
        break;
    case const2:
        statements;
        break;
    default:
        statements;
        break;
}
```
- `expression` must be integer type
- Without `break`: falls through to the next case
- `default` is optional; handles all cases not covered by explicit `case` labels

### While and For (§3.5)
```c
while (expression)
    body;

for (init; condition; increment)
    body;
/* equivalent to: */
init;
while (condition) { body; increment; }
```
- Any of the three parts of `for` may be omitted (infinite loop: `for (;;)`)
- The comma operator separates expressions, evaluated left to right; value = rightmost

### Do-While (§3.6)
```c
do {
    body;
} while (expression);
```
The body is executed at least once; condition tested after each iteration.

### Break and Continue (§3.7)
- `break` — exits the innermost enclosing loop or switch immediately
- `continue` — causes the next iteration of the enclosing loop; in `for` loops, executes the increment step

### Goto and Labels (§3.8)
```c
for (...) {
    for (...) {
        if (disaster)
            goto error;
    }
}
error:
    /* clean up */
```
`goto` is rarely useful; the main use is abandoning nested loops. Labels have the same form as variable names, followed by a colon.

---

## 1.3 Functions and Program Structure (pp. 67–92)

### Basics of Functions (§4.1)
```c
return-type function-name(parameter declarations, if any)
{
    declarations and statements
}
```
- If return type is omitted, `int` is assumed
- If a function takes no arguments, use `void`: `void function_name(void)`
- `return expression;` — the value is converted to the return type if needed
- A function with no return type or `return;` returns no useful value

### Functions Returning Non-Integers (§4.2)
- Declare the function before use with a prototype: `double atof(char s[]);`
- If no prototype, defaults to returning `int` — dangerous for non-int returns

### External Variables (§4.3–§4.4)
- **External variables**: defined outside any function; accessible by name from any function in any file
- Lifetime: permanent (exist throughout execution)
- Declared with `extern` in other files: `extern int max;`
- **Initialization**: external and static variables are initialized to zero by default
- Local (automatic) variables are not initialized automatically

### Scope Rules (§4.3)
- **Automatic (local)** variables: declared inside a function; exist only during function execution; no connection to variables with the same name elsewhere
- **External variables**: accessible from declaration point to end of file
- Declaration vs. Definition: a variable is defined exactly once (allocates storage); declared in every file that uses it (`extern`)

### Header Files (§4.5)
- Use `#include "filename.h"` or `#include <filename.h>`
- Common practice: put shared declarations in a `.h` header file

### Static Variables (§4.6)
- `static` on an external variable/function: limits scope to the file where it's defined
- `static` on a local variable: retains its value between function calls (initialized only once)

### Register Variables (§4.7)
- `register int x;` — advice to compiler to keep variable in a register for fast access
- Cannot take the address of a register variable

### Block Structure (§4.8)
- Variables can be declared inside any block (compound statement)
- Inner declarations shadow outer ones with the same name

### Initialization (§4.9)
- Scalar: `int x = 1;`
- Array: `int days[] = { 31, 28, 31, ... };` — size can be omitted; compiler counts
- Character array: `char s[] = "hello";` — automatically adds `'\0'`
- External/static arrays are initialized to zero if not explicitly initialized

### Recursion (§4.10)
- Functions can call themselves, directly or indirectly
- Each invocation gets its own set of local variables
- Useful for problems with recursive structure (trees, divide-and-conquer)

### The C Preprocessor (§4.11)
- `#include "file"` — includes the file contents
- `#define NAME text` — macro substitution (token replacement); no semicolon
- `#define max(A,B) ((A) > (B) ? (A) : (B))` — parameterized macro
- `#undef NAME` — undefine a macro
- Conditional compilation: `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif`

---

## 1.4 Pointers and Arrays (pp. 93–126)

### Pointers and Addresses (§5.1)
- A pointer is a variable that holds the address of another variable
- `&x` — address of variable x
- `*p` — the value of what p points to (indirection/dereference)
```c
int x = 1, *ip;
ip = &x;       /* ip points to x */
*ip = 0;       /* x is now 0 */
```
- `*` and `&` have higher precedence than arithmetic operators but lower than `()`

### Pointers and Function Arguments (§5.2)
- C passes arguments **by value** — functions receive copies; cannot modify the caller's variables
- To modify a variable in the caller, pass its address:
```c
void swap(int *px, int *py) {
    int temp = *px; *px = *py; *py = temp;
}
/* call: */ swap(&a, &b);
```

### Pointers and Arrays (§5.3)
- `pa = &a[0]` or equivalently `pa = a` — pointer to first element
- `*(pa+1)` accesses `a[1]`; `pa+i` points to `a[i]`
- `a[i]` and `*(a+i)` are equivalent; similarly `&a[i]` and `a+i`
- Array name = pointer to first element; cannot assign to an array name
- `sizeof(array)/sizeof(array[0])` gives the number of elements

### Address Arithmetic (§5.4)
- Pointers to the same array can be subtracted: result = number of elements between them
- Pointer + integer: advances by that many elements (scaled by element size)
- Comparison with `==` and `!=` and ordered comparisons (`<`, `>`) valid for pointers to same array

### Character Pointers and Functions (§5.5)
```c
char amessage[] = "now is the time"; /* an array */
char *pmessage = "now is the time";  /* a pointer */
```
- `amessage` is an array; its contents can be changed
- `pmessage` points to a string literal; **modifying the string is undefined behavior**

### Pointer Arrays; Pointers to Pointers (§5.6)
```c
char *lineptr[MAXLINES]; /* array of MAXLINES pointers to char */
```
- `lineptr[i]` is a character pointer; `*lineptr[i]` is the first character of that string

### Multi-dimensional Arrays (§5.7)
```c
int a[3][4]; /* 3 rows, 4 columns */
a[i][j];     /* element at row i, column j */
```
- In C, a 2D array is an array of arrays; rows are contiguous in memory
- When passed to a function, the column count must be specified: `f(int a[][4])`

### Initialization of Pointer Arrays (§5.8)
```c
char *month_name[] = { "Illegal month", "January", "February", ... };
```

### Pointers vs. Multi-dimensional Arrays (§5.9)
- `int a[10][20]` allocates 200 ints as one block
- `int *b[10]` allocates 10 pointers; each can point to arrays of different lengths (jagged arrays)

### Command-line Arguments (§5.10)
```c
int main(int argc, char *argv[]) { ... }
```
- `argc`: count of command-line arguments (including program name)
- `argv[0]`: program name; `argv[1]` through `argv[argc-1]`: actual arguments
- `argv[argc]` is a null pointer

### Pointers to Functions (§5.11)
```c
int (*comp)(void *, void *); /* pointer to function returning int */
comp = strcmp;               /* assign */
(*comp)(s1, s2);             /* call */
/* or in C: */ comp(s1, s2);
```
- Used in generic algorithms (e.g., `qsort`): `void qsort(void *base, size_t n, size_t size, int (*compar)(const void *, const void *));`

### Complicated Declarations (§5.12)
```c
int *p;          /* pointer to int */
int *p[];        /* array of pointers to int */
int (*p)[];      /* pointer to array of int */
int *f();        /* function returning pointer to int */
int (*f)();      /* pointer to function returning int */
char (*(*x())[])(); /* function returning pointer to array of pointers to functions returning char */
```

---

## 1.5 Structures and Unions (pp. 127–150)

### Basics of Structures (§6.1)
```c
struct point {
    int x;
    int y;
};
struct point pt;          /* declare variable */
pt.x = 5;  pt.y = 10;    /* access members with . */
struct point maxpt = { 320, 200 }; /* initialize */
```

### Structures and Functions (§6.2)
- Structures can be passed to and returned from functions
- Passing by value: a copy of the entire struct is passed
- More efficient to pass a pointer: `void func(struct point *pp)`
```c
struct point *pp = &pt;
pp->x = 5;      /* arrow operator: pointer to struct member */
(*pp).x = 5;    /* equivalent */
```

### Arrays of Structures (§6.3)
```c
struct key { char *word; int count; } keytab[] = {
    { "auto", 0 },
    { "break", 0 },
    /* ... */
};
```

### Pointers to Structures (§6.4)
- `struct point *pp` — pointer to a struct
- `pp->member` — access member via pointer

### Self-referential Structures (§6.5)
```c
struct tnode {
    char *word;
    int count;
    struct tnode *left;   /* pointer to itself */
    struct tnode *right;
};
```
Used for linked lists, binary trees, etc.

### Table Lookup (§6.6)
Hash tables using arrays of `struct` with pointers for chaining.

### Typedef (§6.7)
```c
typedef int Length;         /* Length is a synonym for int */
typedef char *String;       /* String is a synonym for char * */
typedef struct tnode *Treeptr;
typedef struct tnode {
    char *word; int count;
    Treeptr left, right;
} Treenode;
Treenode t;   /* uses the typedef */
```
- `typedef` does not create new types; creates synonyms
- Common use: hide implementation details, improve portability

### Unions (§6.8)
A variable that may hold objects of different types, one at a time:
```c
union u_tag {
    int ival;
    float fval;
    char *sval;
} u;
u.ival = 5;         /* now holds int */
u.fval = 3.14;      /* now holds float (ival no longer valid!) */
```
- Size of union = size of its largest member
- At any one time, only the most recently written member is valid
- Often used within a `struct` to tag the union type

### Bit-fields (§6.9)
```c
struct {
    unsigned int is_keyword : 1;   /* 1-bit field */
    unsigned int is_extern  : 1;
    unsigned int is_static  : 1;
} flags;
```
- Allows packing multiple flags into a single `int`
- Width after `:` specifies number of bits
- Fields without names serve as padding

---

## 1.6 Input and Output (pp. 151–168)

### Standard Input and Output (§7.1)
```c
#include <stdio.h>
int c = getchar();      /* read next input character; returns EOF at end */
putchar(c);             /* write character c to stdout */
```
`EOF` is typically −1; defined in `<stdio.h>`.

### Formatted Output — printf (§7.2)
```c
printf(format_string, arg1, arg2, ...);
```
Format specifiers:
| Spec | Argument type | Output |
|------|--------------|--------|
| `%d`, `%i` | `int` | Decimal integer |
| `%o` | `int` | Unsigned octal |
| `%x`, `%X` | `int` | Unsigned hexadecimal |
| `%u` | `unsigned int` | Unsigned decimal |
| `%c` | `int` | Single character |
| `%s` | `char *` | String (until `\0`) |
| `%f` | `double` | Fixed-point notation |
| `%e`, `%E` | `double` | Scientific notation |
| `%g`, `%G` | `double` | Shorter of `%f` or `%e` |
| `%p` | `void *` | Pointer value |
| `%%` | — | Literal `%` |

Width/precision: `%5d` (width 5), `%-5d` (left-justified), `%05d` (zero-padded), `%8.2f` (width 8, 2 decimal places), `%*.*f` (width and precision as arguments).

### Formatted Input — scanf (§7.4)
```c
scanf(format_string, &var1, &var2, ...);
```
- Takes addresses (`&`) of variables to fill
- Returns number of successfully matched items, or `EOF`
- `%d` reads an integer, `%s` reads a word (whitespace-delimited), `%c` reads a character

### File Access (§7.5)
```c
FILE *fp;
fp = fopen(name, mode);   /* modes: "r", "w", "a", "rb", "wb", etc. */
if (fp == NULL) { /* handle error */ }
getc(fp);          /* read character from fp */
putc(c, fp);       /* write character to fp */
fclose(fp);        /* close file */
```
- `stdin`, `stdout`, `stderr` are pre-opened `FILE *` pointers
- `fprintf(fp, format, ...)` — formatted output to file
- `fscanf(fp, format, ...)` — formatted input from file

### Error Handling — Stderr and Exit (§7.6)
```c
fprintf(stderr, "error: ...\n");
exit(1);    /* terminates program; 0 = success, non-zero = failure */
```

### Line Input and Output (§7.7)
```c
char *fgets(char *line, int maxline, FILE *fp);  /* reads one line; includes '\n' */
int fputs(char *line, FILE *fp);                 /* writes string to file */
/* Equivalent for stdin/stdout: */
char *gets(char *line);    /* unsafe! no length limit */
int puts(char *line);
```

### Miscellaneous Functions (§7.8)
- `sprintf(str, format, ...)` — formatted output to a string buffer
- `sscanf(str, format, ...)` — formatted input from a string

---

## 1.7 The C Standard Library and UNIX System Interface (pp. 169–190)

### String Operations `<string.h>` (§B3)
| Function | Description |
|----------|-------------|
| `strlen(s)` | Length of s (excluding `\0`) |
| `strcpy(t, s)` | Copy s to t; returns t |
| `strncpy(t, s, n)` | Copy at most n chars of s to t |
| `strcat(t, s)` | Concatenate s to end of t |
| `strncat(t, s, n)` | Concatenate at most n chars |
| `strcmp(s, t)` | Compare: <0, 0, >0 |
| `strncmp(s, t, n)` | Compare at most n chars |
| `strchr(s, c)` | Pointer to first occurrence of c in s; NULL if not found |
| `strrchr(s, c)` | Pointer to last occurrence of c in s |

### Character Class Testing `<ctype.h>` (§B2)
`isalpha(c)`, `isupper(c)`, `islower(c)`, `isdigit(c)`, `isspace(c)`, `isalnum(c)`, `ispunct(c)`, `toupper(c)`, `tolower(c)` — all take `int`, return `int`.

### Mathematical Functions `<math.h>` (§B4)
`sin(x)`, `cos(x)`, `atan(x)`, `atan2(y,x)`, `exp(x)`, `log(x)`, `log10(x)`, `pow(x,y)`, `sqrt(x)`, `fabs(x)`, `floor(x)`, `ceil(x)`.

### Utility Functions `<stdlib.h>` (§B5)
| Function | Description |
|----------|-------------|
| `atoi(s)` | String to int |
| `atof(s)` | String to double |
| `strtol(s, endp, base)` | String to long with error checking |
| `rand()` | Random integer in [0, RAND_MAX] |
| `srand(seed)` | Set random seed |
| `malloc(n)` | Allocate n bytes; returns `void *` or NULL |
| `calloc(n, size)` | Allocate n×size bytes, initialized to zero |
| `realloc(p, n)` | Resize allocation at p to n bytes |
| `free(p)` | Free memory allocated by malloc |
| `exit(status)` | Terminate program with status |
| `abs(n)` | Absolute value of int |
| `system(s)` | Execute shell command s |
| `getenv(name)` | Return value of environment variable |
| `bsearch(key, arr, n, size, cmp)` | Binary search |
| `qsort(arr, n, size, cmp)` | Quicksort |

### Memory Allocation (§8.7)
```c
void *malloc(size_t n);    /* allocate n bytes */
void *calloc(size_t n, size_t size); /* n items of given size, zero-initialized */
void free(void *p);        /* return memory to pool */
```
`malloc` returns `NULL` if insufficient memory. Always check!

### UNIX System Interface (§8)
- **File descriptors**: 0 = stdin, 1 = stdout, 2 = stderr
- Low-level I/O (POSIX): `read(fd, buf, n)`, `write(fd, buf, n)`, `open(name, flags, perms)`, `close(fd)`
- Directory operations: `opendir`, `readdir`, `closedir`
- `stat(filename, &stbuf)` — file information (size, times, permissions)

---

# 2. C++ PROGRAMMING LANGUAGE
**Source: [2] Bjarne Stroustrup — The C++ Programming Language, 3rd Edition**

## 2.1 Classes, Objects, Types, and Values (pp. 59–88)

*(Note: pp. 59–88 in Stroustrup cover the Tour of the Standard Library — Chapter 3 and beginning of Chapter 4/5)*

### Types, Variables, and Arithmetic (Ch. 4)
C++ is a statically typed language. Every entity (object, value, name, expression) has a type.

**Fundamental types:**
```cpp
bool    b = true;            // Boolean
char    c = 'a';             // character (1 byte)
int     i = 42;              // integer (4 bytes typically)
double  d = 3.14;            // double-precision float
```

**Variable declaration:**
```cpp
int x;                       // uninitialized
int y = 5;                   // initialized
auto z = 3.14;               // type deduced as double (C++11)
```

**Arithmetic operators:** `+`, `-`, `*`, `/`, `%` — same as C. Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`. Logical: `&&`, `||`, `!`.

**Constants:**
- `const double pi = 3.14159;` — cannot be changed after initialization
- `constexpr double c = 299792.0;` — evaluated at compile time

### Classes (Ch. 6 of Stroustrup / pp. 59–88 context)
A **class** is a user-defined type. It consists of data members and member functions (methods).

```cpp
class Vector {
public:
    Vector(int s);          // constructor
    double& operator[](int i);   // subscript operator
    int size();
private:
    double* elem;           // pointer to elements
    int sz;                 // number of elements
};

Vector::Vector(int s)
    : elem{new double[s]}, sz{s} { }  // member initializer list

double& Vector::operator[](int i) { return elem[i]; }
int Vector::size() { return sz; }
```

**Key concepts:**
- **Encapsulation** — `public:` interface vs `private:` implementation
- **Invariant** — condition always true for all objects; established by constructor
- Constructor name = class name; no return type
- **Destructor**: `~Vector() { delete[] elem; }` — called automatically when object goes out of scope

### Class Hierarchy
```cpp
class Shape {
public:
    virtual void draw() const = 0;  // pure virtual
    virtual void rotate(int) = 0;
    virtual ~Shape() {}             // virtual destructor!
};

class Circle : public Shape {
public:
    void draw() const override;
    void rotate(int) override;
    // ...
};
```
- `virtual` — dynamic dispatch (late binding): the actual function called depends on the runtime type
- `= 0` — pure virtual: makes the class abstract (cannot be instantiated)
- `override` — explicit override of a virtual function (C++11); compiler checks correctness
- Virtual destructors ensure derived class destructors are called correctly

### Copying and Moving
- **Copy constructor**: `Vector(const Vector& v)` — deep copy
- **Copy assignment**: `Vector& operator=(const Vector& v)`
- **Move constructor**: `Vector(Vector&& v)` — transfer ownership without copying
- **Move assignment**: `Vector& operator=(Vector&& v)`
- Rule of five: if you define one of these, define all five

---

## 2.2 Computation: Expressions, Statements, Functions, Vector (pp. 89–132)

### Arrays and Pointers (pp. 89–100, Ch. 5)
```cpp
double a[6];         // array of 6 doubles (indices 0–5)
double* p = &a[3];   // pointer to a[3]
p[2] = 7.0;          // a[5] = 7.0
```
- Array name decays to pointer to first element
- Prefer `std::vector` over raw arrays for safety

**Pointer arithmetic:** `p+n` moves n elements forward.

**References:** An alias for an existing object — cannot be null, cannot be rebound:
```cpp
int var = 1;
int& r = var;   // r is a reference to var
r = 2;          // var is now 2
```

**Null pointer:** `nullptr` (C++11) — use instead of `NULL` or `0`.

### Structures (pp. 102–111, Ch. 5)
```cpp
struct Address {
    string name;
    int number;
    string street;
};
Address jd = { "Jim", 22, "Nassau Street" };
```

### Statements (§6.3, pp. 119–132)
All C control-flow statements work in C++, plus:

**Range-for loop (C++11):**
```cpp
for (int x : v)    // read each element of vector v
    cout << x << '\n';

for (int& x : v)   // write each element
    x *= 2;
```

**Initializer in if/switch (C++17):**
```cpp
if (auto p = m.find(key); p != m.end())
    use(p->second);
```

### Functions (pp. 106–120)
```cpp
Elem* next_elem();                   // no arguments, returns Elem*
void exit(int);                      // void return type
double sqrt(double);                 // one double argument

// Function overloading:
void print(int i) { ... }
void print(double d) { ... }
void print(string s) { ... }

// Default arguments:
void f(int a, int b = 5, int c = 10);   // can call f(1), f(1,2), f(1,2,3)
```

**Argument passing:**
- By value: `void f(int x)` — copy; caller's variable unchanged
- By reference: `void f(int& x)` — alias; modifies caller's variable
- By const reference: `void f(const int& x)` — read-only alias; no copy

**Inline functions:** `inline int f(int x) { return x+1; }` — compiler may substitute call with body.

**Namespace:**
```cpp
namespace My {
    void f();
    int i;
}
My::f();    // using qualified name
using namespace std;  // bring all std names into scope
```

### The `vector` Class
```cpp
#include <vector>
using namespace std;

vector<int> v1 = { 1, 2, 3, 4 };   // initialized list
vector<string> v2(10);              // 10 empty strings
v1.push_back(5);                    // add element
v1.size();                          // number of elements
v1[3];                              // access (no bounds check)
v1.at(3);                           // access with bounds check (throws out_of_range)

// Iteration:
for (auto& x : v1) cout << x;
```

---

## 2.3 Technicalities: Functions, Classes (pp. 255–344)

### Function Declaration and Definition (Ch. 7, §7.1–7.7)
```cpp
// Suffix return type (C++11):
auto f(int a, double b) -> double;

// Trailing return type:
auto operator+(Complex a, Complex b) -> Complex;

// constexpr functions (evaluated at compile time if possible):
constexpr double square(double x) { return x * x; }

// [[noreturn]] — function never returns:
[[noreturn]] void error(string s);
```

**Argument types:**
- `const` reference for read-only large objects: `void f(const vector<int>& v)`
- Pointer for optional: pass `nullptr` if no argument
- Move semantics: use `&&` for "steal" semantics

**Overload resolution:** compiler selects the best match among all overloaded functions based on argument types.

### Namespaces (§8, Ch. 8)
```cpp
namespace Chrono {
    class Date { ... };
    bool operator==(const Date& a, const Date& b);
    Date next_weekday(Date d);
}
// Access: Chrono::Date, Chrono::next_weekday
using Chrono::Date;    // bring into scope
```

### Class Mechanics (Ch. 10, pp. 255–300)
```cpp
class Date {
public:
    // Constructor:
    Date(int d, Month m, int y);
    // Member functions:
    int day() const;    // const: doesn't modify object
    Month month() const;
    int year() const;
    // Operators:
    Date& operator+=(int d);
    // Static members:
    static Date today();
private:
    int d, m, y;
};
```

**Member initialization (in constructor):**
```cpp
Date::Date(int dd, Month mm, int yy) : d{dd}, m{mm}, y{yy}
{
    if (d < 1 || d > 31) throw Bad_date{};
}
```

**Constant members:** `int day() const` — guarantees the function doesn't modify the object; can be called on `const` objects.

**`this` pointer:** implicit pointer to the object on which a member function is called. `this->d` = `d` when unambiguous.

**Static members:** belong to the class, not individual objects. One copy shared among all instances.

### Operator Overloading (Ch. 11, pp. 300–330)
Most operators can be overloaded:
```cpp
class complex {
    double re, im;
public:
    complex(double r, double i) : re{r}, im{i} {}
    complex& operator+=(complex z) { re+=z.re; im+=z.im; return *this; }
    complex& operator-=(complex z) { re-=z.re; im-=z.im; return *this; }
};
// Binary operators as non-members (friends or free functions):
complex operator+(complex a, complex b) { return a += b; }
complex operator-(complex a, complex b) { return a -= b; }
bool operator==(complex a, complex b) { return a.re==b.re && a.im==b.im; }

// << for output:
ostream& operator<<(ostream& os, complex z) {
    return os << '(' << z.real() << ',' << z.imag() << ')';
}
```

**Cannot overload:** `::`, `.`, `.*`, `?:`, `sizeof`, `typeid`.

**Rules:**
- At least one operand must be of user-defined type
- Cannot change arity or precedence
- `=`, `[]`, `()`, `->` must be members

### Templates (Ch. 13, pp. 320–344)
```cpp
template<typename T>
T max(T a, T b) { return (a > b) ? a : b; }

// Usage (type deduced automatically):
max(3, 4);          // T = int
max(3.14, 2.71);    // T = double

// Class template:
template<typename T>
class Stack {
    vector<T> elems;
public:
    void push(const T& t) { elems.push_back(t); }
    T pop() { T t = elems.back(); elems.pop_back(); return t; }
};
Stack<int> si;
Stack<string> ss;
```

---

## 2.4 Input and Output Streams (pp. 345–410)

### The I/O Stream Model (Ch. 21, §21.1)
- **Streams**: `ostream` (output), `istream` (input), `iostream` (both)
- Standard objects: `cout`, `cin`, `cerr`, `clog`
- Operators: `<<` (put to, output), `>>` (get from, input)

### Output (§21.2–21.3)
```cpp
#include <iostream>
using namespace std;

cout << "hello " << name << '\n';
cout << 42;              // integers
cout << 3.14;            // doubles
cout << true;            // bools (0 or 1)
cout << endl;            // flush + newline
cout << '\n';            // newline only (faster)
```

**Formatting:**
```cpp
#include <iomanip>
cout << setw(8) << n;           // field width 8
cout << setprecision(6) << d;   // 6 significant digits
cout << fixed << d;             // fixed-point notation
cout << scientific << d;        // scientific notation
cout << left << setw(10) << s;  // left-aligned
cout << right << setw(10) << s; // right-aligned (default)
cout << setfill('0') << setw(6) << n;  // zero-fill
cout << hex << n;               // hexadecimal
cout << oct << n;               // octal
cout << dec << n;               // decimal (default)
cout << boolalpha << b;         // true/false instead of 1/0
```

### Input (§21.3)
```cpp
int i; double d; string s;
cin >> i;            // read integer
cin >> d;            // read double
cin >> s;            // read whitespace-delimited word
getline(cin, s);     // read entire line including spaces
```
`>>` skips whitespace; `getline` does not.

**State flags:**
- `cin.good()` — no errors
- `cin.fail()` — recoverable error (e.g., non-integer when reading int)
- `cin.bad()` — non-recoverable error
- `cin.eof()` — end of file reached
- `cin.clear()` — reset error state

### File Streams (§21.5)
```cpp
#include <fstream>

// Output file:
ofstream ofs("output.txt");
if (!ofs) cerr << "Cannot open file\n";
ofs << "Hello " << n << '\n';
ofs.close();

// Input file:
ifstream ifs("input.txt");
int x;
while (ifs >> x) { /* process x */ }

// Binary mode:
ofstream binf("data.bin", ios_base::binary);
binf.write(reinterpret_cast<char*>(&obj), sizeof(obj));

ifstream binr("data.bin", ios_base::binary);
binr.read(reinterpret_cast<char*>(&obj), sizeof(obj));
```

**Open modes:**
| Mode | Description |
|------|-------------|
| `ios_base::in` | Open for reading |
| `ios_base::out` | Open for writing |
| `ios_base::app` | Append to end |
| `ios_base::trunc` | Truncate file |
| `ios_base::binary` | Binary mode |

### String Streams (§21.5.3)
```cpp
#include <sstream>

// Write to string:
ostringstream oss;
oss << "Value: " << 42;
string result = oss.str();

// Read from string:
istringstream iss("3.14 hello 42");
double d; string s; int i;
iss >> d >> s >> i;   // d=3.14, s="hello", i=42
```

---

# 3. JAVA PROGRAMMING LANGUAGE
**Source: [3] OCP Oracle Certified Professional Java SE 17 Developer Study Guide**

## 3.1 OOP — Building Blocks (Chapter 1, pp. 1–64)

### Java Environment
- **JDK** (Java Development Kit): `javac` (compiler), `java` (runner), `jar` (packager), `javadoc`
- **JVM** (Java Virtual Machine): runs bytecode (.class files) on any platform
- Java 17 = Long-Term Support (LTS) release

### Class Structure
```java
public class Animal {
    String name;                        // field (instance variable)
    public String getName() { return name; }    // method
    public void setName(String n) { name = n; } // method
}
```
- **Fields**: variables that hold state
- **Methods**: operations on that state
- **Comments**: `// single-line`, `/* multi-line */`, `/** javadoc */`
- Top-level class must match filename; at most one `public` top-level type per file

### Object Creation and Garbage Collection
```java
Animal a = new Animal();    // create object; a is a reference
Animal b = a;               // b points to same object
a = null;                   // a no longer points to the object
```
- Object eligible for garbage collection when no references point to it
- Garbage collector runs automatically; cannot be forced reliably

### Primitive Types
| Type | Size | Range/Description |
|------|------|-------------------|
| `boolean` | 1 bit | `true` or `false` |
| `byte` | 8 bits | −128 to 127 |
| `short` | 16 bits | −32,768 to 32,767 |
| `int` | 32 bits | ~±2 billion |
| `long` | 64 bits | Very large; suffix `L` |
| `float` | 32 bits | Single-precision; suffix `f` |
| `double` | 64 bits | Double-precision |
| `char` | 16 bits | Unicode character `\u0000` to `\uFFFF` |

**Literals:** `1_000_000` (underscores for readability), `0b1101` (binary), `017` (octal), `0xFF` (hex).

**Wrapper classes:** `Integer`, `Long`, `Double`, `Boolean`, `Character`, etc.
- **Autoboxing**: automatic conversion primitive ↔ wrapper: `Integer i = 5; int j = i;`

### Variable Scopes
- **Local**: declared in method/block; must be initialized before use
- **Instance**: declared in class; one per object; initialized to default (0, null, false)
- **Class/static**: declared with `static`; one per class; shared by all instances
- `var` (local variable type inference): `var s = "hello";` — type inferred at compile time

### Text Blocks (Java 13+)
```java
String json = """
              {
                  "name": "Alice"
              }
              """;
```

---

## 3.2 Operators (Chapter 2, pp. 65–100)

### Operator Categories
- **Unary**: `~`, `!`, `++`, `--`, `-`, `+`, `(cast)`
- **Binary arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Shift**: `<<`, `>>`, `>>>` (unsigned right shift)
- **Relational**: `<`, `<=`, `>`, `>=`, `instanceof`
- **Equality**: `==`, `!=`
- **Bitwise**: `&`, `^`, `|`
- **Short-circuit**: `&&`, `||`
- **Ternary**: `? :`
- **Assignment**: `=`, `+=`, `-=`, etc.

**Numeric Promotion Rules:**
1. `byte`/`short`/`char` → `int` before any arithmetic
2. Operands of different types → smaller promotes to larger
3. Arithmetic result: same type as largest promoted operand

**Casting:** required when narrowing (e.g., `double` → `int`): `int i = (int) 3.9;` → 3 (truncation)

**String concatenation:** `+` — if either operand is `String`, both are concatenated as strings: `"a" + 1 + 2 = "a12"` but `1 + 2 + "a" = "3a"`.

---

## 3.3 Making Decisions (Chapter 3, pp. 101–154)

### Pattern Matching for instanceof (Java 16)
```java
if (obj instanceof String s) {
    System.out.println(s.length());  // s is available here
}
```

### Switch Expressions (Java 14+)
```java
// Traditional switch statement:
switch (day) {
    case MONDAY: case FRIDAY: case SUNDAY:
        numLetters = 6; break;
    default: numLetters = -1;
}

// Switch expression (arrow form):
int numLetters = switch (day) {
    case MONDAY, FRIDAY, SUNDAY -> 6;
    case TUESDAY -> 7;
    default -> -1;
};

// Yield in switch expression:
int result = switch (x) {
    case 1 -> 10;
    default -> { yield x * 2; }
};
```

### Loops
```java
// while:
while (condition) { statements; }

// do-while:
do { statements; } while (condition);

// for:
for (int i = 0; i < 10; i++) { statements; }

// enhanced for (for-each):
for (String s : list) { System.out.println(s); }
```

**Labels, break, continue:**
```java
OUTER: for (...) {
    INNER: for (...) {
        break OUTER;      // breaks outer loop
        continue INNER;   // next iteration of inner loop
    }
}
```

---

## 3.4 Methods (Chapter 5, pp. 219–274)

### Method Declaration
```java
public final void nap(int minutes) throws InterruptedException {
    // ...
}
// access_modifier optional_specifier return_type method_name(parameters) throws
```

**Optional specifiers:** `static`, `abstract`, `final`, `synchronized`, `native`, `strictfp`.

### Access Modifiers
| Modifier | Same class | Same package | Subclass | Others |
|----------|-----------|--------------|----------|--------|
| `private` | ✓ | ✗ | ✗ | ✗ |
| package | ✓ | ✓ | ✗ | ✗ |
| `protected` | ✓ | ✓ | ✓ | ✗ |
| `public` | ✓ | ✓ | ✓ | ✓ |

### Varargs
```java
public void walk(int start, int... nums) { }
// Called as: walk(1), walk(1, 2, 3), walk(1, new int[]{2,3})
// Only one vararg per method, must be last parameter
```

### Static vs. Instance Methods
- **Static**: belongs to class; called with `ClassName.method()`; cannot access instance members directly
- **Instance**: needs an object; accessed via object reference

### Overloading
- Same method name, different parameter list (number, types, or order)
- Return type and access modifiers are NOT considered
- Autoboxing, varargs, and type widening apply in overload resolution (in this priority order)

### Pass by Value
Java always passes by **value**. For objects, the value is the **reference** (pointer), not the object itself:
```java
void changeRef(StringBuilder sb) {
    sb = new StringBuilder("new"); // local only; caller's reference unchanged
}
void modifyContent(StringBuilder sb) {
    sb.append(" world"); // modifies the object; caller sees the change
}
```

---

## 3.5 Class Design — Inheritance and Polymorphism (Chapter 6, pp. 275–344)

### Inheritance
```java
public class Animal {
    protected String name;
    public void eat() { System.out.println("Eating"); }
}
public class Dog extends Animal {
    public void bark() { System.out.println("Woof!"); }
}
Dog d = new Dog();
d.eat();    // inherited from Animal
d.bark();   // own method
```
- Java supports **single inheritance** for classes
- All classes implicitly extend `java.lang.Object`
- `final` class cannot be extended; `final` method cannot be overridden

### `this` and `super`
- `this.field` — access instance field (distinguish from local variable)
- `this()` — call another constructor of the same class (must be first statement)
- `super.method()` — call superclass version of a method
- `super()` — call superclass constructor (must be first statement; implicit if omitted)

### Constructors and Initialization Order
1. Static fields/initializers (in order of appearance, once per class load)
2. Instance fields/initializers (in order of appearance, each instantiation)
3. Constructor body

Parent constructors execute before child constructors.

### Overriding Methods
```java
class Animal {
    public String sound() { return "..."; }
}
class Cat extends Animal {
    @Override
    public String sound() { return "Meow"; }  // same signature, same or wider access
}
```
Rules:
- Same method signature (name + parameters)
- Return type must be same or **covariant** (subtype)
- Access modifier cannot be more restrictive
- Cannot throw new or broader checked exceptions

### Hiding Static Methods
Static methods cannot be overridden — they are **hidden**. The version called depends on the reference type, not the object type.

### Abstract Classes and Methods
```java
public abstract class Shape {
    public abstract double area();   // no body
    public void describe() { System.out.println("I am a shape"); } // concrete
}
public class Circle extends Shape {
    private double radius;
    @Override
    public double area() { return Math.PI * radius * radius; }
}
```
- Cannot instantiate an abstract class
- Subclass must implement all abstract methods (or be abstract itself)

### Polymorphism
```java
Animal a = new Dog();   // reference type Animal, object type Dog
a.eat();                // calls Dog.eat() if overridden, otherwise Animal.eat()
// a.bark();            // DOES NOT COMPILE — Animal reference can't see Dog methods
((Dog) a).bark();       // cast required
```
- **Virtual dispatch**: method resolution at runtime based on actual object type
- `instanceof` operator: `if (a instanceof Dog d) { d.bark(); }`

### Immutable Objects
```java
public final class Point {           // final: can't be subclassed
    private final int x;             // final: can't be reassigned
    private final int y;
    public Point(int x, int y) { this.x = x; this.y = y; }
    public int getX() { return x; }
    public int getY() { return y; }
    // No setters!
}
```

---

## 3.6 Beyond Classes — Interfaces, Enums, Records, Sealed Classes (Chapter 7, pp. 345–418)

### Interfaces
```java
public interface Swim {
    int SPEED = 10;             // implicitly public static final
    void swim();                // implicitly public abstract
    default void describe() {   // default method (Java 8+)
        System.out.println("I can swim");
    }
    static void staticHelper() { } // static method (Java 8+)
    private void helper() { }   // private method (Java 9+)
}
public class Dolphin implements Swim {
    @Override
    public void swim() { System.out.println("Splash!"); }
}
```
- A class can implement **multiple interfaces**
- An interface can **extend** multiple interfaces
- All abstract methods must be implemented (or class is abstract)

### Enumerations (`enum`)
```java
public enum Season {
    SPRING, SUMMER, FALL, WINTER;  // enum constants
}
Season s = Season.SUMMER;
s.name();       // "SUMMER"
s.ordinal();    // 1 (0-based index)
Season.values();         // array of all values
Season.valueOf("FALL");  // Season.FALL

// Enum with constructor and fields:
public enum Planet {
    MERCURY(3.303e+23, 2.4397e6),
    VENUS(4.869e+24, 6.0518e6);
    
    private final double mass;
    private final double radius;
    Planet(double mass, double radius) { this.mass = mass; this.radius = radius; }
    double surfaceGravity() { return 6.67300E-11 * mass / (radius * radius); }
}
```
- Enums can have methods, fields, and constructors
- `enum` implicitly extends `java.lang.Enum`; cannot extend another class
- Enum constants are implicitly `public static final`

### Sealed Classes (Java 17)
```java
public sealed class Shape permits Circle, Triangle, Rectangle { }
public final class Circle extends Shape { }
public non-sealed class Triangle extends Shape { }  // can be extended freely
public sealed class Rectangle extends Shape permits Square { }
```
- `sealed` class restricts which classes can extend it
- Permitted classes must be in same package (or same file)
- Each permitted subclass must be `final`, `sealed`, or `non-sealed`

### Records (Java 16)
```java
public record Point(int x, int y) { }
// Automatically provides: constructor, getters x(), y(), toString(), equals(), hashCode()
Point p = new Point(3, 4);
p.x();    // 3
p.y();    // 4
```
- Immutable by default; fields are implicitly `private final`
- Cannot extend another class (but can implement interfaces)
- Can add custom methods and compact constructors

### Nested Classes
- **Static nested class**: `static class Inner { }` — no reference to outer instance
- **Inner class (non-static)**: `class Inner { }` — has reference to outer instance
- **Local class**: defined within a method
- **Anonymous class**: unnamed class defined inline

### Polymorphism with Interfaces
```java
interface Flyable { void fly(); }
class Bird implements Flyable { public void fly() { System.out.println("Flap"); } }

Flyable f = new Bird();  // interface reference
f.fly();                 // calls Bird.fly()
```

### Annotations
Common annotations:
- `@Override` — marks method as overriding superclass; compiler verifies
- `@Deprecated` — marks element as deprecated; generates compiler warning
- `@SuppressWarnings("unchecked")` — suppresses specified compiler warning
- `@FunctionalInterface` — verifies interface has exactly one abstract method
- `@SafeVarargs` — suppresses varargs warnings for generic types

---

## 3.7 Lambdas and Functional Interfaces (Chapter 8, pp. 419–462)

### Lambda Syntax
```java
// Full form:
(Animal a) -> { return a.canHop(); }

// Simplified (one parameter, expression body):
a -> a.canHop()

// No parameters:
() -> System.out.println("Hello")

// Multiple parameters:
(int x, int y) -> x + y
(x, y) -> x + y   // types inferred
```

### Functional Interfaces
An interface with **exactly one abstract method** (can have default/static methods).
`@FunctionalInterface` annotation verifies this.

**Built-in functional interfaces:**

| Interface | Parameters | Return | Abstract Method |
|-----------|-----------|--------|----------------|
| `Supplier<T>` | 0 | T | `T get()` |
| `Consumer<T>` | T | void | `void accept(T)` |
| `BiConsumer<T,U>` | T, U | void | `void accept(T, U)` |
| `Predicate<T>` | T | boolean | `boolean test(T)` |
| `BiPredicate<T,U>` | T, U | boolean | `boolean test(T, U)` |
| `Function<T,R>` | T | R | `R apply(T)` |
| `BiFunction<T,U,R>` | T, U | R | `R apply(T, U)` |
| `UnaryOperator<T>` | T | T | `T apply(T)` |
| `BinaryOperator<T>` | T, T | T | `T apply(T, T)` |
| `Runnable` | 0 | void | `void run()` |

**Primitive variants:** `IntSupplier`, `IntConsumer`, `IntFunction<R>`, `IntPredicate`, `IntUnaryOperator`, `IntBinaryOperator`, etc.

### Method References
```java
// Static method: ClassName::methodName
Function<String,Integer> f = Integer::parseInt;

// Instance method on specific instance: obj::methodName
Consumer<String> c = System.out::println;

// Instance method on arbitrary instance: ClassName::methodName
Function<String,String> upper = String::toUpperCase;

// Constructor: ClassName::new
Supplier<ArrayList> s = ArrayList::new;
```

### Variable Capture
Lambdas can access:
- Their own local variables
- Instance/static variables from enclosing scope
- Effectively final local variables from enclosing scope (cannot be changed after assignment)

---

## 3.8 Collections and Generics (Chapter 9, pp. 463–530)

### Generics
```java
// Generic class:
public class Box<T> {
    private T value;
    public T get() { return value; }
    public void set(T value) { this.value = value; }
}
Box<String> box = new Box<>();

// Generic method:
public <T> T first(List<T> list) { return list.get(0); }

// Bounded type parameter:
public <T extends Comparable<T>> T max(T a, T b) { return a.compareTo(b) > 0 ? a : b; }

// Wildcards:
List<? extends Number> readOnly;   // upper bounded (can read as Number)
List<? super Integer> writeReady;  // lower bounded (can add Integer or subtypes)
List<?> anyList;                   // unbounded wildcard
```

### Java Collections Framework

**List** — ordered, allows duplicates:
```java
List<String> list = new ArrayList<>();    // dynamic array; fast random access
List<String> linked = new LinkedList<>(); // doubly linked; fast insert/delete at ends
list.add("a"); list.add(0, "b");         // add to end or at index
list.get(0); list.set(0, "c");           // get, set
list.remove(0); list.remove("a");        // remove by index or value
list.size(); list.isEmpty();
list.contains("a"); list.indexOf("a");
List.of("a","b","c");  // immutable list (Java 9+)
```

**Set** — no duplicates:
```java
Set<Integer> set = new HashSet<>();       // unordered, O(1) operations
Set<Integer> sorted = new TreeSet<>();    // sorted, O(log n)
Set<Integer> linked = new LinkedHashSet<>(); // insertion-order, O(1)
set.add(1); set.contains(1); set.remove(1);
Set.of(1, 2, 3);   // immutable set
```

**Map** — key-value pairs:
```java
Map<String,Integer> map = new HashMap<>();
Map<String,Integer> sorted = new TreeMap<>();
map.put("a", 1); map.get("a"); map.remove("a");
map.containsKey("a"); map.containsValue(1);
map.getOrDefault("z", 0);
map.putIfAbsent("b", 2);
map.forEach((k, v) -> System.out.println(k + "=" + v));
map.entrySet();  // Set<Map.Entry<K,V>>
map.keySet();    // Set<K>
map.values();    // Collection<V>
Map.of("a", 1, "b", 2);  // immutable map
```

**Queue and Deque:**
```java
Queue<String> q = new LinkedList<>();
q.offer("a");   // add to tail (returns false if full)
q.poll();       // remove from head (returns null if empty)
q.peek();       // view head (null if empty)

Deque<String> d = new ArrayDeque<>();
d.addFirst("a"); d.addLast("b");
d.removeFirst(); d.removeLast();
```

### Sorting and Comparators
```java
// Comparable interface (natural ordering):
class Student implements Comparable<Student> {
    public int compareTo(Student other) { return name.compareTo(other.name); }
}

// Comparator (custom ordering):
Comparator<Student> byAge = (s1, s2) -> s1.age - s2.age;
Comparator<Student> comp = Comparator.comparing(Student::getName)
                                     .thenComparingInt(Student::getAge)
                                     .reversed();

Collections.sort(list, comp);
list.sort(comp);
Arrays.sort(arr);
```

### Collections Utility Methods
```java
Collections.sort(list);
Collections.reverse(list);
Collections.shuffle(list);
Collections.min(list); Collections.max(list);
Collections.frequency(list, obj);
Collections.unmodifiableList(list);  // read-only view
```

---

## 3.9 Streams (Chapter 10, pp. 531–590)

### Creating Streams
```java
Stream<String> empty = Stream.empty();
Stream<Integer> oneEl = Stream.of(1);
Stream<String> from = Stream.of("a", "b", "c");
Stream<String> fromList = list.stream();
Stream<String> fromList2 = list.parallelStream();  // parallel processing
Stream<Integer> infinite = Stream.iterate(0, n -> n + 1);   // infinite
Stream<Double> random = Stream.generate(Math::random);       // infinite
```

**Primitive streams:** `IntStream`, `LongStream`, `DoubleStream` (avoid boxing overhead):
```java
IntStream range = IntStream.range(1, 10);       // 1..9
IntStream closed = IntStream.rangeClosed(1, 10); // 1..10
```

### Intermediate Operations (return Stream, lazy):
```java
stream.filter(s -> s.startsWith("a"))   // Predicate<T>
      .map(String::toUpperCase)          // Function<T,R>
      .flatMap(s -> Stream.of(s.split(""))) // Function<T,Stream<R>>
      .sorted()                          // natural order
      .sorted(Comparator.reverseOrder()) // custom order
      .distinct()                        // remove duplicates
      .limit(5)                          // at most 5 elements
      .skip(3)                           // skip first 3
      .peek(System.out::println);        // for debugging; doesn't modify stream
```

### Terminal Operations (consume stream):
```java
stream.count()                    // long: count elements
stream.min(comparator)            // Optional<T>
stream.max(comparator)            // Optional<T>
stream.findFirst()                // Optional<T>: first element
stream.findAny()                  // Optional<T>: any element (good for parallel)
stream.anyMatch(predicate)        // boolean
stream.allMatch(predicate)        // boolean
stream.noneMatch(predicate)       // boolean
stream.forEach(System.out::println)  // consume each
stream.reduce(0, Integer::sum)    // fold: sum of elements
stream.collect(Collectors.toList())  // collect to List
stream.toList()                   // Java 16+: immutable List
```

### Collectors
```java
import java.util.stream.Collectors;

list.stream().collect(Collectors.toList());
list.stream().collect(Collectors.toSet());
list.stream().collect(Collectors.toMap(Student::getName, s -> s));
list.stream().collect(Collectors.joining(", ", "[", "]")); // String
list.stream().collect(Collectors.groupingBy(Student::getMajor)); // Map<K,List<V>>
list.stream().collect(Collectors.counting());
list.stream().collect(Collectors.averagingInt(Student::getAge));
list.stream().collect(Collectors.partitioningBy(s -> s.getAge() > 18)); // Map<Boolean,List>
```

### Optional
```java
Optional<String> opt = Optional.of("hello");
Optional<String> empty = Optional.empty();
Optional<String> maybe = Optional.ofNullable(nullableValue);

opt.isPresent();         // true
opt.get();               // "hello" (throws if empty)
opt.orElse("default");   // value or default
opt.orElseGet(() -> computeDefault());
opt.orElseThrow();       // throws NoSuchElementException if empty
opt.ifPresent(System.out::println);
opt.map(String::toUpperCase);  // Optional<String>
opt.filter(s -> s.length() > 3); // Optional<String>
```

---

## 3.10 Exceptions (Chapter 11, pp. 591–623)

### Exception Hierarchy
```
java.lang.Throwable
├── java.lang.Error          (unchecked — do not catch; e.g., OutOfMemoryError)
└── java.lang.Exception
    ├── java.lang.RuntimeException  (unchecked — no need to declare or catch)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   ├── IllegalArgumentException
    │   ├── NumberFormatException
    │   ├── ClassCastException
    │   └── ArithmeticException
    └── (checked exceptions — must handle or declare)
        ├── IOException
        ├── SQLException
        ├── ParseException
        └── InterruptedException
```

### Handling Exceptions
```java
try {
    // code that might throw
    int[] arr = new int[5];
    arr[10] = 3;             // throws ArrayIndexOutOfBoundsException
} catch (ArrayIndexOutOfBoundsException e) {
    System.err.println("Error: " + e.getMessage());
} catch (RuntimeException | IOException e) {  // multi-catch (Java 7+)
    e.printStackTrace();
} finally {
    // always executes; used for cleanup
    // Note: finally runs even if catch throws or has return!
}
```

**try-with-resources (Java 7+):**
```java
try (FileInputStream fis = new FileInputStream("f.txt");
     BufferedReader br = new BufferedReader(new InputStreamReader(fis))) {
    // use fis and br; automatically closed (in reverse order) when done
    String line = br.readLine();
} catch (IOException e) {
    e.printStackTrace();
}
// Class must implement AutoCloseable (or Closeable)
```

### Declaring and Throwing Exceptions
```java
// Declare: method may throw checked exception:
void readFile(String name) throws IOException {
    throw new IOException("File not found");  // explicitly throw
}

// Custom exception:
public class AppException extends RuntimeException {
    public AppException(String message) { super(message); }
    public AppException(String message, Throwable cause) { super(message, cause); }
}

// Rethrowing / chaining:
try {
    risky();
} catch (IOException e) {
    throw new AppException("Wrapped IO error", e);  // preserve cause
}
```

### Checked vs Unchecked — Handle or Declare Rule
- **Checked exceptions**: compiler forces you to either `catch` them or `throws` them in method signature
- **Unchecked exceptions** (`RuntimeException` and `Error` subclasses): no compiler enforcement
- `finally` block: runs after try/catch regardless; useful for resource cleanup
- **Suppressed exceptions**: if `finally` throws, it masks the original exception; try-with-resources handles this automatically via `getSuppressed()`

### Common Exceptions Reference
| Exception | When thrown |
|-----------|-------------|
| `NullPointerException` | Accessing member on null reference |
| `ArrayIndexOutOfBoundsException` | Array index < 0 or ≥ length |
| `StringIndexOutOfBoundsException` | String index out of bounds |
| `ClassCastException` | Invalid cast (e.g., `(Dog) cat`) |
| `NumberFormatException` | `Integer.parseInt("abc")` |
| `IllegalArgumentException` | Method called with invalid argument |
| `IllegalStateException` | Method called at invalid time |
| `ArithmeticException` | e.g., integer division by zero |
| `StackOverflowError` | Infinite recursion |
| `OutOfMemoryError` | JVM runs out of heap memory |

---

## 3.11 Byte/Char Streams and I/O (Chapter 14, pp. 661+)

### File Path Operations
```java
import java.io.*;
import java.nio.file.*;

// java.io.File (legacy):
File f = new File("data.txt");
f.exists(); f.isDirectory(); f.isFile();
f.length(); f.lastModified();
f.delete(); f.mkdir(); f.mkdirs();
f.listFiles();  // contents of directory

// java.nio.Path (modern):
Path p = Path.of("data.txt");
Path abs = p.toAbsolutePath();
Files.exists(p); Files.isDirectory(p);
Files.size(p); Files.delete(p);
Files.copy(src, dest, StandardCopyOption.REPLACE_EXISTING);
Files.move(src, dest);
Files.createDirectory(p);
Files.createDirectories(p);
```

### Byte Streams (binary data)
```java
// Input:
try (InputStream is = new FileInputStream("file.bin")) {
    int b = is.read();               // read 1 byte (-1 = EOF)
    byte[] buf = new byte[1024];
    int n = is.read(buf);            // read up to 1024 bytes
}

// Output:
try (OutputStream os = new FileOutputStream("out.bin")) {
    os.write(65);                    // write 1 byte
    os.write(new byte[]{1,2,3});     // write byte array
}

// Buffering for performance:
InputStream buffered = new BufferedInputStream(new FileInputStream("f"));
OutputStream bOut = new BufferedOutputStream(new FileOutputStream("f"));

// Data streams (primitive types):
DataInputStream dis = new DataInputStream(new FileInputStream("f"));
int i = dis.readInt();
double d = dis.readDouble();

// Object serialization:
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("f"));
oos.writeObject(myObject);  // class must implement Serializable
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("f"));
MyClass obj = (MyClass) ois.readObject();
```

### Character Streams (text data)
```java
// Reading text:
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
}

// Writing text:
try (PrintWriter pw = new PrintWriter(new FileWriter("out.txt"))) {
    pw.println("Hello");
    pw.printf("Value: %d%n", 42);
}

// NIO.2 convenience methods:
List<String> lines = Files.readAllLines(Path.of("file.txt"));
String content = Files.readString(Path.of("file.txt"));         // Java 11+
Files.write(Path.of("out.txt"), lines);
Files.writeString(Path.of("out.txt"), "content");               // Java 11+
// Stream of lines (lazy):
try (Stream<String> s = Files.lines(Path.of("file.txt"))) {
    s.filter(l -> l.contains("error")).forEach(System.out::println);
}
```

---

# 4. FREQUENT EXAM TOPICS — ADDITIONS

## 4.1 `memset` and `memcpy` (C — `<string.h>`)

```c
#include <string.h>

// memset — fill memory with a constant byte:
void *memset(void *ptr, int value, size_t n);
// Sets n bytes starting at ptr to the byte value (only low 8 bits of value used)

char buf[100];
memset(buf, 0, sizeof(buf));       // zero out entire buffer
memset(buf, 'A', 10);              // fill first 10 bytes with 'A'

int arr[10];
memset(arr, 0, sizeof(arr));       // zero int array (works for 0)
// memset(arr, 1, sizeof(arr));    // WRONG for ints — sets each byte to 1, not each int!

// memcpy — copy n bytes from src to dst (no overlap guarantee):
void *memcpy(void *dst, const void *src, size_t n);

char src[] = "hello";
char dst[10];
memcpy(dst, src, strlen(src) + 1);  // copy including '\0'

struct Point { int x, y; };
struct Point a = {1, 2}, b;
memcpy(&b, &a, sizeof(a));  // copy struct

// memmove — like memcpy but handles overlapping regions:
void *memmove(void *dst, const void *src, size_t n);
memmove(buf + 2, buf, 5);  // shift right by 2 (overlapping — safe)

// memcmp — compare n bytes:
int memcmp(const void *s1, const void *s2, size_t n);
// Returns 0 if equal, <0 if s1 < s2, >0 if s1 > s2
```

**Key differences from string functions:**
- `mem*` functions work on raw bytes — they do NOT stop at `'\0'`
- `memset(arr, 0, sizeof(arr))` is the standard way to zero an array
- `memcpy` is faster than element-by-element copying for large data

---

## 4.2 `std::string` in C++ (STL)

```cpp
#include <string>
using namespace std;

// Construction:
string s1 = "hello";
string s2("world");
string s3(5, 'x');         // "xxxxx"
string s4 = s1 + " " + s2; // "hello world"

// Common methods:
s1.length();               // or s1.size() — number of characters
s1.empty();                // true if length == 0
s1[0];                     // character access (no bounds check)
s1.at(0);                  // with bounds check (throws std::out_of_range)
s1.front();                // first character
s1.back();                 // last character

s1.append(" world");       // or: s1 += " world"
s1.substr(1, 3);           // substring: start=1, length=3 → "ell"
s1.find("ll");             // position of first "ll" (string::npos if not found)
s1.rfind("l");             // last occurrence
s1.replace(0, 5, "bye");   // replace chars 0..4 with "bye"
s1.erase(2, 3);            // remove 3 chars starting at index 2
s1.insert(2, "XY");        // insert "XY" at position 2

// Comparison (lexicographic):
s1 == s2;  s1 < s2;  s1.compare(s2);  // 0 if equal

// Conversion:
int i = stoi("42");              // string → int
double d = stod("3.14");         // string → double
string str = to_string(42);      // int → string

// C-string interop:
const char* cs = s1.c_str();    // get C-string pointer (null-terminated)
string fromC(cs);                // construct from C-string

// Iteration:
for (char c : s1) cout << c;
for (size_t i = 0; i < s1.size(); i++) cout << s1[i];
```

---

## 4.3 Conversion Constructors in C++

A constructor with **one argument** (or all arguments with defaults except one) acts as an **implicit conversion constructor**:

```cpp
class MyInt {
    int val;
public:
    MyInt(int v) : val(v) {}     // conversion constructor: int → MyInt
    int get() const { return val; }
};

MyInt a = 5;      // implicit conversion: calls MyInt(5)
MyInt b(10);      // explicit construction
// MyInt c = 3.7; // also works: double → int → MyInt (with narrowing warning)

// Implicit conversion in function call:
void display(MyInt m) { cout << m.get(); }
display(42);  // implicitly converts 42 to MyInt(42)

// Preventing implicit conversion with 'explicit':
class Safe {
    int val;
public:
    explicit Safe(int v) : val(v) {}
};

Safe s1(5);      // OK — direct initialization
// Safe s2 = 5; // ERROR — implicit conversion disabled
// display_safe(42);  // ERROR if display_safe takes Safe by value
```

**Practical example — class with pointer (deep copy):**
```cpp
class String {
    char* data;
    int len;
public:
    String(const char* s = "") {          // conversion + default constructor
        len = strlen(s);
        data = new char[len + 1];
        strcpy(data, s);
    }
    String(const String& other) {         // copy constructor (deep copy!)
        len = other.len;
        data = new char[len + 1];
        strcpy(data, other.data);
    }
    String& operator=(const String& other) {  // assignment operator
        if (this != &other) {
            delete[] data;
            len = other.len;
            data = new char[len + 1];
            strcpy(data, other.data);
        }
        return *this;
    }
    ~String() { delete[] data; }
};

String s1 = "hello";   // calls String(const char*) — conversion constructor
String s2 = s1;        // calls copy constructor
```

---

## 4.4 Little-Endian and Byte Casting in C

**Endianness** refers to the byte order used to store multi-byte values in memory.

- **Little-Endian** (x86, most modern CPUs): least significant byte stored first (at lowest address)
- **Big-Endian** (network byte order, some RISC): most significant byte stored first

```c
int x = 0x12345678;
// In memory on Little-Endian:
// Address: [0]    [1]    [2]    [3]
// Value:   0x78   0x56   0x34   0x12   (LSB first!)

// Accessing individual bytes via cast:
char *p = (char *)&x;
printf("%02X\n", (unsigned char)p[0]);  // 0x78 — least significant byte
printf("%02X\n", (unsigned char)p[1]);  // 0x56
printf("%02X\n", (unsigned char)p[2]);  // 0x34
printf("%02X\n", (unsigned char)p[3]);  // 0x12 — most significant byte

// (char) cast of an int extracts the LEAST SIGNIFICANT BYTE:
int n = 0x414243;   // = 4276547
char c = (char)n;   // c = 0x43 = 'C'  (NOT 'A'!)

// Detecting endianness at runtime:
int test = 1;
if (*(char *)&test == 1)
    printf("Little-Endian\n");
else
    printf("Big-Endian\n");
```

**Key exam point:** On a Little-Endian system, `(char)int_value` extracts the **least significant byte** (the last 8 bits), NOT the first/most significant byte.

---

## 4.5 Java `Scanner` Class

`Scanner` is the standard class for reading input from console, files, or strings in Java.

```java
import java.util.Scanner;
import java.io.*;

// Reading from console (stdin):
Scanner sc = new Scanner(System.in);

int i = sc.nextInt();           // read next integer
double d = sc.nextDouble();     // read next double
String word = sc.next();        // read next whitespace-delimited token
String line = sc.nextLine();    // read entire line (including spaces)
boolean b = sc.nextBoolean();   // read "true"/"false"

// Checking before reading (avoid exceptions):
if (sc.hasNextInt()) {
    int n = sc.nextInt();
}
while (sc.hasNextLine()) {
    String l = sc.nextLine();
    System.out.println(l);
}

// Common pitfall — mixing nextInt() with nextLine():
int n = sc.nextInt();
sc.nextLine();       // consume the leftover '\n' after the int!
String s = sc.nextLine();  // now reads the actual next line

// Reading from a file:
try (Scanner fileSc = new Scanner(new File("data.txt"))) {
    while (fileSc.hasNextLine()) {
        System.out.println(fileSc.nextLine());
    }
} catch (FileNotFoundException e) {
    e.printStackTrace();
}

// Reading from a string:
Scanner strSc = new Scanner("10 3.14 hello");
int num = strSc.nextInt();      // 10
double dbl = strSc.nextDouble(); // 3.14
String str = strSc.next();       // "hello"

// Custom delimiter:
Scanner csv = new Scanner("a,b,c,d");
csv.useDelimiter(",");
while (csv.hasNext()) {
    System.out.print(csv.next() + " ");  // a b c d
}

sc.close();  // close when done
```

**Scanner vs. BufferedReader:**
| | `Scanner` | `BufferedReader` |
|---|---|---|
| Parsing | Built-in (`nextInt`, `nextDouble`) | Manual (`Integer.parseInt`) |
| Speed | Slower | Faster |
| Use case | Console input, simple parsing | Large file reading |

---

*Summary created from the exact page ranges specified in the CSIE4 Master Exam bibliography, ASE Bucharest 2025–2026.*

*Coverage: K&R C (pp. 35–190), Stroustrup C++ 3rd Ed. (pp. 59–132, 255–410), OCP Java SE 17 Study Guide (pp. 1–623).*
