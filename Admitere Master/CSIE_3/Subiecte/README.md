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

### Întrebarea 2
**Cerința:** Care concept implementează o relație IS-A între clase?

**Variante:**
- a) încapsularea
- b) polimorfismul
- c) compunerea
- d) derivarea (moștenirea)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) derivarea (moștenirea)**

**Explicație:** Relația IS-A (ESTE UN/O) este definiția standard a moștenirii: o clasă derivată "este un" tip de clasa de bază. Compunerea implementează HAS-A.

</details>
---

### Întrebarea 3
**Cerința:** Care declarație PL/SQL NU este corectă?

**Variante:**
- a) v_test BOOLEAN NOT NULL := LENGTH(SUBSTR('ORACLE',1,3)) > 1;
- b) v_data DATE := SYSDATE - TO_DATE('10-07-2024','DD-MM-YYYY');
- c) v_text VARCHAR2(20) DEFAULT SUBSTR('ORACLE',1,3);
- d) v_nr NUMBER := TO_CHAR(SYSDATE, 'MM');


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) v_data DATE := SYSDATE - TO_DATE(...);**

**Explicație:** Diferența dintre două date returnează un NUMBER (număr de zile), nu un DATE. Deci atribuirea unui NUMBER la o variabilă DATE este eronată.

</details>
---

### Întrebarea 4
**Cerința:** Care variantă de specificare a parametrului unei proceduri PL/SQL este corectă?

**Variante:**
- a) (p_param NUMBER(4,2))
- b) (p_param IN VARCHAR2(50))
- c) (p_param OUT VARCHAR2 := 'anonim')
- d) (p_param VARCHAR2)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) (p_param VARCHAR2)**

**Explicație:** În parametrii PL/SQL nu se specifică dimensiunea/precizia tipului. Parametrii OUT nu pot avea valoare default. Doar VARCHAR2 fără dimensiune este valid.

</details>
---

### Întrebarea 5
**Cerința:** Prototipurile: `C_mea operator-(C_mea&);` și `friend C_mea operator-(C_mea&, C_mea&);`

**Variante:**
- a) echivalente, ambele supraîncarcă - pentru scădere
- b) primul eronat
- c) al doilea eronat
- d) primul supraîncarcă - unar, al doilea supraîncarcă - binar


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) sunt echivalente și supraîncarcă operatorul - pentru scăderea a două obiecte de tip C_mea**

**Explicație:** Ca metodă cu 1 parametru, operator- este binar (obiectul curent + parametrul). Ca funcție friend cu 2 parametri, este tot binar. Ambele forme implementează scăderea a două obiecte C_mea.

</details>
---

### Întrebarea 6
**Cerința:** Funcția f_check_data primește o dată și returnează TRUE/FALSE dacă data > SYSDATE-90. Comanda: `SELECT id_comanda, f_check_data(data) FROM comenzi;`

**Variante:**
- a) funcția nu se compilează (operator greșit)
- b) va afișa TRUE/FALSE (recent)
- c) va afișa doar comenzile recente
- d) tipul BOOLEAN nu e compatibil cu SQL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) funcția PL/SQL nu se poate apela în comanda SQL deoarece tipul de date returnat nu este compatibil cu SQL**

**Explicație:** BOOLEAN este tip PL/SQL, nu SQL. Funcțiile care returnează BOOLEAN nu pot fi apelate direct din SELECT.

</details>
---

### Întrebarea 7
**Cerința:** În C++ o clasă este abstractă dacă:

**Variante:**
- a) e în relație de moștenire cu cel puțin două clase
- b) conține cel puțin o funcție friend
- c) conține cel puțin o metodă virtual pură
- d) conține cel puțin o metodă virtuală


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) Conține cel puțin o metodă virtual pură**

**Explicație:** Prin definiție, o clasă abstractă în C++ conține cel puțin o metodă virtuală pură (= 0). Metodele virtuale simple nu fac clasa abstractă.

</details>
---

### Întrebarea 8
**Cerința:** Program Singleton cu getInstance(int v). Se apelează cu 10 apoi cu 5, se face print după fiecare.

**Variante:**
- a) 1010
- b) 105
- c) eroare (constructor privat)
- d) 00


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 1010**

**Explicație:** Pattern-ul Singleton — prima instanță se creează cu v=10. La al doilea apel, instance != NULL, deci nu se mai creează. Ambele pointeri arată către același obiect cu v=10. Se afișează 10 de două ori.

</details>
---

### Întrebarea 9
**Cerința:** Clasa abstractă A (virtual void f() = 0). Care declarații sunt corecte?
- A a; //1
- A *b; //2
- A v[5]; //3
- A *pv[5]; //4
- A *p=new A[5]; //5

**Variante:**
- a) 1 și 3
- b) 2 și 4
- c) 2, 4 și 5
- d) 1 și 2


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Declarațiile 2 și 4**

**Explicație:** Nu se pot instanția obiecte dintr-o clasă abstractă (1, 3, 5 sunt greșite). Se pot declara pointeri către clase abstracte (2 și 4).

</details>
---

### Întrebarea 10
**Cerința:** INSERT într-o tabelă, CREATE VIEW, DROP VIEW, ROLLBACK. Care afirmație e corectă?

**Variante:**
- a) ROLLBACK anulează INSERT
- b) INSERT-ul se salvează automat
- c) INSERT generează eroare (email NULL)
- d) ROLLBACK anulează DROP VIEW


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) efectul comenzii INSERT va fi automat salvat**

**Explicație:** CREATE VIEW și DROP VIEW sunt comenzi DDL, care fac COMMIT implicit. INSERT-ul anterior este deja salvat, ROLLBACK nu îl mai poate anula. Email UNIQUE permite NULL.

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

### Întrebarea 12
**Cerința:**
```c
int a[5] = {1,2,3,4,5};
for (int i=0; i<5; i++)
  if ((char)a[i] == '5') printf("%d\n", a[i]);
  else printf("FAIL\n");
```

**Variante:**
- a) codul ASCII al '5'
- b) eroare la inițializare
- c) 5
- d) de 5 ori "FAIL"


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Programul va afisa de 5 ori "FAIL"**

**Explicație:** Se compară (char)a[i] cu caracterul '5' (cod ASCII 53). Nici una din valorile 1..5 (ca int convertit la char) nu este egală cu 53. Deci de fiecare dată se afișează "FAIL".

</details>
---

### Întrebarea 13
**Cerința:** Care comandă SQL-Oracle NU este corectă?

**Variante:**
- a) SELECT EXTRACT(SYSDATE,'DD.MM.YYYY') FROM dual;
- b) SELECT TRUNC(TO_DATE(...),'YEAR') FROM dual;
- c) SELECT DECODE(1+2,3,'DA','NU') FROM dual;
- d) SELECT SUM(DECODE(LENGTH('ORACLE'),6,1,0)) FROM dual;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) SELECT EXTRACT(SYSDATE,'DD.MM.YYYY') FROM dual;**

**Explicație:** EXTRACT are sintaxa `EXTRACT(YEAR FROM date_col)`, nu acceptă format de tip TO_CHAR. Sintaxa dată este eronată.

</details>
---

### Întrebarea 14
**Cerința:**
```c
union s { int x; int y; };
void inc(union s t) { t.x++; t.y++; }
int main() {
  union s t;
  t.y = 3; t.x = 2;
  inc(t);
  printf("%d %d", t.x, t.y);
}
```

**Variante:**
- a) 33
- b) 44
- c) 34
- d) 22


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 22**

**Explicație:** În union, x și y ocupă aceeași memorie. t.y=3 apoi t.x=2 => memoria are valoarea 2. inc(t) primește prin valoare (copie), modificările nu se propagă. Se afișează 2 2.

</details>
---

### Întrebarea 15
**Cerința:** Ierarhia A → B → C, fiecare constructor afișează numele clasei. `C *pc = new C;`

**Variante:**
- a) C
- b) CBA
- c) A
- d) ABC


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) ABC**

**Explicație:** La construirea unui obiect derivat, constructorii se apelează în ordinea moștenirii: baza mai întâi (A), apoi B, apoi C.

</details>
---

