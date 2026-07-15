# CSIE4 Master Admission Exam Solutions - ASE Bucharest

## Exam 2024

### Question 1
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h>
#include <string.h>
void fot(char *s1, char *s2, int idx)
{
int min length. = (strlen (31) < strlen(s2)) ? strlen({sl) 
: strlen(s2);
if Gdx 
< (int)strien(sl) &&
idx < (int) strlen (s2))
Li
char temp = sl[idx];
si{idx] = s2i(nin length - 1) - idx];
s2[(min_length - 1) - idx] = temp;
fet(si, s2, idx + 1);
}
int main()
‘ 
char stringi(ij = "ABCD";
char string2[] = "ABC";
fotistringl, string2, 0);
printf (“stringi = %s, string2 = ss\n", stringl, string2):
return 0;
)
```

**Options:**
- a. string1 = DCBA, string2 = CBA
- b. string! = ABCD, string2 = CBA
- c. string = CBAD, string2 = CBA
- d. string! = DCBA, string2 = ABC


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) string = CBAD, string2 = CBA**

</details>
---

### Question 2
**Requirement:** What will be the output of the below C application?

```c
#include <stdio.h>
#include <string.h>
int main)
{
char a[] = ( (At, 'B', 0, "CI;
chart pa = NULL;
pa = a;
printf ("array size = 5u, string length = $u\n",
{unsigned int)sizeof(a), (unsigned int) strlen(pa});

Admitere: Studii universitare da masterat — lulie 2024
return O;
```

**Options:**
- a. array size = 3, string length = 2
- b. array size = 4, string length =4
- c. array size = 4, string length = 2
- d. array size = 2, string length = 2


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) array size = 4, string length = 2**

</details>
---

### Question 3
**Requirement:** What will be the output when the below C application will run?

```c
#include <stdio.h>
int main()
{
int x = 2, y = 3;
int *px = NULL, *py = NULL?
px = &x;
py = ay;
*px += 3;
*py += 5;
int m= x * *px 
< y * *py 
? *px : *py7
printf("\'im = ta\'\n", m);
return 0;
}
```

**Options:**
- a. ‘m=
- b. m=5
- c. m=8
- d. 'm=5%


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) m=8**

</details>
---

### Question 4
**Requirement:** What will be the output when the below C application will run?

```c
#include <stdio.h>
fdefine 
COMP(A, B) 
(A * 3 > (B) ? (A) 
: 
(B))
int main)
‘ 
int x= 3, y= 3, <= 10, t = 5;
printé ("result = %d\n", COMP(x + y, 2 + t));
return 0;

Facultatea; CIBERNETICĂ, STATISTICĂ ŞI INFORMATICĂ ECONOMICĂ
```

**Options:**
- a. result = 6
- b. result = 18
- c. result = 15
- d. result = 10


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) result = 15**

</details>
---

### Question 5
**Requirement:** What will be the output of the following C application?

```c
fineclude <stdio.h>
unsigned char fet (unsigned short int x)
{
unsigned char b = 0, i;
for (i = 0; i < sizeof(x); i++)
if (x & 0)
bit;
return b;
int main()
unsigned short int n = 21;
unsigned char result = fet(n);
printf ("result = ‘hhu\n", result);
return 0;
}
```

**Options:**
- a. result = 3
- b. result = 0
- c. result =4
- d. result = -4


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) result = 0**

</details>
---

### Question 6
**Requirement:** What will be the output of the below C application?

```c
f#ineluda <stdio.h>
aint main)
‘ 
char at] = ( At, 0, "BY, 'G', NOt}?
int* pa = NUL;
pa = (int*)a;
printf("%s\n", (char*)pa);
xeturn 0;

CSIE4b2
aA
```

**Options:**
- b. AOBCO
- c. ABC
- d. BC


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) *(see original PDF)***

</details>
---

### Question 7
**Requirement:** What.will be the output when the below C application will run?

```c
#include <stdio.h>
#include <malloc.h>
void f(int** x)
i
int t = *%*x;
*x = ({int*)malloc (sizeof (int)) ;
LE (*x)
{
key = t + 10;
}
)
int main
{
int a = 65;
int pa = &a;
f (spa):
printf("*pa = td\n", *pa);
free (pa) ;
raturn 0;
}
```

**Options:**
- a. *pa=0
- b. *pa = 75
- c. *pa = 10
- d. *pa= 65


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) *pa = 75**

</details>
---

### Question 8
**Requirement:** What will be the output when the below C application will run?

```c
#include <stdio.h>
int main)
{
CTA, UB, tc;
NULL, *p2a = NULL;
pa za + 2;
p2a = pa - 1;
printf ("*pa = tc, *p2a = ton", *pa, *p2a);
return 0;
```

**Options:**
- a. *pa = C, *p2a = B
- b. *pa = 8, *p2a = A
- c. *pa = C, *p2a = C
- d. *pa =A, *p2a=C


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) *pa = C, *p2a = B**

</details>
---

### Question 9
**Requirement:** Consider the following content saved into a file named Points. txt:

```c
Îi 
~3,+2,4,3

3,4,-1,-3
```

**Options:**
- a. ditf_x = 7, diff_y=5 diff_x= 4, diff_y = 4
- b. diff_x = 7, diff_y=7 diff_x = 4, diff_y = 4 [vă diff_X = 5, diff_y=5 diff x =4, diff. y=7
- d. diff_x=7, diff_y=5 diff_x=4, diff_y=7


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) diff_x=7, diff_y=5 diff_x=4, diff_y=7**

</details>
---

### Question 10
**Requirement:** What will be the output when the below C application will run?

```c
#include. <stdio.h>
#include <stdlib.h>
int main()
i
char al] = 4 t=", 121, 121, "NO", 13, 1001 3;
printi ("sdin", atoi(a));
return 0;
}
```

**Options:**
- a. -12
- b. -123 ¢, -12030
- d. -123.0


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) -12**

</details>
---

### Question 11
**Requirement:** What will be the output of the following C++ program?

```cpp
#include <iostream>
tincluda <string>
using namespace std;
class Car
{
publica:
string producer = "Dacia";
ye
int main()
{
Car a;
Cart pe = &a;
cout << pe->producer;
return 9;
```

**Options:**
- a. runtime error
- b. Dacia
- c. an empty string
- d. compile error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) compile error**

</details>
---

### Question 12
**Requirement:** What is the main reason why the overloading of the >> operator for reading information

```sql
from the console needs to be done using a friend function and not a method?
```

**Options:**
- a. because this is a unary operator
- b. because the first operand is not the same type as the class
- c. in order to get access to the private attributes of the class
- d. in order for the operator to accept chained calls


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) because the first operand is not the same type as the class**

</details>
---

### Question 13
**Requirement:** What will be the output of the following C++ program?

```cpp
##include <iostream>
using namespace std;
class Foo {
public:
Foot) 1)
Foo{const Fook f) 
{
cout << nu;
}
Foo operator=(Foo f) 
[|
cout << "ar;
return. tthis;
}
he
int main) 
{
Foo f, f3;
Foo f2 = f;
f3 = f2;
}
```

**Options:**
- a. #@
- b. HO
- c. to
- d. @@


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) to**

</details>
---

### Question 14
**Requirement:** What will be the output of the following C++ code sequence?

```cpp
Hincluda <iostream>
using namespace std;
class Foo { public: int x = 123; };
int main()
{
Foo f;
Foot pf = &f;
fix = 456;
cout << pf->x;
}
```

**Options:**
- a. the address of f
- b. 456
- c. 123
- d. the address of x


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) 456**

</details>
---

### Question 15
**Requirement:** Taking into consideration the following C++ code, what will be the message printed to the

```cpp
console?
#include <iostream>
class one
{
int x, y; void f0) 
{}
yi
class Two {
int a, b; virtual void f() 
{)}
yi
int main)
{
std::cout << (sizeof (Two) > sizeof(One) ? "Yes : Not);
return 0;
}
```

**Options:**
- a. Yes
- b. 0
- c. No
- d. YesNo


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Yes**

</details>
---

### Question 16
**Requirement:** What will the following C++ code print?

```cpp
##include <iostream>
using namespace std;
class Base {
public:
virtual void show{) 
{

cout << "Base << endl;
class Derived : public Base 
|
public:
void show{) 
{
cout << "Derived" << endl;
}
```

**Options:**
- a. Derived
- b. Base
- c. BaseDerived
- d. it will generate a runtime error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Derived**

</details>
---

### Question 17
**Requirement:** Giving the C++ class 5 from below and assuming that we have included the necessary classes

```cpp
and libraries, what will be the output of the main function?
class §
{
public:
string name;
chart operatori] {int i) 
{
return name[{i];
}
ye
int main {}
{
ss;
s.name =. "ABC;
s[O] = ‘ct;
cout << s(1]:
return 0;
}
```

**Options:**
- a. B
- b. compile error GA
- d. C


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) B**

</details>
---

### Question 18
**Requirement:** Assuming that B is a valid C++ class, what operator(s) could be called in the second line of

```cpp
code frorn the main function?

int main()
i
Bb;
```

**Options:**
- a. only the subtraction operator
- b. only the copy constructor
- c. subtraction operator or explicit cast
- d. subtraction operator or implicit cast


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) subtraction operator or implicit cast**

</details>
---

### Question 19
**Requirement:** Giving the C++ classes from below and assuming that we have included the necessary

```cpp
classes and libraries, what will be the output when the main function is executed?
class Base [
public:
Base() i
cout << "At;
}
“Basei) 
|
cout << "Br;
}
y:
class Derived : public Base {
public:
Derived() 
{
cout << "XK";
}
~Derived() 
(
cout << pu;

hi
int main) 
{
Basa *b = new Derived();
delete b;
return 0;
}
```

**Options:**
- a. AXYB
- b. AXB
- c. XAYB
- d. ABXY


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) AXB**

</details>
---

### Question 20
**Requirement:** What will be the output of the next C++ program?

```cpp
#include <iostream>
using namespace std;

Facultatea; CIBERNETICĂ, STATISTICĂ ŞI INFORMATICĂ ECONOMICĂ
class Foo
{
public:
virtual int f4) 
{ return 100; 
}
int gQ 
{ return 500; 
}
de
glass Boo 
: public Foo
{
public:
int f0 { return 200; 
}
int 9) { return 600; }
yi
int main)

Foot x = new Boot);
cout << x->f{) << x->g();
return 0;
)
```

**Options:**
- a. 100600
- b. 200500
- c. 100500
- d. 200600


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) 200500**

</details>
---

### Question 21
**Requirement:** Can an Oracle SQL select statement directly call a PL/SQL function?

**Options:**
- a. Only if the function doesn't alter the tablespace
- b. No, never
- c. Yes, if certain conditions are met
- d. Only if the function is in another schema


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) Yes, if certain conditions are met**

</details>
---

### Question 22
**Requirement:** What distinguishes a correlated subquery from a non-correlated subquery in SQL?

**Options:**
- a. The execution frequency of the subquery depends on the total number of rows in the database table
- b. A correlated subquery is executed once for each row processed by the outer query
- c. A correlated subquery does not have access to data from the outer query
- d. A correlated subquery can only be used with SELECT statements


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) A correlated subquery is executed once for each row processed by the outer query**

</details>
---

### Question 23
**Requirement:** Which of the following functions can be used with an assignment operator in a PL/SQL

```c
statement?
```

**Options:**
- a. COUNT
- b. SUM
- c. NVL
- d. MAX Şi


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) NVL**

</details>
---

### Question 24
**Requirement:** Consider the tables Customers (columns: Customer_ID, cust_last_name) and Orders

```sql
(columns: Order_ID, Customer_ID, Order_date).
Given the query:
SELECT cust last _name
FROM Customers join Orders on Customers .Customer ID = Orders .Customer ID
ORDER BY count (Order date) DESC;
What will happen if you try to run the query?
```

**Options:**
- a. The query will run successfully and return the last name of the customer with the highest Customer_ID
- b. The query will fail
- c. The query will run successfully and return the last names of customers in descending order of thelr total orders number
- d. The query will run successfully and return the last name of the customer who has placed the most recent order


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) The query will fail**

</details>
---

### Question 25
**Requirement:** The ALTER TABLE statement in SQL can be used to:

**Options:**
- a. Create a new table
- b. Add a constraint to an existing table
- c. insert data into the table
- d. Update a row from the table


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) Add a constraint to an existing table**

</details>
---

### Question 26
**Requirement:** Consider the following PL/SQL block:

```sql
declare
cursor a is select * from employees;
begin
open e;
for r în c loop
null
end ledp;
close e:
end;

The employees table exists and has the following columns: employee_id, first_name,
last_name and hire_date, Which of the following statements is true?
```

**Options:**
- a. The block will raise an exception only if the employees table is empty
- b. The block will not compile
- c. The block will run successfully
- d. The block will always raise an exception


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) The block will not compile**

</details>
---

### Question 27
**Requirement:** What is the purpose of the PRIMARY KEY constraint in SQL Oracle?

**Options:**
- a. It ensures that the values in a column or group of columns match a list of specific values
- b. It ensures that all values în a column or group of columns are different, and it cannot be left empty
- c. It ensures that all values in a column or group af columns are the same
- d. It ensures that a column or group of columns has values, and it cannot be left empty


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) It ensures that all values în a column or group of columns are different, and it cannot be left empty**

</details>
---

### Question 28
**Requirement:** Consider the following two tables:

```sql
Customers
CustomerID 
| 
CustomerName 
| 
ContactNumber

{ 
Doe 
| 
555-1234

| 
Smith 
| 
555-2345

| 
Johnson 
| 
555-3456

| 
Davis 
| 
555-4567
Orders
OrderID 
| 
CustomerID 
| 
Product
1] 1 
| Applies

|! 

| 
Bananas

| 

| 
Grapes

| 

