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

# 1. BAZE DE DATE RELAȚIONALE
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

*Rezumat realizat pe baza paginilor exacte cerute în bibliografia examenului de specialitate Master CSIE3, ASE București 2025–2026.*

*Față de rezumatul de licență, CSIE3 adaugă:*
- *PL/SQL: Tratarea excepțiilor (pp. 83–102) + Funcții extinse (pp. 118–128)*
- *C++: Masive de obiecte (pp. 28–29) + Friends (pp. 44–45) + Fluxuri I/O (pp. 134–161)*
- *C: I/O pe fișiere (pp. 184–196)*
- *SQL: interval ușor diferit (pp. 127–171 vs. 127–178)*
- *BD: intervale de pagini diferite (103–122, 129–131, 144–186, 197–201)*