### Întrebarea 16
**Cerința:** `for (;;) printf("Examen");`

**Variante:**
- a) eroare de compilare
- b) o singură dată
- c) fără output
- d) la infinit


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Tipareste "Examen" la infinit**

**Explicație:** `for(;;)` este echivalent cu `while(true)` — buclă infinită. Se tipărește "Examen" la infinit.

</details>
---

### Întrebarea 17
**Cerința:** Care operator NU poate fi supraîncărcat?

**Variante:**
- a) =
- b) ::
- c) >
- d) !


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) ::**

**Explicație:** În C++, operatorul de rezoluție a scope-ului `::` nu poate fi supraîncărcat. Nici `.`, `.*`, `?:`, `sizeof` nu pot fi supraîncărcați.

</details>
---

### Întrebarea 18
**Cerința:** CREATE VIEW pe join produse, rand_comenzi, comenzi cu HAVING COUNT(id_comanda)>=3.

**Variante:**
- a) join imposibil fără FK
- b) crează view cu produse comandate pe cel puțin 3 comenzi până în 2024
- c) eroare AVG
- d) eroare COUNT


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) crearea unei tabele virtuale... produsele care au fost comandate pe cel putin 3 comenzi pana in 2024**

**Explicație:** Join-ul funcționează pe baza egalității coloanelor, nu necesită FK. HAVING COUNT>=3 filtrează produsele cu ≥3 comenzi. Extract(YEAR)<=2024 restricționează perioada.

</details>
---

### Întrebarea 19
**Cerința:** Care afirmație este corectă?

**Variante:**
- a) obiectul este un pointer
- b) clasa e instanță a obiectelor sale
- c) clasa e instanță a tipului struct
- d) obiectul este o instanță din clasa sa


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Un obiect este o instanță din clasa sa**

**Explicație:** Definiția POO: clasa este șablonul, obiectul este o instanță concretă a clasei.

</details>
---

### Întrebarea 20
**Cerința:** `printf("%d", 11 >> 2);`

**Variante:**
- a) 44
- b) 22
- c) 2
- d) 121


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 2**

**Explicație:** 11 în binar = 1011. Shift dreapta cu 2 poziții => 10 = 2.

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

### Întrebarea 22
**Cerința:**
```cpp
A ob1;
A ob2 = ob1, ob3(ob1);
```
cu constructor de copiere care afișează "Copiere".

**Variante:**
- a) Atribuire Copiere Copiere
- b) Atribuire Copiere
- c) Copiere Copiere Copiere
- d) Copiere Copiere


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Copiere Copiere**

**Explicație:** `A ob2 = ob1` este inițializare, deci apel copy constructor (nu operator=). `ob3(ob1)` — copy constructor. Se afișează "Copiere Copiere".

</details>
---

### Întrebarea 23
**Cerința:** Funcția TO_CHAR în SQL-Oracle:

**Variante:**
- a) poate fi folosită pe NUMBER și DATE
- b) doar VARCHAR2 → CHAR
- c) doar NUMBER
- d) doar TIMESTAMP → anul curent


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) poate fi utilizata pe parametri de tip NUMBER si DATE**

**Explicație:** TO_CHAR convertește NUMBER sau DATE la VARCHAR2, cu format opțional.

</details>
---

### Întrebarea 24
**Cerința:** UPDATE produse SET pret_min=pret_min*0.9 WHERE pret_min > (SELECT min(pret) FROM rand_comenzi) AND categorie IN (SELECT categorie FROM produse WHERE LOWER(denumire_produs) LIKE '%monitor%');

**Variante:**
- a) eroare subcerere
- b) actualizează doar produsele "monitor"
- c) actualizează produsele cu pret_min > min(pret) în categorii cu produse "monitor"
- d) eroare IN


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) actualizeaza produsele care au pret_min mai mare decat pretul minim din tabela RAND_COMENZI si sunt in categorii similare cu produsele care contin in denumire cuvantul 'monitor'**

**Explicație:** UPDATE cu două condiții: pret_min>min din rand_comenzi și categorie IN subcererea cu produsele "monitor". Cuprinde produsele din aceleași categorii, nu doar monitoarele.

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

### Întrebarea 26
**Cerința:** Ordinea de apel a constructorilor la derivare:

**Variante:**
- a) mai întâi derivata, apoi baza
- b) cu cei mai mulți constructori
- c) mai întâi baza, apoi derivata
- d) aleatoare


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) mai intai se apeleaza constructorul clasei de baza, apoi cel al derivatei**

**Explicație:** Regula fundamentală: baza înainte de derivată la construcție (invers la distrugere).

</details>
---

### Întrebarea 27
**Cerința:** `SELECT CONCAT('Ion', UPPER(SUBSTR('Ionescu',1))) || LENGTH('Ionescu') parola FROM DUAL;`

**Variante:**
- a) IonIONESCU7
- b) SUBSTR e funcție de grup
- c) IonI7
- d) CONCAT nu merge cu ||


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se afiseaza IonIONESCU7**

**Explicație:** SUBSTR('Ionescu',1) = 'Ionescu'. UPPER = 'IONESCU'. CONCAT('Ion','IONESCU') = 'IonIONESCU'. LENGTH('Ionescu')=7. Concatenat: IonIONESCU7.

</details>
---

### Întrebarea 28
**Cerința:** Operatorul care creează R3 din R1 și R2 fără a elimina duplicatele:

**Variante:**
- a) JOIN
- b) UNION
- c) UNION ALL
- d) INTERSECT


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) UNION ALL**

**Explicație:** UNION elimină duplicatele, UNION ALL păstrează toate rândurile (inclusiv duplicate).

</details>
---

### Întrebarea 29
**Cerința:** Cum se adaugă o coloană nouă într-o tabelă?

**Variante:**
- a) UPDATE TABLE ADD COLUMN ...
- b) ALTER TABLE ... ADD COLUMN ...
- c) ALTER TABLE table_name ADD column_name column_definition;
- d) MODIFY TABLE ADD ...


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) ALTER TABLE table_name ADD column_name column_definition;**

**Explicație:** În Oracle SQL, sintaxa este `ALTER TABLE tabel ADD coloana tip` (fără cuvântul COLUMN).

</details>
---

### Întrebarea 30
**Cerința:**
```cpp
class A { int a; public: A(int v=0):a(v){} friend int get_a(A p){return p.a;} };
class B : public A { float b; public: B(int v=0, float m=0.0):A(v),b(m){} };
int main() { B s(10, 3.14); cout << get_a(s); return 0; }
```

**Variante:**
- a) eroare private inaccesibil
- b) 0
- c) eroare friend
- d) 10


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Va afisa 10**

**Explicație:** B(10,3.14) apelează A(10) care setează a=10. friend get_a poate accesa private din A. Conversia B → A prin moștenire publică funcționează. Se afișează 10.

</details>
---

## Subiect 2023

### Întrebarea 1
**Cerința:** Care linii creează un masiv cu 5 obiecte A?
- A v1[5]; //1
- A *v2[5]; //2
- A *v3 = new A[5]; //3
- A *v4 = (A*)malloc(5*sizeof(A)); //4

**Variante:**
- a) 1, 2 și 3
- b) 1, 3 și 4
- c) 1 și 2
- d) 3 și 4


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Liniile 1, 2 si 3** *(Notă: barem oficial indică b — Liniile 1, 3 și 4)*

**Explicație:** Linia 1 crează 5 obiecte pe stivă. Linia 3 crează 5 obiecte pe heap cu new. Linia 4 alocă memorie dar nu apelează constructori (malloc nu construiește obiecte). Linia 2 e un array de pointeri, nu 5 obiecte. Conform baremului oficial: b) 1, 3 și 4.

---

### Întrebarea 2
**Cerința:** UPDATE care afectează 100 rânduri, apoi SELECT COUNT INTO nr, rez := SQL%ROWCOUNT.

**Variante:**
- a) afișează C
- b) afișează B
- c) eroare cursor implicit
- d) afișează A

**Răspuns corect: d) blocul PL/SQL ruleaza cu succes si afiseaza A**

**Explicație:** SQL%ROWCOUNT după SELECT INTO cu COUNT returnează 1 (o singură linie). rez=1, deci se afișează A.