| 
Granges
Given these two tables, what will be the result of the following SQL query?
SELECT Customers.CustomerName, Orders. Product
FROM Customers
RIGHT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;
```

**Options:**
- a. A list of all customer ids who have placed orders, along with the product for each order they have placed
- b. A list of all customers, with each customer’s name listed only once, along with the product for each order they have placed, and NULL for customers who have not placed any orders
- c. A list of all customers, with each customer's name listed once, along with a list of all products, regardless of whether the customer has placed an order or not
- d. A list of all customers, with each customer's name possibly listed more than once, along with the product for each order they have placed, but no entries for customers who have not placed any orders


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) A list of all customers, with each customer's name possibly listed more than once, along with the product for each order they have placed, but no entries for customers who have not placed any orders**

</details>
---

### Question 29
**Requirement:** Can a procedure in PL/SQL call a function?

**Options:**
- a. Only if the procedure and function access the same tables
- b. Yes
- c. No, never
- d. Only if the function doesn't modify the database


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) Yes**

</details>
---

### Question 30
**Requirement:** The employees table exists has the following columns: employee_id, first_name, last_name

```sql
and hire_date and 50 rows. Given the Oracle SQL statement:
select 50 from employeas where 1=20;
Which of the following statements is true:
```

**Options:**
- a. CSIE 1 O CSIE 2 CSIE 3 CSIE 5 CIG1 CIG2 ij O O O ch aici m 20 x Sp = dop DAI ETAI EAMI FINI MANI MKI O ce) Ci a] | al O 9% O O O
- b. The statement does not run as there is no column 20
- c. The statement runs successfully and displays no rows
- d. The statement runs successfully and displays some values = Z O O O O O @ O O O o
- e. O MEK2 REII Oo a © © O O o O O O o O O O O O O O o O REI2 REI5 MD OO


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) The statement runs successfully and displays no rows**

</details>
---

## Exam 2023

### Question 1
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h> 
 
unsigned char fct(unsigned short int x) 
{ 
    unsigned char b = 0, i, *px; 
    px = (unsigned char*)&x; 
 
    for (i = 0; i < sizeof(x); i++) 
        if (px[i] & 0x01) 
            b++; 
    return b; 
} 
 
int main() 
{ 
    unsigned short int n = 127; 
 
    unsigned char result = fct(n); 
    printf("result = %hhu\n", result); 
 
    return 0; 
}
```

**Options:**
- a. result = 3
- b. result = 1
- c. result = 4
- d. result = 127


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) result = 1**

</details>
---

### Question 2
**Requirement:** What will be the output when the below C application will run?

```c
#include <stdio.h> 
 
int main() 
{ 
 
char a[] = { 'A', 'B', 'C'}; 
 
char *pa = NULL, *p2a = NULL; 
 
 
pa = a + 1; 
 
p2a = a + 2; 
 
printf("*pa = %c, *p2a = %c\n", *pa, *p2a); 
 
 
return 0; 
}
```

**Options:**
- a. *pa = B, *p2a = C
- b. *pa = B, *p2a = B
- c. *pa = C, *p2a = B
- d. *pa = C, *p2a = C


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) *pa = B, *p2a = C**

</details>
---

### Question 3
**Requirement:** What will be the output of the below C application?

```c
#include <stdio.h> 
#include <string.h> 
 
int main() 
{ 
 
char a[] = { 'A', 0x00, 'B', 0x00, 'C', 0x00}; 
 
char* pa = NULL; 
 
 
pa = a; 
 
 
printf("array size = %u, string length = %u\n",  
 
 
    (unsigned int)sizeof(a), (unsigned int)strlen(pa)); 
 
 
return 0; 
}
```

**Options:**
- a. array size = 3, string length = 3
- b. array size = 6, string length = 1
- c. array size = 1, string length = 3
- d. array size = 2, string length = 1


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) array size = 6, string length = 1**

</details>
---

### Question 4
**Requirement:** What will be the output of the below C application?

```c
#include <stdio.h> 
 
int main() 
{ 
 
char a[] = { 'A', 'B', 'C', 0, '\0'}; 
 
int* pa = NULL; 
 
 
pa = (int*)a; 
 
 
printf("%s\n", (char*)pa); 
 
 
return 0; 
}
```

**Options:**
- a. ABC
- b. ABC0
- c. ABC00
- d. ABC\0


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) ABC**

</details>
---

### Question 5
**Requirement:** What will be the output when the below C application will run?

```c
#include <stdio.h> 
#include <stdlib.h> 

int main() 
{ 
 
char a[] = { '-', '1', '2', 0, '.', '3', '4', 0 }; 
 
 
printf("%.2f\n", (float)atof(a + 4)); 
 
 
return 0; 
}
```

**Options:**
- a. -12.00
- b. -120.34
- c. 0.34
- d. -120.00


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) 0.34**

</details>
---

### Question 6
**Requirement:** What will be the output when the below C application will run?

```c
#include <stdio.h> 
#include <malloc.h> 
 
void f(int* x) 
{ 
 
x[0] = 10; 
} 
 
int main() 
{ 
 
int a = 65; 
 
int *pa = &a; 
 
 
pa = (int*)malloc(sizeof(int)); 
 
 
f(pa); 
 
printf("*pa = %d\n", *pa); 
 
 
free(pa); 
 
 
return 0; 
}
```

**Options:**
- a. *pa = 10
- b. *pa = *pa
- c. *pa = 0
- d. *pa = 65


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) *pa = 10**

</details>
---

### Question 7
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h> 
#include <string.h> 

void fct(char *s1, char *s2, int idx) 
{ 
 
if (idx >= 0) 
 
{ 
 
 
s1[idx] = s2[idx]; 
 
 
 
fct(s1, s2, idx - 1); 
 
} 
} 
 
int main() 
{ 
 
char string1[] = "Exam_1"; 
 
char string2[] = "Exam_2"; 
 
 
int min_length = (strlen(string1) < strlen(string2)) ?  
 
 
 
   strlen(string1) : strlen(string2); 
 
 
fct(string1, string2, min_length - 1); 
 
 
printf("string1 = %s, string2 = %s\n", string1, string2); 
 
 
return 0; 
}
```

**Options:**
- a. string1 = Exam_2, string2 = Exam_1
- b. string1 = Exam_2, string2 = Exam_2
- c. string1 = Exam_1, string2 = Exam_1
- d. string1 = Exa2_2, string2 = Exam_2


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) string1 = Exam_2, string2 = Exam_2**

</details>
---

### Question 8
**Requirement:** What will be the output when the below C application will run?

```c
#include <stdio.h> 
 
#define  COMP(A, B)  ((A) * 3 > B ? (A) : (B)) 
 
int main() 
{ 
 
int x = 3, y = 3, z = 10, t = 5; 
 
 
printf("result = %d\n", COMP(x + y, z + t)); 
 
 
return 0; 
}
```

**Options:**
- a. result = 18
- b. result = 15
- c. result = 6
- d. result = 10


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) result = 18**

</details>
---

### Question 9
**Requirement:** What will be the output when the below C application will run?

```c
#include <stdio.h> 
#include <malloc.h> 
 
int main() 
{ 
 
int x = 2, y = 1; 
 
int *px = NULL, *py = NULL; 
 
 
px = (int*)malloc(x * sizeof(int)); 
 
px[0] = 3; 
 
px[1] = 5; 
 
py = px + 1; 
 
 
 
int m = x * (py - px) < y * *py ? *px : *py; 
 
 
printf("\'m = %d\'\n", m); 
 
 
free(px); 
 
 
return 0; 
}
```

**Options:**
- a. m = 3
- b. ‘m = 5’
- c. m = 5
- d. ‘m = 3’


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) m = 5**

</details>
---

### Question 10
**Requirement:** Consider the following content saved into a file named Points.txt:

```c
What will be the output of the following C application? 
 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
 
#define BUFFER_SIZE 256 
 
typedef struct point point; 
typedef struct rect rect; 
 
 
 
struct point { 
 
int x, y; 
}; 

struct rect { 
 
point point1; 
 
point point2; 
}; 
 
int main() 
{ 
 
FILE* pf = fopen("Points.txt", "r"); 
 
rect r; 
 
char buffer[BUFFER_SIZE], *token, list[] = ",\n"; 
 
long size = 0; 
 
 
fseek(pf, 0, SEEK_END); 
 
size = ftell(pf); 
 
 
if (size <= BUFFER_SIZE) 
 
{ 
 
 
fseek(pf, 0, SEEK_SET); 
 
 
fread(buffer, sizeof(buffer), 1, pf); 
 
 
 
token = strtok(buffer, list); 
 
 
 
while (token) 
 
 
{ 
 
 
 
r.point1.x = atoi(token); 
 
 
 
token = strtok(NULL, list); 
 
 
 
r.point1.y = atoi(token); 
 
 
 
token = strtok(NULL, list); 
 
 
 
r.point2.x = atoi(token); 
 
 
 
token = strtok(NULL, list); 
 
 
 
r.point2.y = atoi(token); 
 
 
 
 
printf("diff_x = %d, diff_y = %d\n", 
 
 
 
 
abs(r.point2.x - r.point1.x), 
 
 
 
 
abs(r.point2.y - r.point1.y)); 
 
 
 
 
token = strtok(NULL, list); 
 
 
} 
 
} 
 
 
return 0; 
}
```

**Options:**
- a. diff_x = 7, diff_y = 5 diff_x = 4, diff_y = 4
- b. diff_x = 7, diff_y = 7 diff_x = 4, diff_y = 4
- c. diff_x = 5, diff_y = 5 diff_x = 4, diff_y = 7
- d. diff_x = 7, diff_y = 5 diff_x = 4, diff_y = 7


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) diff_x = 7, diff_y = 5 diff_x = 4, diff_y = 7**

</details>
---

### Question 11
**Requirement:** What will be the output of the following C++ program?

```cpp
#include <iostream> 
using namespace std; 
 
class A 
{ 
public:  
 
virtual int f() { return 1; } 
 
int g() { return 2; } 
}; 
class B : public A 
{ 
public: 
 
int f() { return 3; } 
 
int g() { return 4; } 
}; 
 
int main() 
{ 
 
A* x = new B(); 
 
cout << x->f() << x->g(); 
 
return 0; 
}
```

**Options:**
- a. 14
- b. 34
- c. 12
- d. 32


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) 32**

</details>
---

### Question 12
**Requirement:** Taking into consideration the following C++ code, what will be the message printed to the

```cpp
console? 
 
#include <iostream> 
 
