# Rezolvări Subiecte CSIE3 - Admitere Master ASE

## Subiect 2024

### Întrebarea 1
**Cerința:** Tabelele ANGAJATI(id_angajat, nume, prenume, salariul, data_angajare, id_departament) și DEPARTAMENTE(id_departament, denumire_departament). Comanda:
```sql
SELECT DISTINCT d.*
FROM departamente d JOIN angajati a ON a.id_departament=d.id_departament
WHERE d.id_departament NOT IN
  (SELECT b.id_departament FROM angajati b
   WHERE b.salariul>=10000 AND b.id_departament IS NOT NULL);
```

**Variante:**
- a) afișează departamentele în care cel puțin un angajat are salariul sub 10000
- b) afișează departamentele în care toți angajații au salarii sub 10000
- c) generează eroare NOT IN
- d) generează eroare (subcerere multi-row)

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) afișează departamentele în care toți angajații au salarii sub 10000**

**Explicație:** Subcererea returnează departamentele care au cel puțin un angajat cu salariul ≥ 10000. NOT IN elimină aceste departamente, rămânând doar cele în care toți angajații au salariul < 10000. NOT IN funcționează corect cu subcereri multi-row.

</details>
---
---

### Întrebarea 2
**Cerința:** Care dintre următoarele concepte implementeaza o relaţie de tip IS-A (ESTE UN/O) intre clase?

**Variante:**
- a) incapsularea
- b) polimorfismul
- c) compunerea
- d) derivarea (moştenirea)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) derivarea (moştenirea)**

</details>
---

### Întrebarea 3
**Cerința:** Precizati care dintre urmatoarele declarari de variabile PL/SQL nu este corecta:

**Variante:**
- a) v_test BOOLEAN NOT NULL:= LENGTH(SUBSTR(ORACLE} 1,3) > 1;
- b) v_data DATE= SYSDATE - TO_DATE(‘10-07-2024,'DD-MM-YYYY'),
- c) v_text VARCHAR2(20) DEFAULT SUBSTR(‘ORACLE’,1,3);
- d) v_nr NUMBER:= TO_CHAR(SYSDATE, ' MM);


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) v_data DATE= SYSDATE - TO_DATE(‘10-07-2024,'DD-MM-YYYY'),**

</details>
---

### Întrebarea 4
**Cerința:** Care dintre urmatoarele variante de specificare a parametrului unei proceduri PL/SQL este corecta:

**Variante:**
- a) (p_param NUMBER(4,2))
- b) (p_param IN VARCHAR2(50))
- c) (p_param OUT VARCHAR2 := 'anonim')
- d) (p_param VARCHAR2)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) (p_param VARCHAR2)**

</details>
---

### Întrebarea 5
**Cerința:** Fie clasa C++, C_mea si in partea publica prototipurile:

```cpp
C_mea operator-(C_mea&);
friend C_mea operator-(C_mea&, C_meaé&);
Ce se poate spune despre cele doua prototipuri?
```

**Variante:**
- a) Sunt echivalente si supraincarca operatorul - pentru scaderea a doua obiecte de tip C_mea
- b) Primul prototip este eronat deoarece operatorul - se supraincarca doar prin functie friend
- c) Al doilea prototip este eronat deoarece operatorul - nu se supraincarca prin functie friend
- d) Primul prototip supraincarca operatorul unar - (de semn) in timp ce al doilea supraincarca operatorul - pentru scaderea a doua obiecte de tip C_mea


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Sunt echivalente si supraincarca operatorul - pentru scaderea a doua obiecte de tip C_mea**

</details>
---

### Întrebarea 6
**Cerința:** Fie tabela COMENZI (id_comanda NUMBER(5) PRIMARY KEY, id_ angajat NUMBER(S),

```sql
id. client NUMBER(S), data DATE) cu cel putin 200 de randuri (inregistrari).
Se considera urmatoarea functie PL/SQL;
CREATE OR REPLACE FUNCTION f_eheck_data (p_data comenzi.data%TYPE)
RETURN BOOLEAN
IS
BEGIN
IF p_data>SYSDATE-90 THEN
RETURN TRUE;
ELSE
RETURN FALSE;
END IF;
END;
/
Se considera urmatoarea comanda SQL-Oracle:
SELECT id_comanda, f_check_data(data) FROM comenzi;
Care afirmatie este corecta?
```

**Variante:**
- a) functia PL/SQL nu se compileaza cu succes deoarece este utilizat gresit operatorul de comparatie
- b) comanda SQL va afisa id-ul comenzilor si TRUE daca acestea au fost plasate in mai putin de 90 de zile de la data curenta
- c) functia PL/SQL se compileaza cu succes, iar comanda SQL va afisa doar comenzile recent incheiate (in mai putin de 90 de zile de la data curenta)
- d) functia PL/SQL nu se poate apela in comanda SQL deoarece tipul de date returnat nu este compatibil cu SQL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) functia PL/SQL nu se poate apela in comanda SQL deoarece tipul de date returnat nu este compatibil cu SQL**

</details>
---

### Întrebarea 7
**Cerința:** In-C++ o clasa este abstracta daca:

**Variante:**
- a) Se afla in relatie de mostenire cu cel putin doua clase
- b) Contine cel putin o functie friend
- c) Contine cel putin o metoda virtual pura
- d) Contine cel putin o metoda virtuala


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) Contine cel putin o metoda virtual pura**

</details>
---

### Întrebarea 8
**Cerința:** Care este rezultatul rularii urmatorului program C++?

```cpp
#include<iostream>
using namespace std;
class A f
private:
int v;
A(int v) { this->v = v; }
Static A* instance;
public:
static A* getlnstance(int v) {
if (instance == NULL) {
instance = new A(v);
}
return instance;
void print) {
cout << y;
}
A* Ac:instance = NULL;
int main) €
A* a= Angetinstance(10);
a->printQ;
A* b = Angetinstance(5);
b->printQ;
return 0;
}
```

**Variante:**
- a) 1010
- b) 105
- c) Va genera o eroare de compilare deoarece constructorul clasei A este privat
- d) 00


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 1010**

</details>
---

### Întrebarea 9
**Cerința:** Fie urmatoarea clasa C++:

```cpp
class A {
public:
virtual void f0 = 0;
};
Care dintre urmatoarele declaratii sunt corecte?
Aa; 
H#Declaratia |
```

**Variante:**
- a) *b; //Declaratia 2
- b) Declaratiile 2 si 4
- c) Declaratiile 2,4 si 5
- d) Declaratiile 1 si 2


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Declaratiile 2 si 4**

</details>
---

### Întrebarea 10
**Cerința:** Se considera urmatoarea secventa de comenzi SQL-Oracle:

```sql
CREATE TABLE angajati
(marca NUMBER(7) PRIMARY KEY,
nume VARCHAR2(20),
email VARCHAR2(20) UNIQUE,
localitate VARCHAR2(20));
INSERT INTO angajati VALUES (117, 'Toma’, NULL, "Bucuresti";
CREATE VIEW angajati_Buc AS
SELECT * FROM angajati
WHERE UPPER (localitate}“BUCURESTI;
DROP VIEW angajati, Buc;
ROLLBACK;
Precizati care dintre urmatoarele afirmatii este corecta:
```

**Variante:**
- a) comanda ROLLBACK va anula efectul comenzii de adaugare a inregistrarii in tabela
- b) efectul comenzii INSERT va fi automat salvat
- c) comanda INSERT va genera eroare deoarece valoarea coloanei email nu poate fi NULL
- d) comanda ROLLBACK va anula efectul comenzii de stergere a tabelei virtuale ut Fie.tabelele: ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30), prenume VARCHAR2(30), salariul NUMBER(10,2), data_angajare DATE, id_departament NUMBER(3)) avand 200 de randuri (iriregistrari), DEPARTAMENTE (id departament NUMBER(3) PRIMARY KEY, denumire departament VARCHAR2(30)) cu cel putin 200 de randuri (inregistrari). Se considera urmatoarea functie PL/SQL: CREATE OR REPLACE FUNCTION calcul. salariu (v_id departamente.id_ departament TYPE) RETURN NUMBER Is v_sal NUMBER(8,2); BEGIN SELECT AVG(salariul) INTO v_sal FROM angajati WHERE id_departament=v_id; RETURN v_sal; END; / Comanda SQL-Oracle: SELECT id_departament,denumire_departament,calcul_salariu(id_departament) salariul FROM departamente WHERE caicul_salariu(id_departament)> 10000;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) efectul comenzii INSERT va fi automat salvat**

</details>
---

### Întrebarea 11
**Cerința:** Funcția calcul_salariu(v_id) returnează AVG(salariul) din departamentul specificat. Comanda:
```sql
SELECT id_departament, denumire_departament, calcul_salariu(id_departament) salariul
FROM departamente
WHERE calcul_salariu(id_departament) > 10000;
```

**Variante:**
- a) funcția nu compilează (lipsă GROUP BY)
- b) eroare (lipsă join)
- c) nu poate fi apelată în WHERE (funcție de grup)
- d) va apela funcția și va afișa departamentele cu salariul mediu > 10000

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) va apela funcția PL/SQL și va afișa departamentele în care salariul mediu depășește 10000**

**Explicație:** Funcțiile PL/SQL pot fi folosite atât în SELECT cât și în WHERE. Funcția returnează NUMBER și rulează un SELECT AVG(salariul) INTO v_sal FROM angajati WHERE id_departament=v_id.

</details>
---
---

### Întrebarea 12
**Cerința:** Care va fi rezultatul rularii programului C de mai jos?

```c
#include <stdio.h>
int main) î
int a[5] = (1,2, 3, 4, 5};
for (int i = 0; 1< 5; i++)
if (char) a[i] == 'S‘)
printi "adi", ali);
else
printi("FAIL\n");
return 0;
}
```

**Variante:**
- a) . Programul va afisa codul ASCII al caracterului '5'
- b) Programul va genera o eroare la initializarea masivului
- c) Programul va afisa $
- d) Programul va afisa de $ ori "FAIL"


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Programul va afisa de $ ori "FAIL"**

</details>
---

### Întrebarea 13
**Cerința:** Precizati care dintre urmatoarele comenzi SQL-Oracle nu este corecta:

**Variante:**
- a) SELECT EXTRACT(SY SDATE,DD.MM.Y Y Y Y') data FROM dual;
- b) SELECT TRUNC(TO_DATE('26-JUL.-2024, 'DD-MON-YYYY"),, YEAR’) an FROM dual;
- c) SELECT DECODE(1+2,3,'DA'"NU’) test FROM dual;
- d) SELECT SUM(DECODE(LENGTH(ORACLE),6,1,0)) suma FROM dual;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) SELECT TRUNC(TO_DATE('26-JUL.-2024, 'DD-MON-YYYY"),, YEAR’) an FROM dual;**

</details>
---

### Întrebarea 14
**Cerința:** Ce va afisa urmatorul program C?

```c
#include<stdio,h>
union s
int x;
int y;
HE
void inc(union st)
{
taht;
tytt;
}
int main)
{ 
.
union s t;
ty=3;
tx =2;
inc(t};
printi('%od %d", tx, ty);
)
```

**Variante:**
- a) 33
- b) 44
- c) 34
- d) 22


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 33**

</details>
---

### Întrebarea 15
**Cerința:** Programul C++:

```cpp
finchide <iostream>
using namespace std;
class A
i
public:
A(){ cout << "A"; }
I
class. B: public A
{
public:
B()(cout << "B";}
class C: public B
{
public:
COL cout <<")
ja
int main()
{
```

**Variante:**
- a) c
- b) CBA OA
- c) *pe = new C; return 0; } va afisa:
- d) ABC


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) CBA OA**

</details>
---

### Întrebarea 16
**Cerința:** Care este rezultatul rularii urmatoarei secvente de cod C?

```c
Hinclude<stdia 
h>
int main)
{
for (;)printf(" Examen"),
return 0;
}
```

**Variante:**
- a) Getiereaza eroare de compilare deoarece sintaxa instructiunii for este gresita
- b) Tipareste o singura data “Examen”
- c) Ruleaza fara sa tipareasca nimic
- d) Tipareste “Examen” Ja infinit


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) Ruleaza fara sa tipareasca nimic**

</details>
---

### Întrebarea 17
**Cerința:** Care dintre urmatorii opertori nu pot fi supraincarcati?


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b)**

</details>
---

### Întrebarea 18
**Cerința:** Se considera tabelele:

```sql
PRODUSE (id_produs NUMBER(5) PRIMARY KEY, denumire produs VARCHAR2(30),
descriere VARCHAR2(50)) cu cel putin 10 randuri (inregistrari).
RAND_COMENZI (id_produs NUMBER(5), id_comanda NUMBER(5), pret NUMBER(8,2),
cantitate NUMBER(8,2)) cu cel putin 200 de randuri (inregistrari).
COMENZI (id_comanda NUMBER(5) PRIMARY KEY, id_client NUMBER(S), data DATE) cu
cel putin 100 de rânduri (inregistrari).
Precizati care este efectul comenzii SQL-Oracle:
CREATE. VIEW v_PRODUSE AS
SELECT denumire_produs, descriere, COUNT(c.id_comanda) numar_comenzi,
ROUND(A VG(re.pret),2) pretm
FROM produse p, rand_ comenzi re, comenzi.c
WHERE p.id_produs=rc.id_produs
and re.id_comanda=c.id_comanda
and EXTRACT(YEAR FROM data)<=2024
GROUP BY denumire_produs, descriere
HAVING COUNT(c.id_comanda) >#3;
```

**Variante:**
- a) jonctiunea dintre tabele nu se poate realiza deoarece tabela RAND COMENZI nu are PRIMARY KEY
- b) crearea unei tabele virtuale pe baza celor trei tabele prin care se vor selecta produsele care au fost comandate pe cel putin 3 comenzi pana in 2024 (inclusiv) o) se va afisa o eroare deoarece functia AVG este incorect utilizata
- d) se va afisa o eroare deoarece functia COUNT utilizeaza coloana id comanda din tabela COMENZI


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) crearea unei tabele virtuale pe baza celor trei tabele prin care se vor selecta produsele care au fost comandate pe cel putin 3 comenzi pana in 2024 (inclusiv) o) se va afisa o eroare deoarece functia AVG este incorect utilizata**

</details>
---

### Întrebarea 19
**Cerința:** Care dintre următoarele afirmatii este corecta?

**Variante:**
- a) Un obiect este un pointer al tipului de date al clasei
- b) O clasă este o instanță a obiectelor sale
- c) O clasă este o instanţă a tipului de date struct
- d) Un obiect este o instanță din clasa sa


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Un obiect este o instanță din clasa sa**

</details>
---

### Întrebarea 20
**Cerința:** Ce va afisa urmatorul cod C?

```c
*include<stdio.h>
int main() 4
printă"%d", 11 >> 2);
return 0;
}
```