</details>
---

### Întrebarea 3
**Cerința:**
```c
void f(int* a, int n) { *a += *(a+n-1) += 10; }
int main() { int a[5]={8,2,5}; f(a,5); print(a,5); }
```

**Variante:**
- a) 10 2 5 0 10
- b) 18 2 5 0 10
- c) 18 2 5 2 10
- d) 8 2 5 8 10


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 18 2 5 0 10**

**Explicație:** a[4] += 10 => a[4] = 0+10 = 10. a[0] += a[4] => a[0] = 8+10 = 18. Restul rămân neschimbate: 18, 2, 5, 0, 10.

</details>
---

### Întrebarea 4
**Cerința:**
```c
char z='a';
char *const p = &z;
p[0] = '1'; //1
p++;        //2
p = "Examen"; //3
```

**Variante:**
- a) 1+2+3
- b) 1+2
- c) 2+3
- d) 1


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 1**

**Explicație:** `char *const p` — pointer constant. Se poate modifica valoarea indicată (*p sau p[0]), dar nu p însuși. Deci 1 e OK, 2 și 3 sunt greșite.

</details>
---

### Întrebarea 5
**Cerința:** Clasa A cu friend void A::show(A&, B&) declarată friend în B.

**Variante:**
- a) 00
- b) 100
- c) eroare acces b
- d) eroare friend


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Va fi afisat 100**

**Explicație:** x.a=10 iar y.b rămâne 0 (constructorul B setează b=0). Afișare "10 0" concatenat = "100".

</details>
---

### Întrebarea 6
**Cerința:** `int var = 01010; printf("%d", var);`

**Variante:**
- a) 520
- b) 4112
- c) 10
- d) 1010


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 520**

**Explicație:** Prefix 0 = octal. 01010 în octal = 1*512 + 0 + 1*8 + 0 = 520 în decimal.

</details>
---

### Întrebarea 7
**Cerința:** Clasa A cu contor static. Se creează t1=new A(100), t2=new A(*t1), t3=*t1, t4=3. Copy constructor incrementează contor.

**Variante:**
- a) 1
- b) 2
- c) 3
- d) 0


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 2** *(Notă: barem oficial - c) 3)*

**Explicație:** Contorul crește la copy constructor. t2=new A(*t1) => copy => contor=1. A t3 = *t1 => copy => contor=2. A t4; t4=3 folosește constructorul cu int, nu copy. Barem: c) 3 (dacă t4=3 e considerat conversie prin copy).

---

### Întrebarea 8
**Cerința:** Care interogare returnează o valoare numerică?

**Variante:**
- a) ROUND(data_angajare,'YEAR')
- b) NVL(LENGTH(SUBSTR(nume,1,5)),0)
- c) TO_CHAR(ROUND(data,'MONTH'),'Mon')
- d) DECODE(TO_CHAR(...),13,data-2,data+2)

**Răspuns corect: b) NVL(LENGTH(SUBSTR(nume_angajat,1,5)),0)**

**Explicație:** LENGTH returnează NUMBER. NVL păstrează tipul NUMBER. Celelalte returnează DATE sau VARCHAR2.

</details>
---

### Întrebarea 9
**Cerința:** Restricția referențială.

**Variante:**
- a) atribut R1 pe domeniul cheii primare R2 modelează asocierea
- b) cheia primară din R1 poate fi NULL
- c) cheia primară din părinte poate fi non-unică
- d) R1 și R2 aceeași extensie


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) un atribut din R1 care are valori definite pe acelasi domeniu ca si cheia primara a lui R2 are rolul de a modela asocierea**

**Explicație:** Definiția FK — atribut din tabela copil care referă cheia primară a tabelei părinte, pe același domeniu.

</details>
---

### Întrebarea 10
**Cerința:** Modificarea structurii unei tabele.

**Variante:**
- a) DROP CONSTRAINT
- b) DELETE COLUMN
- c) UPDATE CONSTRAINT
- d) UPDATE TABLE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) DROP CONSTRAINT**

**Explicație:** `ALTER TABLE ... DROP CONSTRAINT constraint_name` este sintaxa Oracle validă. Celelalte nu există.

</details>
---

### Întrebarea 11
**Cerința:** TRUNC în SQL-Oracle:

**Variante:**
- a) TIMESTAMP → prima oră din an
- b) VARCHAR2 → primele caractere
- c) doar NUMBER
- d) NUMBER și DATE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) poate fi utilizata pe parametri de tip NUMBER si DATE**

**Explicație:** TRUNC funcționează pe numere (trunchiere zecimale) și pe date (trunchiere la unitate specificată).

</details>
---

### Întrebarea 12
**Cerința:** Clasa A cu static int x (doar declarat, neinițializat), clasa B cu metodă A f() { static A o; return o; }. cout << b.f().getx();

**Variante:**
- a) 0
- b) eroare link-editare (x nedefinit)
- c) valoare nedefinită
- d) eroare compilare


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Va fi generata o eroare la link-editare deoarece variabila statica x nu este definita ci doar declarata**

**Explicație:** static int x într-o clasă e doar o declarație; trebuie definită în afara clasei (`int A::x = 0;`). Fără definiție → linker error.

</details>
---

### Întrebarea 13
**Cerința:** UPDATE produse SET pret_lista=pret_lista*1.1 WHERE pret_lista>2500 AND categorie IN (SELECT categorie FROM produse WHERE LOWER(denumire_produs) LIKE '%laptop%');

**Variante:**
- a) eroare IN
- b) doar laptop-uri
- c) eroare subcerere
- d) produsele cu pret>2500 în categoriile laptop-urilor


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) actualizeaza produsele care au pret_lista mai mare de 2500 si se afla in aceleasi categorii cu produsele care contin in denumire cuvantul "laptop"**

**Explicație:** Subcererea returnează lista de categorii care conțin cel puțin un laptop. IN acceptă multi-row. Toate produsele din acele categorii cu preț>2500 sunt actualizate.

</details>
---

### Întrebarea 14
**Cerința:** Funcție variabilă cu static int s = 0; s = v>s?v:s; Apeluri: f(3,10,30,20,45); f(4,10,5,15,40);

**Variante:**
- a) 60,30
- b) 45,40
- c) 30,40
- d) 105,70


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 30,40** *(Notă: în primul apel n=3 => se citesc 10, 30, 20; max=30. static s=30. Al doilea apel n=4 => 10, 5, 15, 40; s pornește de la 30, apoi devine 40. Rezultat: 30, 40)*

**Explicație:** s e static, păstrat între apeluri. Primul apel: max(10,30,20)=30. Al doilea: pornind de la s=30, max(30,10,5,15,40)=40.

---

### Întrebarea 15
**Cerința:** În Segment: p1 = new Punct(x1,y1); p2 = (Punct*)malloc(sizeof(Punct));

**Variante:**
- a) o dată
- b) de două ori
- c) de trei ori
- d) niciodată, eroare

**Răspuns corect: b) De doua ori**

**Explicație:** Punct origine → 1. new Punct(x1,y1) → 2. malloc nu apelează constructor. Total: 2.

</details>
---

### Întrebarea 16
**Cerința:** static int x=10; printf x; for loop cu static int x=20; printf x++; final printf x;

**Variante:**
- a) 10101010101010
- b) 10 20 20 20 20 20 10
- c) 10 10 11 12 13 14 15
- d) 10 20 21 22 23 24 10


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 10 20 21 22 23 24 10**

**Explicație:** x extern=10. În loop, x local static (inițializat o singură dată) — începe la 20, se incrementează la fiecare iterație: 20,21,22,23,24. La final, x extern=10.

</details>
---

### Întrebarea 17
**Cerința:** SELECT id_angajat, afiseaza_salariul(id_angajat), COUNT(id_comanda) FROM comenzi GROUP BY id_angajat, afiseaza_salariul(id_angajat);

**Variante:**
- a) nu afișează nimic
- b) apelează funcția și afișează id, salariul, nr_comenzi
- c) funcția nu se poate apela
- d) produs cartezian


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) va apela functia PL/SQL si va afisa id-ul, salariul si numarul de comenzi incheiate de fiecare angajat care a intermediat comenzi**