class A  
{ 
 
int x; 
 
void f() {} 
}; 
class B { 
 
int y; 
 
virtual void f() {} 
}; 
int main() 
{
```

**Options:**
- a. 0
- b. Yes
- c. YesNo
- d. No


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) No**

</details>
---

### Question 13
**Requirement:** What will be the output of the next C++ program?

```cpp
#include <iostream> 
using namespace std; 
 
class X { public: virtual int function() = 0; }; 
class Y : public X  
{  
public: 
 
int function() { return 1; } 
}; 
class Z : public Y 
{ 
public: 
 
int function() { return 2; } 
}; 
 
int main() 
{ 
 
X* x; Y y; Z z; 
 
y.function() ? x = &z : x = &y; 
 
cout << x-> function (); 
 
return 0; 
}
```

**Options:**
- a. 1
- b. compile/runtime error
- c. 2
- d. 0


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) 2**

</details>
---

### Question 14
**Requirement:** What will the following C++ code print?

```cpp
#include <iostream> 
using namespace std; 
 
class Foo 
{ 
public: 
 
Foo() { cout << "A"; } 
 
~Foo() { cout << "B"; } 
}; 
int main() 
{ 
 
Foo f1, f2; 
 
Foo* pf = new Foo(); 
 
return 0; 
}
```

**Options:**
- a. it will generate a runtime error
- b. AAABBB
- c. AAABB
- d. AABB


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) AAABB**

</details>
---

### Question 15
**Requirement:** What will be the output of the following C++ program?

```cpp
#include <iostream> 
using namespace std; 
 
class Student 
{ 
public: 
 
bool graduated = true; 
}; 
 
int main() 
{ 
 
Student s; 
 
Student* ps = &s; 
 
cout << (*ps).graduated; 
 
return 0; 
}
```

**Options:**
- a. runtime error
- b. 0
- c. compile error
- d. 1


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) 1**

</details>
---

### Question 16
**Requirement:** Giving the C++ class S from below and assuming that we have included the necessary classes

```cpp
and libraries, what will be the output of the main function? 
 
class S 
{ 
public: 
 
string name; 
 
char operator[](int i) { 
 
 
return name[i]; 
 
} 
}; 
 
int main() 
{ 
 
S s; 
 
s.name = "ABC"; 
 
s[0] = 'C'; 
 
cout << s[0]; 
 
return 0; 
}
```

**Options:**
- a. runtime error
- b. C
- c. compile error
- d. A


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) compile error**

</details>
---

### Question 17
**Requirement:** What will be the output of the following C++ code sequence?

```cpp
#include <iostream> 
using namespace std; 
 
class Foo { public: bool x = false; }; 
 
int main() 
{ 
 
Foo** v = new Foo * [1]; 
 
v[0] = new Foo(); 
 
cout << (*v)->x; 
 
return 0; 
}
```

**Options:**
- a. the address of the x attribute
- b. 1
- c. runtime error
- d. 0


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) 0**

</details>
---

### Question 18
**Requirement:** Assuming that B is a valid C++ class, what operator(s) could be called in the second line of

```sql
code from the main function? 
 
int main() 
{
```

**Options:**
- a. multiplication operator or implicit cast
- b. multiplication operator or explicit cast
- c. only the multiplication operator
- d. only the copy constructor


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) multiplication operator or implicit cast**

</details>
---

### Question 19
**Requirement:** What is the main reason why the overloading of the << operator for printing information to

```cpp
the console needs to be done using a friend function and not a method?
```

**Options:**
- a. because this is a unary operator
- b. in order for the operator to accept chained calls
- c. because the first operand is not the same type as the class
- d. in order to get access to the private attributes of the class


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) because the first operand is not the same type as the class**

</details>
---

### Question 20
**Requirement:** Giving the C++ classes from below and assuming that we have included the necessary

```cpp
classes and libraries, what will be the output when the main function is executed? 
 
class A 
{ 
public: 
 
~A() { cout << "A"; } 
}; 
class B 
{ 
public: 
 
~B() { cout << "B"; } 
}; 
 
 
class C : B, A 
{ 
public: 
 
~C(){} 
}; 
 
int main() 
{
```

**Options:**
- a. there will be no output
- b. a compile error because the inheritance is private
- c. AB
- d. BA


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) AB**

</details>
---

### Question 21
**Requirement:** Which of the following functions can be used with an assignment operator in a PL/SQL

```c
statement?
```

**Options:**
- a. UPPER
- b. SUM
- c. COUNT
- d. MIN


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) UPPER**

</details>
---

### Question 22
**Requirement:** Which of the following statements about implicit cursors are true?

**Options:**
- a. Are automatically opened and closed
- b. Store information regarding processing DDL statements
- c. Have user defined names
- d. Can be processed using FOR


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Are automatically opened and closed**

</details>
---

### Question 23
**Requirement:** The employees table exists has the following columns: employee_id, first_name, last_name

```sql
and hire_date and 50 rows. Given the Oracle SQL statement: 
 
select 'ab' column1 from employees where 'a'='b'; 
 
Which of the following statements is true:
```

**Options:**
- a. The statement runs successfully and displays some values
- b. The statement does not run as there is no column 'ab'
- c. The statement runs successfully and displays no rows
- d. The statement does not run as there is no column 'a' or 'b'


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) The statement runs successfully and displays no rows**

</details>
---

### Question 24
**Requirement:** What is the main purpose of the DECODE function in Oracle SQL?

**Options:**
- a. To convert a value from one data type to another
- b. To perform conditional processing
- c. To sort the result set in either ascending or descending order
- d. To calculate the aggregate of a specific set of values


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) To perform conditional processing**

</details>
---

### Question 25
**Requirement:** What does a CASE statement return in SQL Oracle when none of the conditions are met,

```sql
and there is no ELSE clause? 
Example:  
SELECT CASE WHEN salary <= 5000 THEN 'Low' WHEN salary <= 7000 THEN 'Medium' 
END FROM employees;
```

**Options:**
- a. NULL
- b. 0
- c. An error message
- d. FALSE


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) NULL**

</details>
---

### Question 26
**Requirement:** Given the query:

```sql
SELECT cust_last_name 
FROM Customers join Orders on Customers.Customer_ID = Orders.Customer_ID 
group by cust_last_name 
ORDER BY count(Order_date) DESC; 
 
What will happen if you try to run the query? 
 
Consider 
the 
tables 
Customers 
(columns: 
Customer_ID 
number, 
cust_last_name 
varchar2(100)) and Orders (columns: Order_ID number, Customer_ID number, Order_date 
date not null).
```

**Options:**
- a. The query will run successfully and return the last name of the customer with the highest Customer_ID.
- b. The query will run successfully and return the last names of customers in descending order of their total orders number.
- c. The query will fail.
- d. The query will run successfully and return the last name of the customer who has placed the most recent order.


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) The query will run successfully and return the last names of customers in descending order of their total orders number.**

</details>
---

### Question 27
**Requirement:** Can a procedure in PL/SQL call a function?

**Options:**
- a. Yes, always
- b. No, never
- c. Only if the function doesn't modify the database
- d. Only if the procedure and function access the same tables


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Yes, always**

</details>
---

### Question 28
**Requirement:** Can an Oracle SQL select statement directly call a PL/SQL function?

**Options:**
- a. Yes, if certain conditions are met
- b. No, never
- c. Only if the function doesn't alter the tablespace
- d. Only if the function is in another schema


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Yes, if certain conditions are met**

</details>
---

### Question 29
**Requirement:** The ALTER TABLE statement in SQL can be used to:

**Options:**
- a. Drop a constraint from an existing table.
- b. Insert data into the table.
- c. Create a new table.
- d. Update a row from the table.


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Drop a constraint from an existing table.**

</details>
---

### Question 30
**Requirement:** What is the main purpose of a FOREIGN KEY in Oracle SQL?

**Options:**
- a. a
- b. c
- c. b
- d. a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) a**

</details>
---

## Exam 2022

### Question 1
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream> 
using namespace std; 
  
class String 
{ 
private: 
     int length; 
     char* ps; 
public: 
     String(); 
     String(const char*); 
     ~String(); 
  
     const String& operator= (String&); 
     const String& operator+(const String&); 
  
     char* getString() { return this->ps; } 
}; 
  
String::String() { 
     this->length = 0; 
     this->ps = NULL; 
} 
  
String::String(const char* str) 
{ 
     this->length = strlen(str); 
     this->ps = new char[this->length + 1]; 
     strcpy(this->ps, str); 
} 
  
String::~String() { 
     if (this->ps) delete[] this->ps; 
     this->length = 0; 
     this->ps = NULL; 
} 
  
const String& String::operator+(const String& strSrc) { 
     String* tempS; 
     tempS = new String(); 
     tempS->length = this->length + strSrc.length; 
     if (tempS->ps != NULL) delete[] tempS->ps; 
     tempS->ps = new char[tempS->length + 1]; 
     strcpy(tempS->ps, this->ps); 
     strcat(tempS->ps, strSrc.ps); 
     return (*tempS); 
} 
  
const String& String::operator=(String& strSrc) { 
     if (this != &strSrc) { 
           this->length = strSrc.length; 
           if (this->ps) delete[] this->ps; 
           this->ps = new char[this->length + 1]; 
           strcpy(this->ps, strSrc.ps); 
     } 
     return *this; 
} 

int main() 
{ 
     String s1("The first string. "); 
     String s2("and the second one. "); 
     String s3; 
  
     s3 = "A string. "; 
     s3 = s3 + s1.getString(); 
     cout << s3.getString() << endl; 
  
     return 0; 
}
```

**Options:**
- a. “A string. The first string. ”
- b. “A string. “
- c. Nothing, due to compile-time error message for not appropriate implementations of the overloaded operators
- d. “The first string. A string. “


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) “A string. The first string. ”**

</details>
---

### Question 2
**Requirement:** What will be the output of the following C++ application?

```c
#include <stdio.h> 
  
void f(char &x, int& y) 
{ 
     y++; 
     x += y; 
} 
  
int main() 
{ 
     int a = 65; 
     char b = 1; 
  
     f((char&)a, (int&)b); 
  
     printf("%d %d", a, b); 
  
     return 0; 
}
```

**Options:**
- a. Nothing, due to a compile-time error for the call to the function f
- b. 67 2
- c. Nothing, due to a compile-time error for the implementation of the function f
- d. Nothing, due to a run-time error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) 67 2**

</details>
---

### Question 3
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream> 
using namespace std; 
  
int main() 
{ 
     int y = 0; 
     constexpr char n = 'n'; 
     constexpr char m = '?'; 
  
     switch ((char)(y == 0)) { 
     case 'n': 
           cout << "\'n\' has been chosen\n"; 
           break; 
     case 0: 
           cout << y << " has been chosen\n"; 
           break; 

     case m: 
           cout << m << " has been chosen\n"; 
           break; 
     default: 
           cout << "Nothing has been chosen\n"; 
           break; 
     } 
  
     return 0; 
}
```

**Options:**
- a. ‘n’ has been chosen
- b. ? has been chosen
- c. 0 has been chosen
- d. Nothing has been chosen


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) Nothing has been chosen**

</details>
---

### Question 4
**Requirement:** What is the output when the below C application will run (Little-Endian is the rule to store binary content)?

```c
#include <stdio.h> 
  
int main() 
{ 
     int a = 0x12340000; 
  
     printf("0x%02X\n", (char)a + 1); 
  
     return 0; 
 
}
```

**Options:**
- a. 0x12340001
- b. 0x1234
- c. 0x01
- d. 0x12340000


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) 0x01**

</details>
---

### Question 5
**Requirement:** What is the right statement regarding the following C++ application?

```cpp
#include <stdio.h> 
#include <string.h> 
  
class Student 
{ 
public: 
     int age; 
     char* name; 
public: 
     Student(int v = 0, char* sname = NULL) 
     { 
           this->age = v; 
           if (sname != NULL) 
           { 
                this->name = new char[strlen(sname) + 1]; 
                strcpy(this->name, sname); 
           } 
           else 
                this->name = NULL; 
     } 
  
     Student(const Student& s) 
     { 
           this->name = new char[strlen(s.name) + 1]; 
           strcpy(this->name, s.name); 
           this->age = s.age; 
     } 

     ~Student() 
     { 
           if (this->name) 
                delete[] this->name; 
     } 
  
}; 
  
int main() 
{ 
     int age1 = 21; 
  
     Student s1(age1, (char*)"John"); 
     Student s2 = s1; 
     Student s3 = s2; 
     Student s4 = s1; 
  
     s3 = s4; 
  
     return 0; 
}
```

**Options:**
- a. An overloaded version of operator = will be called one single time and the application will run without errors
- b. The default implementation of operator = will be called one single time and the application will run without errors
- c. No call to operator =
- d. The default implementation of operator = will be called one single time and the application will generate run-time error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) The default implementation of operator = will be called one single time and the application will generate run-time error**

</details>
---

### Question 6
**Requirement:** What is the output when the below C++ application will run?

```cpp
#include <iostream> 
using namespace std; 
  
int main() 
{ 
     int count = 0; 
     string name("John Smith"); 
  
     cout << name << " (" << name.length() << ")" << " & "; 
     string name_jr = name + " Jr."; 
     cout << name_jr << " (" << name_jr.length() << ")\n"; 
  
     return 0; 
}
```

**Options:**
- a. John Smith (10) & John Smith Jr. (14)
- b. John Smith (14) & John Smith Jr. (14)
- c. John Smith (10) & John Smith Jr. (10)
- d. John Smith (10) & John Smith (10)


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) John Smith (10) & John Smith Jr. (14)**

</details>
---

### Question 7
**Requirement:** What will be the content of the file test.txt as string view after running the following C application?

```c
#include <stdio.h> 
  
void main() 
{ 
     unsigned char buffer[] = { 'A' , 'B', 'C', 'D'}; 
      
     FILE* fp; 
     fp = fopen("test.txt", "w"); 

     for (int i = 0; i < sizeof(buffer); i++) 
           fwrite((buffer + i), sizeof(unsigned char), 1, fp); 
  
     fclose(fp); 
}
```

**Options:**
- a. 65666768
- b. DCBA
- c. ‘A’’B’’C’’D’
- d. ABCD


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) ABCD**

</details>
---

### Question 8
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h> 
  
void main() 
{ 
     unsigned char v[] = { 1, 2, 9 }; 
     unsigned char* pa = v; 
  
     *(pa + 1) = *(pa) + 1 + pa[2]; 
     printf("\na = %u, *pa = %u", v[1], pa[2]); 
}
```

**Options:**
- a. v[1] = 2, pa[2] = 9
- b. v[1] = 1, pa[2] = 9
- c. v[1] = 2, pa[2] = 11
- d. v[1] = 11, pa[2] = 9


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) v[1] = 11, pa[2] = 9**

</details>
---

### Question 9
**Requirement:** In the following C++ application, how many times the operator delete will be called?

```cpp
#include <stdio.h> 
#include <string.h> 
  
class Student 
{ 
public: 
     int age; 
     char* name; 
public: 
     Student(int v = 0, char* sname = NULL) 
     { 
           this->age = v; 
           if (sname != NULL) 
           { 
                this->name = new char[strlen(sname) + 1]; 
                strcpy(this->name, sname); 
           } 
           else 
                this->name = NULL; 
     } 
  
     Student(const Student& s) 
     { 
           this->name = new char[strlen(s.name) + 1]; 
           strcpy(this->name, s.name); 
           this->age = s.age; 
     } 
  
     Student operator+(Student s) 
     { 
           Student tstud; 
           tstud.age = (this->age + s.age) / 2; 

           tstud.name = new char[strlen(this->name) + strlen(s.name) + 1]; 
           strcpy(tstud.name, this->name); 
           strcpy(tstud.name + strlen(this->name), s.name); 
  
           return tstud; 
     } 
  
     ~Student() 
     { 
           if (this->name) 
           { 
                delete[] this->name; 
           } 
     } 
  
     void operator=(Student s) 
     { 
           if (this->name) 
           { 
                delete[] this->name; 
           } 
           this->name = new char[strlen(s.name) + 1]; 
           strcpy(this->name, s.name); 
           this->age = s.age; 
     } 
}; 
  
int main() 
{ 
     int age1 = 21, age2 = 20; 
  
     Student s1(age1, (char*)"John"), s2(age2, (char*)"James"); 
     Student s3 = s1, *ps = new Student(s2); 
     Student s4; 
      
     s3 = s3 + s2; 
  
     if(ps) 
           delete ps; 
  
     ps = &s3; 
  
     return 0; 
}
```

**Options:**
- a. 10 times
- b. 9 times
- c. Application generates compile-time errors due to wrong call to operator =
- d. 8 times


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) 9 times**

</details>
---

### Question 10
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream> 
using namespace std; 
  
class A 
{ 
public: 
     void print() 
     { 
           cout << "Class A" << endl; 
     } 
}; 

class B 
{ 
public: 
  
     B(const A& x) {} 
     B() {} 
  
     B& operator= (const A& x) { return *this; } 
  
     void print() 
     { 
           cout << "Class B" << endl; 
     } 
}; 
  
int main() 
{ 
     A ob_A, * pob_A = NULL; 
     B ob_B1, ob_B2 = ob_A, * pob_B = NULL; 
  
     ob_B1 = ob_A; 
     pob_B = &ob_B1; 
     pob_A = (A*)pob_B; 
  
     pob_B->print(); 
     pob_A->print(); 
  
     pob_B = (B*)&ob_A; 
     pob_B->print(); 
  
     return 0; 
}
```

**Options:**
- a. Class B Class A Class A
- b. Class B Class B Class A
- c. Class B Class A Class B
- d. Class B Class B Class B


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) Class B Class B Class B**

</details>
---

### Question 11
**Requirement:** What will be the output of the following C++ application (x86 architecture C compiler, pointers are FAR by

```c
default)? 
#include <stdio.h> 
#include <string.h> 
  
int main() 
{ 
     char str[] = "A string"; 
     char* pstr = new char[strlen(str) + 1]; 
     memset(pstr, 0, strlen(str) + 1); 
     memcpy(pstr, str, strlen(str)); 
  
     printf("%d %d %d %d\n", sizeof(str), sizeof(pstr), strlen(str), strlen(pstr + 1)); 
  
     return 0; 
 
}
```

**Options:**
- a. 9 8 7 7
- b. 9 4 8 7
- c. 4 4 8 7
- d. 9 4 8 8


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 9 8 7 7**

</details>
---

### Question 12
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream> 
using namespace std; 
  
class MyClass { 
private: 
     int m; 
public: 
     static int n; 
  
     MyClass() 
     { 
           m = 0; 
           n++; 
     } 
  
     MyClass(const MyClass& s) 
     { 
           this->m = s.m; 
           n++; 
     } 
  
     ~MyClass() 
     { 
           n--; 
     } 
  
}; 
  
int MyClass::n = 0; 
  
int main() { 
     MyClass mc1, * pmc = new MyClass(mc1); 
     MyClass mc2 = mc1; 
  
     cout << MyClass::n << " "; 
     mc1 = mc2; 

     cout << MyClass::n << endl; 
  
     return 0; 
}
```