**Variante:**
- a) 44
- b) 22
- c) 2
- d) 121


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 121**

</details>
---

### Întrebarea 21
**Cerința:** Bloc PL/SQL cu UPDATE care afectează 100 rânduri, apoi SELECT AVG INTO nr FROM angajati WHERE 1=2 (nu returnează rânduri). rez := SQL%FOUND;

**Variante:**
- a) afișează C
- b) afișează B
- c) afișează A
- d) utilizează incorect boolean

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) blocul PL/SQL ruleaza cu succes si afiseaza A**

**Explicație:** SELECT ... INTO cu funcție agregat (AVG) returnează întotdeauna un rând (chiar dacă e NULL). SQL%FOUND devine TRUE. Se afișează A.

</details>
---
---

### Întrebarea 22
**Cerința:** Ce afiseaza programul C++:

```cpp
#include <iostream>
using namespace std;
class A
{
public:
AQ €}
A(const A&) { cout << “Copiere 
"5; }
Facultatea; Cibernetica Statistică si informatica Economică
A& operator=(A x) { cout <<" Atribuire "; return *this; )
}
void main)
i
```

**Variante:**
- a) abl;
- b) Atribuire Copiere
- c) Copiere Copiere Copiere
- d) Copiere Copiere


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) Copiere Copiere Copiere**

</details>
---

### Întrebarea 23
**Cerința:** Functia TO_CHAR in SQL-Oracle:

**Variante:**
- a) poate fi utilizata pe parametri de tip NUMBER si DATE
- b) accepta doar parametri de tip VARCHAR2 si face conversia la tipul de date CHAR
- c) poate fi utilizata doar pe parametri de tip NUMBER
- d) accepta parametri de tip TIMESTAMP si va returna intotdeauna anul curent Se considera tabelele: PRODUSE (id_produs NUMBER(5) PRIMARY KEY, denumire_produs VARCHAR2(150), descriere V ARCHAR2(! 50), categorie VARCHAR2(50), pret_min NUMBER(8,2)) cu cel putin 100 de randuri (inregistrari). RAND_COMENZI (id_produs NUMBER(S), id comanda NUMBER(5), pret NUMBER(8,2); cantitate NUMBER(8,2)) cu cel putin 200 de randuri (inregistrari). Precizati care este efectul comenzii SQL-Oracle: UPDATE produse SET pret_min=pret_min*0.9 WHERE pret_min>(SELECT min(pret) from rand_comenzi) AND categorie IN (SELECT categorie FROM produse WHERE LOWER(denumire_produs) LIKE 'Yomonitor%'); Alegeti varianta corecta:


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) accepta parametri de tip TIMESTAMP si va returna intotdeauna anul curent Se considera tabelele: PRODUSE (id_produs NUMBER(5) PRIMARY KEY, denumire_produs VARCHAR2(150), descriere V ARCHAR2(! 50), categorie VARCHAR2(50), pret_min NUMBER(8,2)) cu cel putin 100 de randuri (inregistrari). RAND_COMENZI (id_produs NUMBER(S), id comanda NUMBER(5), pret NUMBER(8,2); cantitate NUMBER(8,2)) cu cel putin 200 de randuri (inregistrari). Precizati care este efectul comenzii SQL-Oracle: UPDATE produse SET pret_min=pret_min*0.9 WHERE pret_min>(SELECT min(pret) from rand_comenzi) AND categorie IN (SELECT categorie FROM produse WHERE LOWER(denumire_produs) LIKE 'Yomonitor%'); Alegeti varianta corecta:**

</details>
---

### Întrebarea 24
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(S) PRIMARY KEY, nume_angajat

```sql
VARCHAR2(30), prenume_angajat VARCHAR2(30), salariul NUMBER(10,2), data angajare
DATE, id_ functie VARCHAR2(30)) avand 100 de randuri (inregistrari).
Se considera urmatoarea secventa PL/SQL:
SET SERVEROUTPUT ON
DECLARE
nr NUMBER;
rez BOOLEAN;
BEGIN
UPDATE angajati SET salariul=salariul*0.1;
SELECT AVG(salariul) INTO nr FROM angajati WHERE 1=2;
rez:=SQL%FOUND;
IF rez THEN DBMS_QUTPUT.PUT_LINE('A"),
ELSIF rez=FALSE THEN DBMS OUTPUT.PUT_LINE(B);
ELSE DBMS _OUTPUT.PUT_LINE('C);
END IF;
END;
/
Precizati care dintre urmatoarele afirmatii este corecta:
```

**Variante:**
- a) blocul PL/SQL ruleaza cu succes si afiseaza C
- b) blocul PL/SQL ruleaza cu sucoes si afiseaza B
- c) blocul PL/SQL ruleaza cu succes si afiseaza A
- d) blocul utilizeaza incorect o variabila de tip boolean


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) blocul PL/SQL ruleaza cu succes si afiseaza C**

</details>
---

### Întrebarea 25
**Cerința:** Procedura P_CURSOR cu cursor explicit ordonat DESC după salariu, EXIT WHEN rowcount>=3.

**Variante:**
- a) top 3 din departamentul 90 cu salariul > mediu
- b) eroare EXIT din FOR
- c) eroare var
- d) toți angajații

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) blocul PL/SQL ruleaza cu succes si afiseaza un top al primilor 3 angajati din departamentul 90 cu salariul mai mare decat salariul mediu**

**Explicație:** Cursorul selectează angajații din dep. 90 cu salariul > mediu general, ordonat DESC. EXIT WHEN rowcount>=3 oprește după 3 iterații. EXIT poate fi folosit în FOR LOOP.

</details>
---
---

### Întrebarea 26
**Cerința:** Fiind date doua clase intr-o relaţie de tip derivare (moştenire), la definirea unui obiect de clasa

```c
derivata, constructorii se apeleaza în ordinea:
```

**Variante:**
- a) mai intai se apeleaza constructorul clasei derivate, apoi cel al bazei
- b) mai intai se executa constructorul clasei in care au fost definiti cei mai multi constructori
- c) mai intai se apeleaza constructorul clasei de baza, apoi cel al derivatei
- d) aleatoare


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) mai intai se apeleaza constructorul clasei de baza, apoi cel al derivatei**

</details>
---

### Întrebarea 27
**Cerința:** Se considera urmatoarea comanda SQL-Oracle:

```sql
SELECT CONCAT ('lon', UPPER((SUBSTR(‘Tonescv', 
1)))) || LENGTH (‘Ionescu’) parola
FROM DUAL;
Precizati care dintre urmatoarele afirmatii este corecta;
```

**Variante:**
- a) se afiseaza IonlONESCU7
- b) functia SUBSTR este o functie de grup
- c) se afiseaza Ion?
- d) functia CONCAT nu se poate utiliza in combinatie cu operatorul ||


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se afiseaza IonlONESCU7**

</details>
---

### Întrebarea 28
**Cerința:** Avand doua relatii R1 si R2, operatorul care permite crearea unei relatii R3. formata din

```c
inregistrarile din R1 si R2, fara a elimina duplicatele este:
```

**Variante:**
- a) JOIN
- b) UNION
- c) UNIONALL 4d) INTERSECT A


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) UNION**

</details>
---

### Întrebarea 29
**Cerința:** Care dintre urmatoarele optiuni poate fi utilizata pentru adaugarea unei noi coloane intr-o tabela in

```c
SQL-Oracle:
```

**Variante:**
- a) UPDATE TABLE ADD COLUMN column name ();
- b) ALTER TABLE table_name ADD COLUMN column, name ();
- c) ALTER TABLE table_name ADD column_name column _definition;
- d) MODIFY TABLE ADD column_name;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) MODIFY TABLE ADD column_name;**

</details>
---

### Întrebarea 30
**Cerința:** Programul C++:

```cpp
#include <iostream>
using namespace std;
class A {
int a;
public;
Acint v = 0): a€v) €
}
friend mt get_a(A p) {
return p.a;
}
}
class B :; public A {
float b;
public:
B(înt v = 0, float m = 0.0): A(v), b(m) {
}
};
intmaing {
```

**Variante:**
- a) Va genera eroare, membrii private in clasa de baza fiind intotdeauna inaccesibili in clasa derivata
- b) s(10, 3.14); cout << get_a(s); return 0; }
- c) Va genera eroare, campul a nefiind accesibil printr-o funcţie friend în clasa A
- d) Va afisa 10


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Va afisa 10**

</details>
---

## Subiect 2023

### Întrebarea 1
**Cerința:** Fie clasa C++ urmatoare:

```cpp
class A { 
    int x; 
public: 
    A(int v=0){x=v;} 
}; 
In care dintre liniile de cod urmatoare se creeaza un masiv cu 5 obiecte de tip A? 
    A v1[5];                            //Linia 1 
    A *v2[5];                           //Linia 2 
    A *v3 = new A[5];                   //Linia 3 
    A *v4 = (A *)malloc(5 * sizeof(A)); //Linia 4
```

**Variante:**
- a) Liniile 1,2 si 3
- b) Liniile 1,3 si 4
- c) Liniile 1 si 2
- d) Liniile 3 si 4


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Liniile 1,2 si 3**

</details>
---

### Întrebarea 2
**Cerința:** Se considera tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume_angajat

```sql
VARCHAR2(30), prenume_angajat VARCHAR2(30), salariul NUMBER(10,2), data_angajare 
DATE, id_functie VARCHAR2(30)) avand 100 de randuri (inregistrari). 
Fie urmatoarea secventa PL/SQL: 
SET SERVEROUTPUT ON 
DECLARE 
nr NUMBER; 
rez NUMBER; 
BEGIN 
UPDATE angajati SET salariul=salariul*0.1; 
SELECT COUNT(id_angajat) INTO nr FROM angajati; 
rez:=SQL%ROWCOUNT; 
IF rez=1 THEN DBMS_OUTPUT.PUT_LINE('A'); 
ELSIF rez>1 THEN DBMS_OUTPUT.PUT_LINE('B'); 
ELSE DBMS_OUTPUT.PUT_LINE('C'); 
END IF; 
END; 
/ 
Precizati care dintre urmatoarele afirmatii este corecta:
```

**Variante:**
- a) blocul PL/SQL ruleaza cu succes si afiseaza C
- b) blocul PL/SQL ruleaza cu succes si afiseaza B
- c) blocul PL/SQL genereaza o eroare deoarece nu se foloseste corect cursorul implicit
- d) blocul PL/SQL ruleaza cu succes si afiseaza A


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) blocul PL/SQL ruleaza cu succes si afiseaza A**

</details>
---

### Întrebarea 3
**Cerința:** Care va fi outputul generat de urmatorul program C?

```c
#include <stdio.h> 
void f(int* a, int n) 
{ 
    *a += *(a + n - 1) += 10; 
} 
 
void print(int* a, int n) 

 
 
 
 
      { 
    for (int i = 0; i < n; ++i) 
        printf("%d ", a[i]); 
} 
 
int main() 
{ 
    int a[5] = { 8, 2, 5 }; 
    f(a, 5); 
    print(a, 5); 
    return 0; 
}
```

**Variante:**
- a) 10 2 5 0 10
- b) 18 2 5 0 10
- c) 18 2 5 2 10
- d) 8 2 5 8 10


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 18 2 5 0 10**

</details>
---

### Întrebarea 4
**Cerința:** Care dintre instructiunile comentate sunt corecte in programul C de mai jos?

```c
#include <stdio.h> 
int main() 
{ 
 
char z='a'; 
 
char *const p = &z; 
 
p[0] = '1';  
//instructiune 1 
 
p++; 
 
//instructiune 2 
 
p = "Examen"; //instructiune 3 
    
return 0; 
}
```

**Variante:**
- a) 1+2+3
- b) 1+2
- c) 2+3
- d) 1


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 1**

</details>
---

### Întrebarea 5
**Cerința:** Care este rezultatul rularii urmatorului program C++?

```cpp
#include <iostream> 
using namespace std; 
class B; 
class A { 
    int a; 
public: 
    A():a(0) { } 
    void show(A& x, B& y); 
}; 
class B { 
private: 
    int b; 
public: 
    B():b(0) { } 
    friend void A::show(A& x, B& y); 
}; 
void A::show(A& x, B& y) { 
    x.a = 10; 

 
 
 
 
          cout << x.a << " " << y.b; 
} 
int main() { 
    A a; 
    B b; 
    a.show(a,b); 
    return 0; 
}
```

**Variante:**
- a) Va fi afisat 0 0
- b) Va fi afisat 10 0
- c) Va produce o eroare de compilare deoarece campul b din clasa B este inaccesibil in functia show
- d) Va produce o eroare de compilare deoarece functia show este incorect declarata ca functie prietena


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Va fi afisat 10 0**

</details>
---

### Întrebarea 6
**Cerința:** Ce rezultat va afisa urmatorul program C?

```c
#include <stdio.h> 
int main() { 
    int var = 01010; 
    printf("%d", var); 
    return 0; 
}
```

**Variante:**
- a) 520
- b) 4112
- c) 10
- d) 1010


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 520**

</details>
---

### Întrebarea 7
**Cerința:** Ce valoare se va afisa la consola la executia programului C++ de mai jos?

```cpp
#include<iostream> 
using namespace std; 
class A { 
    int a; 
    static int contor; 
public: 
    A(int v=0):a(v) { } 
    A(const A &t) { a = t.a; contor++;} 
    void set_a(int v){a=v;} 
    friend void print(); 
}; 
int A::contor = 0; 
void print(){ cout<<A::contor<<endl; } 
int main() 
{ 
   A *t1, *t2; 
   t1 = new A(100); 
   t2 = new A(*t1); 
   t1->set_a(1000); 
   A t3 = *t1; 
   A t4; 
   t4 = t3; 
   print(); 
   return 0; 
}
```

**Variante:**
- a) 1
- b) 2
- c) 3
- d) 0


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 2**

</details>
---

### Întrebarea 8
**Cerința:** Se considera tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume_angajat

```sql
VARCHAR2(30), prenume_angajat VARCHAR2(30), salariul NUMBER(10,2), data_angajare 
DATE, id_functie VARCHAR2(30)) avand 100 de randuri (inregistrari). 
Care dintre urmatoarele interogari SQL-Oracle va returna o valoare numerica:
```

**Variante:**
- a) SELECT ROUND(data_angajare,'YEAR') FROM angajati;
- b) SELECT NVL(LENGTH(SUBSTR(nume_angajat,1,5)),0) FROM angajati;
- c) SELECT TO_CHAR(ROUND(data_angajare, 'MONTH'),'Mon') FROM angajati;
- d) SELECT DECODE(TO_CHAR(data_angajare,'MM'),13,data_angajare-2, data_angajare+2) FROM angajati;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) SELECT NVL(LENGTH(SUBSTR(nume_angajat,1,5)),0) FROM angajati;**

</details>
---

### Întrebarea 9
**Cerința:** Fie doua relatii R1 si R2. In cazul restrictiei referentiale este adevarata urmatoarea afirmatie:

**Variante:**
- a) un atribut din R1 care are valori definite pe acelasi domeniu ca si cheia primara a lui R2 are rolul de a modela asocierea dintre cele doua relatii
- b) cheia primara din R1 poate fi null
- c) cheia primara din tabela parinte nu trebuie sa fie unica
- d) R1 si R2 trebuie sa aiba aceeasi extensie


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) un atribut din R1 care are valori definite pe acelasi domeniu ca si cheia primara a lui R2 are rolul de a modela asocierea dintre cele doua relatii**

</details>
---

### Întrebarea 10
**Cerința:** Care dintre urmatoarele optiuni poate fi utilizata la modificarea structurii unei tabele in SQL-

```c
Oracle?
```

**Variante:**
- a) DROP CONSTRAINT
- b) DELETE COLUMN
- c) UPDATE CONSTRAINT
- d) UPDATE TABLE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) DROP CONSTRAINT**

</details>
---

### Întrebarea 11
**Cerința:** Functia TRUNC in SQL-Oracle:

**Variante:**
- a) accepta parametri de tip TIMESTAMP si va returna intotdeauna prima ora din anul curent
- b) accepta parametri de tip VARCHAR2 si va afisa doar primele caractere din sir
- c) poate fi utilizata doar pe parametri de tip NUMBER
- d) poate fi utilizata pe parametri de tip NUMBER si DATE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) poate fi utilizata doar pe parametri de tip NUMBER**

</details>
---

### Întrebarea 12
**Cerința:** Ce se va intampla la executarea urmatorului program C++?

```cpp
#include <iostream> 
using namespace std; 
class A 
{ 
    static int x; 
public: 
    int getx() 
    { 
        return x; 
    } 

 
 
 
 
      }; 
class B 
{ 
public: 
    A f() 
    { 
        static A o; 
        return o; 
    } 
}; 
int main() 
{ 
    B b; 
    cout<<b.f().getx(); 
    return 0; 
}
```

**Variante:**
- a) Va fi afisata valoarea 0
- b) Va fi generata o eroare la link-editare deoarece variabila statica x nu este definita ci doar declarata
- c) Va fi afisata o valoare intreaga nedefinita
- d) Va fi generata o eroare la compilare deoarece functia f din clasa A este incorect definita


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Va fi generata o eroare la compilare deoarece functia f din clasa A este incorect definita**

</details>
---

### Întrebarea 13
**Cerința:** Se considera tabela PRODUSE (id_produs NUMBER(6), denumire_produs VARCHAR2(150),

```sql
descriere VARCHAR2(150), categorie VARCHAR2(50), pret_lista NUMBER(4)) si comanda 
SQL-Oracle: 
UPDATE produse 
SET pret_lista=pret_lista*1.1 
WHERE pret_lista>2500 
AND categorie IN  
(SELECT categorie FROM produse  
WHERE LOWER(denumire_produs) LIKE '%laptop%'); 
Alegeti varianta corecta:
```

**Variante:**
- a) afiseaza o eroare deoarece subcererea poate returna mai multe categorii de produse si operatorul IN nu este corect utilizat
- b) actualizeaza doar produsele care contin in denumire cuvantul „laptop”
- c) afiseaza o eroare deoarce subcererea nu se poate utiliza in UPDATE
- d) actualizeaza produsele care au pret_lista mai mare de 2500 si se afla in aceleasi categorii cu produsele care contin in denumire cuvantul „laptop”


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) afiseaza o eroare deoarece subcererea poate returna mai multe categorii de produse si operatorul IN nu este corect utilizat**

</details>
---

### Întrebarea 14
**Cerința:** Programul C:

```c
#include <stdio.h> 
#include <stdarg.h> 
int f(int n, ...) 
{ 
    va_list lp; 
    va_start(lp, n); 
    static int s = 0; 
    for (int i = 0; i < n; i++) 
    { 
        int v = va_arg(lp, int); 
        s =  v > s ? v:s; 
    } 

 
 
 
 
          va_end(lp); 
    return s; 
} 
int main() 
{ 
    int a = f(3, 10, 30, 20, 45); 
    int b = f(4, 10, 5, 15, 40); 
    printf("%d,%d", a,b); 
}
```

**Variante:**
- a) Afiseaza 60,30
- b) Afiseaza 45,40
- c) Afiseaza 30,40
- d) Afiseaza 105,70


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Afiseaza 60,30**

</details>
---

### Întrebarea 15
**Cerința:** De cate ori se va afisa cuvantul "Punct" la executia programului C++ urmator?

```cpp
#include<cstdlib> 
#include<iostream> 
using namespace std; 
class Segment; 
class Punct { 
    int x,y; 
public: 
    friend class Segment; 
    Punct():x(0),y(0){cout<<"Punct"<<endl;} 
    Punct(int x,int y){this->x=x;this->y=y;cout<<"Punct"<<endl;} 
}; 
class Segment{ 
    Punct *p1,*p2; 
public: 
    Segment(int x1,int y1,int x2,int y2){ 
        p1 = new Punct(x1,y1); 
        p2 = (Punct *)malloc(sizeof (Punct)); 
        p2->x=x2;p2->y=y2; 
    } 
}; 
int main() 
{ 
    Punct origine; 
    Segment segment(10,10,20,20); 
    return 0; 
}
```

**Variante:**
- a) O data
- b) De doua ori
- c) De trei ori
- d) Niciodata, va fi generata o eroare de compilare deoarece campurile x si y sunt inaccesibile in clasa Segment


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) De doua ori**

</details>
---

### Întrebarea 16
**Cerința:** Ce va afisa urmatorul program C?

```c
#include <stdio.h> 
int main() { 
    static int x = 10; 

 
 
 
 
          printf("%d", x); 
    for (int i = 0; i < 5; i++) { 
        static int x = 20; 
        printf(" %d", x++); 
    } 
    printf(" %d\n", x); 
    return 0; 
}
```

**Variante:**
- a) 10 10 10 10 10 10 10
- b) 10 20 20 20 20 20 10
- c) 10 10 11 12 13 14 15
- d) 10 20 21 22 23 24 10


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 10 10 10 10 10 10 10**

</details>
---

### Întrebarea 17
**Cerința:** Fie tabelele:

```sql
ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30), prenume 
VARCHAR2(30), salariul NUMBER(10,2), data_angajare DATE, id_departament NUMBER(3)) 
avand 200 de randuri (inregistrari). 
COMENZI (id_comanda NUMBER(5) PRIMARY KEY, id_angajat NUMBER(5) , id_client 
NUMBER(5), data DATE) cu cel putin 200 de randuri (inregistrari). 
Se considera urmatoarea functie PL/SQL: 
CREATE OR REPLACE FUNCTION afiseaza_salariul (v_id angajati.id_angajat%TYPE) 
RETURN NUMBER 
IS 
v_sal NUMBER(8,2); 
BEGIN 
SELECT salariul INTO v_sal FROM angajati WHERE id_angajat=v_id; 
RETURN v_sal; 
END; 
/ 
Comanda SQL-Oracle: 
SELECT id_angajat,afiseaza_salariul(id_angajat) salariul, COUNT(id_comanda) nr_comenzi 
FROM comenzi 
GROUP BY id_angajat,afiseaza_salariul(id_angajat);
```

**Variante:**
- a) nu va afisa nimic deoarece functia PL/SQL este apelata cu inregistrari din tabela COMENZI
- b) va apela functia PL/SQL si va afisa id-ul, salariul si numarul de comenzi incheiate de fiecare angajat care a intermediat comenzi
- c) functia PL/SQL nu poate fi apelata in comanda SQL deoarece contine o alta comanda SQL
- d) se va realiza un produs cartezian intre tabelele ANGAJATI si COMENZI deoarece lipseste jonctiunea dintre acestea


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) va apela functia PL/SQL si va afisa id-ul, salariul si numarul de comenzi incheiate de fiecare angajat care a intermediat comenzi**

</details>
---

### Întrebarea 18
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCHAR2(30), salariul NUMBER(10,2), id_departament NUMBER(3)) cu cel putin 10 
angajati in departamentul 50 si blocul PL/SQL: 
SET SERVEROUTPUT ON 
DECLARE  
nr_angajati NUMBER; 
sal_mediu NUMBER; 
BEGIN 
SELECT COUNT(id_angajat), AVG (salariul) INTO nr_angajati, sal_mediu FROM angajati 
WHERE id_departament=50; 
DBMS_OUTPUT.PUT_LINE(nr_angajati || ' ' || ROUND(sal_mediu,2)); 

 
 
 
 
      END; 
/ 
Care afirmatie este corecta?
```

**Variante:**
- a) blocul contine o eroare deoarece functiile de grup nu pot fi utilizate in blocuri PL/SQL
- b) blocul contine o eroare deoarece lipseste clauza GROUP BY
- c) blocul va afisa numarul mediu de angajati pe fiecare departament
- d) blocul va afisa numarul de angajati si salariul mediu din departamentul 50


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul contine o eroare deoarece lipseste clauza GROUP BY**

</details>
---

### Întrebarea 19
**Cerința:** Ce se va intampla la executia urmatorului program C++?

```cpp
#include <iostream> 
using namespace std; 
class A 
{ 
    int x; 
public: 
    A(int v): x(v) {} 
    int getx() { return x;} 
}; 
class B: private A 
{ 
    int y; 
public: 
    B(int v):A(v){} 
    int getx() { return A::getx();} 
}; 
int main() 
{ 
    B b(10); 
    cout<<b.getx(); 
    return 0; 
}
```

**Variante:**
- a) Va fi afisata valoarea 10
- b) Va fi generata o eroare de compilare deoarece constructorul clasei B este incorect invocat
- c) Va fi generata o eroare de compilare deoarece variabila x este inaccesibila
- d) Va fi afisata valoarea 0


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) Va fi generata o eroare de compilare deoarece variabila x este inaccesibila**

</details>
---

### Întrebarea 20
**Cerința:** Se considera tabelele:

```sql
CLIENTI (id_client NUMBER(5) PRIMARY KEY, nume_client VARCHAR2(30), email_client 
VARCHAR2(50)) cu cel putin 10 randuri (inregistrari).  
COMENZI (id_comanda NUMBER(5) PRIMARY KEY, id_client NUMBER(5), data DATE) cu 
cel putin 100 de randuri (inregistrari). 
Precizati care este efectul comenzii SQL-Oracle: 
CREATE VIEW v_clienti AS  
SELECT nume_client, email_client, COUNT(id_comanda) numar_comenzi 
FROM clienti cl, comenzi c  
WHERE cl.id_client=c.id_client and EXTRACT(YEAR FROM data)<=2023 
GROUP BY nume_client, email_client 
HAVING COUNT(id_comanda) >=5; 
 
 
 

 
 
 
 
      a)  
se va afisa o eroare in cazul in care nu exista nici un client care a incheiat comenzi pana in 
2023
```

**Variante:**
- b) jonctiunea dintre tabele nu se poate realiza deoarece tabela COMENZI nu are FOREIGN KEY
- c) se va afisa o eroare deoarece conditia pentru verificarea datei trebuie inclusa tot in clauza HAVING
- d) crearea unei tabele virtuale pe baza celor doua tabele prin care se vor selecta clientii care au incheiat cel putin 5 comenzi pana in 2023 (inclusiv)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) crearea unei tabele virtuale pe baza celor doua tabele prin care se vor selecta clientii care au incheiat cel putin 5 comenzi pana in 2023 (inclusiv)**

</details>
---

### Întrebarea 21
**Cerința:** Ce se va intampla la executarea urmatorului program C++?

```cpp
#include <iostream> 
using namespace std; 
class A { 
public: 
    virtual int f() { 
        return 2; 
    } 
}; 
class B : public A { 
public: 
    int f() { 
        return 3; 
    } 
}; 
int main() { 
    B b; 
    A *a = &b; 
    cout << a->f(); 
    return 0; 
}
```

**Variante:**
- a) Va fi afisata valoarea 2
- b) Va fi afisata valoarea 3
- c) Va fi afisata valoarea 0
- d) Va fi generata o eroare de compilare deoarece supraincarcarea functiei f este eronata


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Va fi generata o eroare de compilare deoarece supraincarcarea functiei f este eronata**

</details>
---

### Întrebarea 22
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCHAR2(30), salariul NUMBER(10,2), data_angajare DATE, id_functie 
VARCHAR2(30)) avand 100 de randuri (inregistrari). 
Se considera comanda SQL-Oracle: 
SELECT DISTINCT nume||' are salariul '||salariul  
FROM angajati  
WHERE EXTRACT (YEAR FROM data_angajare) < EXTRACT (YEAR FROM SYSDATE); 
Care din urmatoarele afirmatii este falsa?
```

**Variante:**
- a) afiseaza numele si salariul persoanelor angajate inainte de anul curent
- b) se implementeaza operatorul relational de proiectie
- c) se implementeaza operatorul relational de selectie
- d) se implementeaza operatorul relational de concatenare


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) se implementeaza operatorul relational de selectie**

</details>
---

### Întrebarea 23
**Cerința:** Se considera tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume_angajat

```sql
VARCHAR2(30), prenume_angajat VARCHAR2(30), salariul NUMBER(10,2), data_angajare 
DATE, id_functie VARCHAR2(30)) avand 100 de randuri (inregistrari). 

 
 
 
 
      Fie urmatoarea secventa PL/SQL: 
SET SERVEROUTPUT ON 
DECLARE 
var NUMBER:=0; 
CURSOR cursor1 IS SELECT * FROM angajati WHERE salariul > (SELECT AVG(salariul) 
FROM angajati) ORDER BY salariul DESC; 
BEGIN 
FOR var IN cursor1 LOOP 
DBMS_OUTPUT.PUT_LINE('Angajatul '||var.nume_angajat ||' are salariul: '||var.salariul); 
EXIT WHEN cursor1%rowcount>=3; 
END LOOP; 
END; 
/ 
Precizati care dintre urmatoarele afirmatii este corecta:
```

**Variante:**
- a) blocul PL/SQL ruleaza cu succes si afiseaza toti angajatii care au salariul mai mare decat salariul mediu
- b) blocul PL/SQL va genera o eroare deoarece nu se poate iesi cu EXIT dintr-un ciclu FOR
- c) blocul PL/SQL genereaza o eroare deoarece variabila var nu este definita si utilizata corect
- d) blocul PL/SQL ruleaza cu succes si afiseaza un top al primilor 3 angajati cu cel mai mare salariu


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) blocul PL/SQL ruleaza cu succes si afiseaza toti angajatii care au salariul mai mare decat salariul mediu**

</details>
---

### Întrebarea 24
**Cerința:** Care este rezultatul rularii urmatorului program C++?

