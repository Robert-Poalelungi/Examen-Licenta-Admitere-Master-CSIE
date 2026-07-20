# REZUMAT TEORETIC COMPLET — Examen Master CSIE3

> Ghid ultra-detaliat cu analogii din viața reală, explicat astfel încât oricine să înțeleagă.
> Programe: IE cercetare · Baze de date · E-Business · SIMRPE · TIID

---

## CUPRINS

1. [Baze de date relaționale](#1-baze-de-date-relaționale)
2. [Programarea în SQL](#2-programarea-în-sql)
3. [Programarea în PLSQL](#3-programarea-în-plsql)
4. [Programarea în C](#4-programarea-în-c)
5. [Programare orientată obiect în C++](#5-programare-orientată-obiect-în-c)

---

# 1. BAZE DE DATE RELAȚIONALE

## Analogia de bază — ce este o bază de date?

Imaginează-ți că lucrezi la o librărie mare. Ai mii de cărți, sute de clienți, zeci de comenzi pe zi. Dacă ai ține toate informațiile pe foi volante, ar fi un haos total — nu ai găsi nimic, datele s-ar repeta, ai face greșeli.

**Baza de date** este echivalentul unui dulap de fișiere ultra-organizat, unde fiecare sertar conține un tip de informație (cărți, clienți, comenzi), fiecare dosar din sertar este un rând (o carte anume, un client anume), și fiecare câmp din dosar este o informație specifică (titlul cărții, numele clientului).

**Baza de date relațională** înseamnă că aceste sertare (tabele) sunt **legate între ele** — poți să spui "comanda nr. 5 aparține clientului Ion Popescu și conține cartea nr. 42".

---

## 1.1 Modelul relațional — structura datelor

Modelul relațional a fost inventat de **E.F. Codd în 1970** și se bazează pe matematică (teoria mulțimilor și algebra relațională). Are trei componente:

### Structura relațională (cum arată datele)

**Domeniu** = mulțimea tuturor valorilor posibile pentru un tip de informație.

Exemplu: Domeniul "Vârstă" = toate numerele întregi între 0 și 150. Domeniul "Gen" = {'M', 'F'}. Domeniul "Nume" = toate șirurile de caractere de max 50 litere.

**Relație (tabel)** = o colecție de înregistrări de același tip, organizate ca un tabel.

```
Tabelul ANGAJATI:
+----+-------------+--------+------------+
| ID | Nume        | Salar  | Departament|
+----+-------------+--------+------------+
|  1 | Ion Popescu | 5000   | IT         |
|  2 | Ana Ionescu | 6000   | HR         |
|  3 | Mihai Popa  | 4500   | IT         |
+----+-------------+--------+------------+
```

- Fiecare **linie (rând)** = un **tuplu** = o înregistrare = un angajat
- Fiecare **coloană** = un **atribut** = o caracteristică (ID, Nume, Salar, Departament)
- **Gradul relației** = numărul de coloane (aici: 4)
- **Cardinalitatea relației** = numărul de rânduri (aici: 3)

**Cheie primară (Primary Key, PK)** = coloana (sau combinația de coloane) care identifică **în mod unic** fiecare rând. Este ca CNP-ul unui om — nu există două persoane cu același CNP.

Proprietăți:
- **Unicitate**: nu există două rânduri cu aceeași valoare a cheii primare
- **Minimalitate**: nu poți elimina nicio coloană din cheie fără a pierde unicitatea
- **NOT NULL**: cheia primară nu poate fi goală (NULL)

Exemplu: În tabelul ANGAJATI, coloana ID este cheie primară. Nu pot exista doi angajați cu ID=1.

**Cheie externă (Foreign Key, FK)** = coloana dintr-un tabel care face referire la cheia primară dintr-alt tabel. Este ca o adresă — în comanda ta scrie "clientul cu ID=5", iar acel ID=5 trebuie să existe în tabelul CLIENTI.

```
COMENZI:
+----+------------+----------+
| ID | ID_Client  | Produs   |
+----+------------+----------+
|  1 |     5      | Carte A  |
|  2 |     3      | Carte B  |
+----+------------+----------+

CLIENTI:
+----+-------------+
| ID | Nume        |
+----+-------------+
|  3 | Maria Popa  |
|  5 | Dan Ionescu |
+----+-------------+
```

ID_Client din COMENZI este FK care referă ID din CLIENTI. Această legătură se numește **integritate referențială** — nu poți avea o comandă cu ID_Client=99 dacă clientul cu ID=99 nu există.

---

### Operatorii relației (ce poți face cu tabelele)

**Algebra relațională** = un set de operații matematice pe tabele care returnează tot tabele.

Analogie: Imaginează-ți că tabelele sunt mulțimi de bilețele. Poți:
- Combina bilețele din două grămezi (reuniune)
- Lua doar bilețelele care sunt în prima grămadă dar nu în a doua (diferență)
- Lua doar bilețelele comune (intersecție)

**Operații pe mulțimi** (ambele tabele trebuie să aibă aceleași coloane):

- **Reuniunea R₁ ∪ R₂** = toate rândurile din ambele tabele, fără duplicate
- **Diferența R₁ − R₂** = rândurile din R₁ care NU apar în R₂
- **Intersecția R₁ ∩ R₂** = rândurile care apar în AMBELE tabele
- **Produsul cartezian R₁ × R₂** = combinarea FIECĂRUI rând din R₁ cu FIECARE rând din R₂

Exemplu produs cartezian:
```
R₁: {A, B}     R₂: {1, 2, 3}
R₁ × R₂ = {(A,1), (A,2), (A,3), (B,1), (B,2), (B,3)}
```

**Operații relaționale specifice**:

- **Selecția (σ)** = filtrarea rândurilor după o condiție. Ca un filtru de email — arată-mi doar emailurile din ultimele 7 zile.
  - `σ Salar > 5000 (ANGAJATI)` → returnează angajații cu salar mai mare de 5000

- **Proiecția (π)** = selectarea anumitor coloane. Ca un tabel Excel unde ascunzi coloanele care nu te interesează.
  - `π Nume, Salar (ANGAJATI)` → returnează doar coloanele Nume și Salar

- **Joncțiunea (JOIN)** = combinarea tabelelor pe baza unor condiții. Ca lipirea a două foi de calcul pe coloana comună.
  - `ANGAJATI ⋈ DEPARTAMENTE` pe condiția `ANGAJATI.Dep_ID = DEPARTAMENTE.ID`

- **Diviziunea** = inversul produsului cartezian. "Găsește angajații care au lucrat în TOATE proiectele."

---

## 1.2 Dependențe funcționale și normalizare

### Dependența funcțională

**Dependența funcțională X → Y** înseamnă că valorile din coloana X determină în mod unic valorile din coloana Y.

Analogie: CNP → Nume. Dacă știi CNP-ul cuiva, știi cu certitudine numele lui. Dar Nume → CNP NU este adevărat — pot fi mai mulți "Ion Popescu".

Exemple:
- `ID_Angajat → Nume, Salar, Data_angajare` (ID-ul angajatului determină toate info lui)
- `ID_Produs → Pret_unitar` (ID-ul produsului determină prețul)
- `ID_Comanda, ID_Produs → Cantitate` (combinația comandă + produs determină cantitatea)

### Normalizarea

**Normalizarea** = procesul de reorganizare a tabelelor pentru a elimina redundanța și anomaliile.

Analogie: Dacă ai o agendă de telefon unde la fiecare număr de telefon scrii și adresa completă a persoanei, și persoana se mută, trebuie să schimbi adresa la FIECARE număr de telefon al ei — e redundant și predispus la erori. Normalizarea = separi adresa într-o fișă separată și o referi.

**Anomalii** ce apar fără normalizare:
- **Anomalia de inserare**: nu poți adăuga un nou departament fără să ai un angajat în el
- **Anomalia de ștergere**: dacă ștergi ultimul angajat dintr-un departament, pierzi și informațiile departamentului
- **Anomalia de actualizare**: dacă schimbi adresa unui furnizor, trebuie s-o schimbi în toate rândurile

**Forma Normală 1 (1NF)**:
- Fiecare celulă conține o singură valoare (atomică), nu liste
- NU OK: `Telefoane: "0721111111, 0722222222"` (două valori în o celulă)
- OK: Tabel separat TELEFOANE cu câte un rând per număr

**Forma Normală 2 (2NF)**:
- Este în 1NF
- Fiecare coloană care nu e cheie primară depinde de **întreaga** cheie primară (nu doar de o parte)
- Se aplică când cheia primară este compusă (din mai multe coloane)

Exemplu de problemă:
```
DETALII_COMANDA(ID_Comanda, ID_Produs, Cantitate, Nume_Produs, Pret)
```
Cheia primară = (ID_Comanda, ID_Produs). Dar Nume_Produs și Pret depind doar de ID_Produs, nu de combinația (ID_Comanda, ID_Produs). Aceasta este o dependență parțială — trebuie eliminată.

Soluție 2NF:
```
DETALII_COMANDA(ID_Comanda, ID_Produs, Cantitate)
PRODUSE(ID_Produs, Nume_Produs, Pret)
```

**Forma Normală 3 (3NF)**:
- Este în 2NF
- Nu există dependențe tranzitive (A → B → C, unde A e cheia primară)

Exemplu de problemă:
```
ANGAJATI(ID, Nume, ID_Departament, Nume_Departament, Oras_Sediu)
```
ID → ID_Departament → Nume_Departament și Oras_Sediu. Aceasta este o dependență tranzitivă.

Soluție 3NF:
```
ANGAJATI(ID, Nume, ID_Departament)
DEPARTAMENTE(ID_Departament, Nume_Departament, Oras_Sediu)
```

**Forma Normală Boyce-Codd (BCNF)**:
- Versiune mai strictă a 3NF
- Orice dependență funcțională X → Y trebuie ca X să fie superkey (să determine TOATE atributele)

---

## 1.3 Constrângeri de integritate

**Integritatea entității**: Cheia primară nu poate fi NULL.

**Integritatea referențială**: Valorile din cheia externă trebuie să existe în tabelul referit (sau să fie NULL dacă e permis).

**Acțiuni la ștergere/actualizare** (ce se întâmplă cu rândurile referite când șterg/modific cheia primară):
- `CASCADE`: șterge/actualizează automat și rândurile dependente
- `SET NULL`: pune NULL în cheia externă
- `RESTRICT`: blochează operația dacă există rânduri dependente
- `SET DEFAULT`: pune valoarea implicită

---

# 2. PROGRAMAREA ÎN SQL

## Ce este SQL?

**SQL (Structured Query Language)** = limbajul cu care "vorbești" cu baza de date. Este ca limbajul natural, dar pentru computere.

Analogie: Dacă baza de date este o bibliotecă imensă cu milioane de cărți, SQL este limbajul cu care ceri bibliotecarului ce vrei:
- "Dă-mi toate cărțile de programare publicate după 2020" = SELECT
- "Adaugă cartea asta nouă" = INSERT
- "Schimbă prețul cărții X" = UPDATE
- "Șterge cartea Y" = DELETE

SQL are mai multe sub-limbaje:
- **DDL (Data Definition Language)**: CREATE, ALTER, DROP — definești structura (creezi/modifici/ștergi tabele)
- **DML (Data Manipulation Language)**: INSERT, UPDATE, DELETE, SELECT — manipulezi datele
- **DCL (Data Control Language)**: GRANT, REVOKE — controlezi cine ce poate face
- **TCL (Transaction Control Language)**: COMMIT, ROLLBACK, SAVEPOINT — controlezi tranzacțiile

---

## 2.1 DDL — Definirea structurii

### CREATE TABLE — Crearea unui tabel

```sql
CREATE TABLE Studenti (
    ID         NUMBER(5)      PRIMARY KEY,
    Nume       VARCHAR2(50)   NOT NULL,
    Prenume    VARCHAR2(50)   NOT NULL,
    Data_Nast  DATE,
    Email      VARCHAR2(100)  UNIQUE,
    Medie      NUMBER(4,2)    CHECK (Medie BETWEEN 1 AND 10),
    ID_Facultate NUMBER(3)    REFERENCES Facultati(ID)
);
```

Explicație coloană cu coloană:
- `ID NUMBER(5) PRIMARY KEY` = coloana ID, număr de maxim 5 cifre, este cheia primară
- `Nume VARCHAR2(50) NOT NULL` = text de maxim 50 caractere, nu poate fi gol
- `Email VARCHAR2(100) UNIQUE` = fiecare email trebuie să fie diferit (ca la cont Google)
- `Medie NUMBER(4,2) CHECK (Medie BETWEEN 1 AND 10)` = număr cu 4 cifre total, 2 zecimale, trebuie să fie între 1 și 10
- `ID_Facultate REFERENCES Facultati(ID)` = cheie externă — valoarea trebuie să existe în tabelul Facultati

**Tipuri de date frecvente**:
- `NUMBER(p,s)` = număr cu p cifre totale, s zecimale. Ex: NUMBER(5,2) poate stoca 999.99
- `VARCHAR2(n)` = text variabil de maxim n caractere (economisește spațiu)
- `CHAR(n)` = text fix de exact n caractere (completează cu spații dacă e mai scurt)
- `DATE` = dată și oră (în Oracle include și ora)
- `CLOB` = text foarte lung (mii de pagini)
- `BLOB` = date binare (imagini, fișiere)

**Constrângeri (CONSTRAINT)**:
- `PRIMARY KEY` = identificator unic
- `NOT NULL` = câmpul nu poate fi gol
- `UNIQUE` = nu pot exista duplicate
- `CHECK (condiție)` = valoarea trebuie să respecte condiția
- `FOREIGN KEY ... REFERENCES` = legătură cu alt tabel
- `DEFAULT valoare` = valoarea implicită dacă nu se specifică

```sql
-- Constrângere la nivel de tabel (cu nume):
CREATE TABLE Produse (
    ID     NUMBER PRIMARY KEY,
    Pret   NUMBER,
    Stoc   NUMBER,
    CONSTRAINT chk_pret_pozitiv CHECK (Pret > 0),
    CONSTRAINT chk_stoc CHECK (Stoc >= 0)
);
```

### ALTER TABLE — Modificarea structurii

```sql
-- Adaugă o coloană nouă:
ALTER TABLE Studenti ADD (Telefon VARCHAR2(15));

-- Modifică tipul/dimensiunea unei coloane:
ALTER TABLE Studenti MODIFY (Nume VARCHAR2(100));

-- Șterge o coloană:
ALTER TABLE Studenti DROP COLUMN Telefon;

-- Adaugă o constrângere:
ALTER TABLE Studenti ADD CONSTRAINT fk_facultate
    FOREIGN KEY (ID_Facultate) REFERENCES Facultati(ID);

-- Dezactivează o constrângere:
ALTER TABLE Studenti DISABLE CONSTRAINT fk_facultate;
```

### DROP TABLE și TRUNCATE

```sql
-- Șterge tabelul complet (structură + date):
DROP TABLE Studenti;

-- Șterge toate datele, păstrează structura (mult mai rapid decât DELETE):
TRUNCATE TABLE Studenti;
```

---

## 2.2 DML — Manipularea datelor

### INSERT — Inserarea datelor

```sql
-- Inserare cu toate coloanele (ordinea contează):
INSERT INTO Studenti VALUES (1, 'Popescu', 'Ion', DATE '2000-05-15', 'ion@email.com', 9.50, 1);

-- Inserare cu specificarea explicită a coloanelor (recomandat):
INSERT INTO Studenti (ID, Nume, Prenume, Email, Medie)
VALUES (2, 'Ionescu', 'Ana', 'ana@email.com', 8.75);

-- Inserare din rezultatul unui SELECT:
INSERT INTO Studenti_Buni (ID, Nume, Medie)
SELECT ID, Nume, Medie FROM Studenti WHERE Medie >= 9;
```

### UPDATE — Actualizarea datelor

```sql
-- ATENȚIE: fără WHERE, actualizezi TOATE rândurile!
UPDATE Studenti SET Medie = 10 WHERE ID = 1;

-- Actualizare cu expresii:
UPDATE Produse SET Pret = Pret * 1.10 WHERE Categorie = 'IT'; -- crește prețul cu 10%

-- Actualizare cu subquery:
UPDATE Angajati SET Salar = Salar * 1.15
WHERE ID_Dept = (SELECT ID FROM Departamente WHERE Nume = 'IT');
```

### DELETE — Ștergerea datelor

```sql
-- ATENȚIE: fără WHERE, ștergi TOATE rândurile!
DELETE FROM Studenti WHERE ID = 5;

-- Ștergere cu subquery:
DELETE FROM Comenzi WHERE ID_Client IN
    (SELECT ID FROM Clienti WHERE Activ = 'N');
```

---

## 2.3 SELECT — Cel mai important! Interogarea datelor

**SELECT** este 90% din ce folosești în SQL. Structura completă:

```sql
SELECT   [DISTINCT] coloane
FROM     tabele
[WHERE   condiție_filtrare_rânduri]
[GROUP BY coloane_grupare]
[HAVING  condiție_filtrare_grupuri]
[ORDER BY coloane_sortare [ASC|DESC]];
```

**Ordinea de execuție** (NU ordinea în care scrii!):
1. **FROM** — alege tabelele
2. **WHERE** — filtrează rândurile
3. **GROUP BY** — grupează
4. **HAVING** — filtrează grupurile
5. **SELECT** — selectează coloanele
6. **ORDER BY** — sortează rezultatul

Analogie: Ești bucătar care face o salată.
1. **FROM**: alegi ingredientele (tabele)
2. **WHERE**: elimini ingredientele stricate (filtrezi rânduri)
3. **GROUP BY**: pui ingredientele pe categorii (legume, proteine, etc.)
4. **HAVING**: elimini categoriile cu prea puțin din ele
5. **SELECT**: tai și prezinți ce ingrediente vrei în farfurie
6. **ORDER BY**: aranjezi frumos

### SELECT simplu

```sql
-- Toate coloanele, toate rândurile:
SELECT * FROM Studenti;

-- Coloane specifice:
SELECT Nume, Prenume, Medie FROM Studenti;

-- Cu alias (redenumire coloană):
SELECT Nume AS "Numele studentului", Medie * 10 AS "Punctaj" FROM Studenti;

-- Valori distincte (elimină duplicate):
SELECT DISTINCT Departament FROM Angajati;
```

### WHERE — Condiții de filtrare

```sql
-- Operatori de comparație:
SELECT * FROM Studenti WHERE Medie >= 9;
SELECT * FROM Studenti WHERE Medie <> 5; -- diferit de 5 (<> sau != sau ^=)

-- BETWEEN (între două valori, inclusiv):
SELECT * FROM Produse WHERE Pret BETWEEN 100 AND 500;

-- IN (în lista de valori):
SELECT * FROM Studenti WHERE ID_Facultate IN (1, 2, 3);

-- LIKE (potrivire șablon):
-- % = orice număr de caractere (inclusiv 0)
-- _ = exact un caracter
SELECT * FROM Studenti WHERE Nume LIKE 'P%';       -- începe cu P
SELECT * FROM Studenti WHERE Nume LIKE '%escu';     -- se termină cu escu
SELECT * FROM Studenti WHERE Prenume LIKE 'A_a';   -- A, orice caracter, a (ex: Ana, Ala)

-- IS NULL / IS NOT NULL:
SELECT * FROM Studenti WHERE Telefon IS NULL;      -- fără telefon înregistrat
SELECT * FROM Studenti WHERE Email IS NOT NULL;    -- are email

-- Operatori logici:
SELECT * FROM Studenti WHERE Medie >= 8 AND ID_Facultate = 1;
SELECT * FROM Studenti WHERE Medie < 5 OR Absente > 50;
SELECT * FROM Studenti WHERE NOT (Medie >= 5);
```

### Funcții SQL

#### Funcții pe șiruri de caractere

```sql
-- UPPER / LOWER: convertește la majuscule/minuscule
SELECT UPPER('Ion Popescu') FROM DUAL;  -- ION POPESCU
SELECT LOWER('ION') FROM DUAL;          -- ion

-- LENGTH: lungimea unui șir
SELECT LENGTH('Hello') FROM DUAL;  -- 5

-- SUBSTR(text, pozitie_start, lungime): extrage o porțiune
-- Pozițiile încep de la 1 în SQL!
SELECT SUBSTR('Popescu', 1, 3) FROM DUAL;  -- Pop
SELECT SUBSTR('Popescu', 4) FROM DUAL;     -- escu (de la poz 4 până la final)

-- INSTR(text, subtext): găsește poziția unui subtext
SELECT INSTR('Ion Popescu', 'Pop') FROM DUAL;  -- 5

-- REPLACE(text, de_inlocuit, cu): înlocuiește un text
SELECT REPLACE('buna ziua', 'ziua', 'dimineata') FROM DUAL;  -- buna dimineata

-- TRIM / LTRIM / RTRIM: elimină spații (sau caractere specifice)
SELECT TRIM('  hello  ') FROM DUAL;   -- 'hello'
SELECT LTRIM('  hello') FROM DUAL;    -- 'hello'
SELECT RTRIM('hello  ') FROM DUAL;    -- 'hello'

-- CONCAT sau || (concatenare):
SELECT 'Buna ' || 'ziua' FROM DUAL;   -- Buna ziua
SELECT CONCAT('Hello', ' World') FROM DUAL;  -- Hello World

-- LPAD / RPAD: umple cu caractere la stânga/dreapta
SELECT LPAD('42', 5, '0') FROM DUAL;   -- 00042
SELECT RPAD('Ana', 10, '*') FROM DUAL; -- Ana*******
```

#### Funcții numerice

```sql
-- ROUND(nr, zecimale): rotunjire
SELECT ROUND(3.14159, 2) FROM DUAL;  -- 3.14
SELECT ROUND(3.567, 0) FROM DUAL;    -- 4

-- TRUNC(nr, zecimale): trunchiare (fără rotunjire)
SELECT TRUNC(3.99, 0) FROM DUAL;     -- 3 (nu 4!)
SELECT TRUNC(3.789, 1) FROM DUAL;    -- 3.7

-- CEIL / FLOOR: rotunjire în sus/jos
SELECT CEIL(3.1) FROM DUAL;   -- 4
SELECT FLOOR(3.9) FROM DUAL;  -- 3

-- ABS: valoarea absolută
SELECT ABS(-15) FROM DUAL;  -- 15

-- MOD(nr, divizor): restul împărțirii
SELECT MOD(10, 3) FROM DUAL;  -- 1 (10 = 3*3 + 1)

-- POWER(baza, exponent):
SELECT POWER(2, 10) FROM DUAL;  -- 1024

-- SQRT: rădăcina pătrată
SELECT SQRT(16) FROM DUAL;  -- 4
```

#### Funcții pentru date calendaristice

```sql
-- SYSDATE: data și ora curentă a serverului
SELECT SYSDATE FROM DUAL;

-- ADD_MONTHS(data, luni): adaugă luni la o dată
SELECT ADD_MONTHS(SYSDATE, 6) FROM DUAL;  -- peste 6 luni

-- MONTHS_BETWEEN(data1, data2): diferența în luni
SELECT MONTHS_BETWEEN(DATE '2024-01-01', DATE '2023-01-01') FROM DUAL;  -- 12

-- NEXT_DAY(data, ziua_saptamanii): prima zi din săptămână după dată
SELECT NEXT_DAY(SYSDATE, 'MONDAY') FROM DUAL;  -- următoarea luni

-- LAST_DAY(data): ultima zi a lunii
SELECT LAST_DAY(DATE '2024-02-01') FROM DUAL;  -- 2024-02-29 (2024 e bisect)

-- TRUNC(data, 'MM'): trunchierea la prima zi a lunii
SELECT TRUNC(SYSDATE, 'MM') FROM DUAL;  -- Prima zi a lunii curente

-- TO_DATE: convertește text la dată
SELECT TO_DATE('15-05-2024', 'DD-MM-YYYY') FROM DUAL;

-- TO_CHAR: convertește dată la text
SELECT TO_CHAR(SYSDATE, 'DD/MM/YYYY HH24:MI:SS') FROM DUAL;

-- Aritmetică cu date:
SELECT SYSDATE + 30 FROM DUAL;        -- Data de peste 30 de zile
SELECT SYSDATE - DATE '2024-01-01' FROM DUAL;  -- Numărul de zile între date
```

#### Funcții de conversie

```sql
-- TO_NUMBER: text la număr
SELECT TO_NUMBER('3.14') FROM DUAL;

-- TO_CHAR: număr/dată la text
SELECT TO_CHAR(12345.67, '99,999.99') FROM DUAL;  -- 12,345.67

-- NVL(valoare, inlocuitor): înlocuiește NULL cu o valoare
SELECT NVL(Telefon, 'Fara telefon') FROM Studenti;

-- NVL2(valoare, daca_nu_null, daca_null):
SELECT NVL2(Telefon, 'Are telefon', 'Fara telefon') FROM Studenti;

-- COALESCE(val1, val2, val3,...): primul non-NULL din listă
SELECT COALESCE(Telefon, Email, 'Necontactabil') FROM Studenti;

-- NULLIF(val1, val2): returnează NULL dacă val1 = val2, altfel returnează val1
SELECT NULLIF(Salar, 0) FROM Angajati;  -- Dacă salariul e 0, returnează NULL
```

#### Funcții de grup (agregare)

Aceste funcții operează pe **mai multe rânduri** și returnează **un singur rezultat**.

Analogie: Funcțiile de grup sunt ca un profesor care ia notele tuturor elevilor și calculează media clasei, sau găsește nota maximă, etc.

```sql
-- COUNT: numără rândurile
SELECT COUNT(*) FROM Studenti;                    -- Numărul total de studenți
SELECT COUNT(Telefon) FROM Studenti;              -- Câți studenți AU telefon (ignoră NULL)
SELECT COUNT(DISTINCT ID_Facultate) FROM Studenti; -- Câte facultăți distincte

-- SUM: suma valorilor
SELECT SUM(Salar) FROM Angajati;                  -- Fondul total de salarii

-- AVG: media aritmetică (ignoră NULL!)
SELECT AVG(Medie) FROM Studenti;                  -- Media generală a studenților

-- MAX / MIN: maximul și minimul
SELECT MAX(Salar), MIN(Salar) FROM Angajati;      -- Cel mai mare și mic salar

-- Exemplu complet:
SELECT
    COUNT(*) AS "Nr studenti",
    AVG(Medie) AS "Media",
    MAX(Medie) AS "Cea mai mare nota",
    MIN(Medie) AS "Cea mai mica nota"
FROM Studenti
WHERE ID_Facultate = 1;
```

**IMPORTANT**: Funcțiile de grup NU pot apărea în WHERE! Ele vin în HAVING.

---

### GROUP BY — Gruparea datelor

**GROUP BY** împarte tabelul în grupuri pe baza valorilor din una sau mai multe coloane, și aplică funcțiile de grup separat pe fiecare grup.

Analogie: Ești profesor și vrei să calculezi media per clasă. Grupezi elevii după clasă (GROUP BY clasa), apoi calculezi media pentru fiecare grup.

```sql
-- Media salariilor per departament:
SELECT Departament, AVG(Salar) AS "Media salarii"
FROM Angajati
GROUP BY Departament;
```

**Regulă importantă**: Orice coloană din SELECT care NU este o funcție de grup TREBUIE să apară în GROUP BY.

```sql
-- CORECT:
SELECT Departament, Oras, COUNT(*) FROM Angajati
GROUP BY Departament, Oras;

-- GREȘIT (Oras nu e în GROUP BY):
SELECT Departament, Oras, COUNT(*) FROM Angajati
GROUP BY Departament;  -- eroare!
```

### HAVING — Filtrarea grupurilor

**HAVING** filtrează **grupurile** (după GROUP BY), la fel cum WHERE filtrează rândurile.

```sql
-- Departamentele cu mai mult de 5 angajați:
SELECT Departament, COUNT(*) AS nr_angajati
FROM Angajati
GROUP BY Departament
HAVING COUNT(*) > 5;

-- Departamentele cu media salariului > 5000:
SELECT Departament, AVG(Salar) AS media
FROM Angajati
GROUP BY Departament
HAVING AVG(Salar) > 5000
ORDER BY media DESC;
```

**Diferența WHERE vs HAVING**:
- WHERE filtrează rândurile **înainte** de grupare (nu poate folosi funcții de grup)
- HAVING filtrează grupurile **după** grupare (poate folosi funcții de grup)

```sql
-- Vreau departamentele cu > 3 angajați care câștigă > 3000:
SELECT Departament, COUNT(*) AS nr
FROM Angajati
WHERE Salar > 3000        -- mai întâi, păstrez doar angajații cu salar > 3000
GROUP BY Departament
HAVING COUNT(*) > 3;      -- apoi, din grupuri, îl păstrez pe cel cu > 3 oameni
```

### ORDER BY — Sortarea rezultatelor

```sql
-- Sortare crescătoare (implicită):
SELECT * FROM Studenti ORDER BY Medie;
SELECT * FROM Studenti ORDER BY Medie ASC;  -- același lucru

-- Sortare descrescătoare:
SELECT * FROM Studenti ORDER BY Medie DESC;

-- Sortare după mai multe coloane:
SELECT * FROM Angajati ORDER BY Departament ASC, Salar DESC;
-- Sortează mai întâi după departament, iar în cadrul aceluiași departament, după salar descrescător

-- Sortare după poziția coloanei din SELECT:
SELECT Nume, Prenume, Medie FROM Studenti ORDER BY 3 DESC;  -- a 3-a coloana = Medie
```

---

## 2.4 JOIN — Combinarea tabelelor

**JOIN** combină rândurile din două sau mai multe tabele pe baza unei condiții. Este una dintre operațiile cele mai importante din SQL.

Analogie: Ai două foi Excel — una cu studenți (ID, Nume, ID_Facultate) și una cu facultăți (ID, Nume_Facultate). JOIN le lipești împreună pe coloana ID-ului facultății, ca să poți vedea în același loc numele studentului și numele facultății lui.

### INNER JOIN (sau simplu JOIN)

Returnează **doar rândurile care au corespondent în AMBELE tabele**.

Analogie: Vrei studenții care AU o facultate asignată, și facultăților care AU studenți. Orice student fără facultate sau facultate fără studenți NU apare.

```sql
-- Sintaxă cu JOIN ... ON:
SELECT s.Nume, s.Prenume, f.Nume_Facultate
FROM Studenti s
INNER JOIN Facultati f ON s.ID_Facultate = f.ID;

-- Sintaxă veche cu WHERE (echivalent):
SELECT s.Nume, s.Prenume, f.Nume_Facultate
FROM Studenti s, Facultati f
WHERE s.ID_Facultate = f.ID;
```

Aliasurile de tabel (`s` și `f`) sunt prescurtări — scrii `s.Nume` în loc de `Studenti.Nume`.

### LEFT JOIN (LEFT OUTER JOIN)

Returnează **toate rândurile din tabelul din stânga** + rândurile cu corespondent din dreapta. Dacă nu există corespondent în dreapta, coloanele din dreapta sunt NULL.

Analogie: Vrei TOȚI studenții, chiar și cei care nu sunt asignați la o facultate. Studenții fără facultate vor apărea cu NULL în coloana facultate.

```sql
SELECT s.Nume, s.Prenume, f.Nume_Facultate
FROM Studenti s
LEFT JOIN Facultati f ON s.ID_Facultate = f.ID;

-- Rezultat posibil:
-- Ion Popescu | Informatica
-- Ana Ionescu | NULL         <- studentă fără facultate
-- Mihai Popa  | Contabilitate
```

### RIGHT JOIN (RIGHT OUTER JOIN)

Returnează **toate rândurile din tabelul din dreapta** + corespondentele din stânga.

```sql
SELECT s.Nume, f.Nume_Facultate
FROM Studenti s
RIGHT JOIN Facultati f ON s.ID_Facultate = f.ID;

-- Rezultat posibil:
-- Ion Popescu  | Informatica
-- NULL         | Filosofie     <- facultate fără studenți
```

### FULL OUTER JOIN

Returnează **toate rândurile din ambele tabele**, cu NULL acolo unde nu există corespondent.

```sql
SELECT s.Nume, f.Nume_Facultate
FROM Studenti s
FULL OUTER JOIN Facultati f ON s.ID_Facultate = f.ID;
```

### CROSS JOIN

Produsul cartezian — combină fiecare rând din primul tabel cu fiecare rând din al doilea.

```sql
SELECT s.Nume, c.Curs FROM Studenti s CROSS JOIN Cursuri c;
-- Dacă ai 100 studenți și 20 cursuri → 2000 rânduri rezultat
```

### JOIN pe mai multe tabele

```sql
SELECT s.Nume, f.Nume_Facultate, c.Curs
FROM Studenti s
JOIN Facultati f ON s.ID_Facultate = f.ID
JOIN Inscrieri i ON i.ID_Student = s.ID
JOIN Cursuri c ON i.ID_Curs = c.ID
WHERE s.Medie >= 8
ORDER BY s.Nume;
```

---

## 2.5 Subinterogări (Subqueries)

**Subinterogarea** este un SELECT în interiorul altui SELECT. Rezultatul subinterogării este folosit de interogarea exterioară.

Analogie: "Dă-mi angajații care câștigă mai mult decât media firmei." Pentru a rezolva asta, mai întâi calculezi media (subinterogare), apoi compari fiecare angajat cu acea medie (interogare principală).

### Subinterogare în WHERE

```sql
-- Studenți cu media mai mare decât media tuturor studenților:
SELECT Nume, Medie
FROM Studenti
WHERE Medie > (SELECT AVG(Medie) FROM Studenti);

-- Angajații din același departament ca 'Ion Popescu':
SELECT Nume FROM Angajati
WHERE ID_Dept = (SELECT ID_Dept FROM Angajati WHERE Nume = 'Ion Popescu');
```

### Subinterogare cu IN, ANY, ALL

```sql
-- Studenți înscriși la cursul 'Baze de date':
SELECT Nume FROM Studenti
WHERE ID IN (
    SELECT ID_Student FROM Inscrieri
    WHERE ID_Curs = (SELECT ID FROM Cursuri WHERE Denumire = 'Baze de date')
);

-- Angajați cu salariul mai mare decât ORICE angajat din departamentul 2:
SELECT Nume, Salar FROM Angajati
WHERE Salar > ANY (SELECT Salar FROM Angajati WHERE ID_Dept = 2);

-- Angajați cu salariul mai mare decât TOȚI angajații din departamentul 2:
SELECT Nume, Salar FROM Angajati
WHERE Salar > ALL (SELECT Salar FROM Angajati WHERE ID_Dept = 2);
```

### EXISTS — verificarea existenței

```sql
-- Studenți care au cel puțin o notă de 10:
SELECT Nume FROM Studenti s
WHERE EXISTS (
    SELECT 1 FROM Note n
    WHERE n.ID_Student = s.ID AND n.Nota = 10
);
```

EXISTS returnează TRUE dacă subinterogarea returnează cel puțin un rând.

### Subinterogare corelată

Subinterogarea se referă la tabelul din interogarea principală (se execută pentru fiecare rând):

```sql
-- Angajații care câștigă mai mult decât media departamentului lor:
SELECT Nume, Salar, ID_Dept
FROM Angajati a
WHERE Salar > (
    SELECT AVG(Salar) FROM Angajati b
    WHERE b.ID_Dept = a.ID_Dept  -- referință la rândul curent
);
```

---

## 2.6 Operatori pe mulțimi

```sql
-- UNION: reuniunea (elimină duplicate):
SELECT Nume FROM Studenti
UNION
SELECT Nume FROM Profesori;

-- UNION ALL: reuniunea (cu duplicate):
SELECT Nume FROM Studenti
UNION ALL
SELECT Nume FROM Profesori;

-- INTERSECT: intersecția:
SELECT Nume FROM Studenti
INTERSECT
SELECT Nume FROM Profesori;

-- MINUS (Oracle) / EXCEPT (standard): diferența:
SELECT Nume FROM Studenti
MINUS
SELECT Nume FROM Profesori;
-- Studenți care NU sunt și profesori
```

---

## 2.7 Funcția CASE

CASE este ca un if-else din programare, dar în SQL:

```sql
-- CASE simplu:
SELECT Nume,
    CASE Nota
        WHEN 10 THEN 'Excelent'
        WHEN 9  THEN 'Foarte bine'
        WHEN 8  THEN 'Bine'
        ELSE 'Satisfacator'
    END AS "Calificativ"
FROM Note;

-- CASE căutat (cu condiții):
SELECT Nume, Medie,
    CASE
        WHEN Medie >= 9.5 THEN 'Summa Cum Laude'
        WHEN Medie >= 9   THEN 'Magna Cum Laude'
        WHEN Medie >= 8   THEN 'Cum Laude'
        WHEN Medie >= 5   THEN 'Promovat'
        ELSE 'Respins'
    END AS "Status"
FROM Studenti;

-- DECODE (Oracle-specific, echivalent CASE simplu):
SELECT Nume,
    DECODE(Activ, 'Y', 'Activ', 'N', 'Inactiv', 'Necunoscut') AS Status
FROM Utilizatori;
```

---

# 3. PROGRAMAREA ÎN PL/SQL

## Ce este PL/SQL?

**PL/SQL (Procedural Language/SQL)** = extensia Oracle a SQL care adaugă capabilități procedurale (variabile, condiții if/else, bucle, proceduri, funcții, etc.).

Analogie: SQL singur e ca o casă calculatoare bună — îi dai o întrebare, îți dă un răspuns. PL/SQL e ca un robot programabil — poți să-i dai o secvență de instrucțiuni, să ia decizii, să repete operații, să gestioneze erori.

---

## 3.1 Structura unui bloc PL/SQL

Orice cod PL/SQL are această structură:

```sql
DECLARE
    -- Secțiunea de declarații: variabile, cursori, tipuri
    -- Opțional — poate lipsi dacă nu ai variabile
    v_nume     VARCHAR2(50);
    v_varsta   NUMBER := 0;    -- := este operatorul de atribuire în PL/SQL
    v_activ    BOOLEAN := TRUE;
    c_maxim    CONSTANT NUMBER := 100;  -- constantă (nu se poate modifica)

BEGIN
    -- Secțiunea executabilă: instrucțiunile care se execută
    -- OBLIGATORIU
    v_nume := 'Ion Popescu';
    DBMS_OUTPUT.PUT_LINE('Buna ziua, ' || v_nume);

EXCEPTION
    -- Secțiunea de gestionare a erorilor
    -- Opțional
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('A aparut o eroare!');
END;
/   -- Slash-ul execută blocul PL/SQL (în SQL*Plus)
```

---

## 3.2 Variabile și tipuri de date

```sql
DECLARE
    -- Tipuri simple:
    v_text     VARCHAR2(100) := 'Hello';
    v_numar    NUMBER(8,2)   := 3.14;
    v_data     DATE          := SYSDATE;
    v_bool     BOOLEAN       := FALSE;

    -- %TYPE — preia tipul din coloana unui tabel (se actualizează automat):
    v_salar    Angajati.Salar%TYPE;     -- are tipul coloanei Salar din tabelul Angajati
    v_emp_name Angajati.Nume%TYPE;

    -- %ROWTYPE — preia structura unui întreg rând din tabel:
    rec_angajat  Angajati%ROWTYPE;      -- o variabilă cu toate câmpurile din Angajati

BEGIN
    -- Atribuire cu %ROWTYPE:
    SELECT * INTO rec_angajat FROM Angajati WHERE ID = 1;
    DBMS_OUTPUT.PUT_LINE(rec_angajat.Nume || ' ' || rec_angajat.Salar);

    -- Atribuire cu SELECT INTO (pentru valori scalare):
    SELECT Salar INTO v_salar FROM Angajati WHERE ID = 1;
    DBMS_OUTPUT.PUT_LINE('Salariul este: ' || v_salar);
END;
/
```

**De ce %TYPE și %ROWTYPE?**
Dacă schimbi tipul coloanei în tabel (ex: din VARCHAR2(50) în VARCHAR2(100)), variabila declarată cu %TYPE se actualizează automat — nu trebuie să modifici codul PL/SQL. Este o practică excelentă de programare.

---

## 3.3 Instrucțiuni de control

### IF-THEN-ELSIF-ELSE

```sql
DECLARE
    v_nota NUMBER := 7.5;
    v_calificativ VARCHAR2(20);
BEGIN
    IF v_nota >= 9 THEN
        v_calificativ := 'Excelent';
    ELSIF v_nota >= 7 THEN
        v_calificativ := 'Bine';
    ELSIF v_nota >= 5 THEN
        v_calificativ := 'Satisfacator';
    ELSE
        v_calificativ := 'Respins';
    END IF;

    DBMS_OUTPUT.PUT_LINE('Calificativul este: ' || v_calificativ);
END;
/
```

### CASE

```sql
DECLARE
    v_zi NUMBER := 3;
    v_nume_zi VARCHAR2(20);
BEGIN
    CASE v_zi
        WHEN 1 THEN v_nume_zi := 'Luni';
        WHEN 2 THEN v_nume_zi := 'Marti';
        WHEN 3 THEN v_nume_zi := 'Miercuri';
        WHEN 4 THEN v_nume_zi := 'Joi';
        WHEN 5 THEN v_nume_zi := 'Vineri';
        ELSE v_nume_zi := 'Weekend';
    END CASE;

    DBMS_OUTPUT.PUT_LINE('Ziua: ' || v_nume_zi);
END;
/
```

### Bucle (LOOP)

**Loop simplu** (trebuie EXIT manual):
```sql
DECLARE
    v_contor NUMBER := 1;
BEGIN
    LOOP
        DBMS_OUTPUT.PUT_LINE('Iteratia: ' || v_contor);
        v_contor := v_contor + 1;
        EXIT WHEN v_contor > 5;  -- condiția de ieșire
    END LOOP;
END;
/
```

**WHILE LOOP** (verifică condiția la început):
```sql
DECLARE
    v_contor NUMBER := 1;
BEGIN
    WHILE v_contor <= 5 LOOP
        DBMS_OUTPUT.PUT_LINE('Iteratia: ' || v_contor);
        v_contor := v_contor + 1;
    END LOOP;
END;
/
```

**FOR LOOP** (număr fix de iterații):
```sql
BEGIN
    -- Numărare crescătoare de la 1 la 5:
    FOR i IN 1..5 LOOP
        DBMS_OUTPUT.PUT_LINE('i = ' || i);
    END LOOP;

    -- Numărare descrescătoare:
    FOR i IN REVERSE 1..5 LOOP
        DBMS_OUTPUT.PUT_LINE('i = ' || i);  -- 5, 4, 3, 2, 1
    END LOOP;
END;
/
```

---

## 3.4 Cursori

### Ce este un cursor?

Un **cursor** este un pointer care parcurge rând cu rând rezultatul unui SELECT.

Analogie: Când execuți un SELECT care returnează 1000 de rânduri, Oracle nu-ți dă toate 1000 de rânduri odată (ar ocupa multă memorie). Cursorul este ca un deget care arată pe rând fiecare linie a rezultatului — o citești, prelucrezi, apoi cursorul avansează la următoarea.

SQL are de fapt doi cursori:
- **Cursor implicit**: creat automat de Oracle pentru fiecare instrucțiune SQL (INSERT, UPDATE, DELETE, SELECT INTO)
- **Cursor explicit**: declarat de programator pentru a parcurge rând cu rând un SELECT cu mai multe rânduri

### Cursor explicit — ciclu complet

```sql
DECLARE
    -- Pas 1: DECLARI cursorul cu SELECT-ul lui
    CURSOR c_angajati IS
        SELECT ID, Nume, Salar FROM Angajati WHERE Departament = 'IT';

    -- Variabilele pentru a stoca rândul curent:
    v_id     Angajati.ID%TYPE;
    v_nume   Angajati.Nume%TYPE;
    v_salar  Angajati.Salar%TYPE;
BEGIN
    -- Pas 2: DESCHIZI cursorul (execută SELECT-ul, pregătește rezultatele)
    OPEN c_angajati;

    -- Pas 3: PARCURGI rând cu rând
    LOOP
        -- FETCH = citește rândul curent și avansează cursorul
        FETCH c_angajati INTO v_id, v_nume, v_salar;

        -- Verifici dacă mai sunt rânduri:
        EXIT WHEN c_angajati%NOTFOUND;

        DBMS_OUTPUT.PUT_LINE(v_id || ': ' || v_nume || ' - ' || v_salar);
    END LOOP;

    -- Pas 4: ÎNCHIZI cursorul (eliberezi memoria)
    CLOSE c_angajati;
END;
/
```

### Atributele cursorului

```sql
-- %FOUND: TRUE dacă ultimul FETCH a returnat un rând
-- %NOTFOUND: TRUE dacă ultimul FETCH NU a returnat rând (am ajuns la final)
-- %ISOPEN: TRUE dacă cursorul este deschis
-- %ROWCOUNT: numărul de rânduri prelucrate până acum
```

### FOR LOOP cu cursor (cea mai elegantă metodă)

PL/SQL deschide, parcurge și închide cursorul automat:

```sql
DECLARE
    CURSOR c_studenti IS
        SELECT Nume, Medie FROM Studenti ORDER BY Medie DESC;
BEGIN
    FOR rec IN c_studenti LOOP
        -- rec este un %ROWTYPE implicit, cu câmpurile Nume și Medie
        DBMS_OUTPUT.PUT_LINE(rec.Nume || ' - ' || rec.Medie);
    END LOOP;
    -- Cursorul e închis automat!
END;
/
```

### Cursor cu parametri

```sql
DECLARE
    CURSOR c_ang_dept (p_dept VARCHAR2) IS
        SELECT Nume, Salar FROM Angajati WHERE Departament = p_dept;
BEGIN
    -- Poți folosi același cursor cu departamente diferite:
    DBMS_OUTPUT.PUT_LINE('=== IT ===');
    FOR rec IN c_ang_dept('IT') LOOP
        DBMS_OUTPUT.PUT_LINE(rec.Nume || ' - ' || rec.Salar);
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('=== HR ===');
    FOR rec IN c_ang_dept('HR') LOOP
        DBMS_OUTPUT.PUT_LINE(rec.Nume || ' - ' || rec.Salar);
    END LOOP;
END;
/
```

### Cursor FOR UPDATE

Permite modificarea rândurilor parcurse de cursor:

```sql
DECLARE
    CURSOR c_ang IS
        SELECT ID, Salar FROM Angajati FOR UPDATE OF Salar;
BEGIN
    FOR rec IN c_ang LOOP
        IF rec.Salar < 3000 THEN
            -- WHERE CURRENT OF = actualizează rândul curent al cursorului
            UPDATE Angajati SET Salar = Salar * 1.10
            WHERE CURRENT OF c_ang;
        END IF;
    END LOOP;
    COMMIT;
END;
/
```

---

## 3.5 Excepții

### Ce este o excepție?

O **excepție** este o eroare care apare la execuție. PL/SQL permite "prinderea" și gestionarea erorilor fără ca programul să se blocheze.

Analogie: Imaginează-ți că ești la o bancă automată. Dacă introduci un card incorect (eroare), ATM-ul nu se blochează complet — îți afișează un mesaj de eroare și te lasă să încerci din nou. Excepția = eroarea. Gestionarea excepției = mesajul "card invalid, încearcă din nou."

### Excepții predefinite Oracle

```sql
BEGIN
    -- ...
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        -- SELECT INTO nu a găsit niciun rând
        DBMS_OUTPUT.PUT_LINE('Înregistrarea nu a fost găsită!');

    WHEN TOO_MANY_ROWS THEN
        -- SELECT INTO a găsit mai mult de un rând
        DBMS_OUTPUT.PUT_LINE('Prea multe înregistrări!');

    WHEN ZERO_DIVIDE THEN
        -- Împărțire la zero
        DBMS_OUTPUT.PUT_LINE('Nu se poate împărți la zero!');

    WHEN DUP_VAL_ON_INDEX THEN
        -- Violare cheie unică (INSERT cu valoare duplicată)
        DBMS_OUTPUT.PUT_LINE('Valoare duplicată!');

    WHEN VALUE_ERROR THEN
        -- Eroare de tip/dimensiune (ex: text prea lung pentru o variabilă)
        DBMS_OUTPUT.PUT_LINE('Eroare de valoare/tip!');

    WHEN OTHERS THEN
        -- Prinde ORICE altă eroare
        DBMS_OUTPUT.PUT_LINE('Eroare: ' || SQLERRM);  -- SQLERRM = mesajul erorii
        DBMS_OUTPUT.PUT_LINE('Cod: ' || SQLCODE);      -- SQLCODE = codul numeric al erorii
END;
/
```

### Excepții definite de utilizator

```sql
DECLARE
    e_salar_negativ EXCEPTION;  -- declarăm excepția noastră
    v_salar NUMBER := -500;
BEGIN
    IF v_salar < 0 THEN
        RAISE e_salar_negativ;  -- aruncăm excepția
    END IF;

    DBMS_OUTPUT.PUT_LINE('Salar valid: ' || v_salar);

EXCEPTION
    WHEN e_salar_negativ THEN
        DBMS_OUTPUT.PUT_LINE('Eroare: Salariul nu poate fi negativ!');
END;
/
```

### RAISE_APPLICATION_ERROR

Permite trimiterea de mesaje de eroare personalizate cu coduri de eroare custom:

```sql
-- Coduri de eroare disponibile: -20000 până la -20999
IF v_varsta < 0 THEN
    RAISE_APPLICATION_ERROR(-20001, 'Vârsta nu poate fi negativă!');
END IF;
```

---

## 3.6 Proceduri stocate

**Procedura** = bloc PL/SQL salvat în baza de date, cu un nume, care poate fi apelat oricând.

Analogie: O procedură este ca o rețetă de gătit salvată. Nu mai trebuie să respecifici toți pașii de fiecare dată — dai un simplu apel "prepară_carbonara" și rețeta se execută.

```sql
-- CREAREA procedurii:
CREATE OR REPLACE PROCEDURE mareste_salar (
    p_id_angajat  IN  Angajati.ID%TYPE,      -- parametru de intrare
    p_procent     IN  NUMBER,                 -- parametru de intrare
    p_salar_nou   OUT Angajati.Salar%TYPE    -- parametru de ieșire
) AS
    v_salar_curent Angajati.Salar%TYPE;
BEGIN
    SELECT Salar INTO v_salar_curent
    FROM Angajati WHERE ID = p_id_angajat;

    p_salar_nou := v_salar_curent * (1 + p_procent / 100);

    UPDATE Angajati SET Salar = p_salar_nou
    WHERE ID = p_id_angajat;

    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Salariul angajatului ' || p_id_angajat ||
                         ' a crescut la ' || p_salar_nou);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Angajat negăsit!');
        ROLLBACK;
END mareste_salar;
/

-- APELAREA procedurii:
DECLARE
    v_salar_final NUMBER;
BEGIN
    mareste_salar(1, 15, v_salar_final);  -- crește cu 15% salariul angajatului 1
    DBMS_OUTPUT.PUT_LINE('Salariul nou: ' || v_salar_final);
END;
/
```

**Tipuri de parametri**:
- `IN` = parametru de intrare (valoarea vine din exterior, nu poate fi modificat)
- `OUT` = parametru de ieșire (procedura îi atribuie o valoare, apelantul o primește)
- `IN OUT` = intrare și ieșire (vine cu o valoare, se poate modifica, apelantul primește valoarea modificată)

---

## 3.7 Funcții stocate

**Funcția** = ca procedura, dar **returnează o valoare** și poate fi folosită în expresii SQL.

```sql
-- CREAREA funcției:
CREATE OR REPLACE FUNCTION calc_varsta (
    p_data_nastere IN DATE
) RETURN NUMBER AS
    v_varsta NUMBER;
BEGIN
    v_varsta := TRUNC(MONTHS_BETWEEN(SYSDATE, p_data_nastere) / 12);
    RETURN v_varsta;
END calc_varsta;
/

-- FOLOSIREA funcției în SQL:
SELECT Nume, Data_Nastere, calc_varsta(Data_Nastere) AS Varsta
FROM Angajati;

-- FOLOSIREA în PL/SQL:
DECLARE
    v_var NUMBER;
BEGIN
    v_var := calc_varsta(DATE '1990-05-15');
    DBMS_OUTPUT.PUT_LINE('Vârsta: ' || v_var);
END;
/
```

**Diferențe procedură vs funcție**:
| | Procedură | Funcție |
|---|---|---|
| Returnează | Nu returnează (direct) | Returnează o valoare |
| Folosire în SQL | Nu poate fi în SELECT | Poate fi în SELECT |
| Parametri OUT | Poate avea | Nu ar trebui să aibă |
| Scop | Acțiuni (INSERT, UPDATE, etc.) | Calcule, transformări |

---

## 3.8 Pachete (Packages)

Un **pachet** grupează proceduri, funcții, tipuri și variabile înrudite. Este ca o bibliotecă de funcții.

```sql
-- SPECIFICAȚIA (interfața publică):
CREATE OR REPLACE PACKAGE pkg_angajati AS
    -- Ce este vizibil din exterior:
    PROCEDURE adauga_angajat(p_nume VARCHAR2, p_salar NUMBER);
    FUNCTION get_salar(p_id NUMBER) RETURN NUMBER;
    g_max_angajati CONSTANT NUMBER := 1000;
END pkg_angajati;
/

-- CORPUL (implementarea):
CREATE OR REPLACE PACKAGE BODY pkg_angajati AS
    PROCEDURE adauga_angajat(p_nume VARCHAR2, p_salar NUMBER) AS
    BEGIN
        INSERT INTO Angajati (Nume, Salar) VALUES (p_nume, p_salar);
        COMMIT;
    END;

    FUNCTION get_salar(p_id NUMBER) RETURN NUMBER AS
        v_salar NUMBER;
    BEGIN
        SELECT Salar INTO v_salar FROM Angajati WHERE ID = p_id;
        RETURN v_salar;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN RETURN NULL;
    END;
END pkg_angajati;
/

-- APELAREA:
BEGIN
    pkg_angajati.adauga_angajat('Maria Popa', 5000);
    DBMS_OUTPUT.PUT_LINE(pkg_angajati.get_salar(1));
END;
/
```

---

## 3.9 Triggere

Un **trigger** este un bloc PL/SQL care se execută **automat** când are loc o anumită operație (INSERT, UPDATE, DELETE) pe un tabel.

Analogie: Un trigger este ca un senzor de mișcare care aprinde automat lumina când intri într-o cameră. Nu trebuie să faci nimic special — acțiunea declanșează automat altă acțiune.

```sql
-- Trigger care înregistrează automat modificările de salar:
CREATE OR REPLACE TRIGGER trg_audit_salar
BEFORE UPDATE OF Salar ON Angajati
FOR EACH ROW
BEGIN
    IF :OLD.Salar <> :NEW.Salar THEN
        INSERT INTO Audit_Salarii (ID_Angajat, Salar_Vechi, Salar_Nou, Data_Modif)
        VALUES (:OLD.ID, :OLD.Salar, :NEW.Salar, SYSDATE);
    END IF;
END;
/
```

- `:OLD.Salar` = valoarea salariului ÎNAINTE de UPDATE
- `:NEW.Salar` = valoarea salariului DUPĂ UPDATE
- `FOR EACH ROW` = se execută pentru fiecare rând afectat (row-level trigger)
- Fără `FOR EACH ROW` = se execută o singură dată per instrucțiune (statement-level trigger)

---

# 4. PROGRAMAREA ÎN C

## Ce este limbajul C?

**C** este un limbaj de programare creat în 1972 de Dennis Ritchie. Este limbajul "mamă" al majorității limbajelor moderne (C++, Java, C#, Python au toate rădăcini în C).

Analogie: C este ca un cuțit elvețian pentru programare — simplu, puternic, fără extras. Nu are obiecte, nu are multă magie — ești aproape de "metal" (hardware). Controlezi tu direct memoria, tu gestionezi resursele.

---

## 4.1 Structura unui program C

```c
#include <stdio.h>      // Bibliotecă pentru input/output (printf, scanf)
#include <string.h>     // Bibliotecă pentru funcții pe șiruri (strlen, strcpy, etc.)
#include <stdlib.h>     // Bibliotecă pentru funcții generale (malloc, free, atoi, etc.)
#include <math.h>       // Bibliotecă matematică (sqrt, pow, etc.)

// Funcția main = punctul de start al oricărui program C
int main() {
    // Codul tău
    printf("Hello, World!\n");
    return 0;   // 0 = programul s-a terminat cu succes
}
```

`#include` = include o bibliotecă. Fișierele `.h` (header files) conțin declarațiile funcțiilor.

---

## 4.2 Tipuri de date în C

```c
// Tipuri întregi:
char    c = 'A';        // 1 byte, -128 la 127 (sau un caracter ASCII)
short   s = 1000;       // 2 bytes, -32768 la 32767
int     i = 100000;     // 4 bytes, cca -2 miliarde la +2 miliarde
long    l = 1000000L;   // 4 sau 8 bytes (depinde de sistem)
long long ll = 1LL;     // 8 bytes

// Tipuri reale (cu virgulă):
float   f = 3.14f;      // 4 bytes, ~7 cifre semnificative
double  d = 3.14159265; // 8 bytes, ~15 cifre semnificative

// Fără semn (numai pozitive):
unsigned int ui = 4000000000U;  // 0 la ~4 miliarde
unsigned char uc = 255;          // 0 la 255

// Tip boolean (nu există nativ în C89, dar în C99+):
#include <stdbool.h>
bool activ = true;
```

**Dimensiunile tipurilor** pot varia pe sisteme diferite! Folosiți `sizeof()` pentru a afla:
```c
printf("int = %zu bytes\n", sizeof(int));     // de obicei 4
printf("double = %zu bytes\n", sizeof(double)); // de obicei 8
```

---

## 4.3 Operatori

```c
// Aritmetici:
int a = 10, b = 3;
int suma = a + b;     // 13
int dif  = a - b;     // 7
int prod = a * b;     // 30
int cat  = a / b;     // 3 (împărțire întreagă! 10/3 = 3, nu 3.33)
int rest = a % b;     // 1 (10 = 3*3 + 1)

// ATENȚIE la împărțirea întreagă:
double rezultat = (double)a / b;  // 3.333... (cast la double)

// Incrementare/decrementare:
int x = 5;
x++;    // x devine 6 (post-increment: folosește valoarea, apoi incrementează)
++x;    // x devine 7 (pre-increment: incrementează, apoi folosește valoarea)
x--;    // x devine 6
--x;    // x devine 5

// Diferența importantă:
int y = x++;  // y = 5, x = 6 (y primește valoarea ÎNAINTE de increment)
int z = ++x;  // z = 7, x = 7 (z primește valoarea DUPĂ increment)

// Atribuire compusă:
x += 5;   // x = x + 5
x -= 3;   // x = x - 3
x *= 2;   // x = x * 2
x /= 4;   // x = x / 4
x %= 3;   // x = x % 3

// Relaționale (returnează 0 sau 1):
int e = (a == b);   // 0 (fals) - a egal cu b?
int f2 = (a != b);  // 1 (adevărat) - a diferit de b?
int g = (a > b);    // 1 (adevărat)
int h = (a <= b);   // 0 (fals)

// Logici:
int p = 1, q = 0;
int r1 = p && q;    // 0 (ȘI logic: ambii trebuie să fie true)
int r2 = p || q;    // 1 (SAU logic: cel puțin unul trebuie să fie true)
int r3 = !p;        // 0 (negare: inversează true/false)

// Pe biți:
int b1 = 5 & 3;    // 1  (AND pe biți: 101 & 011 = 001)
int b2 = 5 | 3;    // 7  (OR pe biți:  101 | 011 = 111)
int b3 = 5 ^ 3;    // 6  (XOR pe biți: 101 ^ 011 = 110)
int b4 = ~5;        // -6 (NOT pe biți: inversează toți biții)
int b5 = 5 << 1;   // 10 (shift stânga: 101 → 1010 = înmulțire cu 2)
int b6 = 5 >> 1;   // 2  (shift dreapta: 101 → 10 = împărțire la 2)

// Condițional (ternar):
int max = (a > b) ? a : b;  // dacă a > b, max = a, altfel max = b
```

---

## 4.4 Instrucțiuni de control

### If-else

```c
int nota = 7;

if (nota >= 9) {
    printf("Excelent\n");
} else if (nota >= 7) {
    printf("Bine\n");
} else if (nota >= 5) {
    printf("Satisfacator\n");
} else {
    printf("Respins\n");
}
```

### Switch

```c
int zi = 3;
switch (zi) {
    case 1: printf("Luni\n"); break;
    case 2: printf("Marti\n"); break;
    case 3: printf("Miercuri\n"); break;
    case 4: printf("Joi\n"); break;
    case 5: printf("Vineri\n"); break;
    default: printf("Weekend\n"); break;
}
// ATENȚIE: fără break, execuția "cade" în case-urile următoare (fall-through)!
```

### Bucle

```c
// For loop:
for (int i = 0; i < 5; i++) {
    printf("i = %d\n", i);  // 0, 1, 2, 3, 4
}

// While loop:
int n = 10;
while (n > 0) {
    printf("%d ", n);
    n -= 2;  // 10, 8, 6, 4, 2
}

// Do-while (execută cel puțin o dată):
int x = 0;
do {
    printf("x = %d\n", x);
    x++;
} while (x < 3);  // 0, 1, 2

// break și continue:
for (int i = 0; i < 10; i++) {
    if (i == 7) break;     // iese din buclă când i = 7
    if (i % 2 == 0) continue;  // sare la iterația următoare dacă i e par
    printf("%d ", i);      // afișează: 1 3 5
}
```

---

## 4.5 Funcții în C

```c
#include <stdio.h>

// DECLARAȚIA (prototipul) funcției — spune compilatorului că funcția există:
int suma(int a, int b);   // declarație

// Funcția care calculează maximul:
int maxim(int a, int b) {
    return (a > b) ? a : b;
}

// Funcție fără valoare returnată:
void afiseaza_salut(char *nume) {
    printf("Buna ziua, %s!\n", nume);
}

// DEFINIȚIA funcției suma:
int suma(int a, int b) {
    return a + b;
}

int main() {
    int x = 5, y = 8;
    printf("Suma: %d\n", suma(x, y));      // 13
    printf("Maxim: %d\n", maxim(x, y));    // 8
    afiseaza_salut("Ion");                   // Buna ziua, Ion!
    return 0;
}
```

**Transmiterea prin valoare vs prin referință**:
```c
// Prin valoare: funcția primește O COPIE a argumentului
// Modificările din funcție NU afectează variabila originală
void dublu_gresit(int n) {
    n = n * 2;  // modifică doar copia locală
}

// Prin referință (cu pointeri): funcția primește ADRESA argumentului
// Modificările afectează variabila originală
void dublu_corect(int *n) {
    *n = *n * 2;  // modifică valoarea de la adresa n
}

int main() {
    int x = 5;
    dublu_gresit(x);       // x rămâne 5
    dublu_corect(&x);      // x devine 10 (& = adresa lui x)
    printf("%d\n", x);     // 10
    return 0;
}
```

---

## 4.6 Array-uri (Tablouri/Vectori)

Un **array** este o colecție de elemente de același tip, stocate consecutiv în memorie.

Analogie: Un array este ca un bloc de cutii poștale — 10 cutii, numerotate de la 0 la 9, și fiecare cutie conține câte ceva.

```c
// Declarare și inițializare:
int note[5] = {8, 9, 7, 10, 6};   // array de 5 întregi
double x[3] = {1.5, 2.5, 3.5};
char vocale[5] = {'a', 'e', 'i', 'o', 'u'};

// Indexarea: ÎNCEPE DE LA 0!
printf("%d\n", note[0]);  // 8 (primul element)
printf("%d\n", note[4]);  // 6 (ultimul element)
note[2] = 8;              // modifică al treilea element (era 7, devine 8)

// Parcurgerea unui array:
int n = 5;
int suma = 0;
for (int i = 0; i < n; i++) {
    suma += note[i];
}
printf("Suma: %d\n", suma);  // 40

// Array declarat fără dimensiune (se calculează automat):
int primes[] = {2, 3, 5, 7, 11};  // dimensiunea = 5

// Array bidimensional (matrice):
int matrice[3][4];  // 3 linii, 4 coloane

// Inițializare matrice:
int mat[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

// Parcurgere matrice:
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        printf("%d ", mat[i][j]);
    }
    printf("\n");
}
// Output:
// 1 2 3
// 4 5 6
```

---

## 4.7 Pointeri — Conceptul cel mai important (și cel mai greu!)

### Ce este un pointer?

Un **pointer** este o variabilă care conține **adresa de memorie** a altei variabile.

Analogia PERFECTĂ: Imaginează-ți că memoria calculatorului este un bloc de apartamente, cu apartamente numerotate de la 0 la milioane. O variabilă obișnuită (`int x = 5`) este **apartamentul 4521** care conține valoarea **5**. Un pointer (`int *p = &x`) este o **bucată de hârtie pe care scrie "4521"** — adică adresa apartamentului, nu conținutul lui.

```c
int x = 5;         // x stochează valoarea 5, să zicem la adresa 4521
int *p = &x;       // p este un pointer = stochează ADRESA lui x = 4521
                   // & = operatorul "adresa lui"
                   // * în declarație = "aceasta este un pointer"

printf("Valoarea lui x: %d\n", x);    // 5
printf("Adresa lui x: %p\n", &x);     // 4521 (adresa în memorie, în hex)
printf("Valoarea lui p (adresa): %p\n", p);   // 4521 (adresa stocată în p)
printf("Valoarea de la adresa p: %d\n", *p);  // 5 (dereferențiere: valoarea de la adresa)
// * înainte de pointer = "dă-mi valoarea de la acea adresă"

*p = 10;           // modificăm valoarea de la adresa p (= modificăm x)
printf("x acum: %d\n", x);  // 10 — x s-a schimbat!
```

**Operatorii pentru pointeri**:
- `&x` = adresa lui x (Address-of operator)
- `*p` = valoarea de la adresa p (Dereference operator)

### Pointeri și arrays

Array-urile și pointerii sunt strâns legate în C:

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;   // p pointează la primul element (arr == &arr[0])

// Accesarea elementelor:
printf("%d\n", arr[2]);  // 30
printf("%d\n", *(p+2));  // 30 — echivalent! (pointer arithmetic)
printf("%d\n", p[2]);    // 30 — și asta funcționează!

// Iterare cu pointer:
for (int i = 0; i < 5; i++) {
    printf("%d ", *(p + i));  // 10 20 30 40 50
}

// Sau:
for (int *q = arr; q < arr + 5; q++) {
    printf("%d ", *q);  // 10 20 30 40 50
}
```

### Pointeri la funcții

```c
// Declari un pointer la o funcție care primește 2 int și returnează int:
int (*ptr_func)(int, int);

int adunare(int a, int b) { return a + b; }
int inmultire(int a, int b) { return a * b; }

int main() {
    ptr_func = adunare;
    printf("%d\n", ptr_func(3, 4));   // 7

    ptr_func = inmultire;
    printf("%d\n", ptr_func(3, 4));   // 12
    return 0;
}
```

### Alocarea dinamică a memoriei

```c
#include <stdlib.h>

// malloc: alocă n bytes și returnează un pointer la zona alocată (neinițializată)
int *arr = (int *)malloc(5 * sizeof(int));  // 5 întregi

// calloc: alocă și inițializează cu 0
int *arr2 = (int *)calloc(5, sizeof(int));  // 5 întregi, toți = 0

// realloc: redimensionează zona alocată
arr = (int *)realloc(arr, 10 * sizeof(int));  // acum 10 întregi

// Verificarea alocării:
if (arr == NULL) {
    printf("Eroare: nu s-a putut aloca memorie!\n");
    return 1;
}

// Folosire:
for (int i = 0; i < 5; i++) {
    arr[i] = i * 10;
}

// OBLIGATORIU: eliberarea memoriei după folosire
free(arr);
arr = NULL;  // bună practică: pointează la NULL după free
```

---

## 4.8 Șiruri de caractere în C

În C, **șirurile de caractere** sunt arrays de char terminate cu `'\0'` (caracterul null = zero ASCII).

Analogie: Un șir "Hello" în C este stocat ca: `['H', 'e', 'l', 'l', 'o', '\0']` — șase elemente, nu cinci! Ultimul caracter `\0` marchează sfârșitul șirului.

```c
#include <string.h>

// Declarare și inițializare:
char salut[] = "Hello";           // compilatorul adaugă automat '\0'
char mesaj[50] = "Buna ziua";     // 50 bytes, dar mesajul e scurt
char *s = "Constanta";            // pointer la string constant (nu modificabil!)

// Afișare:
printf("%s\n", salut);  // Hello

// Citire:
char nume[50];
scanf("%49s", nume);        // citește un cuvânt (fără spații), max 49 chars
fgets(nume, 50, stdin);     // citește o linie (cu spații), mai sigur

// Funcții din <string.h>:
char s1[50] = "Hello";
char s2[] = " World";

strlen(s1)          // 5 — lungimea (fără '\0')
strcat(s1, s2)      // s1 devine "Hello World" (concatenare — ATENȚIE la buffer!)
strncat(s1, s2, 3)  // concatenare maxim 3 caractere — mai sigur
strcpy(s1, "Bye")   // s1 devine "Bye" (copiere)
strncpy(s1, "Bye", 3)  // copiere sigură
strcmp(s1, s2)      // compară: returnează 0 dacă egale, <0 sau >0 altfel
strchr(s1, 'l')     // pointer la prima apariție a 'l' în s1
strstr(s1, "ll")    // pointer la prima apariție a "ll" în s1
strcasecmp(s1, s2)  // comparare fără distincție majuscule/minuscule (Unix)
atoi("123")         // convertește "123" în int 123
atof("3.14")        // convertește "3.14" în double 3.14
sprintf(buf, "Valoare: %d", n)  // formatare în string
```

---

## 4.9 Structuri (struct)

**Struct** = un tip de date compus, care grupează mai multe câmpuri de tipuri diferite.

Analogie: Un struct este ca o fișă de angajat — conține mai multe informații (nume, vârstă, salar, departament) despre un singur lucru (angajatul).

```c
#include <stdio.h>
#include <string.h>

// Definirea tipului struct:
typedef struct {
    int     id;
    char    nume[50];
    char    prenume[50];
    double  salar;
    int     varsta;
} Angajat;

// Sau cu tag (fără typedef):
struct Punct {
    double x;
    double y;
};

int main() {
    // Declarare și inițializare:
    Angajat ang1 = {1, "Popescu", "Ion", 5000.0, 35};
    Angajat ang2;

    // Accesare câmpuri cu operatorul '.':
    ang2.id = 2;
    strcpy(ang2.nume, "Ionescu");
    strcpy(ang2.prenume, "Ana");
    ang2.salar = 6000.0;
    ang2.varsta = 28;

    printf("Angajat: %s %s, Salar: %.2f\n",
           ang1.prenume, ang1.nume, ang1.salar);

    // Array de structuri:
    Angajat echipa[3] = {
        {1, "Pop", "Dan", 4500.0, 30},
        {2, "Stan", "Ioana", 5500.0, 25},
        {3, "Matei", "Radu", 6000.0, 40}
    };

    for (int i = 0; i < 3; i++) {
        printf("%d: %s %s\n", echipa[i].id, echipa[i].prenume, echipa[i].nume);
    }

    // Pointer la struct — operator '->':
    Angajat *ptr = &ang1;
    printf("Prin pointer: %s, salar %.2f\n", ptr->nume, ptr->salar);
    // ptr->salar echivalent cu (*ptr).salar

    return 0;
}
```

---

## 4.10 Fișiere în C

```c
#include <stdio.h>

int main() {
    FILE *fis;
    char linie[200];
    int n;

    // Deschidere pentru scriere (creează fișierul dacă nu există):
    fis = fopen("date.txt", "w");
    if (fis == NULL) {
        printf("Eroare la deschiderea fișierului!\n");
        return 1;
    }

    // Scrierea în fișier:
    fprintf(fis, "Angajat: Ion Popescu\n");
    fprintf(fis, "Salar: %d\n", 5000);
    fputs("Alta linie\n", fis);

    fclose(fis);  // OBLIGATORIU: închide fișierul

    // Deschidere pentru citire:
    fis = fopen("date.txt", "r");
    if (fis == NULL) { return 1; }

    while (fgets(linie, sizeof(linie), fis) != NULL) {
        printf("%s", linie);  // afișează fiecare linie
    }
    fclose(fis);

    // Moduri de deschidere:
    // "r"  = citire (fișierul trebuie să existe)
    // "w"  = scriere (creează sau șterge conținut existent)
    // "a"  = append (adaugă la final, nu șterge conținut)
    // "rb" = citire binar
    // "wb" = scriere binar
    // "r+" = citire și scriere

    return 0;
}
```

---

# 5. PROGRAMARE ORIENTATĂ OBIECT ÎN C++

## Ce este programarea orientată obiect (OOP)?

**OOP** = o paradigmă de programare care organizează codul în jurul **obiectelor** — entități care combină date (atribute) și comportament (metode/funcții).

Analogie SUPREMĂ: Gândește-te la o mașină reală.
- **Clasa** = planul/blueprintul mașinii (specificațiile tehnice)
- **Obiectul** = mașina concretă construită după acel plan
- **Atributele** = caracteristicile mașinii (culoare, marcă, viteza curentă, nivelul benzinei)
- **Metodele** = ce poate face mașina (accelerează, frânează, pornește, oprește)
- **Encapsularea** = capacul motorului — nu știi cum funcționează motorul, îl pornești și gata
- **Moștenirea** = o mașină electrică este tot o mașină, dar cu motor electric în plus
- **Polimorfismul** = orice mașină poate frâna, dar un camion frânează diferit față de un smart

---

## 5.1 Clase și obiecte

```cpp
#include <iostream>
#include <string>
using namespace std;

class Masina {
private:   // Accesibil DOAR din interiorul clasei
    string marca;
    string culoare;
    int viteza_curenta;
    double nivel_benzina;

public:    // Accesibil din orice parte a programului
    // Constructor (se execută la crearea unui obiect):
    Masina(string m, string c) {
        marca = m;
        culoare = c;
        viteza_curenta = 0;
        nivel_benzina = 100.0;
    }

    // Constructor cu listă de inițializare (stil modern):
    // Masina(string m, string c) : marca(m), culoare(c), viteza_curenta(0), nivel_benzina(100.0) {}

    // Destructor (se execută la distrugerea obiectului):
    ~Masina() {
        cout << "Masina " << marca << " a fost demolata." << endl;
    }

    // Metode (funcții membre):
    void accelereaza(int km_h) {
        viteza_curenta += km_h;
        nivel_benzina -= km_h * 0.1;
        cout << marca << " accelereaza la " << viteza_curenta << " km/h" << endl;
    }

    void franeaza(int km_h) {
        viteza_curenta = max(0, viteza_curenta - km_h);
        cout << marca << " reduce viteza la " << viteza_curenta << " km/h" << endl;
    }

    // Getter: returnează o valoare privată (read-only)
    string getMarca() const { return marca; }
    int getViteza() const { return viteza_curenta; }
    double getBenzina() const { return nivel_benzina; }

    // Setter: modifică o valoare privată (cu validare)
    void setCuloare(string c) {
        if (!c.empty()) culoare = c;
    }

    // Metodă const = nu modifică obiectul
    void afiseaza() const {
        cout << "Masina: " << marca << " (" << culoare << ")"
             << " | Viteza: " << viteza_curenta << " km/h"
             << " | Benzina: " << nivel_benzina << "%" << endl;
    }
};

int main() {
    // Crearea obiectelor (pe stivă):
    Masina m1("BMW", "Albastru");
    Masina m2("Toyota", "Rosu");

    m1.accelereaza(50);   // BMW accelereaza la 50 km/h
    m1.accelereaza(30);   // BMW accelereaza la 80 km/h
    m1.franeaza(20);      // BMW reduce viteza la 60 km/h
    m1.afiseaza();

    // Creare dinamică (pe heap, cu new):
    Masina *m3 = new Masina("Mercedes", "Negru");
    m3->accelereaza(100);  // pointer -> metoda
    delete m3;             // OBLIGATORIU: eliberează memoria

    return 0;
    // m1 și m2 sunt distruse automat la ieșirea din main (destructor apelat)
}
```

---

## 5.2 Encapsularea

**Encapsularea** = ascunderea detaliilor interne ale clasei și expunerea doar a unei interfețe publice.

De ce contează? Poți schimba implementarea internă fără să afectezi codul care folosește clasa. Dacă mâine vrei să stochezi viteza diferit, nimeni din afara clasei nu trebuie să știe.

```cpp
class ContBancar {
private:
    double sold;      // NIMENI din afară nu poate accesa direct sold
    string iban;
    vector<string> tranzactii;

public:
    ContBancar(string iban_init, double sold_initial)
        : iban(iban_init), sold(sold_initial) {}

    bool depune(double suma) {
        if (suma <= 0) return false;
        sold += suma;
        tranzactii.push_back("Depus: " + to_string(suma));
        return true;
    }

    bool retrage(double suma) {
        if (suma <= 0 || suma > sold) return false;  // validare!
        sold -= suma;
        tranzactii.push_back("Retras: " + to_string(suma));
        return true;
    }

    double getSold() const { return sold; }  // read-only access

    void afiseazaExtras() const {
        cout << "IBAN: " << iban << " | Sold: " << sold << " RON" << endl;
        for (const auto &t : tranzactii)
            cout << "  " << t << endl;
    }
};
```

---

## 5.3 Constructori și destructori

```cpp
class Student {
private:
    string nume;
    int *note;   // pointer la array alocat dinamic
    int n_note;

public:
    // Constructor implicit (fără parametri):
    Student() : nume("Necunoscut"), note(nullptr), n_note(0) {
        cout << "Constructor implicit" << endl;
    }

    // Constructor cu parametri:
    Student(string n, int nr_note) : nume(n), n_note(nr_note) {
        note = new int[nr_note]();  // alocare dinamică + inițializare cu 0
        cout << "Constructor pentru " << nume << endl;
    }

    // Constructor de copiere (deep copy):
    Student(const Student &alt) : nume(alt.nume), n_note(alt.n_note) {
        note = new int[n_note];
        for (int i = 0; i < n_note; i++)
            note[i] = alt.note[i];  // copiază VALORILE, nu pointerul!
        cout << "Constructor de copiere pentru " << nume << endl;
    }

    // Operator de atribuire (deep copy):
    Student& operator=(const Student &alt) {
        if (this == &alt) return *this;  // auto-atribuire
        delete[] note;                   // eliberează memoria veche
        nume = alt.nume;
        n_note = alt.n_note;
        note = new int[n_note];
        for (int i = 0; i < n_note; i++)
            note[i] = alt.note[i];
        return *this;
    }

    // Destructor:
    ~Student() {
        delete[] note;  // OBLIGATORIU: eliberează memoria alocată cu new[]
        cout << "Destructor pentru " << nume << endl;
    }

    void setNota(int index, int nota) {
        if (index >= 0 && index < n_note)
            note[index] = nota;
    }

    double calcMedie() const {
        if (n_note == 0) return 0;
        double suma = 0;
        for (int i = 0; i < n_note; i++) suma += note[i];
        return suma / n_note;
    }

    void afiseaza() const {
        cout << "Student: " << nume << " | Medie: " << calcMedie() << endl;
    }
};
```

**Regula celor trei (Rule of Three)**: Dacă definești oricare din: destructor, constructor de copiere, operator de atribuire — atunci trebuie să le definești pe TOATE TREI.

---

## 5.4 Moștenirea

**Moștenirea** = o clasă poate prelua automat atributele și metodele altei clase, extinzând-o.

Analogie: Clasa `Vehicul` definește ce e comun tuturor vehiculelor. Clasa `Masina` moștenește `Vehicul` și adaugă ce e specific mașinilor. Clasa `MasinaElectrica` moștenește `Masina` și adaugă ce e specific mașinilor electrice.

```cpp
// CLASA DE BAZĂ (superclasă, clasă părinte):
class Animal {
protected:   // accesibil în clase derivate (dar nu din afară)
    string nume;
    int varsta;

public:
    Animal(string n, int v) : nume(n), varsta(v) {}

    void mananca() {
        cout << nume << " mananca." << endl;
    }

    void doarme() {
        cout << nume << " doarme." << endl;
    }

    // virtual = poate fi suprascrisă de clase derivate
    virtual void sunet() {
        cout << "Sunet generic de animal." << endl;
    }

    virtual void afiseaza() const {
        cout << "Animal: " << nume << ", varsta " << varsta << endl;
    }

    virtual ~Animal() {}  // destructor virtual = OBLIGATORIU când ai metode virtuale
};

// CLASA DERIVATĂ (subclasă, clasă copil):
class Caine : public Animal {
private:
    string rasa;

public:
    Caine(string n, int v, string r) : Animal(n, v), rasa(r) {}
    // Animal(n, v) apelează constructorul clasei de bază

    // Suprascrierea (override) metodei virtuale:
    void sunet() override {
        cout << nume << " (caine " << rasa << ") latrat: Hau hau!" << endl;
    }

    void afiseaza() const override {
        Animal::afiseaza();  // apelează metoda din clasa de bază
        cout << "Rasa: " << rasa << endl;
    }

    void aduce_mingea() {
        cout << nume << " aduce mingea!" << endl;
    }
};

class Pisica : public Animal {
private:
    bool e_domestica;
public:
    Pisica(string n, int v, bool dom) : Animal(n, v), e_domestica(dom) {}

    void sunet() override {
        cout << nume << " (pisica) miauna: Miau!" << endl;
    }
};
```

**Tipuri de moștenire**:
- `public`: public din bază rămâne public în derivat ✓ (cel mai comun)
- `protected`: public din bază devine protected în derivat
- `private`: public și protected din bază devin private în derivat

---

## 5.5 Polimorfismul

**Polimorfismul** = același cod poate lucra cu obiecte de tipuri diferite, comportamentul variind în funcție de tipul real al obiectului.

Analogie: Ai o funcție `fa_sunet(Animal *a)`. O poți apela cu un câine, cu o pisică, cu o vacă — fiecare va face sunetul lui specific, chiar dacă tu apelezi aceeași funcție cu parametrul generic `Animal`.

```cpp
int main() {
    // Polimorfism prin pointeri la clasa de bază:
    Animal *animale[3];
    animale[0] = new Caine("Rex", 3, "Labrador");
    animale[1] = new Pisica("Whiskers", 5, true);
    animale[2] = new Caine("Buddy", 2, "Poodle");

    // Fiecare obiect răspunde DIFERIT la același apel:
    for (int i = 0; i < 3; i++) {
        animale[i]->sunet();    // apelează suprascrierea specifică fiecărui tip!
        animale[i]->afiseaza();
        cout << endl;
    }

    // Output:
    // Rex (caine Labrador) latrat: Hau hau!
    // Animal: Rex, varsta 3 | Rasa: Labrador
    // Whiskers (pisica) miauna: Miau!
    // ...

    // Polimorfism prin referință:
    Caine cainele("Fido", 4, "Beagle");
    Animal &ref = cainele;
    ref.sunet();  // Hau hau! (nu "Sunet generic") — polimorfism în acțiune

    // Eliberare memorie:
    for (int i = 0; i < 3; i++) delete animale[i];

    return 0;
}
```

**De ce avem nevoie de `virtual`?**

Fără `virtual`, C++ face **legare statică** (la compilare) — decide la compilare ce funcție să apeleze, în funcție de tipul pointerului (Animal*), nu al obiectului real (Caine).

Cu `virtual`, C++ face **legare dinamică** (la execuție) — verifică la runtime tipul real al obiectului și apelează funcția corectă. Aceasta este esența polimorfismului.

---

## 5.6 Clase abstracte și interfețe

O **clasă abstractă** are cel puțin o **funcție virtuală pură** (declarată cu `= 0`). Nu poți crea obiecte direct din ea.

```cpp
class Forma {
public:
    // Funcție virtuală pură = TREBUIE implementată de clasele derivate:
    virtual double arie() const = 0;
    virtual double perimetru() const = 0;
    virtual void afiseaza() const = 0;

    // Poate avea și implementare pentru funcții ne-pure:
    void descriere() const {
        cout << "Aceasta este o forma geometrica." << endl;
        cout << "Arie: " << arie() << endl;
        cout << "Perimetru: " << perimetru() << endl;
    }

    virtual ~Forma() {}
};

class Cerc : public Forma {
private:
    double raza;
    const double PI = 3.14159265;
public:
    Cerc(double r) : raza(r) {}

    double arie() const override { return PI * raza * raza; }
    double perimetru() const override { return 2 * PI * raza; }
    void afiseaza() const override {
        cout << "Cerc cu raza " << raza << endl;
    }
};

class Dreptunghi : public Forma {
private:
    double latime, inaltime;
public:
    Dreptunghi(double l, double h) : latime(l), inaltime(h) {}

    double arie() const override { return latime * inaltime; }
    double perimetru() const override { return 2 * (latime + inaltime); }
    void afiseaza() const override {
        cout << "Dreptunghi " << latime << " x " << inaltime << endl;
    }
};

int main() {
    // Forma f;  // EROARE! Nu poți instanția o clasă abstractă

    Forma *forme[3];
    forme[0] = new Cerc(5.0);
    forme[1] = new Dreptunghi(4.0, 6.0);
    forme[2] = new Cerc(3.0);

    for (int i = 0; i < 3; i++) {
        forme[i]->afiseaza();
        forme[i]->descriere();
        cout << endl;
        delete forme[i];
    }

    return 0;
}
```

---

## 5.7 Suprascrierea operatorilor (Operator Overloading)

C++ permite redefinirea operatorilor (+, -, *, ==, <<, etc.) pentru clasele proprii.

```cpp
class Fractie {
private:
    int numarator, numitor;

    int cmmdc(int a, int b) {
        while (b) { int t = b; b = a % b; a = t; }
        return a;
    }

    void simplifica() {
        int d = cmmdc(abs(numarator), abs(numitor));
        numarator /= d;
        numitor /= d;
        if (numitor < 0) { numarator = -numarator; numitor = -numitor; }
    }

public:
    Fractie(int n = 0, int d = 1) : numarator(n), numitor(d) {
        simplifica();
    }

    // Suprascriere operator +:
    Fractie operator+(const Fractie &alt) const {
        return Fractie(
            numarator * alt.numitor + alt.numarator * numitor,
            numitor * alt.numitor
        );
    }

    // Suprascriere operator *:
    Fractie operator*(const Fractie &alt) const {
        return Fractie(numarator * alt.numarator, numitor * alt.numitor);
    }

    // Suprascriere operator ==:
    bool operator==(const Fractie &alt) const {
        return numarator == alt.numarator && numitor == alt.numitor;
    }

    // Suprascriere operator << (pentru cout):
    friend ostream& operator<<(ostream &out, const Fractie &f) {
        out << f.numarator << "/" << f.numitor;
        return out;
    }
};

int main() {
    Fractie f1(1, 2);  // 1/2
    Fractie f2(1, 3);  // 1/3

    Fractie suma = f1 + f2;   // 1/2 + 1/3 = 5/6
    Fractie prod = f1 * f2;   // 1/2 * 1/3 = 1/6

    cout << f1 << " + " << f2 << " = " << suma << endl;  // 1/2 + 1/3 = 5/6
    cout << f1 << " * " << f2 << " = " << prod << endl;  // 1/2 * 1/3 = 1/6

    return 0;
}
```

---

## 5.8 Template-uri (Șabloane)

**Template-urile** permit scrierea de cod generic care funcționează cu orice tip de date.

```cpp
// Funcție template:
template <typename T>
T maxim(T a, T b) {
    return (a > b) ? a : b;
}

// Clasă template:
template <typename T>
class Stiva {
private:
    T *elemente;
    int varf;
    int capacitate;
public:
    Stiva(int cap = 10) : varf(-1), capacitate(cap) {
        elemente = new T[cap];
    }

    ~Stiva() { delete[] elemente; }

    void push(T elem) {
        if (varf < capacitate - 1)
            elemente[++varf] = elem;
    }

    T pop() {
        if (varf >= 0) return elemente[varf--];
        throw runtime_error("Stiva goala!");
    }

    bool goala() const { return varf == -1; }
    int dimensiune() const { return varf + 1; }
};

int main() {
    cout << maxim(5, 8) << endl;        // 8 (int)
    cout << maxim(3.14, 2.71) << endl;  // 3.14 (double)
    cout << maxim('a', 'z') << endl;    // z (char)

    Stiva<int> s_int;
    s_int.push(1); s_int.push(2); s_int.push(3);
    cout << s_int.pop() << endl;  // 3

    Stiva<string> s_str;
    s_str.push("hello"); s_str.push("world");
    cout << s_str.pop() << endl;  // world

    return 0;
}
```

---

## 5.9 STL (Standard Template Library)

STL este o colecție de structuri de date și algoritmi gata de folosit în C++.

```cpp
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    // VECTOR (array dinamic):
    vector<int> v = {5, 3, 8, 1, 9, 2};
    v.push_back(7);          // adaugă la final
    v.pop_back();            // șterge ultimul
    cout << v.size() << endl; // dimensiunea
    cout << v[0] << endl;    // accesare prin index

    sort(v.begin(), v.end());  // sortare crescătoare
    // v = {1, 2, 3, 5, 8, 9}

    // Parcurgere cu range-for:
    for (int x : v) cout << x << " ";
    cout << endl;

    // MAP (dicționar cheie-valoare):
    map<string, int> frecventa;
    frecventa["ana"] = 3;
    frecventa["ion"] = 7;
    frecventa["maria"]++;  // incrementează (sau creează cu 0 dacă nu există)

    for (auto &pereche : frecventa) {
        cout << pereche.first << ": " << pereche.second << endl;
    }

    // SET (mulțime fără duplicate, sortată):
    set<int> cifre = {5, 3, 8, 3, 1, 5, 9};  // duplicatele 3 și 5 sunt eliminate
    for (int x : cifre) cout << x << " ";
    // Output: 1 3 5 8 9

    // Algoritmi STL:
    auto it = find(v.begin(), v.end(), 5);  // caută valoarea 5
    if (it != v.end())
        cout << "Gasit la pozitia: " << (it - v.begin()) << endl;

    int cnt = count(v.begin(), v.end(), 3);  // câte de 3 sunt

    reverse(v.begin(), v.end());  // inversează vectorul

    return 0;
}
```

---

## 5.10 Excepții în C++

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

double impartire(double a, double b) {
    if (b == 0) {
        throw runtime_error("Impartire la zero!");
        // throw invalid_argument("Numitorul nu poate fi 0");
    }
    return a / b;
}

int main() {
    try {
        cout << impartire(10, 2) << endl;   // 5.0
        cout << impartire(10, 0) << endl;   // aruncă excepție
        cout << "Aceasta linie nu se executa" << endl;
    }
    catch (const runtime_error &e) {
        cout << "Eroare runtime: " << e.what() << endl;
    }
    catch (const exception &e) {
        cout << "Exceptie: " << e.what() << endl;
    }
    catch (...) {
        cout << "Exceptie necunoscuta!" << endl;
    }

    cout << "Programul continua..." << endl;
    return 0;
}
```

---

## 5.11 Fluxuri I/O (Input/Output Streams)

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
using namespace std;

int main() {
    // Formatare output cu iomanip:
    double pi = 3.14159265;
    cout << fixed << setprecision(2) << pi << endl;  // 3.14
    cout << setw(10) << "Hello" << endl;              // "     Hello" (aliniere dreapta)
    cout << left << setw(10) << "Hello" << endl;      // "Hello     " (aliniere stânga)
    cout << hex << 255 << endl;                        // ff (hexazecimal)
    cout << oct << 8 << endl;                          // 10 (octal)
    cout << dec << 10 << endl;                         // 10 (revenire la zecimal)

    // Fișiere text:
    ofstream fout("output.txt");   // deschide pentru scriere
    fout << "Linia 1" << endl;
    fout << "Pi = " << fixed << setprecision(4) << pi << endl;
    fout.close();

    ifstream fin("output.txt");    // deschide pentru citire
    string linie;
    while (getline(fin, linie)) {
        cout << linie << endl;
    }
    fin.close();

    // String streams (buffer în memorie):
    ostringstream oss;
    oss << "Valoarea este " << 42 << " si pi este " << pi;
    string rezultat = oss.str();
    cout << rezultat << endl;

    istringstream iss("10 20 30");
    int a, b, c;
    iss >> a >> b >> c;  // parsează valorile
    cout << a + b + c << endl;  // 60

    return 0;
}
```

---

## 5.12 Funcții prietene (friend)

O **funcție prieten** (`friend`) poate accesa membrii privați ai clasei, deși nu este membră a clasei.

```cpp
class Cerc {
private:
    double raza;
    const double PI = 3.14159265;

public:
    Cerc(double r) : raza(r) {}

    // Declararea funcției/clasei prietene:
    friend double arie_cerc(const Cerc &c);
    friend ostream& operator<<(ostream &out, const Cerc &c);
    friend class InspectorGeometric;  // o clasă prieten
};

// Definiția funcției prietene (în afara clasei):
double arie_cerc(const Cerc &c) {
    return c.PI * c.raza * c.raza;  // accesează raza și PI private!
}

ostream& operator<<(ostream &out, const Cerc &c) {
    out << "Cerc(raza=" << c.raza << ", arie=" << c.PI * c.raza * c.raza << ")";
    return out;
}

class InspectorGeometric {
public:
    void analizeaza(const Cerc &c) {
        cout << "Inspecție: raza = " << c.raza << endl;  // accesează private!
    }
};
```

---

## Rezumat rapid pentru examen

| Concept | C | C++ |
|---------|---|-----|
| Pointer | `int *p = &x; *p = 5;` | Același |
| Array dinamic | `malloc/free` | `new/delete` |
| Struct | `typedef struct {...} Tip;` | `class` sau `struct` |
| Moștenire | Nu există | `class B : public A {}` |
| Virtual | Nu există | `virtual void f() = 0;` |
| Generic | Nu există | `template<typename T>` |

| SQL Concept | Exemplu |
|-------------|---------|
| Filtrare rânduri | `WHERE col > val` |
| Grupare | `GROUP BY col` |
| Filtrare grupuri | `HAVING COUNT(*) > 5` |
| Join | `JOIN t2 ON t1.id = t2.fk` |
| Subinterogare | `WHERE id IN (SELECT ...)` |
| Funcție agregat | `SUM, AVG, COUNT, MAX, MIN` |

| PL/SQL Concept | Exemplu |
|----------------|---------|
| Variabilă | `v_x NUMBER := 0;` |
| Atribuire din BD | `SELECT col INTO v FROM t WHERE ...;` |
| Cursor | `CURSOR c IS SELECT ...; OPEN c; FETCH c INTO v; CLOSE c;` |
| Excepție | `WHEN NO_DATA_FOUND THEN ...` |
| Procedură | `CREATE PROCEDURE p(p IN NUMBER) AS BEGIN ... END;` |
| Funcție | `CREATE FUNCTION f RETURN NUMBER AS BEGIN RETURN x; END;` |