**Options:**
- a. 2 3
- b. 3 2
- c. 2 2
- d. 3 3


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) 3 3**

</details>
---

### Question 13
**Requirement:** What is the right choice to make a valid string size allocation and content use of the heap memory in the below

```c
C++ code?
```

**Options:**
- a. char vstr[] = "tst"; char* str = new char[sizeof("Exam") + sizeof(vstr) + 1]; strcpy(str, vstr); strcat(str, "Exam");
- b. char vstr[] = "tst"; char* str = new char[strlen("Exam") + sizeof(vstr) + 1]; strcpy(str, vstr); strcat(str, "Exam");
- c. char vstr[] = "tst"; char* str = new char[strlen("Exam") + sizeof(vstr)]; strcpy(str, vstr); strcat(str, "Exam");
- d. char vstr[] = "tst"; char* str = new char[sizeof("Exam") + sizeof(vstr)]; strcpy(str, vstr); strcat(str, "Exam");


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) char vstr[] = "tst"; char* str = new char[sizeof("Exam") + sizeof(vstr) + 1]; strcpy(str, vstr); strcat(str, "Exam");**

</details>
---

### Question 14
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream> 
using namespace std; 

class MyClass { 
     char x; 
public: 
     static int n; 
  
     MyClass(char in = '0') 
     { 
           this->x = in; 
           n++; 
     } 
  
     ~MyClass() 
     { 
           n--; 
     } 
  
     void change(char in) 
     { 
           this->x += in; 
     } 
  
     char getX() 
     { 
           return this->x; 
     } 
  
     void setX(char in) 
     { 
           this->x -= in; 
     } 
  
}; 
  
int MyClass::n = 0; 
  
void change(MyClass& obj, char in) 
{ 
     obj.setX(in); 
} 
  
int main() { 
     MyClass mc1(67), mc2(67), * pmc = NULL; 
  
     { 
           MyClass mc3(65); 
           mc2.change(MyClass::n); 
           mc1 = mc3; 
     } 
  
     pmc = &mc2; 
     pmc->change(MyClass::n); 
  
     printf("%d %d\n", mc1.getX(), pmc->getX()); 
  
     return 0; 
}
```

**Options:**
- a. 65 72
- b. 71 72
- c. 65 65
- d. 72 72


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 65 72**

</details>
---

### Question 15
**Requirement:** What will be the output of the following C++ application?

```c
#include <stdio.h> 
  
char f1(char x, int* y) 
{ 
     (*y)++; 
     x += *y; 
  
     return x; 
} 
  
char f1(char* x, int y) 
{ 
     y++; 
     *x += y; 
  
     return *x + y; 
  
} 
  
int main() 
{ 
     char a[] = { 35, 36, 37 }; 
     int b = 7; 
  
     a[0] = f1(a[0], &b); 
     b = f1(a, b); 
  
     printf("%d %d\n", a[0], b); 
  
     return 0; 
}
```

**Options:**
- a. 43 61
- b. 52 61
- c. 52 53
- d. 43 53


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) 52 61**

</details>
---

### Question 16
**Requirement:** How will be displayed the “car01.txt”, file after running the following Java code?

**Options:**
- a. b.
- c. Runtime error
- d. 


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) *(see original PDF)***

</details>
---

### Question 17
**Requirement:** What will display the following Java code, if the given input in console is "Hello World Java/Kotlin!"?

**Options:**
- a. Nothing because of compilation error
- b. Hello World Java/Kotlin!
- c. Nothing because of runtime error
- d. Hello quit


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) Hello World Java/Kotlin!**

</details>
---

### Question 18
**Requirement:** What will display the following Java code?

**Options:**
- a. # Class C Constr. # Class B Constr. # Class A Constr.
- b. # Class A Constr. # Class B Constr. # Class C Constr.
- c. compilation error
- d. runtime error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) compilation error**

</details>
---

### Question 19
**Requirement:** What will display the following Java code?

**Options:**
- a. Nothing because of compilation error
- b. 500
- c. Nothing because of runtime error
- d. 400


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) 400**

</details>
---

### Question 20
**Requirement:** What will display the following Java code?

**Options:**
- a. Nothing because of compilation error
- b. Nothing because of runtime error
- c. val = John
- d. val = null


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) val = John**

</details>
---

### Question 21
**Requirement:** What will display the following Java code?

**Options:**
- a. Nothing because of compilation error
- b. Nothing because of runtime error
- c. p1 equals p2 - false \n p1 == p2 - true
- d. p1 equals p2 - true \n p1 == p2 - true


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) p1 equals p2 - true \n p1 == p2 - true**

</details>
---

### Question 22
**Requirement:** What will display the following Java code?

**Options:**
- a. Always runtime exception
- b. Always “Americano”
- c. Sometimes “Americano” and sometimes runtime exception
- d. Nothing because of compilation error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) Sometimes “Americano” and sometimes runtime exception**

</details>
---

### Question 23
**Requirement:** What will display the following Java code?

**Options:**
- a. Nothing because of compilation error
- b. 94 92 # 94 50 92 # 92 -1 92 # 94 -1 50
- c. 94 92 # 94 50 92 # 92 -1 92 # 94 50
- d. Nothing because of runtime error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Nothing because of compilation error**

</details>
---

### Question 24
**Requirement:** What will be displayed, after running the following Java code?

**Options:**
- a. 0 4 8 12
- b. 0 2 4 6
- c. Runtime error
- d. 0 1 2 3


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) 0 2 4 6**

</details>
---

### Question 25
**Requirement:** What will display the following Java code?

**Options:**
- a. sum = 140
- b. Nothing because of runtime error
- c. Nothing because of compilation error
- d. sum = 105


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) sum = 105**

</details>
---

### Question 26
**Requirement:** What will display the following Java code?

**Options:**
- a. 91 73 21
- b. Nothing because of compilation error
- c. 91 73
- d. Nothing because of runtime error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) Nothing because of runtime error**

</details>
---

### Question 27
**Requirement:** What will display the following Java code?

**Options:**
- a. Nothing because of runtime error
- b. CAPPUCCINO, 17.000000; FLAT WHITE, 16.000000;
- c. CAPPUCCINO, 17.000000;
- d. CAPPUCCINO, 17.000000; CAPPUCCINO, 17.000000; FLAT WHITE, 16.000000; FLAT WHITE, 16.000000;


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) CAPPUCCINO, 17.000000; CAPPUCCINO, 17.000000; FLAT WHITE, 16.000000; FLAT WHITE, 16.000000;**

</details>
---

### Question 28
**Requirement:** What will display the following Java code?

**Options:**
- a. 2034
- b. 7834.5
- c. Nothing because of runtime error
- d. Nothing because of compilation error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) 7834.5**

</details>
---

### Question 29
**Requirement:** What will display the following Java code?

**Options:**
- a. 305
- b. runtime error
- c. 897
- d. compilation error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 305**

</details>
---

### Question 30
**Requirement:** What will display the following Java code?

**Options:**
- a. c
- b. c
- c. a
- d. b


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) a**

</details>
---

## Exam 2021

### Question 1
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h>
void main()
{
char vi] = 
( 
97, 
99, 
102 };
char: pa = v;
*(pa + 1) 
= *{(pa + 
1) 
- 2;
print ("ina = $d, *pa = 8x", vi], pal2]};
a} 
a= 98, *pa=66
```

**Options:**
- b. a=99,*pa=98
- c. a=98, *pa=99 dj a= 62, *pa=65
- e. a=98,*pa=98


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) a=98, *pa=99 dj a= 62, *pa=65**

</details>
---

### Question 2
**Requirement:** What will be the content of the file test.bin as hexa-decimal pairs of figures (1 pair means 1 Byte)

```c
after running the following C application (little-endian approach}?
#include <stdio.h>
void main)
{
long int buffer = 0x12345678;
FILE* fp;
fp = fopen("test.bin", "wb");
for (int i = 0; i < sizeof(long int); i++)
fwrite((char*) ((char*) &buffer + i), sizeof(char}), 1, fp);
Eclose(fp);
```

**Options:**
- a. 78563412
- b. 56781234
- c. 12347856
- d. 12345678
- e. 87654371


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 78563412**

</details>
---

### Question 3
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h>
char fl(char x, int* y)
{

(ty) tt:
x += *yi
return x;
}
char f2{char &x, int y)
(
yrti
x += y;
return x + y;
}
void main()
{
char a = 0x65;
int b = 1;
```

**Options:**
- a. 106109
- b. 106 110
- c. 102 109
- d. 101210
- e. 105 109


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 106109**

</details>
---

### Question 4
**Requirement:** What will be the output of the following C++ application?

```c
#include <stdic.h>
void Eichar x, int *y)
{
yt;
Ke ys
}
void main 
()
{
char a = 65;
char b 
1;
ii
tb, (int*) say;
printt ("sd $d",

&
—
Compilation error triggered by the implementation of function f
Compilation error triggered by the call to the function f
651
65 66
661
RE
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c)**

</details>
---

### Question 5
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h>
#include <string.h>
void main)
{
char pattern[] = "exam";
char* pv = pattern + 1;
if (pv == pattern)
printf ("Same content\n");
else
print ("Different content\n");
if (spy != (chart*)pattern)
printf("Different content\n");
else
print (“Same content\n");
if (*pv => pattern[1])
printf ("Same content\n");
else
printf (“Different content\n");
if ({stremp(ev, pattern) )
printf ("Same content\n");
else
printf ("Different content\n");
a}
Different content
Different content
Same content
Different content
Same content
Same content
Same content
Same content
Different content

Same content
Different content
Different content
d)
Different content
Different content
Different content
Same content
e)
Same content
Different content
Different content
Same content
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c)**

</details>
---

### Question 6
**Requirement:** Whatis the right choice to make a valid string size allocation and content use of the heap memory

```c
in C++ code?
a)
char vstr[| = “tst";
chart str = new char[atrlen ("Exam") ] ;
str[strlen(vstr)] = 0;
strnopy (str, vstr, strlen{vstr));
cha
cna
else OTE am" } 
Ray
n{"Baean') 
a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a)**

</details>
---

### Question 7
**Requirement:** What will be the output of the following C application (x86 architecture C compiler, pointers are

```c
FAR by default)?
include 
bdio.h>
ale

#include <string.h>
void main)
{
char stri] = "A string";
char* pstr = new char{strlen(str) + 1];
stropy(pstr, str);
printi ("td td. $d $d\n", strlen(str), sizeof(str), sizeofi(pstr), sizeof(*pstr));
```

**Options:**
- a. 8944
- b. 8841
- c. 8944
- d. 9941
- e. 9844


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) 8944**

</details>
---

### Question 8
**Requirement:** In the following C++ application, how many times the destructor of the class Student is called?

```c
#include <stdio.h>
class Student
{
private:
int age;
char* name;
public:
Student (int v = 0)
i
this->age = v;
this->name = NULL;
}e
void main)
{
Student x;
int agel = 21, age2 = 20;
Student sl (agel);
Student 82 (age2);
for (int d= 1; 

<= 3; i++)
{
Student s3 = sl;
}
x = 827
```

**Options:**
- a. 6 times
- b. Stimes
- c. Otimes
- d. 7 times
- e. There is no destructor attached to the class Student


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 6 times**

</details>
---

### Question 9
**Requirement:** Inthe following C++ application, how many times the operator = is called for the objects Students?

```cpp
#include <stdio.h>
finelude <string.h>
class Student
{
public:
int age;
char* name;
public:
Student (int v = 0, char* sname = NULL)
{
this->age = v;
if (sname != NULL)
i
this->name = new char[strlen(sname) + 1];
strcpy(this->name, sname) ;
}
else
this->name = NULL;
}
Student (const Studenté s)
{
this->name = new char[strlen(s.name) 
+ 1];
strepy (this->name, s.name);
this->age = s.age;
}
~Student 
()
{
if (this->name)
delete[] this->name;
im
void main()
{
int agel = 21;
Student sl(agel, "John");
Student s2 = sl;
Student 83 = sl;
Student s4;
s4 = $3;
```

**Options:**
- a. 1 single time
- b. 3 times
- c. No call to overloaded operator =
- d. 4times
- e. Compilation error because there is no overload of operator = implemented by the class Student


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 1 single time**

</details>
---

### Question 10
**Requirement:** în C++, the default constructor is called when

**Options:**
- a. An objectis created by using predefined values for its attribute members
- b. An object is created from another object of the same type
- c. An object is passed to a method by its reference
- d. An obiect is returned by its reference as result of a method
- e. An object is initialized by using the attribute member values of other object


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) An object is passed to a method by its reference**

</details>
---

### Question 11
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream>
using namespace std;
class MyClass 
{
public:
static int n;
MyClass 4)
i
n+;
}
~MyClass ()
i
n--;
}
be
int MyClassiin = 0;
void main() 

MyClass mel, me2, 
*pme;
pmc = new MyClass;
cout << MyClassiin << " ";
pme = amc2;
cout << MyClass::n << endl;
```

**Options:**
- a. 33 by 32
- c. 22
- d. 23
- e. 31


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 33 by 32**

</details>
---

### Question 12
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream>
using namespace std;
class MyClass 
{
char x;
public:
static int n;
MyClass(char in =
{
this->x =
net;
}
~MyClass 
()
{
ne;
)
10)
in;
void change(char in)
{
this->x += in;
i
char getX{}
{
return this->x;
}
void setX(char in)
i
this->x <= iin;
}
i
int MyCiass::n = 0;
void change (MyClassé obj,
{
ob} .setX (in);
}
void main({) 
{
char in)
MyClass mol (67), me2(67), 
*pme;
change (mel, 2)
me2 „change 
(2);
mol = moZ;
pme = &mel;
pmo~>change 
(2);
printi ("$d Sani,
sn,
mel .getă (), mc2,„getă (0);
```

**Options:**
- a. 7169
- b. 6969 ce) 6566
- d. 6974
- e. 7171


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 7169**

</details>
---

### Question 13
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream>
using namespace std;
class A
{
public:
void print 
()
{
cout << "Class A" << endl;
i
he
class B
{
public:
Biconst A& x} 
{}
BO) 
{}
B&é opérator= {const A& x) 
{ 
return *this; 
}
void print 
()
{
cout << "Class B" << endl;
}
Me
void main()
{
```

**Options:**
- a. b) Compilation error message
- b. ob Bl, ob _B2 = ob A; ob Bl = ob A; ob Bl.print Q; ob BZ.print(); ob_A.print Q;
- c. Ciass B Class A Class A
- d. Clase A Ciass A Ciass A Class A Ciass B Class A


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) b) Compilation error message**

</details>
---

### Question 14
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <lostream>
using namespace std;
class String
t
private:
int Length;
char* ps:
public:
String 
i) +
String (const char*};
~String(};
const Strings operator> (const String&);
const String& operatort (const String&);
const String& operator+ (const char*);
char*® getStringi) 
{ 
return this->ps; 
}
Vi
String::String(! 
[
this->length = 0;
this->ps = NULL;
}
String: :Stringiconst char* str) 
|
this->length = strien(str);
this->ps = new char[this->length + 1];
strepy(this->ps, str};
}
Stringi:~String() 
{
if {this->ps) delete[}] this->ps;
this- length = 0;
this->ps = NULL;
)
const String& String: roperatort (const String& steSre) 
¢
String* tenips;
tempS = new String 
()7
tempS->length = this->length + strsSre.length;
if (tempS~>ps 
f= NULL) delete[] tempS->ps:
temp$->ps = new char{tempS->length + 1];
strepy (tempS->ps, this->ps);
stroeat (LempS->ps, strSrca.ps};
veturn (*tempS);
}
const Stringe String