```cpp
#include <iostream> 
using namespace std; 
class Punct 
{ 
    int x,y; 
public: 
    Punct(int a, int b):x(a),y(b){} 
    Punct operator+(Punct c){ 
        return Punct((x+c.x)/2,(y+c.y)/2); 
    } 
    friend ostream &operator<<( ostream &out, const Punct &p ) 
            {   out << "("<<p.x*2<<","<<p.y*2<<")";   return out; } 
}; 
int main() 
{ 
    Punct c1(0,2); 
    Punct c2(3,5); 
    Punct c3 = c1 + c2; 
    cout<<c3<<endl; 
    return 0; 
}
```

**Variante:**
- a) Va fi generata o eroare de compilare deoarece operatorul de afisare este incorect definit
- b) Se va afisa (3,7)
- c) Va fi generata o eroare de compilare deoarece operatorul de adunare este incorect definit
- d) Se va afisa (2,6)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Va fi generata o eroare de compilare deoarece operatorul de afisare este incorect definit**

</details>
---

### Întrebarea 25
**Cerința:** Fie tabelele:

```sql
PRODUSE (id_produs NUMBER(8) PRIMARY KEY, denumire_produs VARCHAR2(30)); 
RAND_COMENZI (id_comanda  NUMBER(6), id_produs NUMBER(8), cantitate NUMBER(7), 
pret NUMBER(7,2))  

 
 
 
 
      avand cel putin 200 de randuri precum si interogarea SQL-Oracle: 
SELECT denumire_produs, count(id_comanda) nr_comenzi, ROUND(AVG(cantitate*pret)) 
VAL_MEDIE  
FROM rand_comenzi r, produse p  
WHERE p.id_produs=r.id_produs 
GROUP BY denumire_produs  
HAVING COUNT(id_comanda) >=3; 
Care din urmatoarele afirmatii este adevarata?
```

**Variante:**
- a) se afiseaza denumirea produselor, numarul de comenzi pe care au fost comandate si valoarea medie a acetora daca au fost comandate pe cel putin 3 comenzi
- b) se afiseaza valoarea medie a comenzilor daca acestea contin cel putin trei produse
- c) jonctiunea dintre cele 2 tabele nu se poate realiza fara restrictia de FOREIGN KEY pe tabela RAND_COMENZI
- d) interogarea contine o eroare deoarece functia ROUND este incorect utilizata


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se afiseaza denumirea produselor, numarul de comenzi pe care au fost comandate si valoarea medie a acetora daca au fost comandate pe cel putin 3 comenzi**

</details>
---

### Întrebarea 26
**Cerința:** Care din urmatoarele functii sau instructiuni nu pot fi folosite direct in cadrul unei instructiuni

```sql
PL/SQL de atribuire:
```

**Variante:**
- a) SUM
- b) TO_NUMBER
- c) NVL
- d) ROUND


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) SUM**

</details>
---

### Întrebarea 27
**Cerința:** Considerand secventa urmatoare de cod C, ce realizeaza functia f?

```c
#include <stdio.h> 
void f(char str1[], char str2[]) 
{ 
 
while(*str1++ = *str2++); 
}
```

**Variante:**
- a) Copiaza str1 in str2
- b) Copiaza str2 in str1
- c) Compara continutul a doua siruri de caractere
- d) Utilizeaza incorect doua masive de caractere, deorece acestea nu sunt lvalues (nu ocupa o locatie identificabila in memorie)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Utilizeaza incorect doua masive de caractere, deorece acestea nu sunt lvalues (nu ocupa o locatie identificabila in memorie)**

</details>
---

### Întrebarea 28
**Cerința:** Programul C++ urmator:

```cpp
#include <iostream> 
using namespace std; 
class A 
{ 
public: 
    A() { cout<<"A"; } 
    ~A() {cout<<"-A"; } 
}; 
class B: public A 
{ 
public: 
    B(){ cout<<"B"; } 
    ~B() {cout<<"-B";} 
}; 

 
 
 
 
      int main() 
{ 
    B b; 
    return 0; 
} 
va afisa:
```

**Variante:**
- a) AB
- b) AB-A-B
- c) AB-A
- d) AB-B-A


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) AB-A-B**

</details>
---

### Întrebarea 29
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCHAR2(30), salariul NUMBER(8,2), id_departament NUMBER(3)) cu cel putin 100 
de randuri (inregistrari). Se considera urmatorul bloc PL/SQL: 
CREATE FUNCTION afiseaza_salariul (v_id id_angajat.angajati%TYPE) 
RETURN NUMBER 
IS 
v_sal NUMBER(8,2); 
BEGIN 
SELECT salariul INTO v_sal FROM angajati WHERE id_angajat=v_id; 
RETURN v_sal; 
END; 
/ 
Care dintre urmatoarele afirmatii este corecta:
```

**Variante:**
- a) se genereaza o eroare deoarece parametrul functiei este incorect specificat
- b) se genereaza o eroare deoarece variabila v_sal nu este initializata
- c) functia nu va putea fi apelata in cadrul unei interogari SQL
- d) in cazul in care nu exista niciun angajat cu id-ul specificat prin parametru, se va returna NULL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se genereaza o eroare deoarece parametrul functiei este incorect specificat**

</details>
---

### Întrebarea 30
**Cerința:** Fie tabela COMENZI (id_comanda NUMBER(5) PRIMARY KEY, id_angajat NUMBER(5) ,

```sql
id_client NUMBER(5), data DATE) cu cel putin 200 de randuri (inregistrari). 
Se considera urmatoarea functie PL/SQL: 
CREATE OR REPLACE FUNCTION f_data_comanda (p_data comenzi.data%TYPE) 
RETURN NUMBER 
IS 
BEGIN 
RETURN ROUND(MONTHS_BETWEEN(SYSDATE, p_data),0); 
UPDATE comenzi 
SET data=SYSDATE-30 
WHERE data=p_data; 
END; 
/ 
Si urmatoarea comanda SQL-Oracle: 
SELECT id_comanda, f_data_comanda(data) FROM comenzi; 
Care afirmatie este corecta?
```

**Variante:**
- a) functia PL/SQL se compileaza cu succes, iar comanda SQL va modifica data comenzilor incheiate in ziua primita ca parametru
- b) functia PL/SQL nu se poate apela in comanda SQL deoarece contine comanda UPDATE
- c) comanda SQL va afisa id-ul comenzilor si numarul de luni de la data plasarii acestora
- d) functia PL/SQL nu se compileaza cu succes deoarece contine comanda UPDATE BAR EM Seria ....... 1 ............ Data .~I ... ~f ~0..tN r. Codul variantei ( 1 - 6 ) • Modulul de specializare 0 •


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) functia PL/SQL nu se compileaza cu succes deoarece contine comanda UPDATE BAR EM Seria ....... 1 ............ Data .~I ... ~f ~0..tN r. Codul variantei ( 1 - 6 ) • Modulul de specializare 0 •**

</details>
---

## Subiect 2022

### Întrebarea 1
**Cerința:** Care dintre urmatoarele optiuni poate fi utilizata la stergerea unei tabele?

**Variante:**
- a) PRIOR
- b) CASCADE CONSTRAINTS
- c) CONNECT BY
- d) DELETE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) CASCADE CONSTRAINTS**

</details>
---

### Întrebarea 2
**Cerința:** Fie doua relatii R1 si R2. Operatia definita pe cele doua relatii, R1 si R2, care consta din construirea unei noi

```c
relatii R3, prin concatenarea unor tupluri din R1 cu tupluri din R2, pe baza unei conditii specificate explicit in 
cadrul operatiei, poarta denumirea de:
```

**Variante:**
- a) reuniune
- b) intersectie
- c) jonctiune
- d) produs cartezian


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) jonctiune**

</details>
---

### Întrebarea 3
**Cerința:** Fie secventa de cod C urmatoare:

```c
#include <stdio.h> 
int f1(int *a) 
{ 
    int n=sizeof (a)/sizeof (*a),s=0; 
    for(int i=0;i<n;i++){s+=a[i];} 
    return s; 
} 
int f2(int a[]) 
{ 
    int n=sizeof (a)/sizeof (*a),s=0; 
    for(int i=0;i<n;i++){s+=a[i];} 
    return s; 
} 
int f3(int a[],int n) 
{ 
    int s=0; 
    for(int i=0;i<n;i++){s+=a[i];} 
    return s; 
} 
 