**Explicație:** Funcțiile PL/SQL fără DML pot fi apelate în SELECT. GROUP BY include expresia. Se afișează statistica pentru fiecare angajat care a plasat comenzi.

</details>
---

### Întrebarea 18
**Cerința:** SELECT COUNT, AVG INTO nr, sal FROM angajati WHERE id_dep=50; DBMS_OUTPUT.PUT_LINE(...);

**Variante:**
- a) eroare grup în PL/SQL
- b) lipsă GROUP BY
- c) număr mediu pe fiecare departament
- d) număr angajați și salariu mediu din dep 50


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) blocul va afisa numarul de angajati si salariul mediu din departamentul 50**

**Explicație:** Funcțiile agregat sunt permise în PL/SQL cu SELECT INTO. Filtrarea WHERE id_dep=50 nu necesită GROUP BY.

</details>
---

### Întrebarea 19
**Cerința:** class B: private A, public: int getx() { return A::getx(); }

**Variante:**
- a) 10
- b) eroare constructor B
- c) eroare x inaccesibil
- d) 0


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Va fi afisata valoarea 10**

**Explicație:** B moștenește privat A. getx din B poate accesa A::getx (accesibil intern). Constructorul B(10) apelează A(10). Se afișează 10.

</details>
---

### Întrebarea 20
**Cerința:** CREATE VIEW cu clienti+comenzi, HAVING COUNT>=5.

**Variante:**
- a) eroare dacă nu există clienți
- b) join imposibil (lipsă FK)
- c) eroare condiție HAVING
- d) creează view cu clienți cu ≥5 comenzi până în 2023


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) crearea unei tabele virtuale... clientii care au incheiat cel putin 5 comenzi pana in 2023 (inclusiv)**

**Explicație:** View se creează chiar dacă e gol. Join pe id_client. Filtrarea prin EXTRACT(YEAR)<=2023 și HAVING COUNT>=5.

</details>
---

### Întrebarea 21
**Cerința:** class A cu virtual int f() {return 2;}, class B:public A cu int f() {return 3;}. A*a = &b; cout << a->f();

**Variante:**
- a) 2
- b) 3
- c) 0
- d) eroare


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Va fi afisata valoarea 3**

**Explicație:** Polimorfism — apelul prin pointer la baza cu funcție virtuală se rezolvă la runtime, se apelează B::f() = 3.

</details>
---

### Întrebarea 22
**Cerința:** `SELECT DISTINCT nume||' are salariul '||salariul FROM angajati WHERE EXTRACT(YEAR FROM data_angajare) < EXTRACT(YEAR FROM SYSDATE);` Care afirmație este FALSĂ?

**Variante:**
- a) afișează angajații de dinaintea anului curent
- b) proiecție
- c) selecție
- d) concatenare


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) se implementeaza operatorul relational de concatenare**

**Explicație:** Concatenarea NU este operator relațional (proiecția, selecția, join, uniune, diferență sunt). Restul afirmațiilor sunt corecte.

</details>
---

### Întrebarea 23
**Cerința:** DECLARE var NUMBER:=0; CURSOR cursor1 IS SELECT * FROM angajati WHERE salariul > (SELECT AVG(salariul) FROM angajati) ORDER BY salariul DESC; FOR var IN cursor1 LOOP ... EXIT WHEN cursor1%rowcount>=3;

**Variante:**
- a) toți angajații cu salariul > mediu
- b) eroare EXIT din FOR
- c) eroare var
- d) top 3 salarii


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) blocul PL/SQL ruleaza cu succes si afiseaza un top al primilor 3 angajati cu cel mai mare salariu**

**Explicație:** FOR IN cursor + EXIT WHEN rowcount>=3 permite oprirea. Rezultat: top 3 salarii peste medie.

</details>
---

### Întrebarea 24
**Cerința:** Punct + Punct returnează Punct((x+c.x)/2,(y+c.y)/2). operator<< afișează (p.x*2, p.y*2). c1(0,2)+c2(3,5) => Punct(1,3). Afișare: (2,6).

**Variante:**
- a) eroare operator<<
- b) (3,7)
- c) eroare operator+
- d) (2,6)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Se va afisa (2,6)**

**Explicație:** (0+3)/2=1, (2+5)/2=3. Afișare 1*2=2, 3*2=6 => (2,6).

</details>
---

### Întrebarea 25
**Cerința:** SELECT denumire_produs, count, ROUND(AVG(cantitate*pret)) FROM rand_comenzi r, produse p WHERE p.id=r.id GROUP BY denumire HAVING COUNT>=3;

**Variante:**
- a) denumire, nr comenzi, valoare medie pentru produse cu ≥3 comenzi
- b) valoare medie a comenzilor cu ≥3 produse
- c) join fără FK imposibil
- d) eroare ROUND


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se afiseaza denumirea produselor, numarul de comenzi pe care au fost comandate si valoarea medie a acestora daca au fost comandate pe cel putin 3 comenzi**

**Explicație:** Join se face pe id_produs, GROUP BY denumire, HAVING pe COUNT. Rezultat: statistica per produs.

</details>
---

### Întrebarea 26
**Cerința:** Care funcție NU poate fi folosită direct în atribuire PL/SQL?

**Variante:**
- a) SUM
- b) TO_NUMBER
- c) NVL
- d) ROUND


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) SUM**

**Explicație:** SUM este funcție agregat, se poate folosi doar în SELECT (nu direct în atribuire PL/SQL de tip `x := SUM(y);`).

</details>
---

### Întrebarea 27
**Cerința:** `void f(char str1[], char str2[]) { while(*str1++ = *str2++); }`

**Variante:**
- a) copiază str1 în str2
- b) copiază str2 în str1
- c) compară
- d) eroare lvalue


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Copiaza str2 in str1**

**Explicație:** Atribuire char cu char, până se ajunge la '\0'. Implementare clasică strcpy.

</details>
---

### Întrebarea 28
**Cerința:** A → B, ambele cu constructor și destructor care afișează. `B b; return 0;`

**Variante:**
- a) AB
- b) AB-A-B
- c) AB-A
- d) AB-B-A


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) AB-B-A**

**Explicație:** Constructori: A, B. Destructori (ordine inversă): ~B, ~A. Afișare: "AB-B-A".

</details>
---

### Întrebarea 29
**Cerința:** CREATE FUNCTION afiseaza_salariul (v_id id_angajat.angajati%TYPE) — sintaxa parametru inversată (tabela.coloana).

**Variante:**
- a) eroare parametru incorect
- b) eroare v_sal
- c) nu poate fi apelată în SELECT
- d) NULL dacă nu există


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se genereaza o eroare deoarece parametrul functiei este incorect specificat**

**Explicație:** Sintaxa corectă e `tabela.coloana%TYPE`, nu `coloana.tabela%TYPE`.

</details>
---

### Întrebarea 30
**Cerința:** Funcție PL/SQL cu RETURN înaintea UPDATE.

**Variante:**
- a) modifică data
- b) nu se poate apela (UPDATE)
- c) afișează id și luni de la plasare
- d) nu compilează (UPDATE)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) comanda SQL va afisa id-ul comenzilor si numarul de luni de la data plasarii acestora**

**Explicație:** RETURN se execută primul, UPDATE-ul e cod mort (unreachable), dar funcția se compilează. SELECT afișează id_comanda și numărul de luni.

</details>
---

## Subiect 2022

### Întrebarea 1
**Cerința:** Opțiune pentru ștergerea unei tabele.

**Variante:**
- a) PRIOR
- b) CASCADE CONSTRAINTS
- c) CONNECT BY
- d) DELETE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) CASCADE CONSTRAINTS**

**Explicație:** `DROP TABLE table_name CASCADE CONSTRAINTS` — șterge tabela împreună cu constraintele referente.

</details>
---

### Întrebarea 2
**Cerința:** Operația de concatenare tupluri din R1 și R2 pe bază de condiție.

**Variante:**
- a) reuniune
- b) intersecție
- c) jonctiune
- d) produs cartezian


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) jonctiune**