String* temps;
tempS = new String);
tempS->length = this->length + (int)strlen (str);
if (tempS->ps i= NULL) delete[] tempS->ps;
tempS->ps = new char[tempS->length + 1];
strepy (tempS~aps, this->ps);
streat (cempS~>ps, str);
return (*tempS};
)
const String& String: :operator= (const. Stringă strârc) 
|
if (this I= &strSre) 
{
thig->length = strSre. length;
if (this-Sps) delete[] this->pa;
this->ps = new char[this<>length + 1};
strepy(this->ps, stxrSrc.ps);
eturn *this;
void main
{
String sl{"The first string ");
String s2(“'and the second one. ");
String s3("A string. ");
s3 = 853 
+ "Plus a new string. ";
53 = s3 + s2.getStringO;
cout << s3,getString() << endl;
```

**Options:**
- a. “A string. Plus a new string. and the second one.”
- b. “The first string and the second one. Plus a new string. “
- c. “Plus a new string. “
- d. Runtime errors due to heap memory sharing
- e. Compilation error message due to wrong implementation of the overloaded operators


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) “A string. Plus a new string. and the second one.”**

</details>
---

### Question 15
**Requirement:** in the following C++ application, how many times the operator delete is called?

```cpp
#include <stdia.h>
#include <string.h>
class Student
(
public:
int age;
char* name;
public:
Student (int v = 0, chart sname = NOLL)
i
this->age
Lf (sname
i
this->name = new char(strian(sname)
strepy(this->name, snate) ;
}
else
this->name = NULL;

}
Student (const Students& s)
i
this->name = new char[strlen (s.nama) 
+ 1];
strepy(this->name, s.name);
this->age = s.age;
}
Student operator: (Student s)
i
Student tstud;
tstud. age 
(this->age + s.age) / 2;
tstud.name = new char[strlen(thia->name) 
+ strlen{s.name} + 1];
stropy (tstud.name, thigs->name) ;
strepy (tstud.name + strlen(this=>name), s.name);
return tstud;
}
“Student 
[)
i
if (this~>name)
delete[{] this->name;
i
void operator=(Studenté -s)
i
LE (this->name)
delete[] this->name;
this->name = new charistrlenis.name) 
+ 1};
strepy(this->name, s.name);
this->age = s.age;
yi
void main)
{
int agel = 21, age2 = 20;
Student si(agel, *John");
Student sZiagezZ, "Jamest);
sa = sl + s2;
Student s3 = sl + s2;
Student s4;
s4 = 83;
```

**Options:**
- a. 10 times
- b. Compilation errors due do wrong call to copy constructor
- c. Stmes
- d. Compilation errors due do wrong call to operator +
- e. 11 times


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 10 times**

</details>
---

### Question 16
**Requirement:** What will display the following Java code?

```java
package eu.uni. jtest;
import java.util HashMap;
import java.util.Map;
final class Url {
private final String protocol, domain, uri;
private final Integer port;

public Url(String protocol, String domain, Integer port, String uri} {
this.protecol = consistencyCheck(protecél, “http");
this. domain = domain;
this.port = Integer. decode( consistencyCheck(''" + port, "80°99;
this.uri = uri;
y
private static String consistencyCheck(String val, String expectedval) î
Lf (val. compareToCexpectadVal) t= 0)
throw new ILLegalArgumentException(val + n: 
* + expectedVal);
return val;
i
@verride
public boolean equals(Object o) {
if Co == this)
return true;
if (Co instanceof Url))
return false;
Url url = (Url) o;
return url protocol, equals(protocol) && url, domain. equal s(domain)
&& url uri .equals(uri) && url. port.equalsCport):

}
public class MainTestz {
public static void main(String[] args) {
Map<Url, String> m = new HashMap<();
Url k = new Url("“http", "ww.ase.ro”, 80, “best;
m.put(k, “First Url");
String val = m.get(k);
System.out.printin("val = "+ val);
```

**Options:**
- a. val = First Url
- b. val = null
- c. Nothing because of compilation error
- d. Nothing because of runtime error
- e. None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 17
**Requirement:** What will display the following Java code?

```java
package eu.uni.jtest:
import java.util.Arrays:
class LinearDataStructureContainer implements Cloneable {
private Object{] elements;
private int size = @;
private static final int DEAAULT.INITIAL.CAPACITY = 5;
public LinearDataStructureContainer® {
this. elements = new Object (DEFAULT. 
INITIAL,. CAPACITY) ;
}
i

public void push(Object e) {
ensureCapacity();
elements[size++] = e;
}
public Object pop) throws Exception {
af (size. == 9)
throw new Exception();
Object result = elements[-~size];
elements[size] = null; // Eliminate obsolete reference
return result;
}
private void ensureCapacity() { // Ensure space for ot Least one more element,
if Celements. Length == size)
elements = Arrays. capy0fCelements, 2 * size + 1;
}
GOverrida protected Object clone() throws CloneNotSupportedException {
try 
{
LinearDataStructureContainer result = CLinearDataStructureContainer) super clone);
result elements = elements;
return result;
} catch (CloneNotSupportedException e) {
throw new AssertionErrorQ;
Ei

Override public String toStringQ) {
StringBuffer r = new StringBufferQ;
r„appendC” ["+elements[0]); int i = 1;
for(Object o : elemerits) {
LfC > 1) r.appendC", "+09; i++;
Ei
r-appendO"7");
return r.toStringQ;
public class MainTest2 {
public static void main(String[] args)
LinearDataStructureContainer dsi = new LinearDataStructureContainerO;
dsi.push("1"); dsi.push("5"); dsi.push("9");
try 
{
LinearDataStructureContainer ds2 = CLinearDataStructureContainer) dsi.cloneQ);
String s = (String)dsi.popQ);
System. avé.printin("dst = "+ dsi.toString() +", ds2 =" + ds2.toStringO + "sata 8);
} catch (Exception e) {
```

**Options:**
- a. ds1=[1, 5, null, null, null], ds2 = [1, 5, null, null, null], s #9
- b. dst=[1, 5, null, null, nul], ds2 =[1, 5, 9, null, null], s =9
- c. Nothing because of compilation error
- d. ds1=[1, 5], ds2=[1, 5, 9],s=9
- e. None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 18
**Requirement:** What will display the following Java code?

```c
package eu.uni.jtest;

private findl Date date;
public Exam(String location, Date date) {
this. location = location;
this. date 
= (Date) date. clone;
}
public String getLocationO) {
return location;
y
public Date getDate() {
return date;
}
#over ride
public String toString {
return new StringC"Location = "+location+“, date = “+date);

+
public class MainTest2 {
public static void main(String[] args) {
String location = new StringC Bucharest");
Date data = new Date();
Exam e1 = new Exam(location, date);
Exam e2 = new Exam(location, date);
System. 
out, printin("pl equals p2 ~ “ + Cel. equals(e2)>>;
System. aué.printin("pl == p2 - “ + (el == e2));
```

**Options:**
- a. pi equals p2 - false în p1 == p2 - false
- b. pi equals p2 - true în pi == p2 — false
- c. Nothing because of compilation error
- d. Nothing because of runtime error ej None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 19
**Requirement:** What will display the following Java code?

```c
package eu.uni.jtest;
interface FiPrime {
boolean checkPrimeCint num);

public class MainTest2 {
public static void main(String... args) {
FiPrime myPrimeFunc = (num) -> {
boolean boolFlag = false;
for (var i = 2; i <= num / 2; 7.
if (num / i == @) f
boolFlag = true;
break;
Ei ‘
del
}
return boolFlag;

int n = 301;
System. out.printfC”Is the number n = %d prime? Yes = %b", n, myPrimetunc.checkPrime(381));
}
}
```

**Options:**
- a. Is the number n = 301 prime? Yes = false
- b. Is the number n = 301 prime? Yes = true
- c. Nothing because of compilation error
- d. Nothing because of runtime error
- e. None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 20
**Requirement:** What will display the following Java code?

```java
package eu.uni.jtest;
import java.util Date;
class Exam { 
we
private final String Locatio
```

**Options:**
- b. 2021.5 6) 2021
- d. Nothing because of compilation error
- e. None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 21
**Requirement:** What will display the following Java code?

```c
package ev.uni.jtest;
class MyGen<T> {
T var;
void set(T t) f
this.var =.t;
+
T get) {
return var;
}
i
public class MainTest2 {
public static void main(Stringf] args) 1
var m = new MyGen<Double>();
m.set(2021.5);
System. opt.printinc”" + Integer. porseznt("“ + m. get O);
```

**Options:**
- a. sum = 42
- b. sum=43 <) Nothing because of compilation error
- d. Nothing because of runtime error
- e. None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 22
**Requirement:** What will display the following Java code?

```java
package eu.uni.jtest;
import java.util.List;
import java.util. LinkedList;
public class MainTest2 {
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 23
**Requirement:** public static void main(String[] args) {

```java
List<Double> doubleLinkedList = new LinkedList<Dauble>Q;
doubleLinkedList.add(991.5); doubleLinkedList.add(2421.0);
for (Double d : doubleLinkedList) {
System. out.print(d + "5
}
System, ové.printc” # ");
doubleLinkedList .remove(1);
doubleLinkedList.stream(). forEach(System. out: :print);
doubleLinkedList.add(991d); doubleLinkedii 
st .add(2022d) ;
doublel 
inkadi ist add(1, 2018.7);
System. out.print“ # "5;
Systam.out print“ ° + doubleLinkedList.get(1));
System. 
out. print” “ + doubleLinkedList.index0f(Z));
System, out.print(“ * + doubleLinkedList. remove(3));
System. 
out. print” # "9;
doubleLinkedList.stream().forEach(x -> System. out.printfC"%s; *, x);
```

**Options:**
- a. b) Nothing because of runtime error 6) Nothing because of compilation error
- b. Nothing because of compilation error ¢) 991.5 2021.0 #2021.0# 2018.7 -1.2022.0 # 991.5; 2018,7; 991.0;
- d. e) None of the existing answers
- e. None of the existing answers What will display the following Java code? package eu.uni.jtest; import java.util List; import java.util ArrayList; public class MainTest2 { public static void main(String[] args) { List<Integer> bits = new ArrayList<Integer>(); bits.add(2); bits.add(2); bits -add(4); var value = @; for(var i = @; î < bits, sizeQ); it+) _ value A= bits.getCi); ae System. out.printfC"value = Xd", value);


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 24
**Requirement:** What will display the following Java code?

```java
package eu.uni.jtest;
‘import java.util.Arrays;
import java.util.List;
public class MainTest2 {
public static void main(String[] args)
{
List<Integer> numbers = Arrays.asList(100, 15, 30, 49);
int facter = 5;
System. out. printin€
numbers.stream().filterCnumber -> number % 3 == 0)
„maptolnt(e -> e * factor) .sum());
+
}
```

**Options:**
- a. 225
- b. Nothing because of compilation error c} 280
- d. Nothing because of runtime error
- e. None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 25
**Requirement:** What will display the following Java code, if the given input in console is “strike” without quotes?

```java
import java.io.BufferedReader;
import java.io. IOException;
import java.io. InputStreamReader ;
public class MainTest2 {
public static void main(String[] args)
{
String str = °";
BufferedReader obj = new BufferedReaderCnew InputStreamReader(System. 
24));
do {
try {
str = (String) obj.readLined);
} catch CIOException e) {
```

**Options:**
- a. strike
- b. Nothing because of compilation error
- c. Hello strike
- d. Nothing because of runtime error
- e. None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 26
**Requirement:** What will display the following Java code if run within an empty directory/folder?

```java
package eu.uni.jtest;
import java.io.File;
import java.io. TOException;
public class MainTest2 {
public static void main(String[] args)
{
String name = null;
File file = null;
try {
file = new FileC”exam.txt", name);
} catch(Exception tee) {
}
LFCfile == null |! file. exists)
System. aut.print("Exp01");
else
System. 
out printC"Expd2");
```

**Options:**
- a. ExpOi
- b. compilation error
- c. Exp02
- d. Runtime error
- e. None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 27
**Requirement:** Whal will display the following Java code?

```c
package ‘eu.uni.jtest;
interface I {
public default void FO {
System. oué.printin("This is a default method within interface");

}
abstract class A implements 1 {
private int 1 = 207;
}
class & extends A {
private int i = 133;
@0verride
public void FO î
System. out.printin(’i = " + this. î);
public class MainTestz

public static void main(String[] args) 1
T a = new BO;
```

**Options:**
- a. 133
- b. compilation error sc) “This is.a default method within interface” - text without quotes
- d. runtime error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 28
**Requirement:** What will display the following Java code?

```java
package eu.uni.jtest;
class A {
public AQ) {
System.out.printC’ # Class A Constr,");
Da
}
class 8 extends A {
public BO {
System.oué.print(” # Class B Constr.");
y
}
class € extends 8 {
private int x = 8;
public CO {
System. aué.print(” # Class C Constr.");
}
public CCC oc} f
System. aut.print(" 4 Class C Copy Constr.");
this.x = €.x;
}
public class MainTest2 {
public static void main(String[] args) {
€ cl = new CO;
```

**Options:**
- a. # Class A Constr. # Class B Constr, # Class C Constr. # Class A Constr. # Class B Constr. # Class C Copy Constr.
- b. compilation error
- c. # Class A Constr. 4 Class B Constr, # Class C Constr. # Class C Copy Constr.
- d. runtime error ej None of the existing answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 29
**Requirement:** How will be displayed the “car.txt” in hex file after running the following Java code?

```java
package eu.uni.jtest;
import. java.io. DataQutputStream;
import java,io.FileOutputStream;
import java.io. 10Exception;
class Car î
private int weight = @;
private String type = 
“";
private String color = "";
public Car(int weight, String type, String color){
this weight = weight; this.type = type; this.color = color;

public Integer getWeightQ 1 return. weight;}
public void setWeight(Integer weight) { this.weight = weight; >
public String. getTypeQ) { return type; }
public String getColor©O { return color; }
public void setColor(String color) { this.color = color; }
public String toString) {
return “Cor{" + “color='" 
+ color +
+", type = '" + type + "", weight=
ora 
wis
"+ weight + "7;
>
public class Maintest2 î
public static void main(String[] args)
{
try CFileOutputStream fos = new FileOutputStreamC" 
car. tat”);
DataOutputStream out = new DataQutputStream(fes);) {
Car ¢ = mew Car(1024, "Audi AG", “black");
out writeUTFC"" + ¢,getWeightQ);
out writeUTF 
Cc. getTypeQ) ;
out. writeUTF(e, getColor());
} catch CIOException e) {
e.printStackTraceQ);
}
(2!

00 04 31 30 32 34 00 07 41 75 64 69 20 41 34 00 05 62 SC 61 63 6B
00 04 31 30 32 34 00 07 41 75 64 69 20.41 34 00 05 62 6C 61 63 6B OD OA
00 04.31 30 32 34 00 07 41 75 64 69 20 41 34 00 05 62 6C 61 63 GB OA
Runtime error
None of the existing answers
pap 
Ep
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 30
**Requirement:** What will display the following Java code?

```java
package eu.uni.jtest;
import, java.util HashMap;
import jova.util. Iterator;
import java.util Set;
public class MainTest2 {
public static void main(String[] args) {
HashMap<String, Integer> hashMapPhoneAgenda = new HashMap<String, Integer>();
hashMapPhoneAgenda.put("John", 783500);
hashMapPhoneAgenda.putC" 
Andrew", 235000);
hashMapPhoneAgenda .put("Alex" , 295600);
Set<String> keys = hashMapPhoneAgenda.keySetC);
Iteratar<String> it = keys.iteratorQ);
String K = it.nextd);
for (; it. hasNextQ); K = it.nextQ) {
System.out.print("; Key =" + K+", Value = "4 hashMapPhoneAgenda.get(K3);
ii
; Key = Alex, Value = 295600; Key = Andrew, Value = 235000
; Key = Alex, Value = 295600; Key = Andrew, Value = 235000; Key = John, Value =783500
Compilation error
Runtime error
None of the existing answers
pane
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

## Exam 2020

### Question 1
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h> 
ee 
é
void main()
{
char a = 97;
chart pa = NULL;
pa = &a;
*pa = *pa - 1;
printf(’\na = %d; *pa = %X", a, *pa);
```

**Options:**
- a. Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 2
**Requirement:** What will be the content of the file test.bin as hexa-decimal pairs. of figures (1 pair means 1

```c
Byte) after running the following C application (little-endian approach)?
#include <stdio.h>
void main()
{
long int buffer = 9x12345678;
FILE *fp;
fp = fopen(“test.bin", "wb");
fweite(&buffer, sizeof(char), 3, fp);
fclose(fp);
```

**Options:**
- a. 785634
- b. 123456
- c. 12345678
- d. 78563412 Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 3
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h>
void f(char *x, int y)
{
yer;
SX t= Y5
)
void main)

char a = 0x65;
int b= 1;
f(&a, b);
printf(“%X %d", a, b);
671
651
652
672
ooo 
ef
wae 
ST Se
Correct: a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 4
**Requirement:** What will be the output of the following C++ application?

```c
#Hinclude <stdio.h>
void f(char *x, int &y)
{
yet;
i 
+= ¥3
}
void main()
{
char a = 65;
int b= 13 
:
fi&a, &b);
printf("%d 4d", a, b);
)
```

**Options:**
- a. Compilation error message
- b. 671
- c. 672
- d. 652 Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 5
**Requirement:** What will be the output of the following C application?

```c
#include <stdio.h>
void main)
{
char pattern[] = “test”;
int found = @, i = 8;
while (pattern[it+] I= @)
{
i
found++;

printf("%d", found);
ao 
oO
m 
e ee
DU 
o te
Correct: a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 6
**Requirement:** Whatis the right choice to make a valid allocation and use of the heap memory in C++ code?

```c
a}
char* str = new charistrlen("Exam")+1];
sircpy(str, "Exam’);
```

**Options:**
- b. char“ str = new charjstrien("Exam"+1)]; strepyistr, "Exam”);
- c. char* str = new char[strien("Exam+1")]; stropy(str, “Exam’):
- d. char str = new char[strien("Exam")}; strepy(str, "Exam”); Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 7
**Requirement:** Whatwill be the output of the following C application?

```c
#include <stdia.h>
#include <string.h>
void maing}
{
char str[] = "A string";
printf("%d %d", strlen(str), sizeof(str));
a) 

b) 88
ch} 

d) 98
Correct: a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 8
**Requirement:** In the following C++ application, how many times the destructor of the class Student

```c
is
called?
#include <stdio.h>
class Student
{
private:

int age;
chart name;
public:
Student(int v = 8)
{
this->age = v;
this-oname = NULL;
)i
void main)
{
Student x;
int agel = 21; int age2 = 20;
Student sl(agel);
Student s2(age2);
Student s3 = si;
Student $4;
```

**Options:**
- a. vw
- b. 3times : i
- c. 4times oO.
- d. There îs no destructor attached to the class Student Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 9
**Requirement:** inthe following C++ application, how many times the operator = is called?

```cpp
#include <stdio.h>
#include <string.h>
class Student
{
public:
int age;
char* name;
public:
Student(int v = 8, char* sname = NULL)
{
this-sage = v3
if (sname f= NULL)
this->namé = new char[strlen(sname) + 1];
strepy(this->name, sname);
}
else
this~soname = NULL;
}
Student(const Student& s)
{
this->name = new char[strlan(s.name) + 1];
strepy(this->name, s.name);
this-yage = s.age;
}
void operator=(Student& s)
{
if (this->name)

deletef] this->name;
this->name = new char[strlen(s.name) + 1];
strapy(this->name, s.name);
this-»>age = s,age;
}
~Student()
if (this->name)
delete[] this->name;
void main() 
:
{
int agei = 21; int age2 = 20;
Student si(age1, “John");
Student s2(age2, “James”);
sl .= s2;
Student s3 = si;
Student. s4;
s4 = 523
}
```

**Options:**
- a. 2 times
- b. 3 times
- c. 1single time
- d. No call to overloaded operator = Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 10
**Requirement:** In C++, the copy constructor is called when

**Options:**
- a. Building an object taking over another one with the same type, passing an object by value as input parameter to a function/method, returning an object by value as result from a function/method
- b. Two objects of the same type are involved in an assignment operation
- c. Building an object taking over another one with the same type, passing an object by reference as input parameter to a function/methed, returning an object by value as result from a function/method
- d. Building an object taking over another one with the same type where there are only run-time attributes in heap memory Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 11
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream>
using namespace std;
class MyClass {
public:
static int n;
MyClass()
n

~MyClass()
i
}
n-a
i
int MyClass::n = 8;
void main() {
MyClass mol, mc2, *pme;
prac = new MyClass;
MyClass tmc;
}
cout << MyClass:in. << endl;
delete pmc; 
aa
}
a) 

b) 

cs) 

d 

Correci: a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 12
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream>.
using namespace std;
class MyClass {
char x;
public:
static int n;
MyClass{char in = '9')
{
this->x = in;
ners
}
~MyClass()
i
n--j
}
void change(char in)
{
this-ox += in;
}
char getX()
{
return this->x;
}

int MyClass::n = 8;
void change(MyClass& obj, char in)
{
)
void maint) 4
MyClass mci(67), mc2('a'), *pmc;
pmc = new MyClass;
abj.x -= in;
change(mci, 2);
printf("Md\n", med.getXx())3 
i 
, 
;
delete punc;
}
```

**Options:**
- a. Compilation error message i
- b. c)
- d. Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 13
**Requirement:** What will be the output of the following C++ application?

```cpp
#include <iostream>
using namespace std;
class A
{
public:
void print()
cout << "Class ATM << endl;
}
ts
class B
{
public:
B(const A& x) {}
BC) {}
B& operator= (const A& x) { return *this; }
operator A() { return AQ); }
void print()
cout << "Class B” << endl;
}
ti
void main()
{
```

**Options:**
- a. Class B Class A
- b. Class B Ciass B 0) Class A Class. A
- d. Compilation error message Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 14
**Requirement:** What will be the right statement to be added for the following C++ application?

```cpp
#include <iostream>
using namespace std;
class String
{
private:
int length;
char* ps;
public:
String();
String(const char*);
~String();
const String& operator=(const String&);
const String& operator+(const String&);

String: :String() {
this->length = 8;
this->ps = NULL;
String: :String(const char* str) {
this->length = strlen(str);
this-ops = new char[this->length + 1];
strepy(this->ps, str);
String: :-StringQ) {
Lf (this->ps) delete[] this->pa;
this->length = 8;
this=>ps = NULL;
)
const String& String: :operator+(const String& strSrc) {
String* temps;
temp5 = new String);
tempS->length = this->length + strSrc.length;
if (tempS->ps [= NULL) delete[] tempS->ps;

tempS->ps = new char[tempS->length + 1];
strepy(tempS->ps, this->ps);
strcat(tempS->ps, strSrc.ps);
return. (*tempS);
)
const String& String: :operator=(const String& strSrc) {
if (this t= &strSre) {
this->length = strSrc-length;
if (this~ops) delete[] this->ps;
this->ps = new char[this->length + 1];
strepy(this->ps, strSrc.ps);
}
return *this;
}
void main)
{
String s1("The first string ");
String s2(”and the second one.");
String 53;
// add new statements here
)
```

**Options:**
- a. s2;
- b. "olus a new string"; o} = "The Final string " + s2;
- d. Compilation error message Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 15
**Requirement:** in the following C++ application, how many times the operator delete is called?

```cpp
#include <stdio.h>
#include <string.h>
class Student
i
public:
int age;
chart name;
public:
Student(int v = @, char* sname = NULL)
{
this->age = v;
if (sname f= NULL)
{
this->name = new char[strlen(sname) + 1];
strepy(this->name, 5name);
)
else
this->name = NULL};
}
Student(const Student& s)
{
this->name = new char[strlen(s.name) + 1];
strepy(this->name, s.name);
this->age = s.age;

Student operator+(Student& s)
{
Student tstud;
tstud.age = (this->age + s.age) / 2;
tstud.name = new char[strlen(this->name) + strlen(s.name) + 1];
strepy(tstud. name, this->name);
strepy(tstud.name + strien(this->name), s.name) ;
return tstud;
}
~Student()
{
if (this->name)
delete[] this->name;
}
void operator=(Student& s)
{
if (this->name)
delete[] this->name; 
,
this->name = new char[strlen(s.name) + 1];
strcpy(this->name, s.name) ;
this- age = s.age;
}

void main()
{
int agel = 21; int age2 = 28;
Student si(agel, “John");
Student s?(age2, “James");
$2 = si + 82;
Student s2 = si;
Student s4;
)
```

**Options:**
- a. 6times
- b. 5 times
- c. 7 times
- d. 4 times Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 16
**Requirement:** What will display the following Java code?

```java
import java. 
util .HashMap;
import java.util.Map;
final. class PhoneNumber {
private final short areaCode, prefix, LineNum;
public PhoneNumberCint areaCode, int prefix, int LineNum) {
this.areaCode = rangeCheckCareaCode, 999, "area code");
this.prefix = rangeCheck(prefix, 999, “prefix");
this.lineNum = rangeCheck(lineNum, 9999, “Line num”);
Y
private static short rangeCheckCint val, tnt max, String arg) î
if Gal < @ 
11 val > max)
throw new IllegalArgumentException(arg +": * + val);
return (short) val;
}
@0verride
public boolean equalsCObject 0) f
if (o == this)
return true;
if CiCo instanceof PhoneNumber))
return false;
PhoneNumber pn = CPhoneNumber) o;
return pn, LineNum == LineNum && pn.prefix == prefix && pn.areaCode ==
areaCode;
}
@Qverride public int hashCodeQ) { return 42; }
i
public class MainTest2 {
public static void main(String[] args)
{
Map<PhoneNumber, String> m = new HashMap<>();
m.putCnew PhoneNumber(707, 867, 5309), “Jenny;
m.putCnew PhoneNumber(708, 967, 5309), “Mark;
String vall = m.getCnew PhoneNumber(707, 867, 5309));
String val2 = m.getCnew PhoneNumber(7@8, 967, 5309));
System, ové.printinC'vali = "+ vall + ", val2 = “ + val2);
}
}
```

**Options:**
- a. valt = Jenny, val2 = Mark
- b. valt = Jenny, val2 = Jenny
- c. Nothing because of compilation error
- d. Nothing because of runtime error Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 17
**Requirement:** What will display the following Java code?

```java
import java.util.Arrays;
import java.util. EmptyStackException;
class Stack implements Cloneable {
private Object[] elements;
private int size = 9;
private static final int DEFAULT_INITIAL CAPACITY = 5;
public StackQ {
this.elements = new Object [DEFAULT_INITIAL. 
CAPACITY] ;
}
public void push(Object e) {
ensureCapacityO;
elements[sizet++] = e;
Hi
public Object popO {
af Csize == 0)
throw new EmptyStackException®,
Object result = elements[--size];
elements[size] = null; // Eliminate obsolete reference
return result;
}
private void ensureCapacityO { // Ensure space for at least one more
element .
if Celements. length == size)
elements = Arrays. copyOfCelements, 2 * size + 1);
+
@0verrida
protected Object clone() throws CloneNotSupportedException {
return super.clone();

@Qverride public String toString {
StringBuffer r = new StringBufferQ);
r.appendC ["+elements[0]);
int i= 1;
forCObiect o : elements) {
if > 1) r.append(", "+0);
L445
}
r.append("}");
return r.toStringQ;
i
public class MainTest2 {
public static void main(String[] args)
{
Stack sti = new StackQ);
sti.pushC°1"); st]. push("S"); st1.pushC"9");
try {
Stack st2 = (Stack) stL.cloneQ;
String ş = (String)stî.popQ);
System.out.printinC’stl = "+ stI.toStringO +", st2 = * + st2.toStringQ));
} catch CCloneNotSupportedException 8) {
@.printStackTrace();
}
```

**Options:**
- a. sit = (1,5, null, null, null], st2 = [1, 5, null, null, null]
- b. sti =[1, 5), si2 = [4,5]
- c. Nothing because of compilation error
- d. sti =([1, 5], st2 = [1, 5, 9] Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 18
**Requirement:** What will display the following Java code?

```c
import jova.util. Arrays;
public class MainTest2 {
public static void main(String... args) {
int sum = Arrays. streannew int(]{1, 2, 117)
„Filterți -> î >= 2)
„mapCi -> i * 3)
„Sun;
System. 
out. printfC"' sum = Xd", sum);
```

**Options:**
- a. sum = 39
- b. sum = 42
- c. Nothing because of compilation error
- d. Nothing because of runtime error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 19
**Requirement:** What will display the following Java code?

```c
interface FIFact {
int getValueCint num);
}
public class MainTest2 {
public static void main(String... args) {
FIFact myFactorialFunc = (num) -> {
int fact = 1;
forcint i = 1; i <= num; i+ 
{
fact = i * fact;
Hi
return fact;
3;
System. out.printinC"Factorial is " + myFactorialFunc.getValue(4));
i
```

**Options:**
- a. factorial is 24
- b. factorial is 6 ©) Nothing because of compilation error
- d. Nothing because.of runtime error Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 20
**Requirement:** What will display the following Java code?

```java
class Period i
private final Date start;
private final Date end;
public Period(Date start, Date end) {
if (start. comparețo(end) > 2)

throw new IllegalArgumentException(start + “ after * + end);
this.start
this.end
start;
end;
i]
It
}
public Date start {
return start;
}
public Date endQ) {
return end;
}
@Override
public String toString® { 
,
return new String("start = "+start+", end = “+end);
y
}
public class MainTestz {
public static void main(String[] args) î
Date start = new Date);
Date end = new DateQ);
Period pl = new Period(start, end);
Period p2 = new Period(start, end);
System. ovt.println("pi equals p2 - " + Cpl.equals(p2)));
end. setY¥ear(78);
System.out.printin("pl == p2 - "+ Cpl == p29);
Be
a) pi equals p2 - false în p1 == p2 - false
bj pi equals p2 - true în pl == p2 - false
e) Nothing because of compilation error
f) Nothing because of runtime error
Correct: a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 21
**Requirement:** What will display the following Java code?

```c
class MyGen<T>
i
T var;
void set 
(T var)
{
this.var = var;
i
T get
{
return var;

@SuppressWarningsC"unchecked”)
void set(String 5) {
var = (T) s;

}
public class MainTest2 {
public static void moin(String[] args) {

MyGen<Double> m = new MyGen<Double>Q);
m.setC"2034.5");
System. out. printiacm.getQ);
```

**Options:**
- a. 2034.5
- b. Nothing because of compilation error
- d. Nothing because of runtime error Correct: a
- e. 2034


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 22
**Requirement:** What will display the following Java code?

```java
import java.util.List;
import java.util. ArrayList;
public class MainTest2 {
public static void moin(String[] args) {
List<Integer> marks = new ArrayList<Integer>();
marks .add(34);
marks .add(32);
for (integer x : marks) {
System. oué.print(x + " ");

System.oué.printc’ # "9;
marks.add(1, 39);
for (Integer x : marks) {
System. oué.printcx +");
}System. 
out. print” # ");
System. 
out. printc” ” + marks. get(2));
System. 
out. printc’ “ + marks. indexOf@@));
System.ové.printC’ “ + marks. remove(2));
System. out.printc” # ");
for (Integer x 
: marks)
{
System. oué.printc” ° + x);

System. out. printinQ;
```

**Options:**
- a. 3432 4343032 # 32-1 32% 3430
- b. Nothing because of compilation error
- c. 3432 #343032 # 32-1 32# 343230
- d. Nothing because of runtime error Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 23
**Requirement:** What will display the following Java code?

```java
import java.util.List;
import java.util. ArrayList;
public class MainTestz. {
public static void main(String[] args) {

List<Integer> marks = new ArrayList<Integer>();
try {
marks.add(91); marks.add(73); marks.add(21);
marks. removeC73);
} catchCException e) {}
for Cinteger x : marks) {
System. out.printCx +" ");
```

**Options:**
- a. 917321
- b. compilation error
- c. 9121
- d. runtime error Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 24
**Requirement:** What will display the following Java code?

```java
import java.util. Arrays;
import java.util.List;
public class MainTest2 {
public static void main(String[] args)
i
List<Integer> numbers = Arrays.aslist(i@, 25, 35, 40);
int factor = 2;
System. out. printin(
numbers stream), 
fi lterCnumber -> number % 2 == 8)
„mapTolnt(e -> e * factor).sumQ);

Ei
```

**Options:**
- a. 100
- b. Nothing because of compilation error cj 220
- d. Nothing because of runtime error Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 25
**Requirement:** What will display the following Java code, if the given input in console îs “Hello Test!*?

```java
import java.io. BufferedReader;
import java.io. IOException;
import java.io. InputStreamReader ;
public class MainTest2 {
public static void main(String[] args)
{
String str =";
BufferedReader obj = new BufferedReader(new InputStreamReader(System. 
i);
do {
try {
str = (String) obj.readLineQ;
} catch (IOException e) î
```

**Options:**
- a. Hello Test
- b. Nothing because of compilation error
- c. Hello strong
- d. Nothing because of runtime error
- e. printStackTraceQ; ii System, out, print(str); } whileC!str.equalsC’strong"));


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 26
**Requirement:** What will display the following Java code?

```java
import java.io.File;
public class MainTest2 {
public static void main(String[] args)
{
String name = null;
File file = new File(".", name);
if(file.existsO)
System. 
out. printCExpal");
else
System. out.printC“Expe2");
a) 
runtime error
b} 
compilation error
ce} 
ExpOi
d) 
Exp02
Correct: a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 27
**Requirement:** How will be displayed the “car1.txt”, file after running the foliowing.Java code?

```java
import java.10.0bjectOutputStream;
import java.io. FileQutputStream;
import java.io. IOException;
class Car {
private int weight = @;
sn
private String type = 
“";
private String color ="";
public CarCint weight, String type, String color){
this.weight = weight; this.type = type; this.color = color;
}
public Integer getWeightQ) { return weight; }
public void setWeightCInteger weight) { this.weight = weight; }
public String getType() { return type; }
public String getColorQ { return color; }
public void setColor(String color) { this.color = color; }
public String toString® {
return “Car{" + “colore'* + color +
4", type = "7 + type + "', weight" + weight + '}';
wee

public class MainTest2 {
public static void main(String[] args)
{
try (FileOutputStream fos = new FileQutputStream("carl 
txt");
ObjectOutputStream out = new ObjectOutputStream(fos);) î
Car c = new Car(10, "BMW X5", “gri”);
out .writeObjectC" "+09;
3 catch CIOException e) {
@.printStackTrace();
}
}
?
, 
ove.
60 26 43 61. 72 7B 63 GF GC GF 72 30.27 67 Ja 69 
27-20 
20° 
"2 
t Carfeclor=‘ari?,
4302827 42:40. 52.20.58 35 27:2 20 77 65:69 67, 
68°74 30) 
tye 
1800 ASI, Weight=
a 
19)
aja 61, 72 7863 
GF 6C Be 70 30 27 67 72 69 27/2 20.74 79 70 65 20'30:20||tantcolarutari, “tyne =
p, 
24/27 42 4B 57 20 $8 
38.27/20 20 77 65 69 67 68 74 30 31.30 7D 
{BME XS! wel gheol Oy
AC 
20.7479. 78 OS RO 3020; 27-42-40 SF coloret grt! 
types 
GEN
cH 
74 30 34 30 
LOXBSy welohteto
d, 
The source code is incorrect and it cannot be compiled
Correct: a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 28
**Requirement:** How will be in HEX displayed the “car.txt” file after running the following Java code?

```java
import java.io. DatadutputStream;
import java.io. FileOutputStream;
import java.io. IOException;
class Car {
private int weight = @;
private String type = °";
nie
private String color = 
"";
public CarCint weight, String type, String color)f
this.weight = weight; this.type = type; this.color = color;
}
public Integer getWeight() 1 return weight;}
public void setWeightCInteger weight) { this.weight = weight; }
public String getTypeQ) { return type; } 
i
public String getlolorO { return color; } 
:
public void setColor(String color) { this.color = color; }
public String toString f{
return "Cart" + “color='" + color +
+", type = '" + type + "', weight=" + weight + ')';
wate
}
public class MainTest2 {
public static void main(String[] args)
{
try C(FileOutputStream fos = new FileQutputStream("car.txt");
DataQutputStream out = new DataQutputStream(fos);) {
Car c = new Car€1024, “BMW X5", "black";
out.writeInt(c.getWeightO);
out -writeUTFCc.getTypeQ));
out writelTFCc.getColor();
} catch CIOException e) {
e.printStackTrace();
}
00 00 04 00 00 06 42 4D 57 20 58 35 00 05 62 6C 61 63 6B
00 04 31 30 32 34 00 06 42 4D 57 20 58 35 00 05 62 6C 61 63 6B
00 00 09 C4 00 DO 06 42 4D 57 20 58 35 00 05 62 6C 61 63 6B
00 04.00 00 00 06 42 4D 57 20 58 35 00 05 62 6C 61 63 6B
ao 
ee
Correct: a
```


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 29
**Requirement:** What will display the following Java code?

```c
class A
{
}
int i = 195;

class 8 extends A
i
int i = 207;
}
public class MainTest2
{
public static void main(String[] args) {
Aa = new BO;
System. 
out. printinca.1);
}
}
```

**Options:**
- a. 105
- b. compilation error cy 207
- d. runtime error Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

### Question 30
**Requirement:** What will display the following Java code?

```c
class A
public AO {
System. 
out. printC"4 Class A Constructor");
}
i
class B extends A
{
public BO {
System. 
out. print("4 Class B Constructor");
}
}
class C extends B
public CO {
System. 
out. printC"4 Class C Constructor");

}
public class MainTest2
{
public static void main(String[] args)
{
Cc = new CO;
```

**Options:**
- a. #Class A Constructor# Class B Constructor# Class C Constructor
- b. compilation error
- c. #Class C Constructor# Class B Constructor# Class A Constructor
- d. runtime error Correct: a


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: *(not available — barem OCR unreadable)*

</details>
---

## Exam 2019

### Question 1
**Requirement:** Which of the following is an invalid class declaration in C++:

**Options:**
- a. class A { int x; };
- b. { };
- c. public class A { };
- d. static class


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) public class A { };**

</details>
---

### Question 2
**Requirement:** What will be the output for the following C++ source code:

```cpp
#include <iostream>
#include<stdio.h>
using namespace std;
class Utils {
public:
static short method(char* array, short length) {
short e = 0;
for (short i = 0; i < length; i++) {
if (array[i] != 0) {
break;
}
else {
cH;
}
}
return c;
}
}
int main(int rgc, char** argv) {
char v1[{8] = { 0, 0, 1, 3, 5, 0, 0, 0 };
short c = Utils::method(v1, 8);
for (short i = c; i < sizeof(v1/sizeof(v1[0]); i++) {
printf(" %02X,", v1 [i]);
}
return 0;
}
```

**Options:**
- a. There is no output because the source code has the compilation errors.
- b. 01, 03, 05
- c. 00, 00, 01, 03, 05, 00, 00, 00,
- d. 01, 03, 05, 00, 00, 00,


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) 00, 00, 01, 03, 05, 00, 00, 00,**

</details>
---

### Question 3
**Requirement:** Which operator should be overloaded in the following C++ code

```cpp
free?

to make the program error

Facultatea: Cibernetică Statistică și Informatică Economică
“#include <iostream>
Hinclude <string>
using namespace std;
class Box{
int capacity;
public:
Box(){}
Box(double capacity){
this->capacity = capacity;
}
)
int main(int argc, char const *arev[])
i
Box bl(10);
Box b2 = Box(14);
if(bi == b2){
cout<<"Equal";
else{
cout<<"Not Equal";
}
return 0;
}
```

**Options:**
- a. +
- b. =
- d. O
- e. =


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) =**

</details>
---

### Question 4
**Requirement:** What is the output of the following C program?

```c
#include <stdio.h>
void xyz(int pl, int *p2) {
++pl;
+4¥p2;
printf("%d%d"pl,*p2);
void main {
int 210;
xyz(at+,&a);
xyz(at+,&a);
printi('%d",a);
}
```

**Options:**
- a. 1011121313
- b. 1112131314
- c. 1011121213
- d. 1112131414


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 1011121313**

</details>
---

### Question 5
**Requirement:** What is the output of following C pro gram?

```c
Facultatea: Cibernetică Statistică. și Informatică Economica
#include <stdio.h>
void main()4
int i;
for(i= Litt <=1Li+-+)
fortei)
Pes
printf("%od", 
1);
}
```

**Options:**
- a. 12
- b. 11
- c. 13
- d. none of these


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) none of these**

</details>
---

### Question 6
**Requirement:** What will be the output of the following C code:

```c
int vi] = (1,2,3.4,5}, 2 = 5;
for (inti= 0;i<n/2; i++) 4
vf] *= v[n-i- 1;
v[n-i- 1) 4= vii:
v[i] = v[n -i- 1];
}
for (inti=0;i<n;it+) {
printed "v[i]);
)
```

**Options:**
- a. 54321
- b. 12345
- c. 00000
- d. None of the mentioned


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 54321**

</details>
---

### Question 7
**Requirement:** What is the output of following C program?

```java
#include <stdio.h>
void mainQ{
int a=1;
while(at++<=1)
while(at++<=2);
printf(’"%d",a);
What will be the output for the following Java source code:
package eu.ase;
import java.io.BufferedinputStream;
import java.io. BufferedOutputStream;

Facultatea: Cibernetică Statistică și Informatică Economică
import java.io,DatalnputStream;
import java.io.DataOutputStream;
import java.io. EOFException;
import java.io.FilelnputStream;
import java.io.FileOutputStream;
import java.io JOException;
public class Test {
public static void main(String[] args) +
double[] frequency = {12, 3, 21, 24};
int{] values = {7, 9, 10, 11};
try {
DataOutputStream out = new DataOutputStream(new
BufferedOutputStream(new FileOutputStream("test.txt")));
for (int i = 0; i < frequency length; i++) {
out. writeDouble(frequency[i]);
out.writeInt(values[i]);
}
out.flush();
out.closeQ);
DatalnputStream in = new DatalnputStream(new BufferedInputStream(new
FileInputStream("test.txt")));
try {
while (true) {
double frecv = in.readDouble();
int val = in.readint);
System.out.format("Value %d - %.2f frequency ", val, frecv);
}
} catch (EOFException e) {in.close();}
} catch GOException ioe) {ioe.printStackTrace();}
}
}
```

**Options:**
- a. Value 7 - 12.00 frequency Value 9 - 3.00 frequency Value 10 - 21.00 frequency Value 11 - 24.00 frequency
- b. The example generates compiler errors
- c. The example generates runtime exceptions
- d. Value 7 - 24.00 frequency Value 9 - 21.00 frequency Value 10 - 3.00 frequency Value 11 - 12.00 frequency


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) The example generates compiler errors**

</details>
---

### Question 8
**Requirement:** *(question 8 — could not be extracted from PDF)*


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a)**

</details>
---

### Question 9
**Requirement:** Which of the below is not an implementation of List interface?

**Options:**
- a. ArrayList
- b. Stack ce) LinkedList
- d. SessionList


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) SessionList**

</details>
---

### Question 10
**Requirement:** In the following C++ code how many times the string “A’s constructor called” will be

```cpp
printed?
#include <iostream>