int main() 
{ 
    int a[3] = { 8, 4, 5 }; 
    int n = sizeof (a)/sizeof (*a); 
    ... 
    return 0; 
} 
Care dintre urmatoarele apeluri ale functiilor f1, f2 si f3 vor intoarce corect suma elementelor vectorului a?
```

**Variante:**
- a) f1(a) si f2(a)
- b) f3(a,n)
- c) f1(a), f2(a) si f3(a,n)
- d) f1(a)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) f3(a,n)**

</details>
---

### Întrebarea 4
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30), prenume

```sql
VARCHAR2(30), data_angajare DATE, salariul NUMBER(10,2)) cu cel putin 100 de randuri (inregistrari) si 
blocul PL/SQL: 

 
 
 
 
             
SET SERVEROUTPUT ON 
DECLARE 
CURSOR cursor1 IS SELECT nume, salariul FROM angajati; 
vnume angajati.nume%TYPE; 
vsalariul angajati.salariul%TYPE; 
BEGIN 
OPEN cursor1; 
WHILE cursor1%NOTFOUND LOOP 
FETCH cursor1 INTO vnume, vsalariul; 
DBMS_OUTPUT.PUT_LINE('Angajatul '||vnume|| 'are salariul '||vsalariul); 
END LOOP; 
END; 
/ 
Care afirmatie este corecta?
```

**Variante:**
- a) blocul va afisa numele tuturor angajatilor din tabela ANGAJATI
- b) blocul se executa, dar nu afiseaza nimic
- c) blocul va afisa numele primului angajat din tabela
- d) blocul contine o eroare deoarece nu este corect utilizata conditia cursor1%NOTFOUND


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul se executa, dar nu afiseaza nimic**

</details>
---

### Întrebarea 5
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30), prenume

```sql
VARCHAR2(30), salariul NUMBER(10,2), comision NUMBER(4,2)).  
Se considera blocul PL/SQL: 
SET SERVEROUTPUT ON 
DECLARE  
v_venit NUMBER; 
BEGIN 
SELECT SUM(salariul*(1+NVL(comision,0))) INTO v_venit FROM ANGAJATI WHERE 
id_departament=50; 
DBMS_OUTPUT.PUT_LINE(v_venit); 
END; 
/ 
Care afirmatie este corecta?
```

**Variante:**
- a) blocul este eronat deoarece lipseste clauza GROUP BY
- b) blocul se va rula cu succes si se va afisa venitul total din departamentul 50 in cazul in care acesta exista si zero in cazul in care departamentul 50 nu exista
- c) in cazul in care departamentul 50 nu exista va apare un mesaj de eroare
- d) blocul se va rula cu succes si se va afisa venitul total din departamentul 50 in cazul in care acesta exista si nu se va afisa nimic in cazul in care departamentul 50 nu exista


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul se va rula cu succes si se va afisa venitul total din departamentul 50 in cazul in care acesta exista si zero in cazul in care departamentul 50 nu exista**

</details>
---

### Întrebarea 6
**Cerința:** Fie functia C definita in felul urmator:

```c
int f(int a,int b) 
{ 
    if (a<b) 
    { 
        return f(a+3,b-1); 
    } 
    else 
    { 
        return a + b; 
    } 
} 
Ce rezultat va intoarce apelul f(1000,2000)?
```

**Variante:**
- a) 1500
- b) 3000
- c) 3500
- d) Va genera eroare de executie si va afisa un mesaj de depasire stiva


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 3500**

</details>
---

### Întrebarea 7
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30), prenume

```sql
VARCHAR2(30), data_angajare DATE, salariul NUMBER(10,2)) cu cel putin 100 de randuri (inregistrari) si 
urmatoarea secventa de comenzi: 
CREATE OR REPLACE FUNCTION f_emp_vechime 
(p_data_angajare IN angajati.data_angajare%type)  
return NUMBER  
IS 
BEGIN 
RETURN to_number(round((sysdate-p_data_angajare)/365,0)); 
END f_emp_vechime; 
/ 
SELECT id_angajat, nume, prenume, f_emp_vechime(data_angajare)  
FROM angajati 
WHERE f_emp_vechime(data_angajare)>10; 
Care afirmatie este corecta?
```

**Variante:**
- a) instructiunea SELECT afiseaza angajatii cu vechimea mai mare de 10 ani
- b) instructiunea SELECT afiseaza angajatii cu vechimea mai mare de 10 zile
- c) functia f_emp_vechime returneaza numarul de zile dintre data curenta si data primita ca parametru
- d) se va genera o eroare deoarece functia f_emp_vechime nu poate fi utilizata in comanda SELECT


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) instructiunea SELECT afiseaza angajatii cu vechimea mai mare de 10 ani**

</details>
---

### Întrebarea 8
**Cerința:** Ce se va intampla la rularea urmatorului program C?

```c
#include <stdio.h> 
void f(int i); 
int main() 
{ 
    f(1); 
} 
void f(int i) 
{ 
    if (i > 10) 
        return ; 
    printf("%d ", i); 
    return f((i+=3, --i)); 
}
```

**Variante:**
- a) Se va afisa: 1 4 7 10
- b) Programul va rula fara sa afiseze nimic
- c) Va fi generata o eroare de depasire stiva
- d) Se va afisa: 1 3 5 7 9


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Se va afisa: 1 4 7 10**

</details>
---

### Întrebarea 9
**Cerința:** Sa se precizeze care dintre interogarile SQL-Oracle de mai jos afiseaza urmatoarea zi de duminica fata de data

```sql
curenta?
```

**Variante:**
- a) SELECT sysdate('SUNDAY') from dual;
- b) SELECT next_day('SUNDAY') from sysdate;
- c) SELECT last_day(sysdate, 'SUNDAY') from dual;
- d) SELECT next_day(sysdate, 'SUNDAY') from dual;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) SELECT next_day(sysdate, 'SUNDAY') from dual;**

</details>
---

### Întrebarea 10
**Cerința:** Ce va afisa urmatorul program C?

```c
#include "stdio.h" 
int main() 
{ 
    int i = 3; 
    goto LOOP; 
    i++; 

 
 
 
 
             
    for (i = 0; i < 10; i+=2) 
    { 
        printf("%d", i); 
    LOOP: 
        continue; 
        printf("%d", i++); 
    } 
    return 0; 
}
```

**Variante:**
- a) Nu va afisa nimic
- b) 356789
- c) 579
- d) 3579


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 3579**

</details>
---

### Întrebarea 11
**Cerința:** Care va fi valoarea afisata de urmatorul program C?

```c
#include <stdio.h> 
int main() 
{ 
    static int s=1; 
    for(int i=0;i<5;i++) 
    { 
        static int s=0; 
        s+=i; 
    } 
    printf(" %d", s); 
    return 0; 
}
```

**Variante:**
- a) O valoare intreaga nedefinita
- b) 10
- c) 11
- d) 1


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 1**

</details>
---

### Întrebarea 12
**Cerința:** Fie a, un masiv bidimensional de tip double cu n linii si n coloane, n intreg par.

```c
Care instructiune dintre cele specificate in raspunsurile de mai jos poate inlocui punctele de suspensie (...) din 
secventa de program C urmatoare, astfel incat executarea acesteia sa permita memorarea in variabila s a 
valorii sumei elementelor aflate pe diagonalele matricei? 
int s=0; 
for(int i=0;i<n;i++){ 
 
... 
}
```

**Variante:**
- a) s+=a[n-i-1][i]+a[i][n-i-1];
- b) s+=a[i][i]+a[i][n-i-1];
- c) s+=a[i][i]+a[n-i-1][n-i-1];
- d) s+=a[i][n-i-1]+a[n-i-1][i];


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) s+=a[n-i-1][i]+a[i][n-i-1];**

</details>
---

### Întrebarea 13
**Cerința:** Care dintre urmatoarele afirmatii despre cursorii expliciti in PL/SQL este adevarata?

**Variante:**
- a) la deschidere se utilizeaza intotdeauna clauza NOTOPEN
- b) stocheaza informatii cu privire la procesarea instructiunilor LCT (limbajul de control al tranzactiilor)
- c) pot fi declarati ca variabile si constante
- d) pot avea parametri


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) stocheaza informatii cu privire la procesarea instructiunilor LCT (limbajul de control al tranzactiilor)**

</details>
---

### Întrebarea 14
**Cerința:** Care va fi outputul generat la executia urmatorului program C?

```c
#include<stdio.h> 
int main() 
{ 
    int a[5] = { 5 }; 
    for (int i = 0; i < 5; i++){ 
        if ((char)a[i] != '5'){ 
            printf("FAIL "); 
        } else { 
            printf("%d ",a[i]); 
        } 
    } 
    return 0; 
}
```

**Variante:**
- a) FAIL FAIL FAIL FAIL 5
- b) 5 FAIL FAIL FAIL FAIL
- c) 5 5 5 5 5
- d) FAIL FAIL FAIL FAIL FAIL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 5 5 5 5 5**

</details>
---

### Întrebarea 15
**Cerința:** Ce se va afisa in urma executarii urmatorului program C?

```c
#include <stdio.h> 
#include <string.h> 
void f(char str1[], char str2[]) 
{ 
    if (*str1++ = *str2++) { f(str1, str2); } 
} 
int main() 
{ 
    int k='a'-'A'; 
    char a[100]; 
    f(a,"Examen Master 2022"); 
    for(int i=0;i<(int)strlen(a);i++) 
        a[i]=a[i]>='a'&&a[i]<='z'?a[i]-k:a[i]; 
    printf("%s",a); 
    return 0; 
}
```

**Variante:**
- a) EXAMEN MASTER 2022
- b) EXAMENMASTER
- c) XAMEN ASTER 2022
- d) Va genera o eroare deoarece functia f utilizeaza incorect doua masive de caractere care nu sunt lvalues


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) EXAMEN MASTER 2022**

</details>
---

### Întrebarea 16
**Cerința:** Se considera tabela PRODUSE (id_produs NUMBER(6), denumire_produs VARCHAR2(150), descriere

```sql
VARCHAR2(150), categorie VARCHAR2(50), pret_lista NUMBER(4)) si interogarea: 
SELECT denumire_produs, descriere  
FROM produse WHERE categorie IN  
(SELECT categorie FROM produse  
WHERE LOWER(denumire_produs) LIKE '%laptop%')  
AND pret_lista >100; 
Alegeti varianta corecta:
```

**Variante:**
- a) afiseaza produsele care au pret_lista mai mare de 100 si se afla in aceleasi categorii cu produsele care contin in denumire cuvantul „laptop”
- b) afiseaza doar produsele care contin in denumire cuvantul „laptop”
- c) afiseaza o eroare deoarce subcererea returneaza mai multe valori
- d) afiseaza o eroare deoarece operatorul LIKE nu este corect utilizat


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) afiseaza o eroare deoarce subcererea returneaza mai multe valori**

</details>
---

### Întrebarea 17
**Cerința:** Ce va afisa urmatorul program C?

```c
#include<stdio.h> 
int main() 
{ 
   printf("%d", 3<<2 ); 
   return 0; 
}
```

**Variante:**
- a) 9
- b) 2
- c) 12
- d) 6


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 2**

</details>
---

### Întrebarea 18
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30), prenume

```sql
VARCHAR2(30), salariul NUMBER(10,2), id_departament NUMBER(3)) cu cel putin 200 angajati care 
lucreaza in peste 10 departamente si blocul PL/SQL: 
SET SERVEROUTPUT ON 
DECLARE 
CURSOR cursor2 IS SELECT id_departament, COUNT(salariul) nr_angajati, AVG (salariul) sal_mediu 
FROM Angajati GROUP BY id_departament ORDER BY 2 DESC; 
r2 cursor2%rowtype; 
BEGIN 
FOR r2 IN cursor2 LOOP 
DBMS_OUTPUT.PUT_LINE('In departamentul '||r2.id_departament|| ' lucreaza '||r2.nr_angajati|| ' cu salariul 
mediu '||r2.sal_mediu); 
EXIT WHEN cursor2%ROWCOUNT>3; 
END LOOP; 
END; 
/ 
Care afirmatie este corecta?
```

**Variante:**
- a) blocul contine o eroare deoarece nu este corect utilizata conditia cursor2%ROWCOUNT
- b) blocul va afisa primele trei departamente cu cei mai multi angajati
- c) blocul va afisa toate departamentele
- d) blocul va afisa primele patru departamente cu cei mai multi angajati


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul va afisa primele trei departamente cu cei mai multi angajati**

</details>
---

### Întrebarea 19
**Cerința:** Fie tabela RAND_COMENZI (id_comanda  NUMBER(6), id_produs NUMBER(8), cantitate NUMBER(7),

```sql
pret NUMBER(7,2)) avand 100 de randuri precum si interogarea SQL Oracle: 
SELECT id_comanda, ROUND(AVG(cantitate*pret)) VAL_MEDIE  
FROM rand_comenzi  
GROUP BY id_comanda  
HAVING COUNT(id_produs) >=3; 
Care din urmatoarele afirmatii este adevarata?
```

**Variante:**
- a) interogarea contine o eroare deoarece clauza HAVING este incorect utilizata
- b) se afiseaza valoarea medie a produselor daca acestea apar pe cel putin trei comenzi
- c) se afiseaza valoarea medie a comenzilor daca acestea contin cel putin trei produse
- d) interogarea contine o eroare deoarece functia ROUND este incorect utilizata


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) interogarea contine o eroare deoarece functia ROUND este incorect utilizata**

</details>
---

### Întrebarea 20
**Cerința:** Care va fi outputul generat de urmatorul program C?

```c
#include <stdio.h> 
int f() 
{ 
  static int v = 10; 
  return v--; 

 
 
 
 
             
} 
 