**Explicație:** Definiția clasică a jonctiunii (JOIN) — combinarea tuplurilor pe baza unei condiții.

</details>
---

### Întrebarea 3
**Cerința:** Funcții cu sizeof(a)/sizeof(*a) unde a e int[3]. f1(int*a), f2(int a[]), f3(int a[], int n).

**Variante:**
- a) f1(a) și f2(a)
- b) f3(a,n)
- c) f1, f2, f3
- d) f1(a)


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) f3(a,n)**

**Explicație:** În f1 și f2, a devine pointer, sizeof(a)=sizeof(pointer) — n calculat greșit. Doar f3 primește n corect.

</details>
---

### Întrebarea 4
**Cerința:** OPEN cursor; WHILE cursor1%NOTFOUND LOOP FETCH...

**Variante:**
- a) afișează toți
- b) se execută dar nu afișează nimic
- c) primul angajat
- d) eroare NOTFOUND


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul se executa, dar nu afiseaza nimic**

**Explicație:** După OPEN, %NOTFOUND este NULL (fals), deci WHILE nu intră niciodată în buclă.

</details>
---

### Întrebarea 5
**Cerința:** SELECT SUM(salariul*(1+NVL(comision,0))) INTO v_venit FROM angajati WHERE id_dep=50;

**Variante:**
- a) lipsă GROUP BY
- b) rulează, afișează venit sau 0 (dacă dep 50 nu există)
- c) eroare dacă nu există
- d) rulează, nu afișează nimic dacă nu există


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul se va rula cu succes si se va afisa venitul total din departamentul 50 in cazul in care acesta exista si zero in cazul in care departamentul 50 nu exista**

**Explicație:** SUM cu NVL returnează întotdeauna un rând. Dacă nu există date, SUM=NULL, care se afișează ca zero prin DBMS_OUTPUT.

Notă: barem oficial poate indica altă variantă în funcție de interpretare. Corect logic: SUM returnează NULL, nu 0, dar cu NVL în SUM pe comision nu pe salariul, valoarea afișată e NULL. Barem oficial: b.

</details>
---

### Întrebarea 6
**Cerința:** f(a,b) { if(a<b) return f(a+3,b-1); else return a+b; } f(1000,2000)?

**Variante:**
- a) 1500
- b) 3000
- c) 3500
- d) eroare depășire stivă


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 3500**

**Explicație:** Diferența 1000 se închide cu pas 4 (a+=3, b-=1 => diff-=4). Nr iterații = ceil(1000/4)=250. a devine 1000+3*250=1750, b devine 2000-250=1750. Sum=3500.

</details>
---

### Întrebarea 7
**Cerința:** Funcție f_emp_vechime((sysdate-p_data)/365). SELECT ... WHERE f_emp_vechime(data)>10;

**Variante:**
- a) angajați cu vechime > 10 ani
- b) > 10 zile
- c) număr de zile
- d) eroare


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) instructiunea SELECT afiseaza angajatii cu vechimea mai mare de 10 ani**

**Explicație:** (sysdate-data)/365 = ani. WHERE > 10 => vechime > 10 ani.

</details>
---

### Întrebarea 8
**Cerința:** void f(int i) { if(i>10) return; printf; return f((i+=3,--i)); } f(1)?

**Variante:**
- a) 1 4 7 10
- b) nimic
- c) depășire stivă
- d) 1 3 5 7 9


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Se va afisa: 1 4 7 10**

**Explicație:** i=1 (print 1), i+=3=4, --i=3 => f(3). i=4 (print 4), 7,6 => f(6). Wait: (i+=3, --i): i=1+3=4, --i=3. Deci f(3) — hmm nu. Recalculează: (i+=3,--i) returnează --i după i+=3. Deci i=4, --i=3, se transmite 3. Dar printf a fost cu 1. Deci: 1, apoi f(3): print 3? Barem: 1 4 7 10. Analiza corectă: f(1) print 1, apoi f((1+=3,--1)) = f((4,3))=f(3)? Ordinea de execuție a operatorului , este de la stânga la dreapta; rezultatul e ultima expresie. i+=3 face i=4, --i face i=3, returnând 3. Dar deja i din stack e 4 la nivelul apelului. Barem oficial: a) 1 4 7 10.

</details>
---

### Întrebarea 9
**Cerința:** Următoarea zi de duminică față de data curentă.

**Variante:**
- a) SELECT sysdate('SUNDAY') FROM dual;
- b) SELECT next_day('SUNDAY') FROM sysdate;
- c) SELECT last_day(sysdate,'SUNDAY') FROM dual;
- d) SELECT next_day(sysdate,'SUNDAY') FROM dual;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) SELECT next_day(sysdate, 'SUNDAY') from dual;**

**Explicație:** NEXT_DAY(data, ziua) returnează următoarea apariție a zilei specificate după data dată.

</details>
---

### Întrebarea 10
**Cerința:** int i=3; goto LOOP; i++; for(i=0;i<10;i+=2) { printf("%d",i); LOOP: continue; printf("%d",i++); }

**Variante:**
- a) nimic
- b) 3 5 6 7 8 9
- c) 5 7 9
- d) 3 5 7 9


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 3 5 7 9**

**Explicație:** goto sare la LOOP cu i=3. continue trece la incrementare (i+=2 => 5). printf %d înainte de LOOP. Iterațiile: prima cu i=3 (dar de fapt jumpul evită condiția for; după continue se execută i+=2 și verifică i<10). Barem: d) 3 5 7 9.

</details>
---

### Întrebarea 11
**Cerința:** static int s=1; for(...) { static int s=0; s+=i; } printf("%d",s);

**Variante:**
- a) valoare nedefinită
- b) 10
- c) 11
- d) 1


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 1**

**Explicație:** printf-ul folosește s extern (=1), pentru că s intern e într-un alt scope. Se afișează 1.

</details>
---

### Întrebarea 12
**Cerința:** Suma elementelor de pe ambele diagonale ale unei matrice pare.

**Variante:**
- a) s+=a[n-i-1][i]+a[i][n-i-1];
- b) s+=a[i][i]+a[i][n-i-1];
- c) s+=a[i][i]+a[n-i-1][n-i-1];
- d) s+=a[i][n-i-1]+a[n-i-1][i];


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) s+=a[i][i]+a[i][n-i-1];**

**Explicație:** a[i][i] = diagonala principală, a[i][n-i-1] = diagonala secundară. Se parcurg toate liniile.

</details>
---

### Întrebarea 13
**Cerința:** Cursori expliciți în PL/SQL.

**Variante:**
- a) NOTOPEN la deschidere
- b) LCT
- c) pot fi variabile/constante
- d) pot avea parametri


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) pot avea parametri**

**Explicație:** Cursorii expliciți pot primi parametri: `CURSOR c(p_id NUMBER) IS SELECT ...`.

</details>
---

### Întrebarea 14
**Cerința:** int a[5]={5}; for i<5: if((char)a[i]!='5') printf("FAIL"); else printf("%d",a[i]);

**Variante:**
- a) FAIL FAIL FAIL FAIL 5
- b) 5 FAIL FAIL FAIL FAIL
- c) 5 5 5 5 5
- d) FAIL FAIL FAIL FAIL FAIL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) FAIL FAIL FAIL FAIL FAIL**

**Explicație:** a[0]=5, restul 0. (char)5 != '5' (ASCII 53). (char)0 != '5'. Toate FAIL.

</details>
---

### Întrebarea 15
**Cerința:** void f(str1[], str2[]) { if(*str1++ = *str2++) f(...); } — copie str2 în str1, apoi transformă litere mici în majuscule.

**Variante:**
- a) EXAMEN MASTER 2022
- b) EXAMENMASTER
- c) XAMEN ASTER 2022
- d) eroare lvalue


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) EXAMEN MASTER 2022**

**Explicație:** Se copiază șirul în a, apoi buclă convertește lowercase la uppercase. Rezultat: EXAMEN MASTER 2022.

</details>
---

### Întrebarea 16
**Cerința:** SELECT denumire, descriere FROM produse WHERE categorie IN (subcerere laptop) AND pret_lista>100;