Facultatea: Cibernetică Statistică și informatică Economică
#include <string>
using namespace std;
class A {
int ay
public:
AQ {
cout<<"A's constructor called";
}
}s
class B {
static Aa;
public:
BO {
cout<<"B's constructor called";
}
static A get() {
return a;
}
ys
AB:a;
int main(int argc, char const *argv[])
{
Bb;
```

**Options:**
- a. Shows {2
- b. Shows 16
- c. None of the mentioned
- d. Shows 24


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Shows {2**

</details>
---

### Question 11
**Requirement:** *(question 11 — could not be extracted from PDF)*


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c)**

</details>
---

### Question 12
**Requirement:** What is the output of the following C++ code?

```cpp
#include <iostream>
#include <string>
using namespace std:
class Box
int capacity;
public:
Box(Q){}
Box(double capacity)
this->capacity = capacity;
}
bool operator<(Box b){
return b.capacity <this->capacity? true : false;
ij
```

**Options:**
- a. Bl's capacity is smaller
- b. B2's capacity is smaller ¢) Error
- d. Segmentation fault


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) B2's capacity is smaller ¢) Error**

</details>
---

### Question 13
**Requirement:** What is the output of this C++ program?

```cpp
#include <iostream>
using namespace std;
class Mylnterface
{
public:

Facultatea: Cibernatică Statistică și Informatică Economică
virtual void Display) = 0;
h
class Class! : public Mylaterface
{
public:
void Display)
(
int a=5;
cout << a;
}
LE
class Class2 : public MyInterface
{
public:
void Display()
i
cout <<" 5" << endl;
}
hi
int main)
{
Class! objl;
objl.DisplayQ;
Class2-0bj2;
obj2.DisplayQ);
return 0;
}
```

**Options:**
- a. 5
- b. 10
- c. None of the mentioned
- d. 55


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) 5**

</details>
---

### Question 14
**Requirement:** What is the output of the following Java program:

```java
class B {
void printO {
System.out.printin(’Class B");
}
}
class A extends B {
@Override
public void print) {
System.out.printin("Class A");
}
)
public class $4405 {
public static void main(String{] args) {
Bb=new AQ;
```

**Options:**
- a. Class B
- b. Class A
- c. Compilation error message
- d. Runtime error message


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) Class A**

</details>
---

### Question 15
**Requirement:** What will happen when you attempt to compile and run the following Java code?

```java
public class JavaS1 {
static {
inta = 10;
static int a, b;
public static void main(String args[]) 4
ans
myMethodQ;
System.out.printin(a + b+at+);
}
public static void myMethod() {
pratt t+ Ha;
}
}
```

**Options:**
- a. Compile-time error
- b. prints : 3
- c. prints : 2
- d. prints : 43


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Compile-time error**

</details>
---

### Question 16
**Requirement:** What will be the output for the following Java source code:

```java
package eu.ase;
class. Container {
private String name,
private static Container instance = null;
private Container) {
this name = "NA";
public static Container getinstance() {
if (instance == null) {
instance = new Container();
}
return instance;
public void setName(String x) {
this name = x;
public String getName() {
yeturn this.name;
}

Lo
LI
CSIEA b1 i
Facultatea: Cibernetică Statistică si Informatică Economică
public class Test {
public static void main(String[] args) {
Container ob1 = Container.getInstance();
Container ob2 = Container.getInstance();
obl.setName("Container 1");
ob2.setName("Container 2"),
System.out.printin("s1=" + ob] .getName() + ", s2=" + ob2.geiName());
}
```

**Options:**
- a. sl=Container 1, s2=Container 2
- b. The example generates compiler errors
- c. sl=Container 2, s2=Container-2
- d. si=Container 1, s2=Container |


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) sl=Container 2, s2=Container-2**

</details>
---

### Question 17
**Requirement:** How many times the below loop will get executed?

```c
#include <stdio.h>
void main() {
inti:
j= 10;
for G=i==10 5 j<=105 j++) €
printf("\n%d",j);
}
}
```

**Options:**
- a. 1
- b. Compilation Error
- c. 11
- d. 10


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) 11**

</details>
---

### Question 18
**Requirement:** The following C++ program:

```cpp
#include<iostream>
using namespace std;
class Person { public: void Show() { cout << "a person”; } };
class Student : public Person { public: void ShowQ { cout << "a student"; } };
void main)
i
Person* p = new Student);
p->ShowQ;
delete p;
)
```

**Options:**
- a. does not compile because it contains syntax errors
- b. outputs “a student"
- c. outputs "a person"
- d. does not compile because we can't assign a Student to a Person


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) outputs “a student"**

</details>
---

### Question 19
**Requirement:** What is the output of the following C++ program?

```cpp
Facultatea: Cibernetică Statistică și Informatică Economică
#include <iostream>
using namespace stă;
void swap(int &a, int &b);
int main)
i
inta =5,b=10;
swap(a, b);
cout <<" În main “<<a << b;
return 0;
}
void swap(int da, int &b)
i .
int temp;
temp = a;
a=b;
```

**Options:**
- a. Inswap 105 In main 105
- b. In swap 105 In main 510
- c. In swap 510 In main 105
- d. None of the mentioned


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) In swap 510 In main 105**

</details>
---

### Question 20
**Requirement:** What will be the output for the following C++ source code:

```cpp
#include <iostream>
#include<stdio.h>
using namespace std;
class Utils {
public:
static void method(const char* array, short length, short* startOff, short* stopOff,
short* newLength) {
int 
i= 0;
*startOff = 0; *stopOff = length; *newLength = length;
while (array[i] == 0x00)
itt;
*startOff = i
while (array{length - 1] == 0x00)
length--;
if dength > i)
* newLength = (length - i);
else
*newLength = 0;
*stopOff = length;
}
};
int-main(int rec, char** argv) {
short startOff = 0; short stopOff = 0; short newLength = 0;
char v1[8] = (0, 0, 1,2, 0, 4, 0,0};
Utils:method(v1, 8, &startOff, &stopOft, &newLength);
10 / 14

ACADEMIA DE STUDH ECONOMICE DIN. BUCURESTI 
Facultatea: Cibernetică Statistică și Informatică Economică
printi” startOff = %d, stopOff = Yd, newLength = %d *, startOft, stopOFf,
newLength);
for (short i = startOfi i < stopOii; itt) {
printi“ %02X,", vi fil;
}
for (short i = 0; i < newLength; i++) {
printf(" %02X,", (&v1 {startOff) Li);
}
return 0;
}
```

**Options:**
- a. There is no output because the source code has the compilation errors.
- b. startOff = 2, stopOff= 6, newLength = 4 00, 00, 01, 02, 00, 04, 01, 02, 00, 04,
- c. startOff = 2, stopOff = 6, newLength = 4 01, 02, 00, 04, 01, 02, 00, 04,
- d. startOff= 2, stopOff = 6, newLength = 4 01, 02, 00, 04, 00, 00, 01, 02, 00, 04,


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) startOff = 2, stopOff = 6, newLength = 4 01, 02, 00, 04, 01, 02, 00, 04,**

</details>
---

### Question 21
**Requirement:** Which statement is not true in Java language?

**Options:**
- a. A public member of a class can be accessed in all the packages
- b. A protected member of a class can be accessed from its derived class
- c. A private member of a class cannot be accessed from its derived class
- d. A private member of a class cannot be accessed by the methods of the same class


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) A private member of a class cannot be accessed by the methods of the same class**

</details>
---

### Question 22
**Requirement:** What is the output of the following C++ pro gram?

```cpp
#include<iostream>
using namespace std;
class X {
int m;
public:
XO: m(0) 0
X(int mm): m(mm) {}
int getm() { return m; }
ie
class Y : public X
{
int a;
public:
Y(int nn) : n(n) (}
int getn() { return n; }
}
int mainQ)
4
Le
Y yobj(100);
cout << yobj.getmQ <<" " << yobj.getnQ) << endl;
)