int main() 
{ 
  for(f(); f(); f()) 
    printf("%d ", f()); 
  return 0; 
}
```

**Variante:**
- a) Va rula la infinit si va genera o eroare de executie pentru depasire stiva
- b) 8 5 2
- c) Va genera eroare de compilare deoarece bucla for este incorecta sintactic
- d) 8 6 4 2


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 8 5 2**

</details>
---

### Întrebarea 21
**Cerința:** In modelul relational pentru baze de date:

**Variante:**
- a) cheia primara nu trebuie sa fie unica
- b) proiectia, negatia si produsul cartezian sunt operatori din algebra relationala
- c) sunt utilizati operatori din algebra relationala
- d) selectia, conjunctia si jonctiunea sunt operatori din calculul relational


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) sunt utilizati operatori din algebra relationala**

</details>
---

### Întrebarea 22
**Cerința:** Care va fi numarul de afisari ale cuvantului Examen la rularea programului C de mai jos?

```c
#include <stdio.h> 
int main() 
{ 
    unsigned int i = 10; 
    for (; i; i >>= 1) 
        printf("Examen\n"); 
    return 0; 
}
```

**Variante:**
- a) 0
- b) 4
- c) 10
- d) 3


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 3**

</details>
---

### Întrebarea 23
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30), prenume

```sql
VARCHAR2(30), salariul NUMBER(10,2), id_departament NUMBER) avand 200 randuri (inregistrari). 
Precizati ce rezultat va furniza interogarea urmatoare: 
SELECT * FROM angajati a WHERE salariul > (SELECT MAX(salariul) FROM angajati WHERE 
id_departament=a.id_departament) 
ORDER BY salariul;
```

**Variante:**
- a) afiseaza angajatii care au salariul cel mai mare in departamentul in care lucreaza
- b) se executa, dar nu afiseaza nimic
- c) afiseaza toti angajatii indiferent de salariu deoarece conditia din subcerere este adevarata intotdeauna
- d) va apare o eroare deoarece lipseste clauza GROUP BY in subcerere


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) afiseaza angajatii care au salariul cel mai mare in departamentul in care lucreaza**

</details>
---

### Întrebarea 24
**Cerința:** Ce va afisa urmatorul program C?

```c
#include<stdio.h> 
int main() 
{ 
    char p[] = "ropot"; 
    char t; 
    int l = sizeof (p)/sizeof (p[0])-1; 
    for (int i= 0, j = l-1; i < j; i++) 
    { 

 
 
 
 
             
        t = p[i]; 
        p[i] = p[j]; 
        p[j] = t; 
    } 
    printf("%s", p); 
    return 0; 
}
```

**Variante:**
- a) ropot
- b) Nu va afisa nimic
- c) tropo
- d) topor


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) tropo**

</details>
---

### Întrebarea 25
**Cerința:** Care din urmatoarele functii SQL nu poate fi folosita in instructiuni de atribuire specifice PL/SQL?

**Variante:**
- a) AVG
- b) TO_DATE
- c) INSTR
- d) NVL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) NVL**

</details>
---

### Întrebarea 26
**Cerința:** Ce va afisa urmatorul program C?

```c
#include <stdio.h> 
int g(int n,int v) { 
    if (n) { 
        return g(n / 10,v) * 10 + n % 10; 
    } 
    else { 
        return v==n; 
    } 
} 
int main() 
{ 
    int n = 6779; 
    printf("%d",g(n,n)); 
}
```

**Variante:**
- a) 9776
- b) 6779
- c) 1
- d) 0


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 1**

</details>
---

### Întrebarea 27
**Cerința:** Ce valoare contine variabila C de tip double a, in urma atribuirii: a = 9 * 3 / 2 * 2 / 3?

**Variante:**
- a) 9
- b) 8
- c) 0
- d) Atribuirea va genera o eroare deoarece nu este permisa o expresie aritmetica formata doar din constante


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Atribuirea va genera o eroare deoarece nu este permisa o expresie aritmetica formata doar din constante**

</details>
---

### Întrebarea 28
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30), prenume

```sql
VARCHAR2(30), salariul NUMBER(10,2), data_angajare DATE, id_departament NUMBER(3)) avand 200 
randuri (inregistrari). 
Alegeti varianta corecta referitoare la urmatoarea comanda SQL: 
UPDATE angajati SET salariul=salariul *1.1 
WHERE EXTRACT(month from data_angajare) = EXTRACT(month from sysdate) 
AND id_departament IN (SELECT id_departament FROM angajati WHERE salariul > (SELECT 
AVG(salariul) FROM angajati));
```

**Variante:**
- a) se majoreaza doar salariile angajatilor care au in prezent salariul mai mare decat salariul mediu
- b) se majoreaza doar salariile persoanelor angajate in luna curenta, indiferent de zi sau an, daca acestea lucreaza in prezent intr-un departament in care toti angajatii au salariul mai mai mare decat salariul mediu
- c) instructiunea este eronata deoarece in tabela nu exista coloana sysdate
- d) se majoreaza salariile persoanelor angajate in luna curenta, indiferent de zi sau an, daca acestea lucreaza in prezent intr-un departament in care exista angajati care au salariul mai mai mare decat salariul mediu


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) se majoreaza doar salariile persoanelor angajate in luna curenta, indiferent de zi sau an, daca acestea lucreaza in prezent intr-un departament in care toti angajatii au salariul mai mai mare decat salariul mediu**

</details>
---

### Întrebarea 29
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(20), prenume

```sql
VARCHAR2(30), salariul NUMBER(10,2), id_departament NUMBER) avand 200 randuri (inregistrari). 
Se considera urmatorul bloc PL/SQL: 
SET SERVEROUTPUT ON 
DECLARE 
CURSOR cursor1 IS SELECT id_angajat, nume FROM angajati ORDER BY salariul DESC; 
vid angajati.id_angajat%TYPE; 
vnume CHAR (20); 
BEGIN 
OPEN cursor1; 
FETCH cursor1 INTO vid,vnume; 
DBMS_OUTPUT.PUT_LINE('Angajatul '||vnume); 
CLOSE cursor1; 
END; 
/ 
Precizati care dintre urmatoarele afirmatii este corecta:
```

**Variante:**
- a) afiseaza numele tuturor angajatilor ordonati descrescator in functie de salariu
- b) lucreaza cu un cursor implicit
- c) blocul PL/SQL genereaza o eroare deoarece lipseste structura repetitiva
- d) se afiseaza numele angajatului cu cel mai mare salariu


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) blocul PL/SQL genereaza o eroare deoarece lipseste structura repetitiva**

</details>
---

### Întrebarea 30
**Cerința:** Ce se va intampla la executia urmatorului program C?

```c
#include<stdio.h> 
struct st 
{ 
    int x; 
    struct st *next; 
}; 
int main() 
{ 
    struct st temp; 
    temp.x = 100; 
    temp.next = &temp; 
    printf("%d", temp.next->next->x); 
    return 0; 
}
```

**Variante:**
- a) Va fi generata o eroare de compilare deoarece recursivitatea in descrierea unei structuri nu este permisa
- b) Va fi afisata valoarea 100
- c) Va fi afisata valoarea 0
- d) Va fi afisata o valoare intreaga nedefinita Barem 1 b 2 c 3 b 4 b 5 d 6 c 7 a 8 d 9 d 10 c 11 d 12 b 13 d 14 d 15 a 16 a 17 c 18 d 19 c 20 b 21 c 22 b 23 b 24 c 25 a 26 b 27 b 28 d 29 d 30 b


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Va fi afisata valoarea 100**

</details>
---

## Subiect 2021

### Întrebarea 1
**Cerința:** Inversare șir "master" cu buclă for cu bug (j=strlen(p)-1 nu strlen(p)-1).

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) rastem**

**Explicație:** Buclă cu i<j; se swap p[i] cu p[j-i]. Rezultat conform baremului: "rastem".

</details>
---

### Întrebarea 2
**Cerința:** f(int*a,int n) { *a+=*(a+n-2)+=10; } a={10,20,30}; n=SIZE(a) — dar #define nu are ; (bug); f(a,5).

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 40 30 30**

**Explicație:** a[1]+=10 => 30. a[0]+=a[1] => 10+30=40. Rezultat: 40 30 30.

</details>
---

### Întrebarea 3
**Cerința:** SELECT id, ROUND(AVG(cant*pret)) FROM rand GROUP BY id_comanda HAVING COUNT(id_produs)>=3;

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) se afiseaza valoarea medie a comenzilor daca acestea contin cel putin trei produse**

**Explicație:** Similar cu 2022 Q19.

</details>
---

### Întrebarea 4
**Cerința:** Funcții C care returnează răsturnatul unui număr.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) f, w și h**

**Explicație:** f folosește iterativ m=m*10+n%10, w recursiv, h similar cu f. g e greșit pentru că înmulțește rezultatul apoi adaugă cifra actuală, dar la nivel corect matematic. Barem: a.

</details>
---

### Întrebarea 5
**Cerința:** struct st { int x; struct st next; }; — membru de tip struct NU pointer.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) Va fi generată o eroare de compilare deoarece recursivitatea în descrierea unei structuri nu este permisă**

**Explicație:** Un struct nu poate conține un membru de propriul tip (dimensiune infinită); doar pointeri.

</details>
---

### Întrebarea 6
**Cerința:** int a[5]={10}; print a[0..4];

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 10 0 0 0 0**

**Explicație:** Restul elementelor sunt inițializate cu 0 (default).

</details>
---

### Întrebarea 7
**Cerința:** for i<10: if(!i%3) print continue; else print break;

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 2**

**Explicație:** !i%3 se evaluează (!i)%3. i=0: !0=1, 1%3=1 (adevărat) => print "examen", continue. i=1: !1=0, 0%3=0 (fals) => else: print "examen", break. Rezultat: 2 afișări.

</details>
---

### Întrebarea 8
**Cerința:** f(a,b) { if(a<b) return f(a+2, b+1); else return a+b; } f(1544, 2152)?

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 5520**

**Explicație:** a<b infinitely because a+=2, b+=1, diff scade cu 1. Nr iterații=608 (2152-1544). a=1544+2*608=2760, b=2152+608=2760. Sum=5520.

</details>
---

### Întrebarea 9
**Cerința:** CREATE VIEW clienti+comenzi HAVING COUNT<10, WHERE EXTRACT(YEAR)<2021.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) crearea unei tabele virtuale... clientii care au incheiat pana in 2020 inclusiv mai putin de 10 comenzi**

**Explicație:** View cu clienți cu <10 comenzi până în 2020 inclusiv.

</details>
---

### Întrebarea 10
**Cerința:** SELECT sysdate INTO data FROM dual WHERE data IS NULL; EXCEPTION NO_DATA_FOUND print v.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se afiseaza data curenta** *(dar barem indică opțiunea de sus)*

Notă: analiza precisă — variabila 'data' e locală, NULL. Condiția WHERE data IS NULL e adevărată. Se selectează sysdate. Rezultat: data curentă.

</details>
---

### Întrebarea 11
**Cerința:** for cu switch; case 0: i+=10; continue; case 10: i+=10; break; case 20/30/default: i+=10.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 50** *(dar în listă apare "50" ca ans corect)*

**Explicație:** Analiza: i=0 → case 0: i=10, continue → i+=10=20. case 20: i=30, i=40 (fall-through default). break. print 40. i+=10=50. case 50 → default: i=60. print 60. Barem: 50 (probabil single print). Vezi barem oficial.

</details>
---

### Întrebarea 12
**Cerința:** CREATE FUNCTION cu parametru id_angajat.angajati%TYPE (invers).

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se genereaza o eroare deoarece parametrul functiei este incorect specificat**

**Explicație:** Sintaxa corectă: tabela.coloana%TYPE.

</details>
---

### Întrebarea 13
**Cerința:** Care afirmație despre normalizare nu este adevărată?

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) se transforma mai multe relatii cu extensii mai simple, in relatii mai complexe**

**Explicație:** Normalizarea descompune relații complexe în mai simple, nu invers.

</details>
---

### Întrebarea 14
**Cerința:** Opțiune pentru ștergerea tabelei.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) CASCADE CONSTRAINTS**

**Explicație:** La fel ca 2022 Q1.

</details>
---

### Întrebarea 15
**Cerința:** Cursori impliciți PL/SQL.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) sunt automat deschisi la comenzile LMD**

**Explicație:** Cursori impliciti se deschid automat la orice DML/SELECT INTO.

</details>
---

### Întrebarea 16
**Cerința:** UPDATE cu WHERE EXTRACT(year, data_angajare) = EXTRACT(year, sysdate)-1 AND id_functie IN (SELECT id_functie WHERE salariul < AVG).

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se majoreaza salariile persoanelor angajate anul trecut, indiferent de luna, daca acestea detin in prezent o functie similara cu angajatii care au salariul mai mic decât salariul mediu**

**Explicație:** Anul trecut = year-1, funcții cu cel puțin un angajat sub medie.

</details>
---

### Întrebarea 17
**Cerința:** În PL/SQL, pentru DROP TABLE folosim:

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) EXECUTE IMMEDIATE**

**Explicație:** DDL în PL/SQL se rulează prin dynamic SQL: `EXECUTE IMMEDIATE 'DROP TABLE ...'`.

</details>
---

### Întrebarea 18
**Cerința:** char str1[]="Examen"; char str2[]={'E','x','a','m','e','n'}; sizeof(str1)?sizeof(str2)?

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) n1=7, n2=6**

**Explicație:** str1 e literal string (are '\0'), size=7. str2 nu are '\0', size=6.

</details>
---

### Întrebarea 19
**Cerința:** SELECT WHERE categorie IN (SELECT ... LIKE '%laptop%') AND pret_lista>100.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) afiseaza produsele care au pret_lista mai mare de 100 si se afla in aceleasi categorii cu produsele care contin in denumire cuvantul "laptop"**

</details>
---

### Întrebarea 20
**Cerința:** union u {int x; char s[4];}; t.x=0; t.s[0]='1'; t.s[1]='1'; t.s[3]='1'; printf("%s",t.s);

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Se va afisa 11**

**Explicație:** s[0]='1', s[1]='1', s[2]=0 (deja 0 din x=0), s[3]='1'. String se termină la primul '\0': "11".

</details>
---

### Întrebarea 21
**Cerința:** union s {int x; int y;}; swap(t): int tmp=t.x; t.x=t.y; t.y=tmp; main: t.x=1, t.y=2; swap(t); print t.x, t.y;

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 22**

**Explicație:** union cu x și y pe aceeași memorie. t.x=1 apoi t.y=2 → memory=2. swap prin valoare (nu modifică main). Print: 2 2.

</details>
---

### Întrebarea 22
**Cerința:** WHERE salariul<5000 OR salariul>10000; care afirmație e falsă?

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) se implementeaza operatorul de intersectie**

**Explicație:** OR e uniune, nu intersecție.

</details>
---

### Întrebarea 23
**Cerința:** WHILE cursor1%FOUND LOOP FETCH...

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul ruleaza, dar nu afiseaza nimic**

**Explicație:** Similar cu 2022 Q4 — după OPEN, %FOUND e NULL/false, nu intră în buclă.

</details>
---

### Întrebarea 24
**Cerința:** int f(int*x, int y) {*x-=y; y+=*x; *x=y-*x; return *x>y?*x:y;} main: j=5, k=10; l = f(&j,k)==f(&k,j); print j,k,l;

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 10 10 1**

**Explicație:** Funcția swap valori. După f(&j,10): j devine 10. După f(&k,j): unde j e deja 10, k devine 10. Rezultat 10==10 → l=1. Print 10 10 1.

</details>
---

### Întrebarea 25
**Cerința:** Similar cu 2023 Q14 dar cu s += v>s ? v-s : 0.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Afișează 30,30**

**Explicație:** static s păstrat. Primul: max(10,30,15)=30. Al doilea: s deja 30, cu 40 s ar deveni 40. Barem: 30,30 (probabil pentru că se apelează cu n=3 chiar dacă sunt 4 args ulterior).

</details>
---

### Întrebarea 26
**Cerința:** SELECT COUNT+AVG INTO nr,sal FROM angajati WHERE id_dep=50.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) blocul va afisa numarul de angajati si salariul mediu din departamentul 50**

</details>
---

### Întrebarea 27
**Cerința:** Funcții nested cu static int y=2; y+=2; x+=2; f(x)+g(x) unde x global=3.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 47**

**Explicație:** Ordine de evaluare stânga-dreapta. f(10) apelează g(15): y=4, x=5, ret 5+4+15=24. f returnează 24. g(10) în main: y=6, x=7, ret 7+6+10=23. 24+23=47.

</details>
---

### Întrebarea 28
**Cerința:** Restricția referențială.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) un atribut din R1 care are valori definite pe acelasi domeniu ca si cheia primara a lui R2 are rolul de a modela asocierea dintre cele doua relatii**

</details>
---

### Întrebarea 29
**Cerința:** Funcție care NU poate fi folosită direct în atribuire PL/SQL.

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) MAX**

**Explicație:** Funcțiile agregat nu pot în atribuire directă.

</details>
---

### Întrebarea 30
**Cerința:** int i=5; goto LOOP; for(i=0;i<10;i++) { print i; LOOP: continue; }

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 6789**

**Explicație:** goto sare la LOOP cu i=5. continue → i++=6. print 6. LOOP continue → i=7. print 7. Etc. Rezultat: 6789.

</details>
---

## Subiect 2020

### Întrebarea 1
**Cerința:** Ce va afişa următorul program C?

```c
#include <stdio.h>
int main)
{
int 
x = 5, y 
= 10, 
2 = 15;
x= y == zi
printf ("%d", x);
getchar 
() ;
}
```

**Variante:**
- a) 0
- b) 5
- c) 10
- d) 15


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 2
**Cerința:** Ce va afişa următorul program C?

```c
int suma_swap (int* x, int y)
{
ex == ys
yo t= *x;
ex = ¥ - Fx;
return *x+¥7;
}
int main()
i
int î=0, 7 = 1, k=5, Ll;
1 = suma_swap(&j, k) == suma swap(&k, 3)
printf ("%d %d $d %d", i++, J, k, L);
}
```

**Variante:**
- a) 0550
- b) 055I 01550
- d) 1551


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 3
**Cerința:** Care va fi outputul generat de următorul program Cc?

```c
#include<stdio.h>
int main)
{
chart si] = { "timpul", "costa", "bani" };
char** p;