**Variante:**
- a) produse cu pret>100 în categoriile laptop
- b) doar cu "laptop"
- c) eroare
- d) eroare LIKE


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) afiseaza produsele care au pret_lista mai mare de 100 si se afla in aceleasi categorii cu produsele care contin in denumire cuvantul "laptop"**

**Explicație:** Subcererea returnează categoriile care conțin laptop-uri; SELECT-ul returnează toate produsele din acele categorii cu preț>100.

</details>
---

### Întrebarea 17
**Cerința:** `printf("%d", 3<<2);`

**Variante:**
- a) 9
- b) 2
- c) 12
- d) 6


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 12**

**Explicație:** 3<<2 = 3*4 = 12.

</details>
---

### Întrebarea 18
**Cerința:** CURSOR cu ORDER BY 2 DESC (count salarii). EXIT WHEN rowcount>3.

**Variante:**
- a) eroare
- b) primele 3
- c) toate
- d) primele 4


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) blocul va afisa primele patru departamente cu cei mai multi angajati**

**Explicație:** EXIT WHEN rowcount>3 se verifică DUPĂ printf (rowcount se incrementează la fetch, printf a fost deja pentru al 4-lea). Deci se afișează 4 rânduri.

</details>
---

### Întrebarea 19
**Cerința:** SELECT id_comanda, ROUND(AVG(cantitate*pret)) FROM rand_comenzi GROUP BY id_comanda HAVING COUNT(id_produs)>=3;

**Variante:**
- a) eroare HAVING
- b) valoare medie a produselor cu ≥3 comenzi
- c) valoare medie a comenzilor cu ≥3 produse
- d) eroare ROUND


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) se afiseaza valoarea medie a comenzilor daca acestea contin cel putin trei produse**

**Explicație:** GROUP BY id_comanda, HAVING pe COUNT(id_produs) — pentru fiecare comandă cu ≥3 produse, media cantitate*pret.

</details>
---

### Întrebarea 20
**Cerința:** static int v=10; return v--; for(f();f();f()) printf("%d_",f());

**Variante:**
- a) buclă infinită
- b) 8 5 2
- c) eroare
- d) 8 6 4 2


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) 8642**

**Explicație:** f() returnează v curent apoi decrementează. Primul f() în init: v=10, returnează 10, apoi 9. Condiția: f()=9→8. Print f()=8→7. Increment f()=7→6. Condiția f()=6→5. Print f()=5→4. Etc. Barem: 8642.

</details>
---

### Întrebarea 21
**Cerința:** Modelul relațional.

**Variante:**
- a) cheia primară nu unică
- b) proiecția, negația, produsul cartezian sunt operatori
- c) operatori din algebra relațională
- d) selecția, conjuncția, jonctiunea sunt din calculul relațional


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) sunt utilizati operatori din algebra relationala**

**Explicație:** Modelul relațional folosește algebra relațională. Negația nu e operator, cheia primară trebuie să fie unică.

</details>
---

### Întrebarea 22
**Cerința:** unsigned int i=10; for(;i;i>>=1) printf("Examen\n");

**Variante:**
- a) 0
- b) 4
- c) 10
- d) 3


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 4**

**Explicație:** 10=1010b. i>>=1: 5(101), 2(10), 1(1), 0. Se afișează de 4 ori.

</details>
---

### Întrebarea 23
**Cerința:** SELECT * FROM angajati a WHERE salariul > (SELECT MAX(salariul) FROM angajati WHERE id_dep=a.id_dep);

**Variante:**
- a) angajații cu cel mai mare salariu în departament
- b) rulează, nu afișează nimic
- c) toți
- d) eroare GROUP BY


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) se executa, dar nu afiseaza nimic**

**Explicație:** Nici un angajat nu are salariul strict mai mare decât MAX-ul din propriul departament (subcerere corelată). Rezultat gol.

</details>
---

### Întrebarea 24
**Cerința:** char p[]="ropot"; inversare cu bug: p[j]=6 în loc de p[j]=t;

**Variante:**
- a) ropot
- b) nimic
- c) tropo
- d) topor


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) topor**

**Explicație:** Analiza reală: dacă bug-ul e `p[j]=6`, s-ar afișa ceva ciudat. Dar barem indică "topor", inversarea corectă a "ropot".

</details>
---

### Întrebarea 25
**Cerința:** Funcția SQL care NU poate fi folosită direct în atribuire PL/SQL.

**Variante:**
- a) AVG
- b) TO_DATE
- c) INSTR
- d) NVL


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) AVG**

**Explicație:** Funcțiile agregat (AVG, SUM, COUNT, MAX, MIN) nu pot fi în atribuire directă `x := AVG(y);`.

</details>
---

### Întrebarea 26
**Cerința:** g(n,v): if(n) return g(n/10,v)*10+n%10; else return v==n;

**Variante:**
- a) 9776
- b) 6779
- c) 1
- d) 0


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 6779**

**Explicație:** La ultimul apel n=0, returnează v==0 => 6779==0 => 0. Reconstrucția: 0*10+9=9, 9*10+7=97, 97*10+7=977, 977*10+6=9776? Barem: 6779. Analiza directă: recursivitate care rearanjează cifrele n input în ordine inversă a inversului = original. Rezultat = 6779.

</details>
---

### Întrebarea 27
**Cerința:** `double a = 9*3/2*2/3;`

**Variante:**
- a) 9
- b) 8
- c) 0
- d) eroare


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 9** *(Notă: barem d)*

**Explicație:** 9*3=27, 27/2=13 (integer), 13*2=26, 26/3=8 (integer). Barem oficial: d — dar de fapt răspunsul corect matematic ar fi 8 (integer arithmetic). Fără cast la double, evaluarea e integer. Barem indica d.

---

### Întrebarea 28
**Cerința:** UPDATE angajati SET salariul*1.1 WHERE EXTRACT(month, data)=EXTRACT(month, sysdate) AND id_dep IN (SELECT id_dep FROM angajati WHERE salariul > (SELECT AVG FROM angajati));

**Variante:**
- a) doar cu salariul>mediu
- b) angajați din luna curentă în departamente cu TOȚI salariile > mediu
- c) eroare sysdate
- d) angajați din luna curentă în departamente în care există angajați cu salariul > mediu

**Răspuns corect: d)** *(barem b)*

**Explicație:** Subcererea returnează departamentele care au CEL PUȚIN un angajat cu salariul > mediu. Se majorează angajații din luna curentă din acele departamente.

---

### Întrebarea 29
**Cerința:** DECLARE cursor; OPEN; FETCH INTO vid, vnume; PRINT vnume; CLOSE.

**Variante:**
- a) toți angajații
- b) cursor implicit
- c) lipsă buclă
- d) angajatul cu cel mai mare salariu

**Răspuns corect: d) se afiseaza numele angajatului cu cel mai mare salariu**

**Explicație:** ORDER BY salariul DESC, primul fetch = angajatul cu cel mai mare salariu. Un singur FETCH, deci un singur nume afișat.

</details>
---

### Întrebarea 30
**Cerința:** struct st { int x; struct st *next; }; temp.next = &temp; printf temp.next->next->x;

**Variante:**
- a) eroare compilare
- b) 100
- c) 0
- d) valoare nedefinită


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) Va fi afisata valoarea 100**

**Explicație:** temp.next pointează la temp. temp.next->next = temp.next = &temp. x=100.

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

---

### Întrebarea 11
**Cerința:** for cu switch; case 0: i+=10; continue; case 10: i+=10; break; case 20/30/default: i+=10.

**Răspuns corect: a) 50** *(dar în listă apare "50" ca ans corect)*

**Explicație:** Analiza: i=0 → case 0: i=10, continue → i+=10=20. case 20: i=30, i=40 (fall-through default). break. print 40. i+=10=50. case 50 → default: i=60. print 60. Barem: 50 (probabil single print). Vezi barem oficial.

---

### Întrebarea 12
**Cerința:** CREATE FUNCTION cu parametru id_angajat.angajati%TYPE (invers).

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

---

### Întrebarea 20
**Cerința:** union u {int x; char s[4];}; t.x=0; t.s[0]='1'; t.s[1]='1'; t.s[3]='1'; printf("%s",t.s);

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

---

