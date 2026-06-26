# 📚 REZUMAT TEORETIC — Examen Licență Informatică Economică (RO)
> Extras complet din paginile cerute în bibliografie. Toate cele 14 teme.

---

## CUPRINS
1. [Modele de date](#1-modele-de-date) — [1] pp. 49–65
2. [Sisteme de baze de date](#2-sisteme-de-baze-de-date) — [1] pp. 68–94
3. [Baze de date relaționale](#3-baze-de-date-rela%C8%9Bionale) — [1] pp. 103–203
4. [Programarea în SQL](#4-programarea-în-sql) — [2] pp. 101–178
5. [Programarea în PL/SQL](#5-programarea-în-plsql) — [5] pp. 9–118
6. [Tipuri fundamentale de date și clase de memorie în C](#6-tipuri-fundamentale-de-date-%C8%99i-clase-de-memorie-în-c) — [3] pp. 16–28
7. [Operatori și expresii în C](#7-operatori-%C8%99i-expresii-în-c) — [3] pp. 30–46
8. [Instrucțiuni de bază ale limbajului C](#8-instruc%C8%9Biuni-de-baz%C4%83-ale-limbajului-c) — [3] pp. 48–58
9. [Masive și pointeri în C](#9-masive-%C8%99i-pointeri-în-c) — [3] pp. 60–74
10. [Lucru cu șiruri de caractere în C](#10-lucru-cu-%C8%99iruri-de-caractere-în-c) — [3] pp. 76–88
11. [Funcții în C](#11-func%C8%9Bii-în-c) — [3] pp. 90–114
12. [Structuri și uniuni în C](#12-structuri-%C8%99i-uniuni-în-c) — [3] pp. 118–168
13. [Preprocesarea în C](#13-preprocesarea-în-c) — [3] pp. 170–177
14. [Programare orientată obiect (C++)](#14-programare-orientat%C4%83-obiect-c) — [4] pp. 11–133

---

# 1. MODELE DE DATE
**Sursă: [1] Lungu — Tratat de baze de date, pp. 49–65**

## 1.1 Definirea modelelor de date (pp. 49–50)

Un **model de date** reprezintă o abstractizare matematică a datelor și a operațiilor care pot fi efectuate asupra lor. Definirea unui model de date presupune identificarea a trei elemente fundamentale:
- **Structura de date** — modalitatea de stocare și organizare a datelor
- **Operatorii** — operațiile care acționează asupra structurii
- **Regulile de integritate** — asigurarea corectitudinii și coerenței datelor

Prin intermediul modelelor de date se realizează o reprezentare unificată a formatelor de date din diferite aplicații.

## 1.2 Structuri de date (pp. 50–61)

O **structură de date** este o modalitate de stocare a informațiilor într-un sistem informatic astfel încât să poată fi utilizate eficient. Ea este o colecție de date între care s-au stabilit relații ce conduc la un mecanism de selecție și identificare.

**Elementele de bază ale unei structuri:**
- **Câmp** — cel mai mic element al unei structuri care poate fi prelucrat
- **Grup simplu sau compus** — rezultat din gruparea câmpurilor
- **Înregistrare** — un ansamblu de câmpuri și grupuri

### Tipuri de asocieri (legături) între entități:
- **Unu la unu (1:1)** — unei instanțe din prima entitate îi corespunde o singură instanță din a doua
- **Unu la mulți (1:N)** — unei instanțe din prima entitate îi corespund mai multe instanțe din a doua
- **Mulți la mulți (M:N)** — fiecărei instanțe din prima entitate îi corespund mai multe din a doua și reciproc

### Clasificarea structurilor de date:
- **După modul de acces:** secvențial vs. direct
- **După tipul componentelor:** omogene vs. eterogene
- **După posibilitatea de modificare:** statice vs. dinamice
- **După nivelul de structurare:** logice vs. fizice

### Tipuri de structuri logice (după tipul legăturilor):

**Structura punctuală** — o entitate grup izolată, fără relații explicite între instanțe.

**Structura liniară** — există o relație de ordine totală. Proprietăți:
- cardinalul mulțimii elementelor inițiale = 1
- cardinalul mulțimii elementelor terminale = 1
- orice element neterminal are un succesor imediat unic
- relațiile sunt de tip 1:1

Variante: **simplă**, **inelară/circulară** (ultimul element se leagă de primul), **cu elemente arborescente/rețea**.

Principale structuri liniare: masive (vectori, matrice), stiva (LIFO), liste.

**Tipuri de liste:**
- **Simplu înlănțuite** — legătură cu nodul următor, parcurgere într-un singur sens
- **Dublu înlănțuite** — legătură cu nodul următor și precedent, parcurgere în ambele sensuri
- **Circulare** — legătură suplimentară între ultimul și primul nod

**Structura arborescentă** — colecție de date cu relație de ordine; graf aciclic cu structură ierarhică. Caracteristici:
- Element unic numit **rădăcină**
- Orice nod diferit de rădăcină are un predecesor imediat unic (**părinte**)
- Orice nod neterminal are succesori imediați (**copii**)
- Relațiile sunt de tip 1:N
- Arbore binar = arbore ordonat de gradul 2
- Un arbore este **echilibrat** dacă diferența dintre drumuri de la rădăcină la orice nod terminal este cel mult 1

**Structura rețea** — colecție de date cu relație de preordine. Caracteristici:
- Graf cu legături bidirecționale
- Un nod poate fi predecesor al propriului predecesor (cicluri)
- Cardinalul mulțimii nodurilor inițiale ≥ 1
- Relațiile sunt de tip M:N

**Structura relațională** — colecție de date organizate în tabele fără legătură fizică între ele. Componentele tabelei:
- Să nu existe date la nivel agregat (valorile să fie elementare)
- Liniile să fie distincte
- Să nu existe coloane repetitive
- Să fie în una din cele 5 forme normale (FN1–FN5)

## 1.3 Operatori asupra structurilor de date (pp. 61–62)

Operații frecvente:
- **Crearea** — memorarea inițială a datelor
- **Actualizarea** — adăugare, ștergere, modificare
- **Consultarea** — accesul la elemente pentru prelucrare
- **Sortarea** — aranjarea după criterii
- **Ventilarea** — descompunerea în structuri mai mici
- **Fuzionarea** — formarea unei noi structuri din mai multe

Structura relațională are operații specifice: **proiecție, selecție, joncțiune, intersecție, reuniune, închidere tranzitivă**.

## 1.4 Restricții de integritate (pp. 62–63)

**Restricțiile de integritate** (constrângeri/reguli de integritate) mențin datele corecte, consistente și coerente. Tipuri:
- **Restricții de comportament** — valori încadrate în limite, simboluri, lungimi
- **Restricții de unicitate** — nu există mai multe entități cu aceleași valori de identificare
- **Restricții de legătură logică** — asigură coerența datelor
- **Restricții de obligativitate** — unele câmpuri trebuie să aibă valori

## 1.5 Tipologia modelelor de date (pp. 62–65)

Conform ANSI/75, există 3 tipuri de modele:
- **Modele conceptuale** — descriu semantica domeniului; reprezentate prin schema conceptuală. Exemplu: Modelul Entitate-Asociere (Chen, 1976) și Modelul EAE extins
- **Modele logice** — descriu structura logică; reprezentate prin schema logică
- **Modele fizice** — descriu modul de stocare; reprezentate prin schema internă/fizică

**Schemele** conceptuală, logică și fizică au un anumit grad de **independență** — modificarea uneia nu o afectează neapărat pe cealaltă.

### Modele de date în funcție de structura definită:

**Modelul ierarhic** — primul model propus, structură arborescentă. Un nod rădăcină, noduri copii în forma de arbore. Legăturile sunt de tip 1:1 și 1:M. Limitare: relațiile fizice creează dependență față de implementare.

**Modelul rețea** — similar ierarhic, dar un nod poate avea mai mulți părinți. Introdus în 1969. Operații de actualizare pe tipurile înregistrărilor și pe legături.

**Modelul relațional** — bazat pe algebra relațională și calculul cu predicate. Singura structură: **relația (tabela)** = submulțime a produsului cartezian al unor domenii. Limbaj de interogare: **SQL** (declarativ). Permite manipularea la nivel de mulțime.

**Modelul orientat-obiect** — permite structuri complexe și ierarhii. Un obiect este o entitate cu stare, comportament și identitate. **Metodele** = implementarea operațiilor. **Clasa** = tipul abstract care definește comportamentul obiectelor.

---

# 2. SISTEME DE BAZE DE DATE
**Sursă: [1] Lungu — Tratat de baze de date, pp. 68–94**

## 2.1 Organizarea datelor în fișiere (pp. 68–80)

Un **fișier** este o colecție omogenă de date, cu două componente:
- **Partea de identificare** — etichetele BOF (Begin Of File) și EOF (End Of File)
- **Partea de date** — colecția omogenă: fișier → înregistrări → câmpuri → valori

### Moduri de organizare a fișierelor:

**Organizarea standard** — prezentă pe toate calculatoarele. Înregistrarea = șir de caractere pe o linie.

**Organizarea secvențială** — înregistrările dispuse fără ordine prestabilită; localizarea = parcurgere secvențială; actualizarea necesită recrearea fișierului.

**Organizarea relativă** — înregistrările numerotate; localizare secvențială sau directă prin număr de realizare.

**Organizarea indexată** — înregistrări în ordine strict crescătoare după o cheie; fișier de index atașat (valorile cheii + adresele fizice); localizare secvențială sau directă prin cheie.

**Organizarea parțională (hashing)** — împărțirea în blocuri prin algoritmul de dispersie (hash); acces direct.

**Organizarea multiindexată** — mai multe chei (principală + secundare).

**Organizarea inversă** — două fișiere: fișierul de bază (secvențial) + fișierul invers (structură de tip index); utilizat în arhive și biblioteci.

**Fișiere text** — codificare ASCII, organizare secvențială, înregistrări cu lungime variabilă.

**Fișiere XML** — standard internațional, auto-descriptibil, unitate fundamentală = documentul XML.

## 2.2 Conceptul de bază de date (pp. 77–80)

Conceptul a apărut în 1969 (CODASYL) ca: „una sau mai multe colecții de date aflate în interdependență, împreună cu un fișier de descriere globală a datelor și a legăturilor dintre ele".

O **bază de date** este un ansamblu de colecții de date aflate în interdependență, împreună cu **dicționarul de date** (care conține descrierea datelor și a legăturilor), asigurând independența datelor față de aplicații.

**Caracteristicile bazei de date:**
- Organizată pe trei niveluri: conceptual, logic, fizic
- Structurată conform unui model de date
- Coerentă prin restricțiile de integritate
- Cu redundanță minimă și controlată
- Accesibilă mai multor utilizatori

**Niveluri de organizare:**
- **Nivelul conceptual** — viziunea proiectantului/administratorului; independent de aplicații; rezultă **schema conceptuală**
- **Nivelul logic** — viziunea dezvoltatorului de aplicații; rezultă **schema logică** (parte din schema conceptuală)
- **Nivelul fizic** — viziunea inginerului de sistem; rezultă **schema internă/fizică** (definită în termeni de fișiere și înregistrări fizice)

## 2.3 Sistemul de gestiune a bazelor de date — SGBD (pp. 84–94)

**SGBD** (DataBase Management System — DBMS) = suită de aplicații software cu rolul principal de a **administra o bază de date** și de a oferi interfața între utilizatori și baza de date.

Asigură: definirea structurii BD, încărcarea datelor, accesul la date (interogare, actualizare), întreținerea BD, reorganizarea BD, securitatea datelor.

### Obiectivele SGBD:
- **Facilități sporite de utilizare** — acces multicriterial, limbaje performante de regăsire
- **Redundanță minimă și controlată** — fiecare dată apare o singură dată
- **Independența datelor față de aplicații:**
  - *Independența fizică* — modificarea stocării nu implică rescrierea programelor
  - *Independența logică* — adăugarea de noi date nu implică rescrierea programelor existente
- **Securitate sporită** — acces doar prin canale corespunzătoare; autorizare
- **Integritatea datelor** — proceduri de validare, protocoale de control concurent, proceduri de refacere după incidente
- **Partajabilitatea datelor** — mai mulți utilizatori accesează aceleași date simultan

### Funcțiile SGBD:
- **Funcția de descriere** — definirea structurii BD (schema BD)
- **Funcția de manipulare** — încărcare, adăugare, suprimare, modificare, selecție, editare
- **Funcția de utilizare** — interfețe pentru utilizatori (finali, dezvoltatori, administrator)
- **Funcția de administrare** — gestionarea BD pentru funcționare optimă

### Tipologia SGBD:
- **SGBD ierarhice și rețea** — prima generație (anii '60–'70)
- **SGBD relaționale (SGBDR)** — date simple, interogări complexe; cele mai răspândite
- **SGBD orientate-obiect (SGBDOO)** — date complexe, interogări dificile
- **SGBD relational-obiectuale (SGBDOR)** — date complexe + interogări complexe; cel mai complet model

### Sistemul de baze de date (SBD):
Un **sistem de baze de date** = ansamblu de elemente intercondiționate care contribuie la realizarea și exploatarea unei aplicații cu baze de date. Componente:
- **Datele** — colecțiile de date + dicționarul de date + fișierele anexe
- **Software** — SGBD + programele de aplicație
- **Elemente auxiliare** — proceduri, reglementări legale, hardware, personal
- **Utilizatorii** — finali + specialiști (administratori, analișți, programatori)

**Arhitecturi SBD:**
- **Pe componente** — software ca componentă centrală, cu date, elemente auxiliare și utilizatori în jur
- **Pe niveluri** — trei niveluri de organizare: conceptual, logic, fizic

---

# 3. BAZE DE DATE RELAȚIONALE
**Sursă: [1] Lungu — Tratat de baze de date, pp. 103–203**

## 3.1 Modelul relațional (pp. 103–110)

Modelul relațional (E.F. Codd, 1970) se bazează pe teoria matematică a algebrei relaționale. Are trei componente:

### a) Structura relațională
**Domeniu** = ansamblu de valori, caracterizat printr-un nume. Definit explicit (prin enumerare) sau implicit (prin proprietăți).

**Relație** = subansamblu al produsului cartezian al mai multor domenii, caracterizat printr-un **nume**, conținând tupluri cu semnificație.

Reprezentare convenabilă: **tabelul bidimensional** — liniile = tuplurile, coloanele = domeniile.

**Atribut** = coloana relației, caracterizată printr-un nume și un domeniu de valori.

**Schema relației R** = R(A₁:D₁, A₂:D₂, ..., Aₙ:Dₙ) unde Aᵢ sunt atributele și Dᵢ domeniile.

**Grad** = numărul de atribute ale relației.
**Cardinalitate** = numărul de tupluri.

### b) Operatorii relației
Definesc operațiile de interogare, adăugare, modificare, ștergere.

### c) Restricții de integritate
Permit definirea stărilor coerente ale BD.

### Avantaje ale modelului relațional:
- Independența programelor față de organizarea datelor
- Manipularea datelor la nivel de mulțime
- Nu folosește pointeri sau fișiere inverse
- Normalizarea relațiilor minimizează riscurile de eroare la actualizare

## 3.2 Structura relațională a datelor (pp. 105–113)

### Cheie primară
Mulțimea minimă de atribute ale relației prin care se identifică în mod unic orice tuplu. Nu poate lua valoarea NULL.

### Cheie externă (Foreign Key)
Un atribut (sau grup de atribute) al unei relații care este cheie primară în altă relație. Asigură legăturile între relații.

### Restricții de integritate fundamentale:
- **Integritatea entității** — nici un atribut din cheia primară nu poate fi NULL
- **Integritatea referențială** — valorile cheii externe trebuie să existe în relația referită sau să fie NULL

## 3.3 Algebra relațională (pp. 113–143)

Opera pe **relații** și returnează relații. Operatori:

### Operații pe mulțimi:
- **Reuniunea (R₁ ∪ R₂)** — tuplurile din R₁ sau R₂ (schemele identice)
- **Diferența (R₁ − R₂)** — tuplurile din R₁ care nu sunt în R₂
- **Intersecția (R₁ ∩ R₂)** — tuplurile comune
- **Produsul cartezian (R₁ × R₂)** — toate combinațiile de tupluri

### Operații relaționale:
- **Selecția (σ)** — extrage tuplurile care satisfac un predicat: σ_cond(R)
- **Proiecția (π)** — extrage coloane specifice: π_{A1,A2,...}(R)
- **Joncțiunea (⋈)** — combină tupluri din două relații pe baza unui predicat de egalitate

**Tipuri de joncțiune:**
- **Joncțiunea naturală** — pe atribute cu același nume; elimină duplicatele
- **Joncțiunea externă stânga (LEFT JOIN)** — toate tuplurile din R₁, chiar dacă nu au corespondent în R₂ (completate cu NULL)
- **Joncțiunea externă dreapta (RIGHT JOIN)** — toate tuplurile din R₂
- **Joncțiunea externă completă (FULL JOIN)** — toate tuplurile din ambele relații
- **Semijoncțiunea** — conservă atributele unei singure relații participante

- **Intersecția** — tupluri comune din două relații cu aceeași schemă

## 3.4 Realizarea bazelor de date relaționale — Proiectare (pp. 144–203)

### Analiza statică
Se identifică **entitățile** (persoane, obiecte, concepte din lumea reală) și **asocierile** (relațiile) dintre ele.

**Modelul Entitate-Asociere (EA)**:
- **Entitate** = obiect din lumea reală, identificabil și distinct
- **Atribut** = proprietate a entității
- **Asociere** = legătură între entități, cu un anumit tip (1:1, 1:N, M:N)
- **Grad asociere** = numărul de entități participante

**Asocieri speciale:**
- **Unare** — o entitate se asociază cu ea însăși
- **Binare** — două entități
- **Multiple** — mai mult de două entități participante

**Dificultăți**: legăturile directe vs. indirecte (tranzitivitate), redundanța asocierilor.

### Proiectarea conceptuală
Rezultat: **schema conceptuală** reprezentată prin diagrama EA (notații Chen sau Oracle). Include entitățile, atributele și asocierile.

### Proiectarea logică
Transformarea schemei conceptuale în tabele relaționale:
- Fiecare entitate → o relație (tabelă)
- Asociere 1:N → cheie externă în tabelul de pe partea N
- Asociere M:N → relație nouă (tabelă de legătură) cu cheile primare ale ambelor entități

### Normalizarea datelor
Proces de eliminare a redundanțelor și anomaliilor. Se bazează pe **dependențe funcționale**.

**Dependența funcțională** X → Y: pentru orice două tupluri cu același X, au același Y.

**Forme normale:**
- **FN1 (Prima formă normală)** — toate valorile sunt atomice (indivizibile); nu există atribute multivaluate sau compuse
- **FN2 (A doua formă normală)** — în FN1 + orice atribut non-cheie depinde funcțional de întreaga cheie primară (nu de o parte din ea)
- **FN3 (A treia formă normală)** — în FN2 + nu există dependențe tranzitive; orice atribut non-cheie depinde direct de cheia primară
- **FNBC (Boyce-Codd)** — formă mai strictă decât FN3; orice determinant este cheie candidat
- **FN4** și **FN5** — privesc dependențele multivaluate și joncțiunile fără pierderi

**Anomalii eliminate prin normalizare:**
- **Anomalie de inserare** — imposibilitatea de a insera date fără alte date
- **Anomalie de ștergere** — ștergerea unui tuplu duce la pierderea altor informații
- **Anomalie de actualizare** — modificarea unui fapt necesită actualizări în mai multe locuri

---

# 4. PROGRAMAREA ÎN SQL
**Sursă: [2] Lungu — Baze de date Oracle. Limbajul SQL, pp. 101–178**

## 4.1 Actualizarea structurii bazei de date (DDL) — pp. 101–122

### CREATE TABLE
```sql
CREATE TABLE nume_tabel (
  col1 tip_data [constrangeri],
  col2 tip_data [constrangeri],
  ...
  [constrangeri_la_nivel_de_tabel]
);
```

**Tipuri de date principale Oracle:**
- `VARCHAR2(n)` — șir de caractere variabil, max n caractere
- `CHAR(n)` — șir de lungime fixă
- `NUMBER(p,s)` — număr cu p cifre semnificative și s zecimale
- `DATE` — dată și oră
- `CLOB` — text lung; `BLOB` — date binare

**Constrângeri (constraints):**
- `NOT NULL` — câmpul nu poate fi NULL
- `UNIQUE` — valori unice (permite NULL)
- `PRIMARY KEY` — cheie primară (NOT NULL + UNIQUE)
- `FOREIGN KEY ... REFERENCES` — cheie externă
- `CHECK (condiție)` — verifică o condiție

### ALTER TABLE
```sql
ALTER TABLE tabel ADD (col tip_data);          -- adaugă coloană
ALTER TABLE tabel MODIFY (col tip_data_nou);   -- modifică coloana
ALTER TABLE tabel DROP COLUMN col;            -- șterge coloana
ALTER TABLE tabel ADD CONSTRAINT constr...;   -- adaugă constrângere
ALTER TABLE tabel DISABLE CONSTRAINT constr;  -- dezactivează
ALTER TABLE tabel DROP CONSTRAINT constr;     -- șterge constrângere
```

### DROP TABLE
```sql
DROP TABLE tabel [CASCADE CONSTRAINTS];
```

### CREATE INDEX
```sql
CREATE [UNIQUE] INDEX idx_name ON tabel(col1, col2, ...);
DROP INDEX idx_name;
```

### CREATE SEQUENCE
```sql
CREATE SEQUENCE seq_name
  START WITH valoare_initiala
  INCREMENT BY pas
  [MAXVALUE max | NOMAXVALUE]
  [CYCLE | NOCYCLE];
```
Utilizare: `seq_name.NEXTVAL`, `seq_name.CURRVAL`.

### CREATE VIEW
```sql
CREATE [OR REPLACE] VIEW view_name AS
  SELECT ...
  FROM ...
  [WHERE ...];
```

## 4.2 Actualizarea datelor (DML) — pp. 123–126

### INSERT
```sql
-- Inserare cu valori explicite
INSERT INTO tabel (col1, col2, ...) VALUES (v1, v2, ...);

-- Inserare din SELECT
INSERT INTO tabel (col1, col2)
  SELECT col1, col2 FROM alta_tabel WHERE conditie;
```

### UPDATE
```sql
UPDATE tabel
SET col1 = val1, col2 = val2, ...
[WHERE conditie];
```
Fără clauza WHERE — se actualizează **toate** înregistrările.

### DELETE
```sql
DELETE FROM tabel
[WHERE conditie];
```
Fără WHERE — se șterg **toate** înregistrările.

### TRUNCATE
```sql
TRUNCATE TABLE tabel;
```
Șterge toate înregistrările mai rapid (DDL, nu DML; nu poate fi anulat cu ROLLBACK).

## 4.3 Interogarea datelor — SELECT (pp. 127–178)

### Sintaxa generală:
```sql
SELECT [DISTINCT] col1, col2, ... | *
FROM tabel1 [alias], tabel2 [alias], ...
[WHERE conditie]
[GROUP BY col1, col2, ...]
[HAVING conditie_grup]
[ORDER BY col [ASC|DESC], ...];
```

### Condiționarea datelor (WHERE):
- Operatori de comparație: `=`, `<>`, `<`, `>`, `<=`, `>=`
- `BETWEEN val1 AND val2` — interval (inclusiv)
- `IN (v1, v2, ...)` — valoare dintr-o listă
- `LIKE 'pattern'` — potrivire după șablon (`%` = orice secvență, `_` = un caracter)
- `IS NULL` / `IS NOT NULL` — testarea valorii NULL
- Operatori logici: `AND`, `OR`, `NOT`

### Funcții SQL esențiale:
**Funcții numerice:** `ROUND(n,d)`, `TRUNC(n,d)`, `MOD(n,m)`, `ABS(n)`, `POWER(n,p)`, `SQRT(n)`, `CEIL(n)`, `FLOOR(n)`

**Funcții șir:** `UPPER(s)`, `LOWER(s)`, `INITCAP(s)`, `LENGTH(s)`, `SUBSTR(s,p,n)`, `INSTR(s,sub)`, `LTRIM(s)`, `RTRIM(s)`, `LPAD(s,n,c)`, `RPAD(s,n,c)`, `REPLACE(s,a,b)`, `CONCAT(s1,s2)` sau `s1||s2`

**Funcții dată:** `SYSDATE`, `ADD_MONTHS(d,n)`, `MONTHS_BETWEEN(d1,d2)`, `NEXT_DAY(d,zi)`, `LAST_DAY(d)`, `TO_DATE(str,'format')`, `TO_CHAR(d,'format')`

**Funcții de conversie:** `TO_CHAR(n,'format')`, `TO_NUMBER(str)`, `NVL(expr, val_default)`, `NVL2(expr, val_nn, val_n)`, `DECODE(expr, val1,rez1, val2,rez2, ..., default)`, `CASE WHEN ... THEN ... ELSE ... END`

### Funcții de grup (agregare):
- `COUNT(*)` / `COUNT(col)` — numără înregistrările
- `SUM(col)` — suma
- `AVG(col)` — media aritmetică
- `MAX(col)` / `MIN(col)` — maximul/minimul

Funcțiile de grup **ignoră valorile NULL**. Se folosesc cu `GROUP BY`. Filtrarea grupurilor se face cu `HAVING` (nu `WHERE`).

### Joncțiuni (JOIN):
```sql
-- Joncțiune naturală (ANSI):
SELECT ... FROM t1 NATURAL JOIN t2;

-- Joncțiune cu USING (ANSI):
SELECT ... FROM t1 JOIN t2 USING (col_comuna);

-- Joncțiune cu ON (ANSI):
SELECT ... FROM t1 JOIN t2 ON t1.col = t2.col;

-- Joncțiune externă stânga (ANSI):
SELECT ... FROM t1 LEFT JOIN t2 ON t1.col = t2.col;

-- Joncțiune externă dreapta (ANSI):
SELECT ... FROM t1 RIGHT JOIN t2 ON t1.col = t2.col;

-- Sintaxă Oracle tradițională:
SELECT ... FROM t1, t2 WHERE t1.col = t2.col;    -- inner join
SELECT ... FROM t1, t2 WHERE t1.col = t2.col(+); -- left join
```

### Subcereri (subqueries):
```sql
-- Subcerere pe un singur rând:
SELECT * FROM angajati WHERE salariu > (SELECT AVG(salariu) FROM angajati);

-- Subcerere pe mai multe rânduri (IN, ANY, ALL):
SELECT * FROM produse WHERE id_produs IN (SELECT id_produs FROM comenzi);
```

### Operatori pe mulțimi:
- `UNION` — reuniunea (elimină duplicate)
- `UNION ALL` — reuniunea (cu duplicate)
- `INTERSECT` — intersecția
- `MINUS` — diferența

### Structuri ierarhice:
```sql
SELECT nivel, id, parinte
FROM tabel
START WITH conditie_radacina
CONNECT BY PRIOR id = parinte;
```

---

# 5. PROGRAMAREA ÎN PL/SQL
**Sursă: [5] Bâra et al. — Baze de date. Limbajul PL/SQL, pp. 9–77, 103–118**

## 5.1 Introducere în PL/SQL (pp. 9–18)

**PL/SQL** (Procedural Language Extension to SQL) = limbaj procedural structurat pe bloc, specific Oracle. Permite combinarea instrucțiunilor SQL cu structuri de control procedurale.

**Caracteristici:**
- Procesare în **blocuri** (modularizare)
- Tipurile de date din SQL pot fi folosite
- Blocurile sunt procesate de **motorul PL/SQL** (rezident pe serverul Oracle sau pe instrumente de dezvoltare)

**Tipuri de blocuri PL/SQL:**
- **Blocuri anonime** — nu au nume, nu pot fi apelate din alte blocuri; nu sunt stocate în BD
- **Proceduri și funcții** — blocuri cu nume, stocate în BD, pot fi apelate
- **Declanșatori (triggers)** — blocuri asociate evenimentelor de pe tabele

## 5.2 Structura unui bloc PL/SQL

```
DECLARE
  -- secțiunea de declarare (opțională)
  -- variabile, cursori, excepții
BEGIN
  -- secțiunea executabilă (obligatorie)
  -- instrucțiuni SQL și PL/SQL
EXCEPTION
  -- secțiunea de tratare a excepțiilor (opțională)
END;
/
```

Secțiunile:
- **DECLARE** (opțională) — declarare variabile locale, constante, cursori
- **BEGIN...END** (obligatorie) — instrucțiunile propriu-zise
- **EXCEPTION** (opțională) — tratarea erorilor

## 5.3 Variabile PL/SQL (pp. 19–52)

### Declarare și inițializare:
```plsql
DECLARE
  var_name tip_data [:= valoare_initiala];
  var_const CONSTANT tip_data := valoare;  -- constantă
```

### Tipuri de variabile:

**Scalare:** `NUMBER`, `CHAR`, `VARCHAR2`, `DATE`, `BOOLEAN` (specific PL/SQL)

**Tip %TYPE** — preia tipul unei coloane din tabelă:
```plsql
var_salariu angajati.salariu%TYPE;
```

**Tip %ROWTYPE** — preia întreaga structură a unui rând din tabelă:
```plsql
rec_angajat angajati%ROWTYPE;
-- Acces: rec_angajat.nume, rec_angajat.salariu
```

**Tipuri compuse:**
- `TABLE` (colecție indexată / tablou asociativ)
- `VARRAY` (vector de dimensiune fixă)
- `NESTED TABLE` (tabel imbricat)
- `RECORD` (tip înregistrare, cu câmpuri de tipuri diferite)

### Structuri de control:

**Structura alternativă:**
```plsql
IF conditie THEN
  instructiuni;
ELSIF alta_conditie THEN
  instructiuni;
ELSE
  instructiuni;
END IF;
```

**Structura CASE:**
```plsql
CASE variabila
  WHEN val1 THEN instructiuni;
  WHEN val2 THEN instructiuni;
  ELSE instructiuni;
END CASE;
```

**Structura repetitivă LOOP:**
```plsql
LOOP
  instructiuni;
  EXIT WHEN conditie;
END LOOP;
```

**Structura WHILE:**
```plsql
WHILE conditie LOOP
  instructiuni;
END LOOP;
```

**Structura FOR:**
```plsql
FOR i IN [REVERSE] val_min..val_max LOOP
  instructiuni;
END LOOP;
```

### Instrucțiuni SQL în PL/SQL:
Se pot folosi: `SELECT INTO`, `INSERT`, `UPDATE`, `DELETE`, `COMMIT`, `ROLLBACK`.

```plsql
SELECT col1, col2 INTO var1, var2
FROM tabel WHERE conditie;
-- Atenție: SELECT INTO trebuie să returneze exact 1 rând!
```

### Tratarea excepțiilor:
```plsql
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    -- niciun rând returnat
  WHEN TOO_MANY_ROWS THEN
    -- mai mult de un rând returnat
  WHEN ZERO_DIVIDE THEN
    -- împărțire la zero
  WHEN OTHERS THEN
    -- orice altă eroare
    DBMS_OUTPUT.PUT_LINE(SQLERRM);
```

**Excepții predefinite:** `NO_DATA_FOUND`, `TOO_MANY_ROWS`, `ZERO_DIVIDE`, `VALUE_ERROR`, `CURSOR_ALREADY_OPEN`, `DUP_VAL_ON_INDEX`.

**Excepții definite de utilizator:**
```plsql
DECLARE
  exc_proprie EXCEPTION;
BEGIN
  IF conditie THEN RAISE exc_proprie; END IF;
EXCEPTION
  WHEN exc_proprie THEN instructiuni;
END;
```

## 5.4 Mecanismul de cursor (pp. 53–77)

Un **cursor** = pointer asociat unei cereri SELECT, care permite accesarea iterativă a rândurilor din setul de rezultate.

### Cursori impliciti
Creați automat de Oracle pentru fiecare instrucțiune SQL DML sau SELECT INTO. Atribute: `SQL%FOUND`, `SQL%NOTFOUND`, `SQL%ROWCOUNT`, `SQL%ISOPEN`.

### Cursori expliciti
Declarați, deschiși și închiși manual.

```plsql
DECLARE
  CURSOR c_angajati IS
    SELECT id, nume, salariu FROM angajati WHERE dept_id = 10;
  v_id    angajati.id%TYPE;
  v_nume  angajati.nume%TYPE;
  v_sal   angajati.salariu%TYPE;
BEGIN
  OPEN c_angajati;
  LOOP
    FETCH c_angajati INTO v_id, v_nume, v_sal;
    EXIT WHEN c_angajati%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(v_nume || ' - ' || v_sal);
  END LOOP;
  CLOSE c_angajati;
END;
```

**Pași obligatori:** DECLARE → OPEN → FETCH (în buclă) → CLOSE.

**Atribute cursor explicit:** `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, `%ISOPEN`.

### Cursor FOR LOOP (simplificat):
```plsql
FOR rec IN (SELECT id, nume FROM angajati) LOOP
  DBMS_OUTPUT.PUT_LINE(rec.id || ' ' || rec.nume);
END LOOP;
```
Nu necesită DECLARE, OPEN, FETCH, CLOSE explicit.

### Cursori cu parametri:
```plsql
CURSOR c_dep (p_dept NUMBER) IS
  SELECT * FROM angajati WHERE dept_id = p_dept;
-- Utilizare:
OPEN c_dep(10);
```

### Cursor FOR UPDATE:
Permite blocarea rândurilor pentru actualizare:
```plsql
CURSOR c IS SELECT * FROM tabel FOR UPDATE;
-- În buclă:
UPDATE tabel SET col = val WHERE CURRENT OF c;
```

## 5.5 Gestiunea subprogramelor — Proceduri și funcții (pp. 103–118)

### Proceduri stocate:
```plsql
CREATE [OR REPLACE] PROCEDURE nume_proc
  (param1 [IN|OUT|IN OUT] tip, ...)
IS
  -- declaratii locale
BEGIN
  -- corp procedura
EXCEPTION
  -- tratare erori
END [nume_proc];
/
```

**Moduri de transfer al parametrilor:**
- `IN` — parametru de intrare (valoare transmisă procedurii, nu poate fi modificată)
- `OUT` — parametru de ieșire (returnează valoare apelantului)
- `IN OUT` — intrare și ieșire (transmis și returnat)

**Apel procedură:**
```plsql
BEGIN
  nume_proc(arg1, arg2, ...);
END;
```

### Funcții stocate:
```plsql
CREATE [OR REPLACE] FUNCTION nume_func
  (param1 IN tip, ...)
RETURN tip_returnat
IS
  -- declaratii locale
BEGIN
  -- corp functie
  RETURN valoare;
END [nume_func];
/
```

Funcțiile returnează **un singur** valor. Pot fi apelate din SQL (dacă nu conțin DML).

**Apel funcție:**
```plsql
DECLARE v tip; BEGIN v := nume_func(arg); END;
-- sau direct în SQL:
SELECT nume_func(col) FROM tabel;
```

---

# 6. TIPURI FUNDAMENTALE DE DATE ȘI CLASE DE MEMORIE ÎN C
**Sursă: [3] Smeureanu, Dârdală — Programarea în limbajul C/C++, pp. 16–28**

## 6.1 Tipuri fundamentale de date și constante (pp. 16–21)

| Tip de dată | Lungime (octeți) | Domeniu de valori |
|---|---|---|
| `char` | 1 | −128...127 (signed) / 0...255 (unsigned) |
| `int` | 2 sau 4 | −32768...32767 / −2147483648...2147483647 |
| `short int` | 2 | −32768...32767 |
| `long int` | 4 | −2147483648...2147483647 |
| `unsigned int` | 2 sau 4 | 0...65535 / 0...4294967295 |
| `float` | 4 | 1.2E−38...3.4E+38 |
| `double` | 8 | 2.2E−308...1.8E+308 |
| `long double` | 10 | 3.4E−4932...1.2E+4932 |
| `void` | 0 | — |

**Modificatori de tip:**
- `unsigned` — nu tratează bitul cel mai semnificativ ca bit de semn
- `signed` — tratează bitul cel mai semnificativ ca bit de semn
- `long` — extinde dimensiunea zonei de memorie
- `short` — reduce dimensiunea zonei de memorie

### Tipul caracter (`char`):
- Subtipologie a tipului întreg, 1 octet
- Descriptori: `%c` (afișare simbol grafic), `%d` (afișare cod ASCII)

### Tipul întreg (`int`):
- În implementările pe 32 biți: memorat pe 4 octeți
- Descriptori: `%d` (zecimal), `%o` (octal), `%x` (hex), `%u` (unsigned)

### Tipul real (`float`, `double`):
- Reprezentare în virgulă mobilă
- `float` — simplă precizie; `double` — dublă precizie; `long double` — precizie extinsă
- Descriptori: `%f`, `%e`, `%g`

### Constante:
- **Întregi:** zecimale (ex: 123), octale (prefix 0, ex: 0123), hexazecimale (prefix 0x, ex: 0x7F)
- **Reale:** 3.14, 3.14f, 3.14e2
- **Caracter:** 'a', '\n', '\t', '\0', '\\'
- **Șir de caractere:** "text" (terminat cu '\0')
- **Simbolice:** `#define PI 3.14159`

## 6.2 Specificatorul de format (pp. 21–25)

Folosit în `printf()` și `scanf()` pentru a specifica modul de citire/scriere:

`%[flags][width][.precision][modifier]type`

| Specificator | Tip |
|---|---|
| `%d`, `%i` | întreg zecimal |
| `%u` | întreg fără semn |
| `%o` | întreg octal |
| `%x`, `%X` | întreg hexazecimal |
| `%f` | real în virgulă fixă |
| `%e`, `%E` | real în notație exponențială |
| `%g`, `%G` | real (cel mai scurt format) |
| `%c` | caracter |
| `%s` | șir de caractere |
| `%p` | adresă (pointer) |

**Flag-uri:**
- `-` — aliniere la stânga
- `+` — afișează semnul
- `0` — umplere cu zerouri
- `#` — prefixul 0 (octal) sau 0x (hex)

## 6.3 Clase de memorie (pp. 25–28)

Clasa de memorie determină **durata de viață** și **vizibilitatea** variabilei.

### `auto` (implicită pentru variabile locale)
- Declarate în interiorul unui bloc
- Viață limitată la blocul respectiv
- Memorate pe stivă (stack)

### `register`
- Solicită stocarea în **registru** (pentru acces mai rapid)
- Nu se poate lua adresa (`&` interzis)
- Utilizare: variabile cu acces frecvent (contori de buclă)

### `static`
- **Static local** — variabilă locală cu durată de viață permanentă; se inițializează o singură dată; valoarea se păstrează între apeluri de funcție
- **Static global** — vizibilitate limitată la fișierul curent (extern nu are efect)

### `extern`
- Declară că variabila e definită într-un alt fișier/modul
- Nu alocă memorie; înștiințează compilatorul de existența variabilei

---

# 7. OPERATORI ȘI EXPRESII ÎN C
**Sursă: [3] Smeureanu, Dârdală — Programarea în limbajul C/C++, pp. 30–46**

## 7.1 Clase de operatori (pp. 30–42)

**Prioritatea** scade de la prima clasă la ultima. Evaluare de la stânga la dreapta, excepție: operatori unari, operator condițional, operatori de atribuire (dreapta la stânga).

### Clasa I — Operatori pentru funcții, masive, structuri:
- `[]` — indexare masiv
- `()` — apel funcție, grupare expresii
- `.` — acces câmp structură (prin variabilă)
- `->` — acces câmp structură (prin pointer)

### Clasa II — Operatori unari (dreapta la stânga):
- `!` — negație logică (`!0 = 1`, `!nonzero = 0`)
- `~` — complementare pe biți (NOT bit cu bit)
- `++` — incrementare (prefix: crește înainte; postfix: crește după)
- `--` — decrementare (similar)
- `-` — minus unar (schimbare semn)
- `+` — plus unar
- `*` — dereferențiere pointer (acces la conținut)
- `&` — adresa variabilei
- `(tip)` — conversie explicită (cast)
- `sizeof` — dimensiunea în octeți a unui tip/variabile

### Clasa III — Operatori multiplicativi:
- `*` — înmulțire
- `/` — împărțire (pentru întregi: împărțire entieră)
- `%` — modulo (restul împărțirii întregi)

### Clasa IV — Operatori aditivi:
- `+` — adunare
- `-` — scădere

### Clasa V — Operatori de deplasare pe biți:
- `<<` — deplasare la stânga (echivalent cu înmulțire cu puterea lui 2)
- `>>` — deplasare la dreapta (echivalent cu împărțire cu puterea lui 2)

### Clasa VI — Operatori de relație:
- `<`, `>`, `<=`, `>=` — comparații

### Clasa VII — Operatori de egalitate:
- `==` — egal
- `!=` — diferit

### Clasa VIII–X — Operatori pe biți:
- `&` — ȘI pe biți (AND)
- `^` — SAU exclusiv pe biți (XOR)
- `|` — SAU pe biți (OR)

### Clasa XI–XII — Operatori logici:
- `&&` — ȘI logic (AND scurtcircuitat)
- `||` — SAU logic (OR scurtcircuitat)

### Clasa XIII — Operatorul condițional (ternar):
- `expr ? val_adev : val_fals`
- Ex: `max = (a > b) ? a : b;`

### Clasa XIV — Operatori de atribuire (dreapta la stânga):
- `=` — atribuire simplă
- `+=`, `-=`, `*=`, `/=`, `%=` — atribuire compusă aritmetică
- `<<=`, `>>=`, `&=`, `^=`, `|=` — atribuire compusă pe biți

### Clasa XV — Operatorul virgulă:
- `,` — evaluează expresiile de la stânga la dreapta; rezultatul = valoarea ultimei expresii
- Ex: `for(i=0, j=10; i<10; i++, j--)`

## 7.2 Conversii în expresii (pp. 43–46)

### Conversii implicite (automate):
Se realizează în expresii cu operanzi de tipuri diferite:
1. `char`, `short` → `int`
2. `float` → `double`
3. Dacă operanzii sunt de tipuri diferite: se convertește tipul "mai mic" la tipul "mai mare": `int → long → float → double → long double`

**Regulă:** tipul rezultatului = tipul operandului cu precizia mai mare.

### Conversii explicite (cast):
```c
(tip) expresie
```
Ex: `(float) i / j` — convertește `i` la `float` înainte de împărțire; rezultat `float`.

---

# 8. INSTRUCȚIUNI DE BAZĂ ALE LIMBAJULUI C
**Sursă: [3] Smeureanu, Dârdală — Programarea în limbajul C/C++, pp. 48–58**

## 8.1 Structura liniară (p. 48)
Evaluarea unor expresii:
```c
i++;
a = 7;
printf("\n a=%d", a);
;  // instrucțiunea vidă
```

## 8.2 Structura alternativă (pp. 48–49)

**Pseudoalternativă:**
```c
if (expr) instr;
```

**Alternativă:**
```c
if (expr) instr_1;
else instr_2;
```

**Alternativă multiplă:**
```c
if (expr_1) instr_1;
else if (expr_2) instr_2;
...
else instr_n+1;
```

**Regula else:** `else` se asociază cu **ultimul `if` activat**. Pentru a schimba asocierea, se folosesc acolade `{}`.

## 8.3 Structuri repetitive (pp. 50–52)

### WHILE (condiționată anterior):
```c
while (expr) instr;
```
Verifică condiția înainte; dacă e falsă de la început, nu execută niciodată.

### DO-WHILE (condiționată posterior):
```c
do { instr; } while (expr);
```
Execută cel puțin o dată; verifică condiția după execuție.

### FOR (cu contor):
```c
for (expr_init; expr_cond; expr_incr) instr;
```
- `expr_init` — inițializarea (o dată, la început)
- `expr_cond` — condiția de continuare
- `expr_incr` — actualizarea

Oricare din expresii poate fi vidă. `for(;;)` = buclă infinită.

## 8.4 Selecția multiplă — switch (pp. 52–53)
```c
switch (expr_intreaga) {
  case val1:
    instructiuni;
    break;
  case val2:
    instructiuni;
    break;
  default:
    instructiuni;
}
```
**Atenție:** fără `break`, execuția "cade" (fall-through) în case-ul următor! `default` se execută dacă nicio valoare nu coincide.

## 8.5 Alte instrucțiuni (pp. 54–58)

### `break`
Ieșire forțată din `switch`, `while`, `do-while`, `for`.

### `continue`
Sare la iterația următoare (omite restul corpului buclei).

### `return`
Ieșire din funcție, cu sau fără valoare returnată:
```c
return;          // funcție void
return expresie; // funcție cu valoare
```

### `goto`
Salt necondiționat la o etichetă (utilizare descurajată):
```c
goto eticheta;
...
eticheta: instructiune;
```

---

# 9. MASIVE ȘI POINTERI ÎN C
**Sursă: [3] Smeureanu, Dârdală — Programarea în limbajul C/C++, pp. 60–74**

## 9.1 Pointeri și aritmetica de pointeri (pp. 60–67)

Un **pointer** = variabilă care conține **adresa** altei variabile. Definire cu operatorul `*`:
```c
int x, *px, *py;
```
`px` este un pointer la întreg (conține adresa unui întreg).

**Operatori esențiali:**
- `&` — extragerea adresei: `px = &x;`
- `*` — dereferențierea (accesul la conținut): `*px` este echivalent cu `x`

**Inițializare:**
```c
int x = 7, *px = &x;  // px conține adresa lui x
```

**Pointerul NULL** — pointer care nu pointează nimic: `int *p = NULL;`

**Aritmetica de pointeri:**
- `p + n` — avansează pointerul cu `n * sizeof(tip)` octeți
- `p - n` — retrocedează similar
- `p++`, `p--` — avansează/retrocedează cu un element
- `p1 - p2` — diferența (numărul de elemente între cei doi pointeri)
- **NU** se pot aduna doi pointeri

**Modificatorul `const` cu pointeri:**
- `tip *const p` — pointer constant (adresa nu poate fi modificată)
- `const tip *p` — pointer la o zonă constantă (conținutul nu poate fi modificat)

**Alocarea dinamică:**
```c
int *p = (int*) malloc(sizeof(int));  // C
int *p = new int;                     // C++
free(p);      // eliberare C
delete p;     // eliberare C++
// Pentru masive:
int *v = new int[n];
delete[] v;
```

## 9.2 Masive unidimensionale și multidimensionale (pp. 67–71)

### Masive unidimensionale (vectori):
```c
int a[10];        // declarare
int b[5] = {1,2,3,4,5};  // declarare cu inițializare
a[0] = 5;        // acces prin index (indexul începe de la 0!)
```
**Relația vector-pointer:** `a` este echivalent cu `&a[0]`, deci `a[i]` = `*(a+i)`.

### Masive multidimensionale (matrice):
```c
int m[3][4];       // 3 linii, 4 coloane
m[i][j] = val;     // acces la elementul de pe linia i, coloana j
```
**Stocarea în memorie:** pe linii (row-major), ca în C.

## 9.3 Masive de pointeri și pointeri la masive (pp. 71–74)

### Masiv de pointeri:
```c
char *siruri[5];   // 5 pointeri la char
siruri[0] = "Luni";
siruri[1] = "Marti";
```

### Pointer la masiv:
```c
int (*pa)[4];      // pointer la un masiv de 4 întregi
int m[3][4];
pa = m;            // pa pointează primul rând din m
pa[i][j] = val;    // echivalent cu m[i][j]
```

---

# 10. LUCRU CU ȘIRURI DE CARACTERE ÎN C
**Sursă: [3] Smeureanu, Dârdală — Programarea în limbajul C/C++, pp. 76–88**

## 10.1 Variabile și constante de tip caracter/șir (pp. 76–80)

**Șirul de caractere** în C = masiv de `char`, terminat cu caracterul **NUL** (`'\0'`).

```c
char sir[20];              // declarare
char s1[] = "salut";       // inițializare (alocă 6 octeți: 5 + '\0')
char s2[10] = "salut";     // alocă 10, inițializează cu "salut\0"
```

**Pointer la șir:**
```c
char *ps = "buna ziua";    // ps pointează constanta "buna ziua"
```
**Diferență crucială:** `char s[]` — masiv (modificabil), `char *s` — pointer la constantă (nemodificabilă în practică).

## 10.2 Funcții de intrare/ieșire pentru caractere (pp. 80–83)

**Pentru caractere individuale:**
```c
int getchar(void);    // citire caracter de la tastatură
int putchar(int c);   // afișare caracter
```

**Pentru șiruri:**
```c
char* gets(char *s);            // citire șir (nesigur! evitat modern)
int puts(const char *s);        // afișare șir + newline
printf("%s", s);                // afișare cu format
scanf("%s", s);                 // citire (se oprește la spațiu!)
```

## 10.3 Funcții pentru prelucrarea șirurilor (pp. 83–88)
Header: `<string.h>`

| Funcție | Descriere |
|---|---|
| `strlen(s)` | Lungimea șirului (fără '\0') |
| `strcpy(dest, src)` | Copiază src în dest |
| `strncpy(dest, src, n)` | Copiază max n caractere |
| `strcat(dest, src)` | Concatenează src la dest |
| `strncat(dest, src, n)` | Concatenează max n caractere |
| `strcmp(s1, s2)` | Compară s1 și s2 (0=egal, <0=s1<s2, >0=s1>s2) |
| `strncmp(s1, s2, n)` | Compară primele n caractere |
| `strchr(s, c)` | Primul pointer la caracterul c în s |
| `strrchr(s, c)` | Ultimul pointer la c în s |
| `strstr(s, sub)` | Primul pointer la subșirul sub în s |
| `strtok(s, delim)` | Tokenizare (împărțire după delimitatori) |
| `sprintf(str, format, ...)` | Scriere formatată în șir |
| `sscanf(str, format, ...)` | Citire formatată din șir |

Header `<ctype.h>` — funcții pentru caractere individuale:
- `isalpha(c)`, `isdigit(c)`, `isalnum(c)`, `isupper(c)`, `islower(c)`, `isspace(c)`
- `toupper(c)`, `tolower(c)`

---

# 11. FUNCȚII ÎN C
**Sursă: [3] Smeureanu, Dârdală — Programarea în limbajul C/C++, pp. 90–114**

## 11.1 Conceptul de funcție și transferul parametrilor (pp. 90–98)

**Funcția** = unitate modulară de program, cu nume, parametri și tip de retur.

**Structura:**
```c
tip_retur nume_functie (lista_param_formali) {
  // corpul funcției
  return expresie;  // dacă tip_retur nu e void
}
```

**Prototipul (declararea):**
```c
tip_retur nume_functie (tip1 param1, tip2 param2, ...);
```
Necesară dacă funcția e definită după punctul de apel.

### Transferul parametrilor — **exclusiv prin valoare** (în C de bază):
- Se transmite o **copie** a valorii; modificările în funcție nu afectează variabila originală
- Pentru a modifica o variabilă din exterior: se transmite **adresa** ei (pointer):
```c
void incrementeaza(int *p) { (*p)++; }
// apel:
int x = 5;
incrementeaza(&x);  // x devine 6
```

## 11.2 Clase de funcții (pp. 98–100)

**Funcții cu tip de retur:** returnează o valoare cu `return expresie`

**Funcții void:** nu returnează nimic (`return;` opțional)

**Funcții externe (implicite):** vizibile în toate fișierele programului

**Funcții statice:** vizibilitate limitată la fișierul de definire

## 11.3 Funcții recursive (pp. 100–102)

O funcție este **recursivă** dacă se apelează pe ea însăși (direct sau indirect).

Orice funcție recursivă are:
- **Cazul de bază** — condiție de oprire (fără apel recursiv)
- **Cazul recursiv** — apelul pe un subproblemă mai mică

```c
long factorial(int n) {
  if (n <= 1) return 1;     // caz de bază
  return n * factorial(n-1); // caz recursiv
}
```

**Avantaje:** claritate, eleganță pentru probleme cu structură recursivă (arbori, fractaluri)
**Dezavantaje:** consum de stivă (stack overflow pentru recursii adânci), performanță

## 11.4 Pointeri la funcții (pp. 102–107)

Un **pointer la funcție** conține adresa unei funcții. Permite apelul indirect al funcțiilor.

```c
// Declarare:
tip_retur (*ptr_func)(tip1, tip2, ...);

// Exemplu:
int (*pf)(int, int);    // pointer la funcție care ia 2 int și returnează int

int suma(int a, int b) { return a + b; }
pf = suma;              // sau: pf = &suma;
int rez = pf(3, 4);     // apel prin pointer: rez = 7
```

**Utilizare:** tablouri de funcții, callback-uri, sortări generice (ex: `qsort`).

## 11.5 Argumentele funcției main() (pp. 107–111)

```c
int main(int argc, char *argv[]) { ... }
```
- `argc` — numărul de argumente de la linia de comandă (inclusiv numele programului)
- `argv` — masiv de pointeri la șiruri; `argv[0]` = numele programului, `argv[1]`...`argv[argc-1]` = argumentele

## 11.6 Funcții cu număr variabil de parametri (pp. 113–114)
Header: `<stdarg.h>` (sau `<varargs.h>`)

```c
#include <stdarg.h>
int suma_variabila(int n, ...) {
  va_list lista;
  va_start(lista, n);       // inițializare
  int total = 0;
  for (int i = 0; i < n; i++) {
    total += va_arg(lista, int); // extragere argument
  }
  va_end(lista);             // terminare
  return total;
}
```

---

# 12. STRUCTURI ȘI UNIUNI ÎN C
**Sursă: [3] Smeureanu, Dârdală — Programarea în limbajul C/C++, pp. 118–168**

## 12.1 Structuri, uniuni și typedef (pp. 118–136)

### Structuri:
O **structură** = tip de date compus din câmpuri de tipuri diferite (similar unui record).

```c
struct persoana {
  char nume[30];
  int varsta;
  float salariu;
};

// Declarare variabilă:
struct persoana p1, p2;
// Sau direct la definire:
struct persoana {
  char nume[30];
  int varsta;
} p1, p2;

// Acces câmpuri:
p1.varsta = 25;
strcpy(p1.nume, "Popescu");
printf("%s are %d ani\n", p1.nume, p1.varsta);
```

**Inițializare:**
```c
struct persoana p = {"Ion", 30, 2500.0};
```

**Structuri imbricate (nested):**
```c
struct data {
  int zi, luna, an;
};
struct angajat {
  char nume[30];
  struct data data_angajare;
};
angajat.data_angajare.an = 2023;
```

**Pointeri la structuri:**
```c
struct persoana *pp = &p1;
pp->varsta = 25;  // echivalent cu (*pp).varsta = 25;
```

**Pasare structuri la funcții:**
- Prin valoare: se copiază întreaga structură (costisitor pentru structuri mari)
- Prin pointer: eficient, modifică structura originală

### Uniuni (`union`):
Toți membrii **partajează aceeași zonă de memorie**. Dimensiunea = dimensiunea celui mai mare câmp.

```c
union date {
  int intreg;
  float real;
  char caracter;
};
union date u;
u.intreg = 5;    // acum zona conține un întreg
u.real = 3.14;   // acum zona conține un real (suprascrie întregul!)
```
**La un moment dat, este valid doar ultimul câmp scris.**

### `typedef` — definire tipuri sinonime:
```c
typedef struct persoana Persoana;  // acum se poate scrie Persoana p; în loc de struct persoana p;
typedef int Intreg;
typedef char* PChar;
// Comun:
typedef struct {
  char nume[30];
  int varsta;
} Angajat;
Angajat a1;
```

## 12.2 Structuri autoreferite — liste înlănțuite (pp. 136–168)

O **structură autoreferită** = structură care conține un câmp pointer la același tip de structură.

```c
struct nod {
  int info;
  struct nod *urm;  // pointer la tipul însuși
};
```

**Nod al unei liste simplu înlănțuite:**
```c
typedef struct nod {
  int info;
  struct nod *urm;
} Nod;

// Creare nod:
Nod *p = (Nod*) malloc(sizeof(Nod));
p->info = 5;
p->urm = NULL;
```

**Operații pe lista simplu înlănțuită:**

**Inserare la început:**
```c
Nod *inserare_inceput(Nod *cap, int val) {
  Nod *p = (Nod*) malloc(sizeof(Nod));
  p->info = val;
  p->urm = cap;
  return p;  // noul cap
}
```

**Parcurgere:**
```c
Nod *curent = cap;
while (curent != NULL) {
  printf("%d ", curent->info);
  curent = curent->urm;
}
```

**Ștergere nod:**
```c
// Ștergere după un nod cunoscut 'prev':
Nod *de_sters = prev->urm;
prev->urm = de_sters->urm;
free(de_sters);
```

**Liste dublu înlănțuite:**
```c
struct nod_dublu {
  int info;
  struct nod_dublu *prec;  // pointer la nodul precedent
  struct nod_dublu *urm;   // pointer la nodul următor
};
```
Permit parcurgere în ambele sensuri.

**Stive și cozi** implementate cu liste înlănțuite:
- **Stivă (LIFO):** inserare și extragere la începutul listei
- **Coadă (FIFO):** inserare la coadă, extragere de la cap

---

# 13. PREPROCESAREA ÎN C
**Sursă: [3] Smeureanu, Dârdală — Programarea în limbajul C/C++, pp. 170–177**

Preprocesarea = pasul anterior compilării propriu-zise. Directivele de preprocesare încep cu `#`.

## 13.1 Substituirea simbolică — tipul `enum` (pp. 170–173)

### `#define` — definire constantă simbolică:
```c
#define PI 3.14159
#define MAX 100
#define SIR "salut"
```
**Textual:** preprocesorul înlocuiește orice apariție a numelui cu textul specificat (nu tipizat!).

### `enum` — tip enumerare:
```c
enum zileSapt { LUNI, MARTI, MIERCURI, JOI, VINERI, SAMBATA, DUMINICA };
enum zileSapt zi = LUNI;
```
Valorile încep automat de la 0, incrementând cu 1. Pot fi specificate manual:
```c
enum culori { ROSU = 1, VERDE = 2, ALBASTRU = 4 };
```

**Avantaje `enum` față de `#define`:** tipizare, vizibilitate în debugger, mai ușor de întreținut.

### `#undef` — eliminare definiție:
```c
#undef MAX
```

### Directive condiționale:
```c
#ifdef SIMBOL     // dacă SIMBOL e definit
  ...
#endif

#ifndef SIMBOL    // dacă SIMBOL NU e definit
  ...
#endif

#if expresie      // dacă expresia e adevărată
  ...
#elif alta_expr
  ...
#else
  ...
#endif
```

**Utilizare tipică — protecție header (include guard):**
```c
#ifndef FISIER_H
#define FISIER_H
  // conținutul header-ului
#endif
```

## 13.2 Macrodefiniții (pp. 173–177)

O **macrodefinție** = `#define` cu parametri; se expandează textual la locul apelului.

```c
#define SQ(x)    ((x)*(x))
#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define ABS(x)   ((x)<0 ? -(x) : (x))
```

**Reguli importante:**
- Întotdeauna **paranteze** în jurul parametrilor și al întregii expresii (altfel operatorul de precedență poate genera erori)
- `SQ(a+1)` cu `#define SQ(x) x*x` → `a+1*a+1` (GREȘIT!)
- `SQ(a+1)` cu `#define SQ(x) ((x)*(x))` → `((a+1)*(a+1))` (CORECT!)

**Macro pe mai multe linii:**
```c
#define AFISARE(x) \
  printf("Valoarea: %d\n", x)
```

**Diferența macro vs. funcție:**
- Macro: expandare textuală, fără overhead de apel, fără verificare de tip
- Funcție: cod compilat, verificare de tip, overhead de apel dar reutilizare mai sigură

**Macro predefinite:**
- `__FILE__` — numele fișierului sursă
- `__LINE__` — numărul liniei curente
- `__DATE__` — data compilării
- `__TIME__` — ora compilării

---

# 14. PROGRAMARE ORIENTATĂ OBIECT (C++)
**Sursă: [4] Smeureanu, Dârdală — Programarea orientată obiect în C++, pp. 11–133**

## 14.1 Abstractizarea datelor. Conceptul de clasă (pp. 11–51)

**Clasa** = tip de date care încapsulează **date** (atribute) și **funcții** (metode) care operează asupra lor. Implementează un concept abstract.

**Avantaje:**
- Specializarea prelucrărilor
- Localizarea facilă a erorilor
- Surprinderea tipologiei relațiilor dintre entități
- Gestionarea accesului prin "ascunderea" datelor
- Moduri de comunicare între entități

### Definirea unei clase:
```cpp
class Persoana {
private:
  int varsta;        // acces doar din interiorul clasei
protected:
  float salariu;     // acces din clasa și din clasele derivate
public:
  char nume[20];     // acces oriunde
  
  // Constructor
  Persoana(char *n = "Anonim", int v = 0, float s = 0.0) {
    strcpy(nume, n); varsta = v; salariu = s;
  }
  
  // Destructor
  ~Persoana() { }
  
  // Metode
  int spuneVarsta() { return varsta; }  // funcție inline
  char* spuneNume();                    // declarată, definită afară
};

// Definire metodă în afara clasei:
char* Persoana::spuneNume() {
  return nume;
}
```

### Specificatori de acces:
- **`private`** — accesibil doar din interiorul clasei (implicit pentru `class`)
- **`protected`** — accesibil din clasă și din clasele derivate (moștenire)
- **`public`** — accesibil oriunde

**Diferența `class` vs. `struct`:** implicit `private` (class) vs. implicit `public` (struct).

### Obiectul = instanța clasei:
```cpp
Persoana p1("Ion", 30, 2500.0);  // creare obiect (apelul constructorului)
p1.spuneVarsta();                // apel metodă
Persoana *pp = &p1;              // pointer la obiect
pp->spuneVarsta();
```

### Constructori:
- Se apelează automat la crearea obiectului
- Pot fi supraîncărcați (mai mulți constructori cu parametri diferiți)
- **Constructor implicit** — fără parametri sau cu toți parametri impliciți
- **Constructor de copiere** — preia un obiect de același tip: `Persoana(const Persoana& p);`

### Destructori:
- Se apelează automat la distrugerea obiectului
- Un singur destructor, fără parametri: `~Persoana()`
- Eliberează resursele alocate dinamic

### Funcții `inline`:
Funcțiile definite direct în clasa = inline. Substituție textuală la locul apelului (fără overhead).

### Date și funcții membre statice:
```cpp
class Contor {
public:
  static int nr_obiecte;       // dată statică: comună tuturor instanțelor
  static int getNrObiecte() { return nr_obiecte; }  // funcție statică
};
int Contor::nr_obiecte = 0;    // definiție obligatorie în afara clasei
// Apel: Contor::getNrObiecte() sau contor_obj.getNrObiecte()
```

## 14.2 Supraîncărcarea operatorilor și funcțiilor (pp. 52–85)

### Supraîncărcarea funcțiilor (overloading):
Aceeași denumire, parametri diferiți (tip și/sau număr). Compilatorul alege versiunea potrivită.

```cpp
int suma(int a, int b) { return a + b; }
double suma(double a, double b) { return a + b; }
int suma(int a, int b, int c) { return a + b + c; }
```

**Nu** se poate supraîncărca doar prin tipul de retur.

### Supraîncărcarea operatorilor:
Permite utilizarea operatorilor standard (`+`, `-`, `*`, `[]`, `<<`, etc.) cu tipuri definite de utilizator.

```cpp
class Complex {
public:
  double re, im;
  Complex(double r=0, double i=0) : re(r), im(i) {}
  
  // Supraîncărcare ca metodă:
  Complex operator+(const Complex& c) const {
    return Complex(re + c.re, im + c.im);
  }
  
  // Supraîncărcare ca funcție externă (prietenă):
  friend ostream& operator<<(ostream& os, const Complex& c);
};

ostream& operator<<(ostream& os, const Complex& c) {
  os << c.re << "+" << c.im << "i";
  return os;
}
```

**Operatori supraîncărcabili:** `+`, `-`, `*`, `/`, `%`, `++`, `--`, `=`, `==`, `!=`, `<`, `>`, `[]`, `()`, `<<`, `>>`, etc.

**Operatori nesupraîncărcabili:** `::`, `.`, `.*`, `?:`, `sizeof`.

**Regulă:** cel puțin un operand trebuie să fie de tip clasă; nu se poate schimba precedența sau aritatea.

## 14.3 Polimorfism (pp. 52–85)

**Polimorfismul** = capacitatea de a trata obiecte de tipuri diferite printr-o interfață uniformă.

**Tipuri de polimorfism:**
- **Compilare (static):** supraîncărcarea funcțiilor și operatorilor
- **Execuție (dinamic):** funcții virtuale + moștenire

## 14.4 Clase derivate. Moștenire. Funcții virtuale (pp. 108–133)

### Moștenirea (inheritance):
Crearea unei **clase derivate** (subclasă) dintr-o **clasă de bază** (superclasă). Clasa derivată moștenește atributele și metodele clasei de bază.

```cpp
class Animal {
protected:
  char nume[30];
public:
  Animal(const char* n) { strcpy(nume, n); }
  virtual void sunet() { cout << "Sunet generic" << endl; }
  void afisare() { cout << "Animal: " << nume << endl; }
};

class Caine : public Animal {
public:
  Caine(const char* n) : Animal(n) {}      // apel constructor baza
  void sunet() override {                   // suprascriere metodă
    cout << "Ham-ham!" << endl;
  }
};
```

**Tipuri de moștenire:**
- **`public`** — public din baza → public în derivată; protected → protected
- **`protected`** — public și protected din baza → protected în derivată
- **`private`** — public și protected din baza → private în derivată

### Funcții virtuale:
Permit **legarea dinamică** (late binding) — decizia ce funcție se apelează se ia la **execuție**, nu la compilare.

```cpp
Animal *a = new Caine("Rex");
a->sunet();  // Cu virtual: Ham-ham! / Fără virtual: Sunet generic
```

**Reguli:**
- Declarate cu cuvântul cheie `virtual` în clasa de baza
- Redefinite în clasele derivate (optional `override` în C++11)
- Apelate prin pointer sau referință la clasa de baza

### Funcții virtuale pure și clase abstracte:
```cpp
class Forma {
public:
  virtual double arie() = 0;   // funcție virtuală pură
  virtual double perimetru() = 0;
};
// Forma este clasă abstractă - NU se pot crea instanțe direct
```
O clasă cu cel puțin o funcție virtuală pură = **clasă abstractă**. Obligă clasele derivate să implementeze funcțiile respective.

```cpp
class Cerc : public Forma {
  double r;
public:
  Cerc(double raza) : r(raza) {}
  double arie() override { return 3.14159 * r * r; }
  double perimetru() override { return 2 * 3.14159 * r; }
};
```

### Destructori virtuali:
Când se lucrează cu pointeri la clasa de baza care pointează obiecte derivate, destructorul trebuie declarat virtual pentru a asigura eliberarea corectă a memoriei:
```cpp
virtual ~Animal() {}
```

### Moștenire multiplă:
```cpp
class C : public A, public B { ... };
```
O clasă poate moșteni din mai multe clase de baza simultan.

---

*Rezumat realizat pe baza paginilor exacte cerute în bibliografie pentru examenul de licență Informatică Economică, ASE București 2025–2026.*