ACADEMIA DE STUDH ECONOMICE DIN BUCURESTI
Facultatea: Cibernetică Statistică și Informatică Economică
```

**Options:**
- a. 10010
- b. 10 100
- d. 100 100
- e. 1010


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) *(see original PDF)***

</details>
---

### Question 23
**Requirement:** What will be the result of executing the following C code:

```c
#include <stdio.h>
void main) {
int i;
for(i=20, #10; i<"20; i++) {
printf("\n %d", i);
}
}
```

**Options:**
- a. Shows Îl
- b. Runtime Error
- c. Shows |
- d. Compilation Error


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) Shows Îl**

</details>
---

### Question 24
**Requirement:** What will be displayed by the following C++ program?

```cpp
“#include <iostream>
using namespace std;
class A
{
public:
int &g0
i
static int =10;
return i;
}
iz
class B
public:
```

**Options:**
- a. it displays 0
- b. it incorrectly addresses a class member | | Facultatea: Cibernetică Statistică și Informatică Economică “c) it incortectly uses the object reference
- d. it displays 10


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) it displays 10**

</details>
---

### Question 25
**Requirement:** Which of the below is not an implementation of Java Set interface?

**Options:**
- a. SortedSet
- b. TreeSet
- c. HashSet
- d. LinkedHashSet


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) SortedSet**

</details>
---

### Question 26
**Requirement:** What is the output of following program?

```c
#include <stdio.h>
void abe(int a) {
printi("%d "j-ba);
}
void main)
int a=10;
abe(++4);
abclatt);
printi("%d",a);
}
```

**Options:**
- a. 121314
- b. 131415
- c. 141414
- d. 121212


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) 141414**

</details>
---

### Question 27
**Requirement:** In C++, the constructor is executed when:

**Options:**
- a. aclass is declared
- b. an object is used
- c. an object is created
- d. an object goes out of scope


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: c) an object is created**

</details>
---

### Question 28
**Requirement:** The following program:

```cpp
#include<iostream>
using namespace std;
class Person
i
public:
Person() { id = countert++; }
void Show() { cout << "Person 4" << id << endl; }
private:
static int counter;
int id;
}
int Person::counter = 1;