p= si
printf (‘tis ", ++* (++p+1));
printf ("ss ", *po-)+
printt ("%s ", *p):
}
```

**Variante:**
- a) ani costa timpul
- b) bani costa timpul
- c) ani timpul costa
- d) ani bani costa


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 4
**Cerința:** Ce se va întâmpla la execuţia următorului program C?

```c
#inchide<stdio.h>
int main)
int x[] = { 10, 20, 30,40); 
Bes
int *p = (int*)(&x+1);
printi("%d *, *(p - 2));
}
```

**Variante:**
- a) Va afişa 30
- b) Va afişa 20
- c) Va afişa o valoare întreagă nedefinită
- d) Va genera o eroare de compilare deoarece variabila p este incorect iniţializată


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 5
**Cerința:** Fie următoarea secvenţă de cod C:

```c
#include<stdio.h>
void init(...) 
€
for (int i = 0; i < 3; itt)
lil (4) = 4;
i
}
int main()
{
int x{31] 1317
init (x) i

Li
Care dintre următoarele variante de parametru formal în metoda ini/() este potrivit pentru ca
metodă să initializeze corect elementele de pe diagonala principală ale matricei x cu 1?
```

**Variante:**
- a) int x{][3]
- b) int x7]
- c) int **x
- d) int *x[3]


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 6
**Cerința:** di

```c
Care va fi outputul generat de următorul program C?
#include <stdio.h>
int main)
{
for (int i = 0; i < 20; i++)
i
switch (i)
{
case 9:
i += 57
case 5:
it=5;
break;
case 10:
i += 5;
case 15:
i+= 5;
default:
i t= 4;
break;
}
printi ("âd ", i);
}
}
```

**Variante:**
- a) 10 1520
- b) 5 10 1520
- c) 1024
- d) 10 15 24


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 7
**Cerința:** Care va fi rezultatul rulării următorului program C?

```c
#include<stdio.h>
int f(int a)
{
if (a<12)
{
return f(f(a+2))7

}
else
return a - 1;
}
}
int main)
{
printe ("&d", f(-1800))7
}
```

**Variante:**
- a) Va afişa ||
- b) Va afişa -1801
- c) Va afişa 12
- d) Va genera eroare de execuţie şi va afişa un mesaj de depăşire stivă


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 8
**Cerința:** Ce va afişa următorul program C?

```c
#include <stdio.h>
glint x)
{
statia int y = 2;
yrwed:
return y + x;
f{int x}
int y = 5;
return g(xty) ;
}
int main()
{
int x = 5;
printi ("să ", f(x) + g(x))e
}
```

**Variante:**
- a) 22
- b) 21
- c) 18
- d) O valoare întreagă nedefinită


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 9
**Cerința:** Ce se va întâmpla la rularea următorului program Cc?

```c
#include<stdic-h>
union test
{
int x;
char ars [4];

Vi
int main({)
{
union test t;
tix = 0;
t.arr [1] = 'G'; t.arr(2] = 'O';
printi ("ts", t.arc);
}
```

**Variante:**
- a) Va rula fără să afişeze nimic
- b) Va afişa 0
- c) Va afișa GOL
- d) Va afișa o valoare întreagă nedefinită


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 10
**Cerința:** Ce va afișa următorul program C?

```c
#include<stdio.h>
#include<string.h>
int main)
{
tearc([3] = 'L';
char pl] = "noroc";
char t;
for (int i= 0, j = strlen(p); i <4; itt)
i
t = piil;
plil = pis - il;
pip - i] = te
}
printf ("%s", pp);
}
```

**Variante:**
- a) Nu va afişa nimic
- b) noroc
- c) coren
- d) ecece


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 11
**Cerința:** Precizati valoarea afișată prin apelul printf ("%d",045) ;

**Variante:**
- a) 37
- b) 45
- c) 69
- d) caracterul cu codul ASC] 45 12. Răspunsuri corecte: a sib Ce va afisa următorul program C? Hinclude <stdio.h> int maing) { int x = 8; n printi ("%d,%d,3d", xt+, x SO 2, a >> 1); “a J


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 12
**Cerința:** int x=8; print x++, x<<2, x>>1;

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 8 36 4** *și b) 9 36 4* (răspuns dublu)

**Explicație:** Comportament nedefinit (order of evaluation). Compilatorul poate produce a sau b.

</details>
---
---

### Întrebarea 13
**Cerința:** Fie funcţia:

```c
int E(int vi], int k}
{
int t;
if (k==0) return v{k];
else return vik-1]<(t=f(v,k-1)) ? v[k-1] 
: t;
}
unde + este un vector de numere întregi şi & > 0 este numărul de elemente al vectorului v.
Ce returnează funcţia f?
```

**Variante:**
- a) Elementul minim din vectorul v
- b) Elementul maxim din vectorul v
- c) Elementul v[0]
- d) Elementul v[&-l]


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 14
**Cerința:** Programul:

```c
ținolude <stdio.h>
int f(int x, int y)
{
static int t = 0;
tr x tye
return t;
}
int maing)
{
printét("%d,", f45, 6));
printe ("sa", f47, 8));
```

**Variante:**
- a) Afişează 11,26
- b) Afişează 11,15
- c) Afişează 5,12
- d) Generează o eroare de compilare deoarece funcţia freturnează o variabilă locală (7)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 15
**Cerința:** Programul:

```c
#include <stdio.h> 
: 
ek
#include <stdarg.h> 
. 
;
int f(int n, ...)
{
va_list lp;
va_start(ip, nm};
int s = 07
for (ink i = 0; i <n; itt)
i
int v = va_arg(1p, int) ;
s += 
v> & ? v-s:07
}
va_end(1p) 7
return s;
)
int main)
{
printi ("%d,%d", f(3, 3, 20, 3), f(2, 10, 2, 30, 4)):
}
```

**Variante:**
- a) Afişează 20,10
- b) Afişează 23,42
- c) Afişează 3,10
- d) Generează o eroare deoarece functia feste incorect definită din punct de vedere sintactic


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 16
**Cerința:** Fie două relaţii RI si R2. In cazul restricției referenţiale care afirmaţie este adevarata?

**Variante:**
- a) un atribut din RI care are valori definite pe același domeniu ca si cheia primară a lui R2 are rolut de a modela asocierea dintre-cele două relații
- b) cheia primară din RI referă obligatoriu cheia primară din R2
- c) cheia primară din tabela părinte nu trebuie să fie compusă
- d) RI şi R2 trebuie să fie neapărat distincte


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 17
**Cerința:** Care dintre următoarele afirmaţii despre normalizare nu este adevărată?

**Variante:**
- a) se transformă mai multe relaţii cu o structură mai simplă, în relaţii mai complexe
- b) -se urmărește eliminarea anomaliilor de adăugare
- c) se urmăreşte reducerea redundantei Ă
- d) atributele dintr-o relaţie normalizată trebuie să fie atomice (i.¢., să nu mai poată fi descompus în alte atribute) =


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 18
**Cerința:** f

```c
i
In SQL din Oracle, pentru a finaliza o tranzacție și a salva modificările realizate se folosește;
comanda:
```

**Variante:**
- a) COMMIT
- b) COMMIT ON TRANSACTION
- c) SET ROLLBACK = OFF
- d) SET AUTOCOMMIT = TRUE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 19
**Cerința:** Se considera tabelele:

```sql
CLIENTI (id_client NUMBER(S), nume_client VARCHAR2(30), email VARCHAR2(50)) cu
cel putin 10 de rânduri (inregistrari).
COMENZI (nr_comanda NUMBER(5) PRIMARY KEY, id_ client NUMBER(S), data DATE) cu
cel putin 100 de rânduri (inregistrări).
Precizati care este efectul comenzii SQL in Oracle:
CREATE VIEW V_ CLIENTI AS
SELECT nume cliente email, COUNT 
(nr _ comanda) numar_comenzi
FROM clienti cl, comenzi c
WHERE cl.id_client=c.id client
GROUP BY 
nume client, email
HAVING COUNT (nr_comanda) >=3;
```

**Variante:**
- a) crearea unei tabele virtuale pe baza celor două tabele prin care se vor selecta clienţii care au încheiat cel puţin 3 comenzi
- b) crearea unei noi tabele prin preluarea întepistrărilor din tabelele CLIENTI si COMENZI
- c) se va afişa o eroare deoarece clauza HAVING este incorect utilizată
- d) se va afişa o eroare în cazul în care nu există nici un client care a încheiat cel putin 3 comenzi


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 20
**Cerința:** Fie tabela ANGAJATI (id_ angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCIHAR2(30), salariul NUMBER(10,2), data angajare DATE, id_funetie
VARCHAR2(30)) având 200 rânduri (înregistrări),
Se consideră comanda SQL-Oracle:

SELECT DISTINCT nume| |” 
!'||prenume nume_complet
FROM angajati
WHERE salariul NOT BETWEEN 5000 AND 10000;
Care din următoarele afirmaţii este falsă?
```

**Variante:**
- a) se implementează operatorul de diferență i
- b) se implementează operatorul relational de proiecție i i
- d) se foloseşte un operator logic os


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 21
**Cerința:** Fie tabela ANGAJATI (id_ angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCHAR2(30), salariul NUMBER(10,2), data angajare DATE, id_ functie
VARCHAR2(30)) având 200 rânduri (înregistrări).
Alegeţi varianta corectă referitoare Ja următoarea comanda SQL:
UPDATE angajati SET salariul-salariul *1.05
WHERE EXTRACT (year from data_angajare) = EXTRACT (year from sysdate) -
AND id Functie IN (SELECT id_functie FROM angajati WHERE salariul <
(SELECT AVG (salariul) FROM angajati));
```

**Variante:**
- a) se majorează salariile persoanelor angajate anul trecut, indiferent de lună, dacă acestea deţin în prezent o funcţie similară cu angajaţii care au salariul mai mic decât salariul mediu
- b) se majorează salariile persoanelor angajate în ziua anterioară dacă acestea deţin în prezent o funcţie similară cu angajaţii care au salariul mai mic decât salariul mediu
- c) instrucţiunea este eronată deoarece în tabelă nu există coloana sysdate
- d) se majorează doar salariile angajaţilor care au în prezent salariul mai mic decât salariul mediu


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 22
**Cerința:** Fie tabela RAND_COMENZI (nr_comanda NUMBER(6), id_produs NUMBER(8), cantitate

```sql
NUMBER(7), pret NUMBER(7,2)) având 100 de rânduri precum şi interogarea SQL Oracle:
SELECT nr_ comanda, ROUND (AVG(cantitate)) val FROM Rand Comenzi GROUP
BY nr_cdmanda ORDER BY 2;
Care
din următoarele afirmaţii este adevărată?
```

**Variante:**
- a) se afişează cantitatea medie comandată din fiecare comandă ordonat crescător după cantitatea medie
- b) se afișează cantitatea medie comandată din fiecare produs ordonat crescător după cantitate medie
- c) interogarea conține o eroare deoarece functia ROUND nu este corect utilizată
- d) interogarea utilizează incorect clauza ORDER BY


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 23
**Cerința:** Fie tabela COMENZI (nr_comanda NUMBER(5) PRIMARY KEY, id_client NUMBER (5), data

```sql
DATE) şi următoarele instrucţiuni:
SELECT id_client FROM comenzi WHERE extract (year from data)=1999
GROUP BY id client HAVING count (nr comanda) 
<2; 
we
12. 
,
SELECT id client FROM comenzi WHERE to_char (data, 'yyyy')=1999
GROUP BY id client HAVING count (nx _comanda) <a; 
Lo
```

**Variante:**
- a) instrucțiunile [1 si I2 returnează acelaşi rezultat
- b) SELECT id client FROM comenzi WHERE to date(data, ‘year') like 13199951 GROUP BY id client HAVING count (nr_comanda) <2; indicaţi răspunsurile corecte:
- c) instrucţiunea 12 este eronată
- d) toate instrucţiunile sunt eronate


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 24
**Cerința:** Care dintre următoarele afirmaţii despre cursorii impliciti din PL/SQL este. adevărată?

**Variante:**
- a) sunt automat închişi după ce instrucţiunea a fost executată
- b) stochează informaţii cu privire la procesarea instrucțiunilor LCT (limbajul de control al tranzacţiilor)
- c) stochează informaţii cu privire la procesarea instrucţiunilor LDD (limbajul de descriere a datelor)
- d) pot fi parcurși folosind instrucţiunea FOR


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 25
**Cerința:** Intr-un bloc PL/SQL din Oracle, pentru a putea rula instrucțiunea care șterge o tabelă folosim:

**Variante:**
- a) EXECUTE IMMEDIATE
- b) DELETE
- c) DROP
- d) CALL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 26
**Cerința:** Care din următoarele funcţii SQL nu poate fi folosită în instrucţiuni specifice PL/SQL?

**Variante:**
- a) DECODE
- b) LENGTH
- c) SUBSTR
- d) NVL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 27
**Cerința:** Se consideră următorul bloc PL/SQL:

```sql
SET SERVEROUTPUT ON
DECLARE
data varchar2 (25);
v mumber (2); 
.
BEGIN 
L
select sysdate~30 into data from dual
where 152;
DBMS_OUTPUT. PUT_LINE (data);
EXCEPTION
WHEN NO DATA FOUND THEN 
Coe
DBMS_OUTBUT. PUT_LINE (v)
```

**Variante:**
- a) blocul se execută cu succes, dar nu afişează nimic
- b) se afişează o dată calendaristică
- c) se afişează un număr de zile
- d) apare o eroare deoarece variabila data este de tip VARCHAR2
- e) END; / Care dintre următoarele afirmaţii sunt corecte:


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 28
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCHAR2(30), data angajare DATE, salariul NUMBER(10,2)) cu cel putin 100 de
rânduri (înregistrări) și blocul PL/SQL:
SET SERVEROUTPUT ON
DECLARE,
CURSOR cursori IS SELECT id angajat, nume FROM Angajati;
vid angajati.iad angajat 41YBE;
vnume VARCHAR2 (50);
BEGIN
OPEN cursori:
WHILB cursori® FOUND LGOP
FETCH cursorl INTO vid, voume;
DBMS_OQUTPUT „RUT LINE (*Angajatul "| forum) +
END LOOP;
BND;
/
Care afirmaţie este corectă?
```

**Variante:**
- a) blocul se execută, dar nu afișează nimic
- b) blocul va afișa numele tuturor angajaţilor din tabela ANGAJATI
- c) blotul va afișa numele ultimului angajat din tabelă
- d) blocul conţine o eroare deoarece variabila vnume nu este corect utilizată


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 29
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCHAR2(30), salariul NUMBER(10,2), id_departament NUMBER(3)) şi blocul
PL/SQL:
SET SERVEROUTPUT ON
DECLARE
nr_angajati NUMBER;
sai. mediu NUMBER;
BEGIN
SELECT COUNT 
(id angajat), AVG (salariul) INTO nr_angajati,
sal_mediu FROM Angajati WHERE. id_departament=50; 
ae 
eG
DBMS_OUTPUT.PUT_LINE(nr_angajati || 
! 
* 
LI 
= 
ROUND (sal_mediu,2));
```

**Variante:**
- a) Care afirmaţie este corecta?
- b) blocul conţine o eroare deoarece lipsește clauza GROUP BY
- c) blocul va afişa numărul mediu de angajaţi pe fiecare departament
- d) blocul conţine o eroare deoarece funcţiile de grup.nu pot fi utilizate în blocuri


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

### Întrebarea 30
**Cerința:** Fie tabela ANGAJATI (id_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCHAR2(30), salariul 'NUMBER(10,2), id_ departament NUMBER(3)) si blocul
PL/SQL:
SEP SERVEROUTPUT ON
DECLARE
id_dep angajati .id departamentttype;
sal tot NUMBER;
BEGIN
SELECT id_departament, SUM (salariul) INTO id_dep, sal_tot
FROM Angajati GROUP BY id departament;
OBMS_OUTPUT.PUT_LINE(id 
dep || 
' 
' 
TI sal tot)?
BND;
p
/
Presupunând că tabela are mai mult de 100 de angajaţi repartizaţi în cel putin 5 departamente,
precizati care dintre afirmaţiile următoare este corectă?
```

**Variante:**
- a) blocul declanşează o excepție deoarece interogarea returnează mai multe rânduri
- b) blocul rulează, dar nu afişează nimic deoarece variabila sal_fof nu este inifializata
- c) blocul rulează si afişează suma totală a salariilor pe fiecare departament
- d) blocul conţine o eroare deoarece nu este coreci declarată variabila id_dep


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: *(indisponibil — barem OCR necitibil)*

</details>
---

## Subiect 2019

### Întrebarea 1
**Cerința:** Fie tabela ANGAJATIGd_angajat NUMBER(5) PRIMARY KEY, nume VARCHAR2(30),

```sql
prenume VARCHAR2(30), salariul NUMBER(10,2), data angajare DATE) si blocul
PL/SQL:
SET SERVEROUTPUT ON
DECLARE
nume_complet VARCHAR2(300);
BEGIN
SELECT nume|! "prenume into nume_complet FROM Angajati
WHERE id_angajat=101;
DBMS_OUTPUT.PUT_LINE(nume_complet);
END;
/
Care afirmatie este corecta?
```

**Variante:**
- a) se foloseste un cursor explicit
- b) blocul contine o eroare si nu va rula
- c) blocul va afisa numele complet al angajatului cu id angajat = 101 (daca exista)
- d) blocul foloseste un operator de grup


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) blocul va afisa numele complet al angajatului cu id angajat = 101 (daca exista)**

</details>
---

### Întrebarea 2
**Cerința:** Fie tabela ANGAJATI (id angajat NUMBER(5) PRIMARY KEY, nume

```sql
VARCHAR2(30), prenume VARCHAR2(30), salariul NUMBER(10,2), data angajare
DATE) avand 107 randuri (inregistrari),
Alegeti varianta corecta referitoare la urmatoarea comanda SQL:
UPDATE Angajati SET salariul=3500 where data angajare 
= EXTRACT(MONTH FROM
sysdate); 
.
```

**Variante:**
- a) se actualizeaza, in sens de modificare, salariile persoanelor angajate anul trecut
- b) se actualizeaza, in sens de modificare, salariile persoanelor angajate in luna curenta
- c) comanda nu ruleaza
- d) se actualizeaza, in sens de modificare, salariile persoanelor angajate in anul curent


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) comanda nu ruleaza**

</details>
---

### Întrebarea 3
**Cerința:** Programul C de mai jos:

```c
#include<stdio.h>
void print(int n)
{
if (n f= 0) {
printf(“%d“, n--);
print(n-1);
}
}
void main()
{
print(9);
}
```

**Variante:**
- a) Produce o bucla infinita
- b) tipareste: 97531
- c) tipareste: 7531
- d) tipareste: 987654321


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) tipareste: 97531**

</details>
---