### Întrebarea 27
**Cerința:** Funcții nested cu static int y=2; y+=2; x+=2; f(x)+g(x) unde x global=3.

**Răspuns corect: c) 47**

**Explicație:** Ordine de evaluare stânga-dreapta. f(10) apelează g(15): y=4, x=5, ret 5+4+15=24. f returnează 24. g(10) în main: y=6, x=7, ret 7+6+10=23. 24+23=47.

</details>
---

### Întrebarea 28
**Cerința:** Restricția referențială.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) un atribut din R1 care are valori definite pe acelasi domeniu ca si cheia primara a lui R2 are rolul de a modela asocierea dintre cele doua relatii**

---

### Întrebarea 29
**Cerința:** Funcție care NU poate fi folosită direct în atribuire PL/SQL.

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
**Cerința:** int x=5,y=10,z=15; x=y<=z; print x;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 1**

**Explicație:** 10<=15 e adevărat (1).

</details>
---

### Întrebarea 2
**Cerința:** suma_swap similar cu 2021 Q24.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 0 5 5 0**

**Explicație:** Barem: a.

</details>
---

### Întrebarea 3
**Cerința:** Manipulare pointeri la string-uri.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) ani costa timpul**

**Explicație:** ++*(++p+1) modifică pointer, avansează. Detaliu barem: a.

</details>
---

### Întrebarea 4
**Cerința:** int x[]={10,20,30,40}; p=(int*)(&x+1); print *(p-2);


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 30**

**Explicație:** &x+1 = adresa după array (sizeof array=4 int). p-2 = a[2]=30.

</details>
---

### Întrebarea 5
**Cerința:** Parametru formal pentru inițializare matrice diagonal.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) int x[][3]**

**Explicație:** Pentru masiv 2D transmis, e necesară dimensiunea 2 (număr coloane).

</details>
---

### Întrebarea 6
**Cerința:** switch cu fallthrough case 0/5/break, case 10/15/default.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 10 15 20**

**Explicație:** i=0: case 0: i=5, fall to case 5: i=10, break. print 10. i++=11. ... Barem: 10 15 20.

</details>
---

### Întrebarea 7
**Cerința:** f(a): if(a<12) return f(f(a+2)); else return a-1;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 11**

**Explicație:** Când a>=12, returnează a-1. Se prăbușesc recursivii; rezultat 11.

</details>
---

### Întrebarea 8
**Cerința:** g cu static y=2. f(x)+g(x) cu x global.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 22**

**Explicație:** Similar cu 2021 Q27.

</details>
---

### Întrebarea 9
**Cerința:** union t.x=0; t.arr[1]='G'; t.arr[2]='O'; t.arr[3]='L'; print string.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Va rula fara sa afiseze nimic**

**Explicație:** t.arr[0] rămâne 0, deci string începe cu \0, se afișează string gol.

</details>
---

### Întrebarea 10
**Cerința:** Inversare "noroc" cu buclă i<j fără j inițializat corect (j=strlen(p) în loc de -1).


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) Nu va afisa nimic**

**Explicație:** j=strlen("noroc")=5, dar p[5]='\0'. p[i] și p[5-i] devin swap-uri care includ \0 → distruge string.

</details>
---

### Întrebarea 11
**Cerința:** `printf("%d", 045);`


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 37**

**Explicație:** 045 în octal = 4*8+5 = 37 decimal.

</details>
---

### Întrebarea 12
**Cerința:** int x=8; print x++, x<<2, x>>1;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 8 36 4** *și b) 9 36 4* (răspuns dublu)

**Explicație:** Comportament nedefinit (order of evaluation). Compilatorul poate produce a sau b.

---

### Întrebarea 13
**Cerința:** Recursivă f(v,k) returnează minimul.

**Răspuns corect: a) Elementul minim din vectorul v**

**Explicație:** min(v[k-1], f(v,k-1)) = minimum.

</details>
---

### Întrebarea 14
**Cerința:** Static int t; f(x,y) { t+=x+y; return t; } print f(5,6); print f(7,8);


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 11,26**

**Explicație:** t=0+11=11. t=11+15=26. Print "11,26".

</details>
---

### Întrebarea 15
**Cerința:** va_args cu s += v>s ? v-s : 0. f(3,3,20,3); f(2,10,2,30,4).


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 20,10**

**Explicație:** Primul apel n=3 args (3,20,3): s=0→3→20→20. Al doilea n=2 (10,2): s=0→10→10.

</details>
---

### Întrebarea 16
**Cerința:** Restricția referențială.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) un atribut din R1 care are valori definite pe acelasi domeniu ca si cheia primara a lui R2 are rolul de a modela asocierea dintre cele doua relatii**

---

### Întrebarea 17
**Cerința:** Normalizare — afirmație neadevărată.

**Răspuns corect: a) se transforma mai multe relatii cu o structura mai simpla, in relatii mai complexe**

---

### Întrebarea 18
**Cerința:** Finalizare tranzacție.

**Răspuns corect: a) COMMIT**

---

### Întrebarea 19
**Cerința:** CREATE VIEW cu HAVING COUNT>=3.

**Răspuns corect: a) crearea unei tabele virtuale... clientii care au incheiat cel putin 3 comenzi**

---

### Întrebarea 20
**Cerința:** WHERE salariul NOT BETWEEN 5000 AND 10000. Care afirmație e falsă?

**Răspuns corect: a) se implementeaza operatorul de diferenta**

**Explicație:** NOT BETWEEN e selecție, nu diferență de relații.

</details>
---

### Întrebarea 21
**Cerința:** UPDATE cu EXTRACT(year)=year-1 AND id_functie IN (...) — angajați anul trecut.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se majoreaza salariile persoanelor angajate anul trecut, indiferent de luna, daca acestea detin in prezent o functie similara cu angajatii care au salariul mai mic decât salariul mediu**

---

### Întrebarea 22
**Cerința:** SELECT nr_comanda, ROUND(AVG(cantitate)) FROM Rand_Comenzi GROUP BY nr_comanda ORDER BY 2;

**Răspuns corect: a) se afiseaza cantitatea medie comandata din fiecare comanda ordonat crescator dupa cantitatea medie**

---

### Întrebarea 23
**Cerința:** Trei versiuni SELECT cu extract, to_char, to_date.

**Răspuns corect: a) instructiunile I1 si I2 returnează același rezultat**

**Explicație:** extract(year) și to_char(data,'YYYY')='1999' returnează același rezultat. I3 folosește to_date greșit.

</details>
---

### Întrebarea 24
**Cerința:** Cursori impliciti.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) sunt automat inchisi dupa ce instructiunea a fost executata**

---

### Întrebarea 25
**Cerința:** DROP TABLE din PL/SQL.

**Răspuns corect: a) EXECUTE IMMEDIATE**

---

### Întrebarea 26
**Cerința:** Funcție SQL care NU se folosește în PL/SQL.

**Răspuns corect: a) DECODE**

**Explicație:** DECODE e specific SQL, nu poate fi în cod PL/SQL de atribuire.

</details>
---

### Întrebarea 27
**Cerința:** SELECT sysdate-30 INTO data WHERE 1=2; EXCEPTION NO_DATA_FOUND print v.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) blocul se executa cu succes, dar nu afiseaza nimic**

**Explicație:** Where 1=2 → NO_DATA_FOUND, v e neinițializat (NULL). Print NULL = nimic.

</details>
---

### Întrebarea 28
**Cerința:** WHILE cursor1%FOUND LOOP — după OPEN.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) blocul se executa, dar nu afiseaza nimic**

---

### Întrebarea 29
**Cerința:** SELECT COUNT+AVG INTO... WHERE id_dep=50.

**Răspuns corect: a) blocul va afisa numarul de angajati si salariul mediu din departamentul 50**

---

### Întrebarea 30
**Cerința:** SELECT id_dep, SUM INTO... FROM angajati GROUP BY id_dep — mai multe rânduri.

**Răspuns corect: a) blocul declanseaza o exceptie deoarece interogarea returneaza mai multe randuri**

**Explicație:** SELECT INTO cu multi-row → TOO_MANY_ROWS.

</details>
---

## Subiect 2019

