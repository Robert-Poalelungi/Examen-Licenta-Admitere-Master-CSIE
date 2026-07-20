# 📚 REZUMAT TEORETIC — Examen Master CSIE3 (Informatică Economică)
> Extras complet din paginile cerute în bibliografie.  
> Programe: IE cercetare · Baze de date · E-Business · SIMRPE · TIID

---

## CUPRINS
1. [Baze de date relaționale](#1-baze-de-date-rela%C8%9Bionale) — [1] pp. 103–122, 129–131, 144–186, 197–201
2. [Programarea în SQL](#2-programarea-în-sql) — [2] pp. 101–171
3. [Programarea în PL/SQL](#3-programarea-în-plsql) — [3] pp. 9–52, 53–77, 83–102, 103–128
4. [Programarea în C](#4-programarea-în-c) — [4] pp. 13–14, 16–28, 30–46, 48–58, 60–74, 76–88, 90–102, 118–135, 184–196
5. [Programare orientată obiect în C++](#5-programare-orientat%C4%83-obiect-în-c) — [5] pp. 11–27, 28–29, 33–35, 44–45, 52–85, 108–123, 134–161

---

> **Notă față de rezumatul de licență:** CSIE3 are intervale de pagini diferite și secțiuni **noi**: excepțiile PL/SQL (pp. 83–102), funcții C fără recursive/variadic (pp. 90–102), structuri C fără liste lungi (pp. 118–135), plus pentru C++: masive de obiecte (pp. 28–29), funcții prietene `friend` (pp. 44–45) și fluxuri I/O (pp. 134–161).

---


---

> **Acest ghid combină:** explicații detaliate cu analogii din viața reală + conținutul complet din manuale (cu referințe de pagini).


# 1. BAZE DE DATE RELAȚIONALE


## 🟢 Ghid pentru înțelegere — Analogii și explicații detaliate


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


---

## 📖 Conținut complet din manual


**Sursă: [1] Lungu — Tratat de baze de date, pp. 103–122, 129–131, 144–186, 197–201**

## 1.1 Modelul relațional — structura datelor (pp. 103–122)

Modelul relațional (E.F. Codd, 1970) se bazează pe teoria matematică a algebrei relaționale și calculului cu predicate. Are trei componente:

### a) Structura relațională
**Domeniu** = ansamblu de valori caracterizat printr-un nume. Definit explicit (enumerare) sau implicit (proprietăți).

**Relație** = subansamblu al produsului cartezian al mai multor domenii, cu un **nume** și tupluri cu semnificație. Reprezentare: **tabelul bidimensional** (linii = tupluri, coloane = domenii/atribute).

**Atribut** = coloana relației, cu nume și domeniu de valori.

**Schema relației R** = `R(A₁:D₁, A₂:D₂, ..., Aₙ:Dₙ)` — atributele și domeniile lor.
- **Grad** = numărul de atribute
- **Cardinalitate** = numărul de tupluri

**Cheie primară** = mulțimea minimă de atribute prin care se identifică unic orice tuplu. Nu poate fi NULL. Proprietăți: **unicitate** și **minimalitate**.

**Cheie externă (Foreign Key)** = atribut (sau grup) al unei relații care este cheie primară în altă relație. Asigură legăturile dintre relații.

### b) Operatorii relației
**Algebra relațională** — operează pe relații și returnează relații:

**Operații pe mulțimi** (relațiile trebuie să aibă aceeași schemă):
- **Reuniunea** `R₁ ∪ R₂` — tupluri din R₁ sau R₂ (fără duplicate)
- **Diferența** `R₁ − R₂` — tupluri din R₁ care nu sunt în R₂
- **Intersecția** `R₁ ∩ R₂` — tupluri comune
- **Produsul cartezian** `R₁ × R₂` — toate combinațiile de tupluri

**Operații relaționale:**
- **Selecția** `σ_cond(R)` — extrage tuplurile care satisfac condiția
- **Proiecția** `π_{A1,A2,...}(R)` — extrage coloanele specificate; elimină duplicate
- **Joncțiunea (JOIN)** `R₁ ⋈ R₂` — combină tupluri pe baza unui predicat de egalitate

**Tipuri de joncțiune:**
- **Joncțiunea naturală** — pe atribute cu același nume; rezultatul conține fiecare atribut comun o singură dată
- **Joncțiunea externă stânga (LEFT JOIN)** — toate tuplurile din R₁, completate cu NULL dacă nu au corespondent în R₂
- **Joncțiunea externă dreapta (RIGHT JOIN)** — toate tuplurile din R₂
- **Joncțiunea externă completă (FULL JOIN)** — tuplurile din ambele relații
- **Semijoncțiunea** — conservă atributele unei singure relații; rezultat identic cu proiecția pe atributele lui R₁ a joncțiunii

**Calculul relațional** = limbaj neprocedural (declarativ) bazat pe logica predicatelor. Utilizatorul specifică **ce** date dorește, nu **cum** să le obțină.

### c) Restricții de integritate (pp. 103–122, 129–131)

**Integritatea entității** — niciun atribut din cheia primară nu poate lua valoarea NULL.

**Integritatea referențială** — valorile cheii externe trebuie să existe în relația referită sau să fie NULL. Asigură coerența legăturilor între relații.

**Restricții de domeniu** — valorile unui atribut trebuie să aparțină domeniului definit.

**Restricții de unicitate** — valorile cheii candidate sunt unice în relație.

**Exemplificări în Oracle:**
```sql
CREATE TABLE angajati (
  id_ang     NUMBER PRIMARY KEY,
  nume       VARCHAR2(50) NOT NULL,
  salariu    NUMBER CHECK (salariu > 0),
  id_dep     NUMBER REFERENCES departamente(id_dep)
);
```

## 1.2 Realizarea bazelor de date relaționale (pp. 144–186, 197–201)

### Analiza statică — Diagrama Entitate-Asociere (pp. 144–163)

**Modelul Entitate-Asociere (EA / ER)** reprezintă structura conceptuală a datelor:

**Entitate** = obiect din lumea reală, identificabil și distinct (ex: Client, Produs).
**Atribut** = proprietate a entității (ex: nume, cod).
**Atribut-cheie** = atribut(e) care identifică unic entitatea.

**Asociere** = legătură semantică între entități. Caracterizată prin:
- **Grad** = numărul de entități participante (binară, unară, ternară)
- **Cardinalitate** = raportul numeric (1:1, 1:N, M:N)
- **Participare** = totală (obligatorie) sau parțială (opțională)

**Tipuri de cardinalitate:**
- **1:1** — o instanță din E1 asociată cu cel mult o instanță din E2 și reciproc
- **1:N** — o instanță din E1 asociată cu mai multe instanțe din E2, dar nu invers
- **M:N** — mai multe instanțe din E1 asociate cu mai multe instanțe din E2

**Asocieri unare** = o entitate se asociază cu ea însăși (ex: angajat conduce angajat).

**Entitate slabă** = entitate care nu are atribute-cheie proprii; identificată prin asocierea cu o altă entitate (entitate-proprietar). Cheie parțială + cheie proprietar = identificator complet.

**Dificultăți în modelarea asocierilor:**
- **Tranzitivitate** — pot exista legăturile indirecte; asocierile redundante complică modelul
- **Calificarea multiplă** — aceeași legătură poate fi calificată în mai multe moduri (ex: un angajat cu doi copii poate fi exprimat ca 1:N sau ca M:N)
- **Asocieri directe vs. indirecte** — important să nu se includă asocieri redundante care pot fi deduse tranzitiv

### Proiectarea structurii conceptuale (pp. 144–163)

Se construiește **diagrama EA** (notații Chen sau Oracle/IE):
- Entitățile = dreptunghiuri
- Atributele = elipse (atributele-cheie subliniate)
- Asocierile = romburi (Chen) sau linii cu notații (Oracle)

### Proiectarea logică (pp. 164–177)

Transformarea schemei EA în tabele relaționale:

| Tip asociere | Regulă de transformare |
|---|---|
| Entitate | → O tabelă cu atributele entității; cheia primară = atributul-cheie |
| Asociere 1:1 | → Cheie externă în una din tabele (de preferință cea cu participare totală) |
| Asociere 1:N | → Cheie externă în tabela de pe partea N |
| Asociere M:N | → Tabelă nouă (de legătură) cu cheile primare ale ambelor entități |
| Entitate slabă | → Cheie primară compusă din cheia parțială + cheia proprietarului |
| Asociere unară 1:N | → Cheie externă în aceeași tabelă (self-referință) |
| Asociere unară M:N | → Tabelă nouă de legătură |

### Proiectarea fizică (pp. 177–186)

Definirea structurii fizice de stocare:
- Alegerea tipurilor de date concrete (Oracle: `NUMBER`, `VARCHAR2`, `DATE`, etc.)
- Definirea indecșilor (pentru coloanele frecvent interogate sau joncționate)
- Definirea spațiilor de tabelă, parametrilor de stocare

### Normalizarea datelor (pp. 144–163, 197–201)

Normalizarea = proces iterativ de eliminare a redundanțelor și anomaliilor de actualizare, bazat pe **dependențe funcționale**.

**Dependența funcțională** X → Y: orice două tupluri cu același X au același Y (X determină funcțional Y).

**Dependența funcțională parțială** — Y depinde funcțional de o parte a cheii compuse (nu de întreaga cheie).

**Dependența funcțională tranzitivă** — X → Y → Z, unde Y nu este cheie candidat.

**Forme normale:**

**FN1 (Prima formă normală)**
- Toate valorile sunt **atomice** (indivizibile)
- Nu există atribute multivaluate sau compuse
- Nu există grupuri repetitive

**FN2 (A doua formă normală)**
- Este în FN1
- Orice atribut non-cheie depinde **funcțional de întreaga cheie primară** (nu doar de o parte a ei)
- Relevantă doar când cheia primară este compusă

**FN3 (A treia formă normală)**
- Este în FN2
- Nu există **dependențe tranzitive** — orice atribut non-cheie depinde direct de cheia primară, nu prin alt atribut non-cheie

**FNBC (Boyce-Codd)**
- Formă mai strictă decât FN3
- Orice **determinant** este cheie candidat

**Anomalii eliminate prin normalizare:**
- **Anomalie de inserare** — imposibilitatea de a insera date fără a include alte date
- **Anomalie de ștergere** — ștergerea unui tuplu duce la pierderea neintenționată de informații
- **Anomalie de actualizare** — modificarea unui fapt necesită actualizări redundante în mai multe locuri

**Exemplu normalizare:**
- **Nenormalizat:** `Comanda(nr_cmd, data, cod_client, nume_client, [cod_prod, den_prod, cant, pret])`
- **FN1** — eliminare atribute repetitive: `Comanda(nr_cmd, data, cod_client, nume_client)` + `LinieCmd(nr_cmd, cod_prod, den_prod, cant, pret)`
- **FN2** — eliminare dependențe parțiale: `Produs(cod_prod, den_prod, pret)` separat
- **FN3** — eliminare dependențe tranzitive: `Client(cod_client, nume_client)` separat

---


# 2. PROGRAMAREA ÎN SQL


## 🟢 Ghid pentru înțelegere — Analogii și explicații detaliate


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


---

## 📖 Conținut complet din manual


**Sursă: [2] Lungu — Baze de date Oracle. Limbajul SQL, pp. 101–171**

## 2.1 Actualizarea structurii bazei de date (DDL) — pp. 101–122

### CREATE TABLE
```sql
CREATE TABLE nume_tabel (
  col1 tip_data [DEFAULT val] [constrangeri_col],
  col2 tip_data [constrangeri_col],
  ...
  [CONSTRAINT constr_name constrangere_tabel]
);
```

**Tipuri de date Oracle:**
- `VARCHAR2(n)` — șir variabil, max n caractere (obligatoriu specificat)
- `CHAR(n)` — șir de lungime fixă (completat cu spații)
- `NUMBER(p,s)` — număr cu p cifre totale și s zecimale
- `DATE` — dată și oră (zi, lună, an, oră, minut, secundă)
- `TIMESTAMP` — dată și oră cu mai multă precizie
- `CLOB` — text lung (max 4GB); `BLOB` — date binare mari
- `BOOLEAN` — nu există în SQL Oracle (există doar în PL/SQL)

**Tipuri de constrângeri:**
| Constrângere | Descriere |
|---|---|
| `NOT NULL` | Câmpul nu poate fi NULL |
| `UNIQUE` | Valori unice (permite NULL, mai mulți NULL posibili) |
| `PRIMARY KEY` | NOT NULL + UNIQUE; max una per tabelă |
| `FOREIGN KEY` | Referință la cheia primară a altei tabele |
| `CHECK (cond)` | Verifică o condiție pentru fiecare rând |

**Constrângeri la nivel de coloană vs. tabelă:**
```sql
-- La nivel de coloană:
id NUMBER PRIMARY KEY,
id_dep NUMBER REFERENCES departamente(id_dep),

-- La nivel de tabelă (necesar pentru chei compuse):
CONSTRAINT pk_ang PRIMARY KEY (id_ang),
CONSTRAINT fk_dep FOREIGN KEY (id_dep) REFERENCES departamente(id_dep)
  ON DELETE CASCADE,  -- sau ON DELETE SET NULL
```

**Opțiunile ON DELETE:**
- `ON DELETE CASCADE` — la ștergerea înregistrării-părinte se șterg și copiii
- `ON DELETE SET NULL` — la ștergerea părintelui, cheia externă devine NULL

### ALTER TABLE
```sql
ALTER TABLE tabel ADD (col tip [constrangere]);         -- adaugă coloană
ALTER TABLE tabel MODIFY (col tip_nou [NOT NULL]);      -- modifică
ALTER TABLE tabel DROP COLUMN col;                     -- șterge coloana
ALTER TABLE tabel DROP (col1, col2);                   -- șterge mai multe
ALTER TABLE tabel RENAME COLUMN col_vechi TO col_nou;  -- redenumire
ALTER TABLE tabel ADD CONSTRAINT c_name c_type (...);  -- adaugă constrângere
ALTER TABLE tabel DROP CONSTRAINT c_name;              -- șterge constrângere
ALTER TABLE tabel DISABLE CONSTRAINT c_name;           -- dezactivează
ALTER TABLE tabel ENABLE CONSTRAINT c_name;            -- reactivează
```

### DROP TABLE
```sql
DROP TABLE tabel;
DROP TABLE tabel CASCADE CONSTRAINTS;  -- șterge și constrângerile referitoare la ea
```

### CREATE/DROP INDEX
```sql
CREATE [UNIQUE] INDEX idx_name ON tabel(col1 [ASC|DESC], col2, ...);
DROP INDEX idx_name;
```

### CREATE SEQUENCE
```sql
CREATE SEQUENCE seq_name
  [START WITH n]
  [INCREMENT BY n]
  [MAXVALUE n | NOMAXVALUE]
  [MINVALUE n | NOMINVALUE]
  [CYCLE | NOCYCLE]
  [CACHE n | NOCACHE];

-- Utilizare:
seq_name.NEXTVAL  -- obține și incrementează valoarea
seq_name.CURRVAL  -- valoarea curentă (după cel puțin un NEXTVAL)

-- Exemplu uzual:
INSERT INTO tabel (id, ...) VALUES (seq_name.NEXTVAL, ...);
```

### CREATE VIEW
```sql
CREATE [OR REPLACE] [FORCE] VIEW view_name [(alias1, alias2, ...)] AS
  SELECT ...
  FROM ...
  [WHERE ...]
  [WITH CHECK OPTION [CONSTRAINT c_name]]
  [WITH READ ONLY];
```
`WITH CHECK OPTION` — INSERT/UPDATE prin view nu pot produce rânduri invizibile prin view.
`WITH READ ONLY` — view-ul nu permite operații DML.

**Ștergere view:** `DROP VIEW view_name;`

### CREATE SYNONYM
```sql
CREATE [PUBLIC] SYNONYM sinonim FOR schema.obiect;
-- PUBLIC = accesibil tuturor utilizatorilor
```

## 2.2 Actualizarea datelor (DML) — pp. 123–126

### INSERT
```sql
-- Cu valori explicite:
INSERT INTO tabel [(col1, col2, ...)] VALUES (v1, v2, ...);

-- Din SELECT (fără VALUES):
INSERT INTO tabel [(col1, col2)]
  SELECT col1, col2 FROM alta_tabel [WHERE conditie];
```
Dacă lista de coloane lipsește, valorile trebuie date în ordinea definită în tabelă, pentru toate coloanele.

### UPDATE
```sql
UPDATE tabel
SET col1 = val1 [, col2 = val2, ...]
[WHERE conditie];
```
**ATENȚIE:** fără WHERE → se actualizează toate rândurile!

### DELETE
```sql
DELETE [FROM] tabel
[WHERE conditie];
```
**ATENȚIE:** fără WHERE → se șterg toate rândurile!

### TRUNCATE (DDL, nu DML)
```sql
TRUNCATE TABLE tabel;
```
Șterge toate rândurile mai rapid (nu se poate anula cu ROLLBACK; eliberează spațiul).

### Tranzacții
```sql
COMMIT;    -- confirmă toate modificările din tranzacția curentă
ROLLBACK;  -- anulează toate modificările
SAVEPOINT sp_name;            -- marchează un punct de restaurare
ROLLBACK TO SAVEPOINT sp_name; -- anulează până la acel punct
```

## 2.3 Interogarea datelor — SELECT (pp. 127–171)

### Sintaxa completă:
```sql
SELECT [DISTINCT | ALL] { * | col [alias], ... | expresie }
FROM tabel1 [alias1], tabel2 [alias2], ...
[WHERE conditie_filtrare]
[GROUP BY col1, col2, ...]
[HAVING conditie_grup]
[ORDER BY col [ASC|DESC], ... [NULLS FIRST|LAST]];
```

**Ordinea de execuție:** FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

### Filtrarea datelor (WHERE):
- **Comparatori:** `=`, `<>` (sau `!=`), `<`, `>`, `<=`, `>=`
- **BETWEEN val1 AND val2** — interval inclusiv
- **IN (v1, v2, ...)** — valoare dintr-o listă
- **LIKE 'pattern'** — `%` orice secvență, `_` exact un caracter; `ESCAPE 'c'` pentru literale
- **IS NULL / IS NOT NULL** — testarea NULL (nu `= NULL`!)
- **AND, OR, NOT** — operatori logici

### Funcții SQL:

**Funcții numerice:**
| Funcție | Descriere |
|---|---|
| `ROUND(n, d)` | Rotunjire la d zecimale |
| `TRUNC(n, d)` | Trunchiere la d zecimale |
| `MOD(n, m)` | Restul împărțirii n/m |
| `ABS(n)` | Valoarea absolută |
| `POWER(n, p)` | n la puterea p |
| `SQRT(n)` | Radical din n |
| `CEIL(n)` | Cel mai mic întreg ≥ n |
| `FLOOR(n)` | Cel mai mare întreg ≤ n |
| `SIGN(n)` | -1, 0 sau 1 |

**Funcții șir de caractere:**
| Funcție | Descriere |
|---|---|
| `UPPER(s)` | Convertire la majuscule |
| `LOWER(s)` | Convertire la minuscule |
| `INITCAP(s)` | Prima literă majusculă |
| `LENGTH(s)` | Lungimea șirului |
| `SUBSTR(s, p, n)` | Subșir de la poziția p, lungime n |
| `INSTR(s, sub, p, n)` | Poziția subșirului sub în s |
| `LTRIM(s, [set])` | Elimină caractere la stânga |
| `RTRIM(s, [set])` | Elimină caractere la dreapta |
| `TRIM([BOTH|LEADING|TRAILING] c FROM s)` | Elimină caractere din șir |
| `LPAD(s, n, c)` | Completare la stânga cu c până la lungimea n |
| `RPAD(s, n, c)` | Completare la dreapta |
| `REPLACE(s, a, b)` | Înlocuire a cu b în s |
| `s1 \|\| s2` sau `CONCAT(s1,s2)` | Concatenare |

**Funcții dată:**
| Funcție | Descriere |
|---|---|
| `SYSDATE` | Data și ora curentă (pseudo-coloană) |
| `ADD_MONTHS(d, n)` | Adaugă n luni la data d |
| `MONTHS_BETWEEN(d1, d2)` | Numărul de luni între d1 și d2 |
| `NEXT_DAY(d, 'zi')` | Ziua din săptămână următoare datei d |
| `LAST_DAY(d)` | Ultima zi a lunii datei d |
| `TO_DATE(str, 'format')` | Conversie șir → dată |
| `TO_CHAR(d, 'format')` | Conversie dată → șir |

Formate dată: `'DD/MM/YYYY'`, `'DD-MON-YYYY'`, `'HH24:MI:SS'`, etc.

**Funcții de conversie și condiție:**
| Funcție | Descriere |
|---|---|
| `TO_CHAR(n, 'format')` | Număr → șir formatat |
| `TO_NUMBER(s, ['format'])` | Șir → număr |
| `NVL(expr, val_default)` | Înlocuiește NULL cu val_default |
| `NVL2(expr, val_nn, val_n)` | val_nn dacă ≠ NULL, val_n dacă NULL |
| `NULLIF(a, b)` | NULL dacă a=b, altfel a |
| `COALESCE(e1, e2, ..., en)` | Prima valoare non-NULL |
| `DECODE(expr, v1,r1, v2,r2, ..., def)` | Comparație multiplă, similar CASE |

**CASE:**
```sql
-- CASE simplu:
CASE col WHEN 'A' THEN 'Excelent' WHEN 'B' THEN 'Bine' ELSE 'Altul' END

-- CASE căutat:
CASE WHEN salariu < 2000 THEN 'Mic'
     WHEN salariu < 5000 THEN 'Mediu'
     ELSE 'Mare' END
```

### Funcții de grup (agregare):
```sql
COUNT(*) | COUNT(DISTINCT col)  -- numără rânduri / valori distincte non-NULL
SUM(col)                        -- suma (ignoră NULL)
AVG(col)                        -- media (ignoră NULL)
MAX(col) | MIN(col)             -- maxim / minim
STDDEV(col) | VARIANCE(col)     -- deviație standard / varianță
```
**Regulă:** funcțiile de grup nu pot fi în WHERE; se folosește **HAVING**. Orice coloană din SELECT (în afara funcțiilor de grup) trebuie să apară în GROUP BY.

```sql
SELECT dep_id, AVG(salariu)
FROM angajati
WHERE dep_id IS NOT NULL
GROUP BY dep_id
HAVING AVG(salariu) > 3000
ORDER BY AVG(salariu) DESC;
```

### Joncțiuni (JOIN):
```sql
-- ANSI (recomandat):
SELECT t1.col, t2.col
FROM t1 [INNER] JOIN t2 ON t1.col = t2.col;      -- inner join
FROM t1 NATURAL JOIN t2;                          -- joncțiune naturală
FROM t1 JOIN t2 USING (col_comuna);               -- joncțiune cu USING
FROM t1 LEFT [OUTER] JOIN t2 ON ...;             -- joncțiune externă stânga
FROM t1 RIGHT [OUTER] JOIN t2 ON ...;            -- joncțiune externă dreapta
FROM t1 FULL [OUTER] JOIN t2 ON ...;             -- joncțiune externă completă
FROM t1 CROSS JOIN t2;                           -- produs cartezian

-- Sintaxă Oracle tradițională:
FROM t1, t2 WHERE t1.col = t2.col;               -- inner join
FROM t1, t2 WHERE t1.col = t2.col(+);            -- left join (t2 e "deficitară")
FROM t1, t2 WHERE t1.col(+) = t2.col;            -- right join
```

**Self-join** (joncțiune a tabelei cu ea însăși):
```sql
SELECT a.nume AS angajat, b.nume AS manager
FROM angajati a JOIN angajati b ON a.id_manager = b.id_ang;
```

### Subcereri (subqueries) — pp. 151–171:
```sql
-- Subcerere pe un singur rând (operatori: =, <>, <, >, <=, >=):
SELECT * FROM angajati
WHERE salariu = (SELECT MAX(salariu) FROM angajati);

-- Subcerere pe mai multe rânduri (operatori: IN, NOT IN, ANY, ALL):
SELECT * FROM angajati
WHERE dep_id IN (SELECT dep_id FROM departamente WHERE locatie = 'Cluj');

-- ANY: cel puțin una din valori satisface condiția
WHERE salariu > ANY (SELECT salariu FROM angajati WHERE dep_id = 10);

-- ALL: toate valorile satisfac condiția
WHERE salariu > ALL (SELECT salariu FROM angajati WHERE dep_id = 20);

-- Subcerere corelată (face referire la tabela exterioară):
SELECT a.* FROM angajati a
WHERE salariu > (SELECT AVG(salariu) FROM angajati WHERE dep_id = a.dep_id);

-- EXISTS / NOT EXISTS:
SELECT * FROM clienti c
WHERE EXISTS (SELECT 1 FROM comenzi WHERE id_client = c.id_client);
```

**Subcereri în clauza FROM (tabel derivat / inline view):**
```sql
SELECT dep_id, avg_sal
FROM (SELECT dep_id, AVG(salariu) avg_sal FROM angajati GROUP BY dep_id)
WHERE avg_sal > 3000;
```

---


# 3. PROGRAMAREA ÎN PL/SQL


## 🟢 Ghid pentru înțelegere — Analogii și explicații detaliate


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


---

## 📖 Conținut complet din manual


**Sursă: [3] Bâra et al. — Baze de date. Limbajul PL/SQL, pp. 9–52, 53–77, 83–102, 103–128**

## 3.1 Elemente de programare procedurală (pp. 9–52)

**PL/SQL** (Procedural Language Extension to SQL) = limbaj procedural structurat pe bloc, specific Oracle. Combină instrucțiunile SQL cu structuri de control procedurale.

### Structura unui bloc PL/SQL:
```plsql
[DECLARE
  -- declarații: variabile, cursori, excepții, tipuri]
BEGIN
  -- instrucțiunile executabile (obligatoriu)
[EXCEPTION
  -- tratarea erorilor]
END;
/
```

**Tipuri de blocuri:**
- **Anonime** — nu au nume, nu se stochează, nu pot fi apelate din alt bloc
- **Proceduri** — blocuri cu nume, stocate, apelabile
- **Funcții** — returnează o valoare
- **Declanșatori (triggers)** — asociate evenimentelor pe tabele

### Variabile și tipuri de date:

**Declarare:**
```plsql
DECLARE
  v_nume   VARCHAR2(30) := 'Ion';   -- inițializare
  v_sal    NUMBER(8,2);
  v_const  CONSTANT NUMBER := 3.14; -- constantă
  v_flag   BOOLEAN := TRUE;         -- tip Boolean (doar în PL/SQL)
```

**Tip `%TYPE`** — preia tipul unei coloane:
```plsql
v_salariu angajati.salariu%TYPE;
v_nume    angajati.nume%TYPE;
```

**Tip `%ROWTYPE`** — preia structura unui întreg rând:
```plsql
rec_ang angajati%ROWTYPE;
-- Acces: rec_ang.id, rec_ang.nume, rec_ang.salariu
```

**Tipuri RECORD:**
```plsql
TYPE t_angajat IS RECORD (
  id     NUMBER,
  nume   VARCHAR2(30),
  salariu NUMBER
);
v_ang t_angajat;
v_ang.id := 1; v_ang.nume := 'Popescu';
```

**Tipuri TABLE (colecții indexate):**
```plsql
TYPE t_salarii IS TABLE OF NUMBER INDEX BY BINARY_INTEGER;
v_sal t_salarii;
v_sal(1) := 2500; v_sal(2) := 3000;
```

### Structuri de control:

**IF-THEN-ELSIF-ELSE:**
```plsql
IF conditie1 THEN
  instructiuni;
ELSIF conditie2 THEN
  instructiuni;
ELSE
  instructiuni;
END IF;
```

**CASE:**
```plsql
-- CASE simplu:
CASE variabila
  WHEN val1 THEN instructiuni;
  WHEN val2 THEN instructiuni;
  ELSE instructiuni;
END CASE;

-- CASE căutat:
CASE
  WHEN conditie1 THEN instructiuni;
  WHEN conditie2 THEN instructiuni;
  ELSE instructiuni;
END CASE;
```

**LOOP (buclă simplă):**
```plsql
LOOP
  instructiuni;
  EXIT WHEN conditie;  -- sau: IF cond THEN EXIT; END IF;
END LOOP;
```

**WHILE:**
```plsql
WHILE conditie LOOP
  instructiuni;
END LOOP;
```

**FOR numeric:**
```plsql
FOR i IN [REVERSE] val_min..val_max LOOP
  instructiuni;  -- i este implicit BINARY_INTEGER, nu se declară
END LOOP;
```

### Instrucțiuni SQL în PL/SQL:
```plsql
-- SELECT INTO (exact 1 rând; altfel: NO_DATA_FOUND sau TOO_MANY_ROWS):
SELECT col1, col2 INTO v1, v2 FROM tabel WHERE conditie;
SELECT * INTO rec FROM tabel WHERE conditie;  -- cu %ROWTYPE

-- DML se folosesc direct:
INSERT INTO tabel VALUES (...);
UPDATE tabel SET col = val WHERE ...;
DELETE FROM tabel WHERE ...;

-- Tranzacții:
COMMIT; ROLLBACK; SAVEPOINT sp; ROLLBACK TO sp;
```

## 3.2 Mecanismul de cursor (pp. 53–77)

**Cursorul** = pointer asociat unei interogări SELECT, permite accesarea iterativă a rândurilor.

### Cursori impliciti
Creați automat de Oracle pentru fiecare DML sau SELECT INTO.

Atribute cursor implicit (prefixate cu `SQL`):
- `SQL%FOUND` — TRUE dacă ultima instrucțiune a afectat cel puțin un rând
- `SQL%NOTFOUND` — TRUE dacă niciun rând nu a fost afectat
- `SQL%ROWCOUNT` — numărul de rânduri afectate de ultima instrucțiune
- `SQL%ISOPEN` — întotdeauna FALSE pentru cursori impliciti

### Cursori expliciti
**Ciclul de viață: DECLARE → OPEN → FETCH → CLOSE**

```plsql
DECLARE
  CURSOR c_angajati IS
    SELECT id_ang, nume, salariu
    FROM angajati
    WHERE dep_id = 10
    ORDER BY salariu DESC;

  v_id    angajati.id_ang%TYPE;
  v_nume  angajati.nume%TYPE;
  v_sal   angajati.salariu%TYPE;
BEGIN
  OPEN c_angajati;                          -- deschide, execută interogarea
  LOOP
    FETCH c_angajati INTO v_id, v_nume, v_sal;  -- avansează la rândul următor
    EXIT WHEN c_angajati%NOTFOUND;          -- ieșire când nu mai sunt rânduri
    DBMS_OUTPUT.PUT_LINE(v_nume || ': ' || v_sal);
  END LOOP;
  CLOSE c_angajati;                         -- eliberează resurse
END;
/
```

**Atribute cursor explicit:**
- `c%FOUND` — TRUE dacă ultimul FETCH a returnat un rând
- `c%NOTFOUND` — TRUE dacă ultimul FETCH nu a returnat niciun rând
- `c%ROWCOUNT` — numărul de rânduri returnate până în prezent
- `c%ISOPEN` — TRUE dacă cursorul este deschis

### Cursor FOR LOOP (simplificat):
```plsql
FOR rec IN (SELECT id_ang, nume FROM angajati WHERE dep_id = 10) LOOP
  DBMS_OUTPUT.PUT_LINE(rec.id_ang || ' ' || rec.nume);
END LOOP;
-- OPEN, FETCH, CLOSE sunt implicite; rec e declarat automat de tip %ROWTYPE
```

Sau cu un cursor declarat:
```plsql
FOR rec IN c_angajati LOOP
  DBMS_OUTPUT.PUT_LINE(rec.nume);
END LOOP;
```

### Cursori cu parametri:
```plsql
CURSOR c_dep (p_dept NUMBER, p_sal NUMBER := 0) IS
  SELECT * FROM angajati WHERE dep_id = p_dept AND salariu > p_sal;

-- Utilizare:
OPEN c_dep(10, 2000);
-- sau în FOR:
FOR rec IN c_dep(10) LOOP ... END LOOP;
```

### Cursor FOR UPDATE:
Blochează rândurile pentru actualizare exclusivă:
```plsql
CURSOR c IS SELECT * FROM angajati WHERE dep_id = 10 FOR UPDATE [NOWAIT];
-- NOWAIT: ridică excepție dacă rândurile sunt deja blocate

-- Actualizare folosind cursorul:
UPDATE angajati SET salariu = salariu * 1.1 WHERE CURRENT OF c;
DELETE FROM angajati WHERE CURRENT OF c;
```

## 3.3 Tratarea excepțiilor (pp. 83–102)

**Excepția** = identificator PL/SQL asociat unei condiții anormale apărute la execuție. Invocarea ei termină blocul și întrerupe execuția normală.

**Tipuri de excepții:**

| Tip | Declarare | Declanșare | Tratare |
|---|---|---|---|
| **Predefinite** | Nu (Oracle le cunoaște) | Automat de Oracle | În EXCEPTION |
| **Non-predefinite** | Da (în DECLARE) | Automat de Oracle | În EXCEPTION |
| **Definite de utilizator** | Da (în DECLARE) | Manual cu RAISE | În EXCEPTION |

### Excepții predefinite Oracle:
| Excepție | Cod eroare | Descriere |
|---|---|---|
| `NO_DATA_FOUND` | ORA-01403 | SELECT INTO nu a returnat niciun rând |
| `TOO_MANY_ROWS` | ORA-01422 | SELECT INTO a returnat mai mult de un rând |
| `ZERO_DIVIDE` | ORA-01476 | Împărțire la zero |
| `INVALID_CURSOR` | ORA-01001 | Operație ilegală pe cursor (ex: FETCH pe cursor închis) |
| `CURSOR_ALREADY_OPEN` | ORA-06511 | OPEN pe cursor deja deschis |
| `VALUE_ERROR` | ORA-06502 | Eroare de conversie sau trunchiere |
| `DUP_VAL_ON_INDEX` | ORA-00001 | Violare constrângere de unicitate |
| `INVALID_NUMBER` | ORA-01722 | Conversie șir → număr eșuată |
| `ROWTYPE_MISMATCH` | ORA-06504 | Tipuri incompatibile la FETCH |
| `LOGIN_DENIED` | ORA-01017 | Autentificare refuzată |
| `NOT_LOGGED_ON` | ORA-01012 | Nu există conexiune la Oracle |
| `PROGRAM_ERROR` | ORA-06501 | Eroare internă PL/SQL |
| `STORAGE_ERROR` | ORA-06500 | Memorie insuficientă |
| `TIMEOUT_ON_RESOURCE` | ORA-00051 | Timeout la așteptarea resursei |

### Structura secțiunii EXCEPTION:
```plsql
EXCEPTION
  WHEN exceptie1 [OR exceptie2] THEN
    instructiuni;
  WHEN exceptie3 THEN
    instructiuni;
  WHEN OTHERS THEN      -- prinde orice excepție netratată; MEREU ultima
    DBMS_OUTPUT.PUT_LINE('Eroare: ' || SQLERRM);
    -- SQLCODE = codul numeric al erorii
    -- SQLERRM = mesajul de eroare
END;
```

### Excepții non-predefinite:
```plsql
DECLARE
  exc_viola_cheie EXCEPTION;
  PRAGMA EXCEPTION_INIT(exc_viola_cheie, -00001);  -- asociere cu codul ORA
BEGIN
  INSERT INTO ...;
EXCEPTION
  WHEN exc_viola_cheie THEN
    DBMS_OUTPUT.PUT_LINE('Cheie duplicată!');
END;
```

### Excepții definite de utilizator:
```plsql
DECLARE
  exc_stoc_zero EXCEPTION;
  v_stoc NUMBER;
BEGIN
  SELECT stoc INTO v_stoc FROM produse WHERE cod = 'P01';
  IF v_stoc = 0 THEN
    RAISE exc_stoc_zero;    -- declanșare manuală
  END IF;
EXCEPTION
  WHEN exc_stoc_zero THEN
    DBMS_OUTPUT.PUT_LINE('Stoc epuizat!');
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('Produs inexistent!');
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('Eroare neprevăzută: ' || SQLERRM);
END;
```

**RAISE_APPLICATION_ERROR** — generează o eroare cu cod personalizat:
```plsql
RAISE_APPLICATION_ERROR(-20001, 'Mesaj de eroare personalizat');
-- Codul trebuie să fie între -20000 și -20999
```

### Propagarea excepțiilor:
- O excepție declanșată în secțiunea BEGIN se caută în secțiunea EXCEPTION a aceluiași bloc
- Dacă nu e găsită, se propagă în blocul exterior, și tot așa
- Dacă niciun bloc nu o tratează, apare eroare în mediul apelant
- Dacă un sub-bloc tratează excepția, execuția continuă în blocul exterior după `END` sub-blocului

## 3.4 Gestiunea subprogramelor — Proceduri și funcții (pp. 103–128)

### Proceduri stocate:
```plsql
CREATE [OR REPLACE] PROCEDURE nume_proc
  (param1 [IN] tip,
   param2 OUT tip,
   param3 IN OUT tip)
IS  -- sau AS
  -- declarații locale
BEGIN
  -- corpul procedurii
EXCEPTION
  -- tratare erori (opțional)
END [nume_proc];
/
```

**Moduri de transfer parametri:**
| Mod | Direcție | Poate fi citit? | Poate fi modificat? | Valoare implicită |
|---|---|---|---|---|
| `IN` | Intrare | Da | Nu | Da (cu DEFAULT) |
| `OUT` | Ieșire | Nu (inițial) | Da | Nu |
| `IN OUT` | Ambele | Da | Da | Nu |

```plsql
-- Apelul unei proceduri:
EXEC(UTE) nume_proc(arg1, arg2, arg3);       -- în SQL*Plus
-- sau:
BEGIN
  nume_proc(arg1, arg2, arg3);
  -- Parametri named notation:
  nume_proc(p_sal => 2000, p_dep => 10);
END;
```

**Vizualizare cod sursă:**
```sql
SELECT text FROM user_source WHERE name = 'NUME_PROC' AND type = 'PROCEDURE';
DESCRIBE nume_proc;  -- afișează parametrii
```

**Ștergere:** `DROP PROCEDURE nume_proc;`

### Funcții stocate:
```plsql
CREATE [OR REPLACE] FUNCTION nume_func
  (param1 [IN] tip, ...)
RETURN tip_returnat
IS
  -- declarații locale
BEGIN
  -- corpul funcției
  RETURN valoare;    -- obligatoriu cel puțin o instrucțiune RETURN
EXCEPTION
  -- tratare erori (opțional)
END [nume_func];
/
```

**Reguli:** funcțiile returnează **un singur** valor; pot fi apelate din SQL dacă nu conțin DML (INSERT/UPDATE/DELETE/MERGE).

```plsql
-- Apel din PL/SQL:
DECLARE v_rez NUMBER;
BEGIN
  v_rez := nume_func(arg1);
  DBMS_OUTPUT.PUT_LINE(v_rez);
END;

-- Apel din SQL (dacă nu conține DML):
SELECT nume_func(col) FROM tabel;
```

**Ștergere:** `DROP FUNCTION nume_func;`

### Subprograme locale:
Proceduri și funcții declarate în secțiunea DECLARE a unui bloc PL/SQL:
```plsql
DECLARE
  PROCEDURE p_locala (x NUMBER) IS
  BEGIN ... END;
  
  FUNCTION f_locala (x NUMBER) RETURN NUMBER IS
  BEGIN ... RETURN x*2; END;
BEGIN
  p_locala(5);
  DBMS_OUTPUT.PUT_LINE(f_locala(3));
END;
```

### DESCRIBE și vizualizare:
```sql
DESCRIBE procedura;          -- parametrii procedurii/funcției
SHOW ERRORS;                 -- erorile de compilare
SELECT * FROM user_errors;   -- erorile detaliate
SELECT * FROM user_objects WHERE object_type IN ('PROCEDURE','FUNCTION');
```

---


# 4. PROGRAMAREA ÎN C


## 🟢 Ghid pentru înțelegere — Analogii și explicații detaliate


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


---

## 📖 Conținut complet din manual


**Sursă: [4] Smeureanu, Dârdală — Programarea în limbajul C/C++**

## 4.1 Operații de intrare/ieșire — introducere (pp. 13–14)

Header-ul standard pentru I/O: `#include <stdio.h>`

**Fișierul standard:**
- **`stdin`** — dispozitivul de intrare standard (tastatura)
- **`stdout`** — dispozitivul de ieșire standard (ecranul)
- **`stderr`** — dispozitivul de ieșire pentru erori

**Funcțiile principale:** `printf`, `scanf`, `getchar`, `putchar`, `gets`, `puts` (detaliate la cap. 10 și 4.9).

---

## 4.2 Tipuri de date și clase de memorie (pp. 16–28)

### Tipuri fundamentale:
| Tip | Lungime | Domeniu |
|---|---|---|
| `char` | 1 octet | −128...127 (signed) / 0...255 (unsigned) |
| `int` | 2 sau 4 octeți | −32768...32767 / −2147483648...2147483647 |
| `short int` | 2 octeți | −32768...32767 |
| `long int` | 4 octeți | −2147483648...2147483647 |
| `unsigned int` | 2 sau 4 octeți | 0...65535 / 0...4294967295 |
| `float` | 4 octeți | 1.2E−38...3.4E+38 |
| `double` | 8 octeți | 2.2E−308...1.8E+308 |
| `long double` | 10 octeți | 3.4E−4932...1.2E+4932 |

**Modificatori:** `unsigned`, `signed`, `long`, `short` — modifică dimensiunea sau interpretarea.

**Specificatorul de format:** `%d`, `%u`, `%o`, `%x`, `%f`, `%e`, `%g`, `%c`, `%s`, `%p`

**Clase de memorie:**
- **`auto`** (implicit local) — pe stivă, durată de viață = blocul curent
- **`register`** — solicită stocare în registru CPU; nu se poate lua adresa
- **`static`** — durată de viață permanentă; inițializat o singură dată; dacă e global, vizibil doar în fișier
- **`extern`** — declară o variabilă definită în alt fișier; nu alocă memorie

---

## 4.3 Operatori și expresii (pp. 30–46)

Prioritatea scade de la clasa I la clasa XV. Evaluare stânga→dreapta, excepție: unari, condițional, atribuire (dreapta→stânga).

**Clase principale:**
- **Clasa I:** `[]`, `()`, `.`, `->` (indexare, apel funcție, calificare structuri)
- **Clasa II (unari):** `!`, `~`, `++`, `--`, `-`, `+`, `*` (deref), `&` (adresă), `(tip)`, `sizeof`
- **Clasa III:** `*`, `/`, `%` (multiplicativi)
- **Clasa IV:** `+`, `-` (aditivi)
- **Clasa V:** `<<`, `>>` (deplasare biți)
- **Clasa VI:** `<`, `>`, `<=`, `>=` (relație)
- **Clasa VII:** `==`, `!=` (egalitate)
- **Clasa VIII:** `&` (AND biți)
- **Clasa IX:** `^` (XOR biți)
- **Clasa X:** `|` (OR biți)
- **Clasa XI:** `&&` (AND logic)
- **Clasa XII:** `||` (OR logic)
- **Clasa XIII:** `? :` (condițional ternar)
- **Clasa XIV:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=` (atribuire)
- **Clasa XV:** `,` (virgulă)

**Conversii implicite:** `char/short → int → long → float → double → long double`
**Conversii explicite (cast):** `(tip) expresie`

---

## 4.4 Instrucțiuni de bază (pp. 48–58)

**Structura liniară:** expresii, atribuiri, apeluri de funcții, instrucțiunea vidă (`;`).

**Structura alternativă:**
```c
if (expr) instr;
if (expr) instr1; else instr2;
if (e1) i1; else if (e2) i2; ... else iN;
```
`else` se asociază cu ultimul `if` activ. Acoladele `{}` modifică asocierea.

**Structuri repetitive:**
```c
while (expr) instr;                           // condiționată anterior
do { instr; } while (expr);                  // condiționată posterior
for (init; cond; incr) instr;                // cu contor
```

**Selecția multiplă:**
```c
switch (expr_intreaga) {
  case v1: instr; break;
  case v2: instr; break;
  default: instr;
}
```
Fără `break` → fall-through (execuție continuă în case-ul următor).

**Alte instrucțiuni:** `break` (ieșire din buclă/switch), `continue` (iterația următoare), `return [expr]` (ieșire din funcție), `goto eticheta` (salt necondiționat, evitat).

---

## 4.5 Masive și pointeri (pp. 60–74)

**Pointerul** = variabilă care conține adresa altei variabile.
```c
int x = 7, *px = &x;  // px conține adresa lui x
*px = 5;              // echivalent cu x = 5
```
Operatori: `&` (adresă), `*` (dereferențiere).

**Aritmetica de pointeri:** `p+n` avansează cu `n*sizeof(tip)` octeți.

**Masive unidimensionale:**
```c
int a[10];           // indexul: 0..9
a[i] ≡ *(a + i)     // relația vector-pointer
```

**Masive multidimensionale:** stocate pe linii (row-major).
```c
int m[3][4];   // m[i][j] ≡ *(*(m+i)+j)
```

**Masive de pointeri și pointeri la masive:**
```c
char *siruri[5];       // masiv de 5 pointeri la char
int (*pa)[4];          // pointer la masiv de 4 întregi
```

**Alocare dinamică:**
```c
int *p = (int*) malloc(n * sizeof(int));  // C
free(p);

int *p = new int[n];  // C++
delete[] p;
```

---

## 4.6 Șiruri de caractere (pp. 76–88)

Șir de caractere = masiv de `char` terminat cu `'\0'`.
```c
char s1[] = "salut";       // 6 octeți: s,a,l,u,t,\0
char *ps  = "buna ziua";   // pointer la constantă (nemodificabilă)
```

**Funcții I/O:** `printf("%s", s)`, `scanf("%s", s)`, `gets(s)` (nesigur), `puts(s)`, `getchar()`, `putchar(c)`.

**Funcții `<string.h>`:**

| Funcție | Descriere |
|---|---|
| `strlen(s)` | Lungimea șirului (fără `\0`) |
| `strcpy(d, s)` | Copiere s în d |
| `strncpy(d, s, n)` | Copiere max n caractere |
| `strcat(d, s)` | Concatenare s la d |
| `strncat(d, s, n)` | Concatenare max n caractere |
| `strcmp(s1, s2)` | Comparare (0=egal, <0=s1<s2, >0=s1>s2) |
| `strncmp(s1, s2, n)` | Comparare max n caractere |
| `strchr(s, c)` | Pointer la prima apariție a lui c în s |
| `strstr(s, sub)` | Pointer la prima apariție a subșirului |
| `strtok(s, delim)` | Tokenizare |
| `sprintf(str, fmt, ...)` | Scriere formatată în șir |
| `sscanf(str, fmt, ...)` | Citire formatată din șir |

**Funcții `<ctype.h>`:** `isalpha`, `isdigit`, `isupper`, `islower`, `isspace`, `toupper`, `tolower`.

---

## 4.7 Funcții și clase de funcții (pp. 90–102)

**Definire:**
```c
tip_retur nume (tip1 p1, tip2 p2, ...) {
  // corp
  return expresie;  // dacă tip_retur ≠ void
}
```

**Prototip (declarare):** necesar dacă funcția e definită după locul de apel.
```c
int suma(int a, int b);   // prototip
```

**Transfer parametri exclusiv prin valoare** — funcția primește copii. Pentru a modifica variabile externe se transmite adresa (pointer):
```c
void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }
swap(&x, &y);
```

**Clase de funcții:**
- **Externe (globale)** — vizibile în toate fișierele programului (implicit)
- **Statice** — vizibilitate limitată la fișierul de definire (`static tip f()`)
- **Inline** — corpul substituie apelul la compilare (`inline tip f()`) — mai ales C++
- **Recursive** — se apelează pe ele însele; necesită caz de bază + caz recursiv

```c
// Funcție recursivă:
long factorial(int n) {
  if (n <= 1) return 1;
  return n * factorial(n-1);
}
```

**Funcții cu parametri impliciți (C++):**
```cpp
void afisare(int n, int baza = 10);  // al doilea parametru are valoare implicită
afisare(255);       // baza = 10
afisare(255, 16);   // baza = 16
```

---

## 4.8 Structuri și uniuni (pp. 118–135)

### Structuri (`struct`):
Tip de date compus din câmpuri de tipuri (posibil) diferite.

```c
struct angajat {
  int   marca;
  char  nume[30];
  float salariu;
};

struct angajat a1, a2;
a1.marca = 100;
strcpy(a1.nume, "Popescu");

// Pointer la structură:
struct angajat *pa = &a1;
pa->salariu = 2500.0;   // echivalent: (*pa).salariu = 2500.0;
```

**Inițializare:** `struct angajat a = {100, "Ion", 2000.0};`

**Structuri imbricate:**
```c
struct adresa { char oras[30]; int cod_postal; };
struct persoana { char nume[30]; struct adresa adr; };
p.adr.cod_postal = 10001;
```

**`typedef`** — definire tip sinonim:
```c
typedef struct angajat Angajat;    // Angajat a; în loc de struct angajat a;
typedef struct {
  int marca; char nume[30];
} Muncitor;                        // Muncitor m;
```

**Pasare structuri:** prin valoare (copie completă) sau prin pointer (eficient, modificabil).

### Uniuni (`union`):
Toți membrii partajează aceeași zonă de memorie. Dimensiunea = dimensiunea celui mai mare câmp.

```c
union valoare {
  int intreg;
  float real;
  char c;
};
union valoare v;
v.intreg = 5;     // zona conține un întreg
v.real = 3.14;    // zona conține un real (SUPRASCRIE întregul!)
```
**La un moment dat, valid doar ultimul câmp scris.**

### Câmpuri de biți:
```c
struct flags {
  unsigned int citire  : 1;  // 1 bit
  unsigned int scriere : 1;
  unsigned int exec    : 1;
};
```

---

## 4.9 Operații de intrare/ieșire în C (pp. 184–196)

Header: `#include <stdio.h>`

### I/O standard (consolă):

**`printf` și `scanf`** — funcții principale de I/O formatat.
```c
printf("format", arg1, arg2, ...);  // afișare formatată
scanf("format", &var1, &var2, ...); // citire formatată
```
Specificatori de format: `%d`, `%i`, `%u`, `%o`, `%x`, `%f`, `%e`, `%g`, `%c`, `%s`, `%p`.

### I/O pe fișiere:

**Tipul `FILE`** — structură ce reprezintă un fișier deschis.

```c
FILE *fp;

// Deschidere fișier:
fp = fopen("fisier.txt", "r");   // citire
fp = fopen("fisier.txt", "w");   // scriere (suprascrie)
fp = fopen("fisier.txt", "a");   // adăugare la sfârșit
fp = fopen("fisier.txt", "r+");  // citire+scriere
fp = fopen("fisier.bin", "rb");  // citire binar
// Returnează NULL dacă nu reușește!

// Verificare:
if (fp == NULL) { perror("Eroare"); exit(1); }

// Închidere (obligatorie!):
fclose(fp);
```

**Moduri de deschidere:** `"r"`, `"w"`, `"a"`, `"r+"`, `"w+"`, `"a+"`, + `"b"` pentru binar.

**I/O formatat pe fișier:**
```c
fprintf(fp, "format", arg1, ...);     // scriere formatată în fișier
fscanf(fp, "format", &var1, ...);     // citire formatată din fișier
```

**I/O caracter cu caracter:**
```c
int c = fgetc(fp);     // citire caracter (returnează EOF la sfârșit)
fputc(c, fp);          // scriere caracter
```

**I/O pe șiruri:**
```c
char *fgets(char *s, int n, FILE *fp);  // citire linie max n-1 caractere
fputs(const char *s, FILE *fp);         // scriere șir (fără newline automat)
```

**I/O binar (blocuri):**
```c
size_t fread(void *buf, size_t size, size_t n, FILE *fp);
size_t fwrite(const void *buf, size_t size, size_t n, FILE *fp);
// size = dimensiunea unui element, n = numărul de elemente
```

**Poziționare în fișier:**
```c
fseek(fp, offset, origine);
// origine: SEEK_SET (față de început), SEEK_CUR (față de curent), SEEK_END (față de sfârșit)

long pos = ftell(fp);   // returnează poziția curentă
rewind(fp);             // revine la început (echivalent fseek(fp, 0, SEEK_SET))
```

**Testare stare fișier:**
```c
feof(fp)    // TRUE dacă s-a atins sfârșitul fișierului
ferror(fp)  // TRUE dacă a apărut o eroare
```

---


# 5. PROGRAMARE ORIENTATĂ OBIECT ÎN C++


## 🟢 Ghid pentru înțelegere — Analogii și explicații detaliate


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


---

## 📖 Conținut complet din manual


**Sursă: [5] Smeureanu, Dârdală — Programarea orientată obiect în C++**

## 5.1 Clase și obiecte (pp. 11–27)

**Clasa** = tip de date care încapsulează **date** (atribute) și **metode** (funcții membre). Implementează un concept abstract.

```cpp
class Persoana {
private:
  int varsta;          // accesibil doar din interiorul clasei
protected:
  float salariu;       // accesibil din clasă și clase derivate
public:
  char nume[20];       // accesibil oriunde

  // Constructor (cu valori implicite):
  Persoana(const char* n = "Anonim", int v = 0, float s = 0.0) {
    strcpy(nume, n); varsta = v; salariu = s;
  }

  // Destructor:
  ~Persoana() { }

  // Metodă inline (definită în clasă):
  int spuneVarsta() const { return varsta; }

  // Metodă declarată în clasă, definită afară:
  char* spuneNume();
};

// Definire în afara clasei:
char* Persoana::spuneNume() { return nume; }
```

**Specificatori de acces:**
- `private` — implicit pentru `class`; accesibil doar din interiorul clasei
- `protected` — accesibil din clasă și clase derivate
- `public` — accesibil de oriunde

**Diferența `class` vs. `struct`:** implicit `private` (class) vs. implicit `public` (struct).

### Crearea și utilizarea obiectelor:
```cpp
Persoana p1("Ion", 30, 2500.0);   // constructor explicit
Persoana p2;                       // constructor implicit
Persoana *pp = new Persoana("Ana", 25, 3000.0);  // alocare dinamică

p1.spuneVarsta();        // apel metodă prin obiect
pp->spuneNume();         // apel prin pointer
delete pp;               // eliberare + apel destructor
```

### Constructori:
- **Constructor implicit** — fără parametri (sau toți cu valori implicite)
- **Constructor de copiere** — inițializează din alt obiect: `Persoana(const Persoana& p);`
  - Apelat la: inițializare cu alt obiect, transfer prin valoare, returnare prin valoare
  - Dacă nu e definit, compilatorul generează unul (copiere bit cu bit — superficială!)
- **Supraîncărcarea** constructorilor — mai mulți constructori cu parametri diferiți

### Destructori:
- Un singur destructor, fără parametri și fără tip de retur: `~NumeClasa()`
- Apelat automat la ieșirea din scope sau la `delete`
- Dacă clasa alocă memorie dinamic, **trebuie** definit destructorul pentru a elibera

### Funcții membre statice și date statice:
```cpp
class Contor {
  static int nr;          // dată statică: comună tuturor instanțelor
public:
  Contor() { nr++; }
  static int getNr() { return nr; }  // funcție statică: fără this
};
int Contor::nr = 0;        // definiție obligatorie în afara clasei

Contor::getNr();            // apel fără obiect
```

### Funcții `inline`:
Funcțiile definite în corpul clasei sunt automat `inline`. Compilatorul substituie apelul cu corpul funcției (elimina overhead-ul apelului, pentru funcții scurte):
```cpp
inline int max(int a, int b) { return a > b ? a : b; }
```

## 5.2 Masive de obiecte (pp. 28–29)

O clasă poate fi folosită ca tip pentru declararea masivelor:

```cpp
Persoana grup[] = {
  Persoana("Adam D.", 35, 75000.0),
  Persoana("Bucur I.", 25, 95000.0),
  Persoana(),                          // constructor implicit
  Persoana("Costea A.", 29, 97000.0)
};
// Dimensiunea dedusă automat (4 elemente)
```

**Alocare dinamică a masivului:**
```cpp
Persoana *echipa = new Persoana[n];   // apelează constructorul implicit pentru fiecare
// Acces:
echipa[i].spuneNume();
(echipa + i)->spuneVarsta();
// Eliberare (obligatoriu delete[]):
delete[] echipa;
```

**Pointer la obiect vs. pointer la masiv de obiecte:**
- `Persoana *p = &obiect;` — pointer la un singur obiect
- `Persoana *p = new Persoana[n];` — pointer la primul element al masivului

**Constructorul** clasei e apelat **repetat**, pentru fiecare element al masivului.

## 5.3 Clase și funcții prietene — `friend` (pp. 44–45)

Mecanismul `friend` acordă acces la membrii **private** și **protected** unor funcții sau clase externe.

### Funcție prietenă:
```cpp
class Persoana {
  int varsta;
  friend int spune_prieten(Persoana& p);  // declarare în clasă
public:
  Persoana(int v = 0) { varsta = v; }
};

// Definire externă (fără ::):
int spune_prieten(Persoana& p) {
  return p.varsta;   // accesează membrul privat!
}
```

### Metodă a altei clase declarată prietenă:
```cpp
class Persoana;   // declarație anticipată (forward declaration)
class Medic {
public:
  int consult(Persoana& p);  // prototip
};

class Persoana {
  int varsta;
  friend int Medic::consult(Persoana& p);   // doar metoda consult
  // sau: friend class Medic;               // toată clasa Medic
public:
  Persoana(int v = 20) { varsta = v; }
};

int Medic::consult(Persoana& p) { return p.varsta; }
```

**Reguli `friend`:**
- Declararea `friend` se face în clasa care **acordă** accesul, nu în cea care beneficiază
- `friend` nu se moștenește
- `friend` nu este tranzitivă (A prieten cu B, B prieten cu C ≠ A prieten cu C)
- Funcțiile friend rămân **externe** clasei; nu au `this`; se apelează normal, cu obiectul ca parametru

## 5.4 Supraîncărcarea operatorilor (pp. 52–85)

### Supraîncărcarea funcțiilor:
Aceeași denumire, parametri diferiți (tip și/sau număr):
```cpp
int suma(int a, int b) { return a + b; }
double suma(double a, double b) { return a + b; }
int suma(int a, int b, int c) { return a + b + c; }
// Compilatorul alege versiunea potrivită după tipul argumentelor
```
Nu se poate supraîncărca numai prin tipul de retur.

### Supraîncărcarea operatorilor:
Permite folosirea operatorilor standard cu tipuri definite de utilizator.

**Sintaxă:**
```cpp
// Ca metodă a clasei:
TipRetur operator@(parametri);

// Ca funcție externă (prietenă):
friend TipRetur operator@(TipStanga, TipDreapta);
```

**Exemplu — clasa Complex:**
```cpp
class Complex {
public:
  double re, im;
  Complex(double r = 0, double i = 0) : re(r), im(i) {}

  // Operatori binari ca metode:
  Complex operator+(const Complex& c) const {
    return Complex(re + c.re, im + c.im);
  }
  Complex operator-(const Complex& c) const {
    return Complex(re - c.re, im - c.im);
  }
  Complex operator*(const Complex& c) const {
    return Complex(re*c.re - im*c.im, re*c.im + im*c.re);
  }

  // Operatori de comparație:
  bool operator==(const Complex& c) const {
    return re == c.re && im == c.im;
  }

  // Operatori de atribuire combinată:
  Complex& operator+=(const Complex& c) {
    re += c.re; im += c.im; return *this;
  }

  // Operator unar minus:
  Complex operator-() const { return Complex(-re, -im); }

  // Operator de indexare (dacă are sens):
  // double& operator[](int i) { return i == 0 ? re : im; }

  // Operatori de I/O (funcții prietene):
  friend ostream& operator<<(ostream& os, const Complex& c);
  friend istream& operator>>(istream& is, Complex& c);
};

ostream& operator<<(ostream& os, const Complex& c) {
  os << c.re;
  if (c.im >= 0) os << "+" << c.im << "i";
  else os << c.im << "i";
  return os;   // returnează referința pentru înlănțuire: cout << c1 << c2
}
```

**Operatori supraîncărcabili:** `+`, `-`, `*`, `/`, `%`, `++`, `--`, `=`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `[]`, `()`, `<<`, `>>`, `new`, `delete`, etc.

**Operatori nesupraîncărcabili:** `::`, `.`, `.*`, `? :`, `sizeof`.

**Reguli:**
- Cel puțin un operand trebuie să fie de tip clasă (nu se pot redefini pentru tipuri predefinite)
- Nu se poate schimba numărul de operanzi (aritatea) sau precedența
- Operatorul `=`, `[]`, `()`, `->` pot fi supraîncărcați **numai ca metode** (nu funcții externe)
- `<<` și `>>` pentru I/O — mereu funcții externe (prietene), returnează `ostream&`/`istream&`

## 5.5 Clase derivate și moștenire (pp. 108–115)

**Moștenirea** = crearea unei clase derivate (subclasă) dintr-o clasă de bază. Clasa derivată moștenește atributele și metodele clasei de bază și poate adăuga altele noi sau supradefini (override) metodele existente.

```cpp
class Animal {
protected:
  char denumire[30];
  int varsta;
public:
  Animal(const char* d, int v) {
    strcpy(denumire, d); varsta = v;
  }
  void afisare() const {
    cout << "Animal: " << denumire << ", varsta: " << varsta << endl;
  }
  virtual void sunet() { cout << "Sunet generic" << endl; }
};

class Caine : public Animal {   // moștenire publică
  char rasa[30];
public:
  Caine(const char* d, int v, const char* r) : Animal(d, v) {
    strcpy(rasa, r);             // apel constructor baza prin lista de inițializare
  }
  void sunet() override {        // supradefinire metodă
    cout << "Ham-ham!" << endl;
  }
  void afisaRasa() const { cout << "Rasa: " << rasa << endl; }
};
```

**Tipuri de moștenire:**
| Tip | `public` din baza | `protected` din baza | `private` din baza |
|---|---|---|---|
| `: public` | → `public` | → `protected` | → inaccesibil |
| `: protected` | → `protected` | → `protected` | → inaccesibil |
| `: private` | → `private` | → `private` | → inaccesibil |

**Constructori și destructori în moștenire:**
- Constructorii **nu** se moștenesc; constructorul derivatei trebuie să apeleze explicit constructorul bazei
- Dacă nu se specifică, se apelează constructorul implicit al bazei
- La creare: mai întâi constructorul **bazei**, apoi al **derivatei**
- La distrugere: mai întâi destructorul **derivatei**, apoi al **bazei**

**Redefinirea (overriding) metodelor:**
```cpp
// Redefinire fără virtual → mascarea metodei bazei (legare statică):
Caine c("Rex", 3, "Labrador");
c.afisare();        // metoda bazei Animal::afisare()
c.afisaRasa();      // metoda derivatei
c.sunet();          // Caine::sunet() (suprascris)
```

**Conversia derivat → baza:**
```cpp
Animal *a = new Caine("Rex", 3, "Labrador");  // valid (up-cast)
// Caine *c = new Animal(...);               // INVALID (down-cast fără cast explicit)
```

**Moștenire multiplă:**
```cpp
class C : public A, public B { ... };
// Constructor: C(...) : A(...), B(...) { }
// Problemă potențială: ambiguitate dacă A și B au membri cu același nume
```

## 5.6 Polimorfismul — funcții virtuale (pp. 116–123)

**Polimorfismul** = capacitatea de a trata obiecte de tipuri diferite printr-o interfață uniformă.

**Legare statică (early binding)** — decizia ce funcție se apelează e luată la **compilare** (pe baza tipului variabilei/pointerului).

**Legare dinamică (late binding)** — decizia e luată la **execuție** (pe baza tipului real al obiectului). Activată prin `virtual`.

### Funcții virtuale:
```cpp
class Animal {
public:
  virtual void sunet() { cout << "Sunet generic\n"; }
  virtual void miscare() { cout << "Mișcare generică\n"; }
};

class Caine : public Animal {
public:
  void sunet() override { cout << "Ham-ham!\n"; }  // supradefinire
  // miscare() nu e suprascrisă → se moștenește din Animal
};

class Pisica : public Animal {
public:
  void sunet() override { cout << "Miau!\n"; }
};

// Polimorfism prin pointer/referință la baza:
Animal *animale[] = { new Caine(), new Pisica(), new Animal() };
for (int i = 0; i < 3; i++) {
  animale[i]->sunet();  // se apelează versiunea corespunzătoare tipului real!
  // Caine::sunet(), Pisica::sunet(), Animal::sunet()
}
```

**Tabela de funcții virtuale (vtable):** compilatorul construiește pentru fiecare clasă o tabelă de pointeri la funcțiile virtuale. Fiecare obiect are un pointer la vtable-ul clasei sale → la execuție, apelul se rezolvă prin această tabelă.

### Funcții virtuale pure și clase abstracte:
```cpp
class Forma {
public:
  virtual double arie() = 0;         // funcție virtuală pură (= 0)
  virtual double perimetru() = 0;
  virtual void afisare() { cout << "Forma"; }  // poate fi non-pura
};
// Forma este clasă abstractă → nu se pot crea instanțe: Forma f; // EROARE!
```

**Clasă abstractă** = clasă cu cel puțin o funcție virtuală pură. Obligă clasele derivate să implementeze acele funcții.

```cpp
class Cerc : public Forma {
  double r;
public:
  Cerc(double raza) : r(raza) {}
  double arie() override { return 3.14159 * r * r; }
  double perimetru() override { return 2 * 3.14159 * r; }
};

class Dreptunghi : public Forma {
  double l, h;
public:
  Dreptunghi(double ll, double hh) : l(ll), h(hh) {}
  double arie() override { return l * h; }
  double perimetru() override { return 2 * (l + h); }
};
```

### Destructori virtuali:
**Obligatoriu** când se lucrează cu pointeri la clasa de baza care pointează obiecte derivate:
```cpp
class Animal {
public:
  virtual ~Animal() { }   // virtual destructor!
};
class Caine : public Animal {
  char* date;
public:
  Caine() { date = new char[100]; }
  ~Caine() { delete[] date; }   // apelat corect dacă destructor virtual
};

Animal *a = new Caine();
delete a;  // Fără virtual destructor: apelează ~Animal() și pierde memoria din Caine!
           // Cu virtual destructor: apelează ~Caine() apoi ~Animal() → corect!
```

## 5.7 Fluxuri de intrare/ieșire (pp. 134–161)

Header: `#include <iostream.h>` (vechi) sau `#include <iostream>` (modern, cu `using namespace std;`)

### Obiectele standard:
- **`cin`** — flux de intrare standard (tastatură), obiect de tip `istream`
- **`cout`** — flux de ieșire standard (ecran), obiect de tip `ostream`
- **`cerr`** — flux de erori standard (nebuferizat)
- **`clog`** — flux de erori (buferizat)

### Operatorii de flux:
- **`<<`** (inserter) — inserează date în flux (scriere)
- **`>>`** (extractor) — extrage date din flux (citire)

```cpp
cout << "Valoarea: " << x << endl;    // scriere, endl = newline + flush
cin >> x >> y;                         // citire mai multor variabile
```

### Formatarea datelor:
**Manipulatori de flux:**
```cpp
#include <iomanip>   // pentru setw, setprecision, setfill, etc.

cout << setw(10)        << x;    // lățime câmp = 10 (completat cu spații)
cout << setprecision(4) << x;    // 4 cifre semnificative
cout << fixed           << x;    // notație virgulă fixă
cout << scientific      << x;    // notație exponențială
cout << left            << x;    // aliniere la stânga
cout << right           << x;    // aliniere la dreapta (implicit)
cout << setfill('0')    << setw(8) << n;  // completare cu '0'
cout << showpoint       << x;    // afișează punct zecimal și zerouri trailing
cout << boolalpha       << b;    // true/false în loc de 1/0
cout << hex  << n;               // hexazecimal
cout << oct  << n;               // octal
cout << dec  << n;               // zecimal (implicit)
cout << uppercase;               // HEX, E în loc de hex, e
cout << flush;                   // golire buffer
```

Manipulatorii fără parametri (`endl`, `hex`, `left`, etc.) nu necesită `<iomanip>`.

**Funcții membre ale fluxurilor:**
```cpp
cout.width(10);           // setw(10)
cout.precision(4);        // setprecision(4)
cout.fill('0');           // setfill('0')
cout.setf(ios::fixed);    // notație virgulă fixă
cout.setf(ios::left, ios::adjustfield);  // aliniere stânga
```

### Detectarea erorilor:
```cpp
if (cin.fail())     // eroare de extracție (tip incompatibil)
if (cin.bad())      // eroare gravă (I/O hardware)
if (cin.eof())      // s-a atins sfârșitul fișierului
if (!cin)           // shorthand pentru cin.fail()

cin.clear();        // resetare flaguri de eroare
cin.ignore(n, '\n'); // ignorare n caractere sau până la '\n'
```

### I/O pe fișiere:
```cpp
#include <fstream>   // sau <fstream.h>

// Fișier de ieșire:
ofstream fout("date.txt");   // sau: ofstream fout; fout.open("date.txt");
if (!fout) { cerr << "Eroare deschidere!\n"; }
fout << "Linie " << i << endl;
fout.close();

// Fișier de intrare:
ifstream fin("date.txt");
int x; string s;
while (fin >> x) { ... }       // citire până la EOF
while (getline(fin, s)) { ... } // citire linie cu linie
fin.close();

// Fișier bidirecțional:
fstream f("date.txt", ios::in | ios::out);

// Moduri de deschidere:
// ios::in    - citire
// ios::out   - scriere (suprascrie)
// ios::app   - adăugare la sfârșitul fișierului
// ios::ate   - poziționare la final la deschidere
// ios::trunc - trunchiere (implicit cu out)
// ios::binary - mod binar
```

**Citire/scriere binară:**
```cpp
ofstream fout("date.bin", ios::binary);
Angajat a = {"Popescu", 100, 2500.0};
fout.write((char*)&a, sizeof(a));
fout.close();

ifstream fin("date.bin", ios::binary);
fin.read((char*)&a, sizeof(a));
```

**Poziționare în fișier:**
```cpp
fin.seekg(n, ios::beg);    // poziționare pentru citire (beg/cur/end)
fin.tellg();               // poziția curentă de citire
fout.seekp(n, ios::beg);   // poziționare pentru scriere
fout.tellp();              // poziția curentă de scriere
```

### Formatarea datelor în memorie — `stringstream`:
```cpp
#include <sstream>

// Scriere în șir:
ostringstream oss;
oss << "Valoarea: " << x << ", alta: " << y;
string rezultat = oss.str();

// Citire din șir:
istringstream iss("123 3.14 salut");
int i; double d; string s;
iss >> i >> d >> s;   // i=123, d=3.14, s="salut"

// Conversii:
// int → string:
ostringstream os; os << n; string str = os.str();
// string → int:
istringstream is(str); int val; is >> val;
```

---


# 6. SUBIECTE FRECVENTE — COMPLETĂRI

## 6.1 SQL dinamic — EXECUTE IMMEDIATE (PL/SQL)

`EXECUTE IMMEDIATE` permite executarea dinamică a instrucțiunilor SQL sau DDL în PL/SQL (SQL care nu se cunoaște la compilare).

```plsql
-- Execuție DDL din PL/SQL (DDL nu se poate folosi direct în PL/SQL):
BEGIN
  EXECUTE IMMEDIATE 'DROP TABLE angajati_temp';
  EXECUTE IMMEDIATE 'CREATE TABLE angajati_temp AS SELECT * FROM angajati WHERE 1=2';
END;

-- Execuție DML dinamic cu variabile de legătură (binding):
DECLARE
  v_tabel VARCHAR2(30) := 'angajati';
  v_sal   NUMBER := 3000;
  v_count NUMBER;
BEGIN
  EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || v_tabel || ' WHERE salariu > :1'
    INTO v_count
    USING v_sal;   -- :1 se înlocuiește cu v_sal
  DBMS_OUTPUT.PUT_LINE('Numar: ' || v_count);
END;

-- Execuție cu parametri OUT:
EXECUTE IMMEDIATE 'SELECT MAX(salariu) FROM angajati' INTO v_sal;

-- UPDATE dinamic:
EXECUTE IMMEDIATE 'UPDATE ' || v_tabel || ' SET salariu = salariu * 1.1 WHERE dep_id = :1'
  USING 10;
COMMIT;
```

**Reguli `EXECUTE IMMEDIATE`:**
- DDL (CREATE, DROP, ALTER, TRUNCATE) se poate executa **doar** prin EXECUTE IMMEDIATE în PL/SQL
- Variabilele de legătură folosesc `:1`, `:2` etc. sau `:nume_parametru`
- `INTO` — pentru SELECT care returnează un singur rând
- `USING` — furnizează valorile variabilelor de legătură

---

## 6.2 ROUND și TRUNC pe DATE

Pe lângă utilizarea numerică, `ROUND` și `TRUNC` funcționează și pe date calendaristice:

```sql
-- ROUND pe DATE — rotunjire la unitatea specificată:
ROUND(data, 'YEAR')   -- 1 iulie → 1 jan anul următor; înainte → 1 jan același an
ROUND(data, 'MONTH')  -- după a 16-a zi → prima zi luna viitoare
ROUND(data, 'DAY')    -- după amiaza → ziua următoare
ROUND(data, 'HH')     -- la ora cea mai apropiată
ROUND(data, 'MI')     -- la minutul cel mai apropiat

-- TRUNC pe DATE — trunchierea la unitatea specificată:
TRUNC(SYSDATE, 'YEAR')    -- 01-JAN-<an curent>
TRUNC(SYSDATE, 'MONTH')   -- prima zi a lunii curente
TRUNC(SYSDATE, 'DAY')     -- prima zi a săptămânii (luni)
TRUNC(SYSDATE)             -- ora 00:00:00 a zilei curente

-- Exemple uzuale:
SELECT TRUNC(hire_date, 'YEAR') FROM employees;   -- anul angajării
SELECT ROUND(SYSDATE, 'MONTH') FROM dual;
```

---

## 6.3 `constexpr` și `const` în C++

```cpp
// const — valoare constantă, inițializată la runtime sau compilare:
const int n = 10;           // constantă (valoarea nu se poate modifica)
const int m = getSize();    // OK — inițializată la runtime

// constexpr — evaluată obligatoriu la COMPILARE:
constexpr int SIZE = 10;    // OK — valoare literală
constexpr int MAX = SIZE * 2; // OK — expresie constexpr

// constexpr function — poate fi evaluată la compilare:
constexpr int square(int x) { return x * x; }
constexpr int s = square(5);   // evaluat la compilare: s = 25

// Utilizare în switch (necesită constexpr sau const integral):
constexpr char sep = '-';
switch (c) {
  case sep:   // OK cu constexpr
    break;
}

// const nu merge în switch dacă e inițializat la runtime:
const char sep2 = getSep();
// switch (c) { case sep2: ... }  // EROARE — nu e constantă la compilare
```

**Diferențe cheie:**
| | `const` | `constexpr` |
|---|---|---|
| Evaluare | Runtime sau compilare | Obligatoriu compilare |
| Funcții | Nu | Da (`constexpr` funcții) |
| Switch/case | Doar dacă literal | Da |

---

## 6.4 Pointer constant vs. Pointer la constantă (C/C++)

```c
int x = 1, y = 2;

// 1. Pointer la constantă — valoarea nu se poate modifica prin pointer:
const int *p1 = &x;   // sau: int const *p1 = &x;
// *p1 = 5;  // EROARE — nu se poate modifica valoarea
p1 = &y;     // OK — pointerul poate fi redirecționat

// 2. Pointer constant — adresa nu se poate modifica:
int *const p2 = &x;
*p2 = 5;    // OK — valoarea se poate modifica
// p2 = &y; // EROARE — pointerul nu poate fi redirecționat

// 3. Pointer constant la constantă — nici adresa, nici valoarea:
const int *const p3 = &x;
// *p3 = 5;  // EROARE
// p3 = &y;  // EROARE

// Exemplu cu char:
char z = 'A';
char *const cp = &z;   // pointer constant la char
*cp = 'B';   // OK
// cp = &z2; // EROARE
```

**Regulă mnemonică:** citește de la dreapta la stânga: `char *const p` = "p este un pointer constant la char".

---

*Rezumat realizat pe baza paginilor exacte cerute în bibliografia examenului de specialitate Master CSIE3, ASE București 2025–2026.*

*Față de rezumatul de licență, CSIE3 adaugă:*
- *PL/SQL: Tratarea excepțiilor (pp. 83–102) + Funcții extinse (pp. 118–128)*
- *C++: Masive de obiecte (pp. 28–29) + Friends (pp. 44–45) + Fluxuri I/O (pp. 134–161)*
- *C: I/O pe fișiere (pp. 184–196)*
- *SQL: interval ușor diferit (pp. 127–171 vs. 127–178)*
- *BD: intervale de pagini diferite (103–122, 129–131, 144–186, 197–201)*