Facultatea: Cibernetică Statistică şi informatică Economică
void main)
{
Person pl. p2, p3;
p2.ShowQ;
}
```

**Options:**
- a. outputs "Person #0"
- b. outputs “Person #2"
- c. outputs “Person #1"
- d. does not compile because it uses the variable counter before initialization


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: b) outputs “Person #2"**

</details>
---

### Question 29
**Requirement:** Which one from the next Java statements ig correct:

**Options:**
- a. abstract classes can contain non-abstract methods and instance variables
- b. interfaces can contain instance variables
- c. abstract classes can be instantiated in objects
- d. none of these answers


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: a) abstract classes can contain non-abstract methods and instance variables**

</details>
---

### Question 30
**Requirement:** Regarding virtual methods which statement is correct in Java:

**Options:**
- a. Modulul de specializare
- b. a method is virtual if the ‘virtual’ keyword is used
- c. none of these answers
- d. all non-static methods are virtual by default and design Notice: Each right answer has three points. Maximum number of points is 90. o 2909000000000 000900000000000e00o = 000000000009060000000e00000090o0 3% 000090290900000000000000e000eo Z ramenvoroo SEAT INSrRDaRanaasaszas SIL N | L_ = _ „o (09 so {20 leo leo fea] 2 [eo || | &| era] >] 9] 29 [eo ]09]09 [eo [eo [ea [eo [eo [en [en [eo [eo [eo | Codul variantei (1-6) : 2 = LI oe <


<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: d) all non-static methods are virtual by default and design Notice: Each right answer has three points. Maximum number of points is 90. o 2909000000000 000900000000000e00o = 000000000009060000000e00000090o0 3% 000090290900000000000000e000eo Z ramenvoroo SEAT INSrRDaRanaasaszas SIL N | L_ = _ „o (09 so {20 leo leo fea] 2 [eo || | &| era] >] 9] 29 [eo ]09]09 [eo [eo [ea [eo [eo [en [en [eo [eo [eo | Codul variantei (1-6) : 2 = LI oe <**

</details>
---