### Întrebarea 4
**Cerința:** Fie tabela RAND_COMENZI (nr_comanda NUMBER(6), id_produs NUMBER(8),

```sql
cantitate NUMBER(7), pret NUMBER(7,2)) si tabela PRODUSE (id_produs NUMBER(8),
denumire produs VARCHAR2(32)) avand 100 de randuri (inregistrari) precum si
interogarea SQL Oracle:
SELECT p.denumire_produs, SUM(pret* cantitate) val
FROM Produse p JOIN Rand_Comenzi r ON p.id_produs=r.id_produs
GROUP BY p.denumire_produs HAVING count(1)>=3 order by count(1) dese;
Care din urmatoarele afirmatii este adevarata?
```

**Variante:**
- a) interogarea va afisa produsele pentru care valoarea totala comandata este mai mare de 3
- b) interogarea va afisa valoarea totala a comenzilor pentru fiecare produs care a fost comandat de cel putin 3 ori
- c) interogarea contine O eroare si nu va rula
- d) se realizeaza o jonciiune externa


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) interogarea va afisa valoarea totala a comenzilor pentru fiecare produs care a fost comandat de cel putin 3 ori**

</details>
---

### Întrebarea 5
**Cerința:** Care este rezultatul obtinut prin rularea umatorului program C?

```c
#include<stdio.h>
void swap(int a, int b) {
a=atb;
b=a-b;
a=a-b;
void main) {
inta 
= 10,b=20;
swap(a, b);
printf(?%d,%d", a, b),
}
```

**Variante:**
- a) 20,10
- b) 10,20
- c) 20,20
- d) 10,10


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 20,20**

</details>
---

### Întrebarea 6
**Cerința:** Fie tabela COMENZI(nr_comanda NUMBER, data DATE, modalitate CHAR), id client

```sql
NUMBER, stare comanda NUMBER, id angajat NUMBER).
Se da urmatoarea secventa de comenzi:
SET SERVEROUTPUT ON
BEGIN
UPDATE Comenzi SET data=data-1 where sysdate!=sysdate;
DBMS _OUTPUT.PUT_LINE (SQL%ROWCOUNT);
ROLLBACK;
EXCEPTION
WHEN OTHERS THEN DBMS_OUTPUT.PUT_LINE(Eroare’);
END;
CSIEZa1 7
Presupunem ca tabela COMENZI are 105 inregistrari. In aceste conditii, blocul PL/SQL
afiseaza:
```

**Variante:**
- a) 0
- b) 'Eroare'
- c) o valoare intre 1 si 105
- d) 105


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 0**

</details>
---

### Întrebarea 7
**Cerința:** Ce va afisa urmatorul program C:

```c
#include <stdio.h>
void mainO{
int a==2;
switch(a)
{
case 1: printf("A");
case 2: printf("B");
case 3: printi("C");
break;
case 4: printf("D");
default : printf("E");
break;
}
```

**Variante:**
- a) E
- b) BC
- c) BE
- d) ABC


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) BC**

</details>
---

### Întrebarea 8
**Cerința:** Care din urmatoarele afirmatii este falsa (SQL Oracle):

**Variante:**
- a) in functie de randurile din tabele, o jonctiune externa intre doua tabele poate returna aceleasi randuri ca o jonctiune interna intre aceleasi doua tabele
- b) cheile externe se definesc in limbajul de descriere a datelor (LDD)
- c) pentru a realiza o jonctiune intre doua sau mai multe tabele trebuie sa fie declarate chei externe intre aceste tabele
- d) o cheie externa trebuie sa refere o cheie primara sau o cheie unica


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) pentru a realiza o jonctiune intre doua sau mai multe tabele trebuie sa fie declarate chei externe intre aceste tabele**

</details>
---

### Întrebarea 9
**Cerința:** Considerand urmatorul program C:

```c
#include <stdio.h>
#define PRINTG, limit) do { if (i++ < limit) { printf("Salut"); continue;} } while (0)
void main)
i
inti= 0;
PRINTG, 6);
}
De cate ori va fi tiparit textul “Salut”?
```


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a)**

</details>
---

### Întrebarea 10
**Cerința:** Ce rezultat va afisa urmatorul program C?

```c
#include <stdio.h>
void main)
{
int var = 0110;
printf(’%d", var);
}
```

**Variante:**
- a) 6
- b) 72
- c) 272
- d) 110


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 72**

</details>
---

### Întrebarea 11
**Cerința:** Se considera urmatorul bloc PL/SQL:

```sql
SET SERVEROUTPUT ON
DECLARE
v CHAR(2):= 'ok’;
BEGIN
IF |==1 THEN
DBMS_OUTPUT.PUT_LINE(y);
END IF;
END;
/
Care afirmatie este corecta?
```

**Variante:**
- a) blocul contine o eroare si nu ruleaza.
- b) blocul nu afiseaza nimic ¢) blocul are o structura repetitiva de program
- d) executia blocului afiseaza intotdeauna variabila v cu valoarea "ok"


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul nu afiseaza nimic ¢) blocul are o structura repetitiva de program**

</details>
---

### Întrebarea 12
**Cerința:** Fie tabela ANGAJATI(id_angajat NUMBER PRIMARY KEY, nume VARCHAR2(30),

```sql
id departament NUMBER, salariul NUMBER NOT NULL) avand 100 de randuri
(înregistrari).
Ce afiseaza comanda:
SELECT nume FROM Angajati a WHERE salariul <= ANY (SELECT salariul FROM
Angajati b);
```

**Variante:**
- a) nimic
- b) toti angajatii
- c) angajatii cu salariul maxim din intreaga firma
- d) angajatii cu salariul minim din intreaga firma


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) angajatii cu salariul maxim din intreaga firma**

</details>
---

### Întrebarea 13
**Cerința:** Fie blocul PL/SQL:

```sql
SET SERVEROUTPUT ON
ACADEMIA DE STUDII ECONOMICE DIN BUCUREȘTI
CSIE3a ~~
%
i
i
i.
i
i
i
ia
DECLARE
n NUMBER(2);
BEGIN
IF n<! THEN DBMS OUTPUT.PUT_LINE(NVL(A\'C);
ELSE DBMS_OUTPUT.PUT_LINE(NV L(B',E))
END IF;
END;
/
Care afirmatie este corecta?
```

**Variante:**
- a) blocul contine o eroare si nu ruleaza
- b) blocul ruleaza si afiseaza E
- c) blocul ruleaza si afiseaza C
- d) blocul ruleaza si afiseaza B


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) blocul contine o eroare si nu ruleaza**

</details>
---

### Întrebarea 14
**Cerința:** Se considera urmatoarea comanda SQL-Oracle:

```sql
SELECT 2 val from DUAL
union all
SELECT 2 from DUAL
minus
SELECT 1 from DUAL;
Ce valoare returneaza comanda anterioara:
```

**Variante:**
- a) 3
- b) 1
- c) 2
- d) NULL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 2**

</details>
---

### Întrebarea 15
**Cerința:** Fie blocul PL/SQL:

```sql
SET SERVEROUTPUT ON
DECLARE
i PLS_INTEGER;
BEGIN
WHILE i < 30 LOOP
DBMS_QUTPUT.PUT_LINE('V aloarea contorului i este: ' || i);
END LOOP;
END;
/
Care afirmatie este corecta?
```

**Variante:**
- a) blocul ruleaza si afiseaza 31 de randuri
- b) blocul ruleaza dar nu afiseaza nimic
- c) blocul contine o eroare si nu ruleaza
- d) blocul ruleaza dar declanseaza o exceptie tmplicita


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul ruleaza dar nu afiseaza nimic**

</details>
---

### Întrebarea 16
**Cerința:** In limbajul PLSQL din Oracle, pentru a putea rula instructiunea care sterge o tabela

```sql
folosim:
```

**Variante:**
- a) DELETE
- b) . EXECUTE IMMEDIATE
- c) ALTER
- d) DROP ACADEMIA DE STI UDII ECONOMICE DIN BUCUREŞTI 17Fie tabela ANGAJ ATIGd_angajat NUMBER(S) PRIMARY KEY, nume VARCHAR2(30), prenume VARCHAR2(30), salariul NUMBER(10,2), data_angajare DATE) avand 107 randuri (inregistrari) si interogarea SQL Oracle: SELECT * FROM Angajati WHERE nume like Yay Care din urmatoarele afirmatii este adevarata?


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) DELETE**

</details>
---

### Întrebarea 17
**Cerința:** WHERE nume LIKE '%a_';

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) interogarea va afisa doar angajatii al caror nume contine pe penultima pozitie litera a**

**Explicație:** '%a_' = orice caractere, 'a', apoi exact un caracter. 'a' pe penultima poziție.

</details>
---
---

### Întrebarea 18
**Cerința:** Care va fi rezultatul rularii urmatorului program Cc:

```c
#include<stdio.h>
void main() {
inta=5,b=6,077;
printi("%d", ib +e) > (at 10)));
)
```

**Variante:**
- a) Va afisa |
- b) Va genera eroare de compilare
- c) Va afisa 15
- d) Vaafisa0


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Vaafisa0**

</details>
---

### Întrebarea 19
**Cerința:** Dupa declaratia

```c
union Test { int i; char c; 1th
valoarea expresiei sizeof(t) este in orice situatie egala cu:
```

**Variante:**
- a) sizeof(int)
- b) sizeof(char) o) sizeof(int) + sizeof(char)
- d) 0


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) sizeof(char) o) sizeof(int) + sizeof(char)**

</details>
---

### Întrebarea 20
**Cerința:** Secventa de cod C:

```sql
intn = 0;
while (1 == 1 if(a> 3) break; else n = n +1;
printi("Yed", n)
afiseaza:
```

**Variante:**
- a) 3
- b) 4
- c) 5
- d) nu afiseaza nimic (bucla infinita) 21Fie tabela RAND_COMENZI (nr_comanda NUMBER(6), id |_produs NUMBER(8), cantitate NUMBER(7), pret NUMBER(7,2)) avand 100 de randuri precum si interogarea SQL Oracle: ( SELECT id produs, TRUNC(AV G(pret*cantitate)) val FROM Rand Comenzi GROUP BY id_produs ORDER BY 2; Care din urmatoarele afirmatii este adevarata?


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 3**

</details>
---

### Întrebarea 21
**Cerința:** SELECT id_produs, TRUNC(AVG(pret*cantitate)) FROM rand_comenzi GROUP BY id_produs ORDER BY 2;

<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se afiseaza valoarea comandata din fiecare produs ordonat crescator dupa valoare**

</details>
---
---

### Întrebarea 22
**Cerința:** Ce va tipari codul de mai jos?

```c
“#include <stdio.h>
int main) {
int i;
forGi=03i<3;1+-+) {
static int a=0;
int b=0;
at;
br,
printf("%d %d “,a,b);
}
return 0;
}
```

**Variante:**
- a) 1121314141
- b) 1121314151
- c) 1020314151
- d) 0120314151


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 1121314151**

</details>
---

### Întrebarea 23
**Cerința:** O tabela este in FN3 daca:

**Variante:**
- a) este in FN1 si fiecare atribut cheie primara depinde tranzitiv de atributele non-cheie
- b) ‘este in FN2 si atributele non-cheie nu sunt dependente tranzitiv de cheia primara a relatiei
- c) este in FN2 si are dependente complete
- d) este in ENI si are dependente functionale incomplete


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) este in FN1 si fiecare atribut cheie primara depinde tranzitiv de atributele non-cheie**

</details>
---

### Întrebarea 24
**Cerința:** Care tip de date nu poate fi folosit pentru a declară o coloana intr-o tabela folosind SQL-

```c
Oracle:
```

**Variante:**
- a) TIMESTAMP
- b) PLS_INTEGER
- c) NUMBER
- d) DATE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) NUMBER**

</details>
---

### Întrebarea 25
**Cerința:** Cate va fi rezultatul afisat de urmatorul program C:

```c
_ #include <stdio.h>
int f(int vf], int *n) {
ints 
= 0; mti=2;
while (i <= *n) {
s=s+v[i]-vfi- 1];
if (v[i] = vii - 1)
*n=*n- 1;
ib;
}
return s;
}
void main) {
int v[10];
v[1] = 1; v[2] = 2; v[3]} = 3;
VA] = 3; v[5] = 4; v6] = 5;v[7] = 6;
intn = 7;
printi("Yod;%d", n, f(v,den));
}
```

**Variante:**
- a) 734
- b) 7:5
- c) 6;4
- d) 6:5


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 6;4**

</details>
---

### Întrebarea 26
**Cerința:** Ceva fi tiparit ca rezultat al operatiilor de mai jos?

```c
#include <stdio.h>
void main() {
int x=7;
printi("%d,%d,%d",x,x<<2,x>>1);
}
```

**Variante:**
- a) 7,24,2
- b) 7,283 0) 7271
- d) 7253


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 7253**

</details>
---

### Întrebarea 27
**Cerința:** De cate ori va fi tiparit textul “Test” de catre programul C de mai jos?

```c
#include <stdio.h>
void main)
(
int i = 1024;
for (ii >= 1)
print{("Test\n’);
}
```

**Variante:**
- a) 10
- b) 11
- c) de un numar infinit de ori
- d) 1024


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 10**

</details>
---

### Întrebarea 28
**Cerința:** Secventa de cod:

```c
int v{] = f 1,234 }; printi('%od", *(v + 1));
```

**Variante:**
- a) afiseaza 0
- b) afiseaza 1
- c) nu acceseaza corect vectorul deoarece.nu foloseste operatorul []
- d) afiseaza 2


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) afiseaza 2**

</details>
---

### Întrebarea 29
**Cerința:** Se considera urmatorul program:

```c
#include <stdio.h>
int sum(int n, int i, int a[]) {
if 
<= n) {
return sum(n, i + 1, a);
ne
else
{
}
void main) {
int af 10];
afl} =-1; a[2] = 2; a[3] = 8;
int s = sum(3, 1, a);
printi("%ed", s);
return 0:
}
Care este rezultatul afisat in urma executiei programului?
```

**Variante:**
- a) 9
- b) 0
- c) 8
- d) Va genera eroare de executie si va afisa un mesaj de depasire stiva


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 0**

</details>
---

### Întrebarea 30
**Cerința:** Ce va afisa programul C de mai jos?

```c
int P(int a, int *b) {
*bt=a; at=*b;
return at+*b;
}
int mainQ {
inta=7; int b= a;
primti("P(a, b) = %d", P(a, &b)),
printi”; a = %d", a);
printi("; b = “din”, by,
| 
return 0;
}
```

**Variante:**
- a) P(a,b)= 105;a=7;b=7
- b) P(a, b) = 56; a= 7; b = 49 ¢) Pia, b) = 105;a= 7; b = 49
- d) Pla, b)=14,a=7;b=7 Observatie ecare raspuns corect valoreaza trei puncte. Punctajul maxim este. de 90 puncte. 000000000000000000000000000600 9900000000000000000000000000000 20000900000090009000006vsoesooeo %00900090000900000009000000000000 be NOM OA = ce a|4 ane D;
- e) ca el cal colea ea cof ea] crf 2] 4) 4) «e 7] Of ea


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) P(a,b)= 105;a=7;b=7**

</details>
---