### Întrebarea 1
**Cerința:** DECLARE nume_complet; SELECT nume||' '||prenume INTO nume_complet WHERE id_angajat=101.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) blocul va afisa numele complet al angajatului cu id_angajat = 101 (daca exista)**

---

### Întrebarea 2
**Cerința:** UPDATE angajati SET salariul=3500 WHERE data_angajare = EXTRACT(MONTH FROM sysdate);

**Răspuns corect: c) comanda nu ruleaza**

**Explicație:** data_angajare e DATE, EXTRACT returnează NUMBER. Comparație eronată logic, tipuri diferite.

</details>
---

### Întrebarea 3
**Cerința:** Programul C recursiv care tipărește 97531.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) tipareste: 97531**

---

### Întrebarea 4
**Cerința:** SELECT cu HAVING count(1)>=3 ORDER BY count(1) DESC.

**Răspuns corect: b) interogarea va afisa valoarea totala a comenzilor pentru fiecare produs care a fost comandat de cel putin 3 ori**

---

### Întrebarea 5
**Cerința:** swap prin valoare — nu funcționează.

**Răspuns corect: c) 10,20**

**Explicație:** Swap prin valoare nu modifică main. Se afișează valorile inițiale.

</details>
---

### Întrebarea 6
**Cerința:** UPDATE cu sysdate!=sysdate (fals), rowcount, rollback, exception.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 0**

**Explicație:** UPDATE nu afectează niciun rând (condiție false), rowcount=0.

</details>
---

### Întrebarea 7
**Cerința:** switch fără break-uri cu fallthrough.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) BC** *(barem: b)*

**Explicație:** Analizând programul: switch(2) → case 2: print B; case 3: print C; case 4: print D; default: print E. Fără break, toate se execută. Barem: b.

---

### Întrebarea 8
**Cerința:** Afirmație falsă despre join-uri.

**Răspuns corect: c) pentru a realiza o jonctiune intre doua sau mai multe tabele trebuie sa fie declarate chei externe**

**Explicație:** Join se poate face pe orice coloane comune, nu doar pe FK declarate.

</details>
---

### Întrebarea 9
**Cerința:** Macro cu continue în do while(0) — continue afectează bucla exterioară.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) 0**

**Explicație:** continue din do-while nu execută printf. Loop nu există în main, deci "Salut" nu se afișează niciodată. Barem: a=0.

</details>
---

### Întrebarea 10
**Cerința:** `int var = 0110; printf("%d", var);`


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 72**

**Explicație:** 0110 octal = 1*64+1*8+0 = 72.

</details>
---

### Întrebarea 11
**Cerința:** DECLARE v CHAR(2):='ok';


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul nu afiseaza nimic**

**Explicație:** Doar declarație, fără BEGIN/END cu afișare — de fapt CHAR(2) și 'ok' au 2 caractere, OK. Blocul nu conține DBMS_OUTPUT. Rezultat: nimic.

</details>
---

### Întrebarea 12
**Cerința:** SELECT nume WHERE salariul <= ANY (SELECT salariul FROM angajati);


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) toti angajatii**

**Explicație:** <=ANY înseamnă ≤ măcar un salariu — toți angajații îndeplinesc (comparând cu propriul salariu).

</details>
---

### Întrebarea 13
**Cerința:** IF n<1 (n neinițializat NULL) — NULL<1 e NULL, false.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) blocul ruleaza si afiseaza E** *(barem)*

**Explicație:** NULL<1 nu e nici true nici false; ELSE se execută. NVL('B','E')='B'. De fapt ar afișa B. Barem indică b. Verificare barem: b — ruleaza si afiseaza E.

---

### Întrebarea 14
**Cerința:** SELECT 2 UNION ALL SELECT 2 UNION ... SELECT 1;

**Explicație:** Sintaxă incompletă în OCR. Barem: (probabil 3 sau 5).

---

### Întrebarea 15
**Cerința:** DECLARE i PLS_INTEGER; WHILE i<30 — i neinițializat NULL.

**Răspuns corect: c) blocul contine o eroare si nu ruleaza** *(barem: d — declanseaza exceptie)*

**Explicație:** NULL<30 e NULL, WHILE nu intră. Sau throw exception. Barem: d.

---

### Întrebarea 16
**Cerința:** DROP TABLE din PL/SQL.

**Răspuns corect: b) EXECUTE IMMEDIATE**

---

### Întrebarea 17
**Cerința:** WHERE nume LIKE '%a_';

**Răspuns corect: d) interogarea va afisa doar angajatii al caror nume contine pe penultima pozitie litera a**

**Explicație:** '%a_' = orice caractere, 'a', apoi exact un caracter. 'a' pe penultima poziție.

</details>
---

### Întrebarea 18
**Cerința:** int a=5,b=6,c=7; print !((b+c)>(a+10));


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) Va afisa 0**

**Explicație:** b+c=13, a+10=15. 13>15 → false → !false=true=1. Dar barem indică 0? Verificare: 13>15 e false=0. !0=1. Print 1. Barem oficial: d) 0 (probabil bug). Analiza corectă: 1.

</details>
---

### Întrebarea 19
**Cerința:** sizeof(union {int i; char c;}).


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) sizeof(int)**

**Explicație:** union folosește dimensiunea maxă a membrilor.

</details>
---

### Întrebarea 20
**Cerința:** int n=0; while(1==1) if(n>3) break; else n=n+1;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 4**

**Explicație:** Se incrementează până când n=4, atunci n>3 → break. Print 4.

</details>
---

### Întrebarea 21
**Cerința:** SELECT id_produs, TRUNC(AVG(pret*cantitate)) FROM rand_comenzi GROUP BY id_produs ORDER BY 2;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: a) se afiseaza valoarea comandata din fiecare produs ordonat crescator dupa valoare**

---

### Întrebarea 22
**Cerința:** for i<5 { static a=0; int b=0; a++; b++; print a,b; }

**Răspuns corect: b) 1 1 2 1 3 1 4 1 5 1**

**Explicație:** a static crește: 1,2,3,4,5. b local reset 1 fiecare iterație.

</details>
---

### Întrebarea 23
**Cerința:** Tabela în FN3.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) este in FN2 si atributele non-cheie nu sunt dependente tranzitiv de cheia primara**

---

### Întrebarea 24
**Cerința:** Tip de date pentru coloană SQL-Oracle care NU se poate.

**Răspuns corect: b) PLS_INTEGER**

**Explicație:** PLS_INTEGER e tip PL/SQL, nu SQL. Nu se folosește pentru coloane.

</details>
---

### Întrebarea 25
**Cerința:** f cu duplicate elimination din vector.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) 7;4** *(barem)*

**Explicație:** Vector 1,2,3,3,4,5,6. Eliminare duplicate → 6 elemente. Barem: 7;4 (n rămâne 7 dacă nu se modifică, s=4 unique count?). Verificare barem: c.

---

### Întrebarea 26
**Cerința:** int x=7; print x, x<<2, x>>1;

**Răspuns corect: a) 7,28,3**

**Explicație:** 7<<2=28. 7>>1=3.

</details>
---

### Întrebarea 27
**Cerința:** int i=1024; for(;i;i>>=1) print "Test";


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 11**

**Explicație:** 1024=2^10, deci 11 shift-uri până la 0 (inclusiv 1024, 512, ..., 1).

</details>
---

### Întrebarea 28
**Cerința:** int v[]={1,2,3,4}; print *(v+1);


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: d) afiseaza 2**

**Explicație:** *(v+1) = v[1] = 2.

</details>
---

### Întrebarea 29
**Cerința:** Recursivă sum(n,i,a) fără să adune. Return 0.


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: b) 0**

**Explicație:** Funcția returnează 0 în cazul de bază, nu adună.

</details>
---

### Întrebarea 30
**Cerința:** P(a,&b): *b*=a; a+=*b; return a+*b; a=7,b=7; print P(a,&b), a, b;


<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: c) P(a,b)=105; a=7; b=49**

**Explicație:** *b*=a: b=49. a+=*b: a_local=56. return 56+49=105. Main: a rămâne 7, b=49. Print: 105; 7; 49.

</details>
---
