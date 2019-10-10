# 데이터베이스(DB)



체계화된 데이터의 모임

**몇 개의 자료 파일을 조직적으로 통합**하여 자**료 항목의 중복을 없애고** 자료를 **구조화하여 기억**시켜 놓은 자료의 집합체



DB로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성
  - 정확한 정보를 보장
- 데이터 일관성
- 데이터 독립성



#### RDBMS (관계형 데이터베이스 관리 시스템)

MySQL, SQLite, PostgreSQL...

특징

- 모든 데이터를 2차원으로 표현(테이블 형태)
- 테이블은 row(record, tuple)와 column(field, item)으로 구성
- 테이블은 상호 연관성을 지니고 하나의 DB에 여러개 존재 가능
- 데이터베이스의 설계도를 ER(Entity Relationship) 모델이라고 하고 ER 모델에 따라 DB 만들어짐



##### - 스키마

: 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조



##### - 테이블

: 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합

- 열(Column) : 고유한 데이터 형식이 지정 / INTEGER, TEXT, NULL 등
- 행(Row) , 레코드 : 테이블의 데이터
- 기본키(PK) : 각 행(레코드)의 고유값 ==> 반드시 설정!



#### SQL (Structured Query Language)

 : RDBMS의 데이터를 관리하기 위해 설계된 **특수 목적(DB와 통신)의 프로그래밍 언어**



| 분류                                                     | 개념                                                         | 예시                                        |
| -------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| DDL - 데이터 정의 언어<br />(Data Definition Language)   | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE<br />DROP<br />ALTER                 |
| DML - 데이터 조작 언어<br />(Data Manipulation Language) | 데이터를 저장, 수정, 삭제, 조회 등을 하기 위한 언어          | INSERT<br />UPDATE<br />DELETE<br />SELECT  |
| DCL - 데이터 제어 언어<br />(Data Control Language)      | 데이터베이스 사용자의 권한 제어를 위해 사용되는 언어         | GRANT<br />REVOKE<br />COMMIT<br />ROLLBACK |



특징

- ; 까지 하나의 명령으로 간주
- . 은 sqlite3 프로그램 기능 실행
- -.schema 테이블이름 ==> ; 를 붙이지 않음





##### SQLite 추가하기

`bit.do/hello_db` 에서 sqlite.zip 다운받아 압출풀기



VS Code 터미널에서 켜기

`$ sqlite3`

종료할 때는,

`ctrl + z + Enter`  또는 `.exit`



데이터베이스 생성

`$ sqlite3 tutorial.sqlite3`

`sqlite> .databases`

`sqlite> .mode csv`

`sqlite> .import hellodb.csv examples`

`sqlite> .SELECT * FROM examples;`



```text
$ sqlite3 tutorial.sqlite3

SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.

sqlite> .databases

main: C:\Users\student\TIL\04_db\00_db_prac_1\tutorial.sqlite3

sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232

sqlite> .headers on
sqlite> .mode column

sqlite> SELECT * FROM examples;
id          first_name  last_name   age         country     phone
----------  ----------  ----------  ----------  ----------  -------------
1           길동          홍           600         충청도         010-2424-1232
```





##### Datatype

SQLite은 동적 데이터 타입으로, 기본적으로 유연하게 데이터가 들어감

BOOLEAN은 따로 타입이 존재하지 않기 때문에 정수 0, 1 로 저장



▶ SQLite 는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는 PK 옵션을 가진 **rowid**를 만들어 줌

```text
sqlite> SELECT rowid, * FROM classmates;
rowid       name        age         address
----------  ----------  ----------  ----------
1           홍길동         23
2           홍길동         30          서울
```

▶ id를 PK로 설정하면 INSERT 할 때 id를 직접 지정해줘야 함 ==> rowid가 더 편함



##### Table 및 Schema 조회

- 테이블 목록 조회

  : `.tables`

- 스키마 조회

  : `.schema 테이블이름`

##### Table 삭제(DROP)

- `DROP TABLE 테이블이름;`

##### Data 추가(INSERT)

 : 특정 table에 새로운 행을 추가하여 데이터 추가(레코드 추가)

- `INSERT INTO 테이블(column명 명시) VALUES (해당하는 데이터);`

##### Data 조회(SELECT)

- 해당 테이블의 모든 데이터 조회

  `SELECT * FROM 테이블;`

- LIMIT을 사용하면 원하는 '개수'만큼 가져옴

  `SELECT rowid, name FROM classmates LIMIT 1;`

- OFFSET을 사용하면 '몇 번째' 데이터 가져옴 (인덱스라 3번째 원하면 OFFSET 2)

  `SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;`

- WHERE을 사용하면 '특정한 값'만 가져옴 (주소가 서울인 사람만)

  `SELECT rowid, name FROM classmates WHERE address='서울'`

- DISTINCT 사용해서 '중복없이' 데이터 가져옴 (나이 값 중복없이 다 가져오기)

  `SELECT DISTINCT age FROM classmates;`

- 불러올 데이터의 조건이 2개 이상일 때  'and' 사용

  `SELECT first_name, last_name FROM users WHERE first_name="승진" and last_name="하";`

- COUNT() 사용하면 레코드 개수 반환

  `SELECT COUNT(*) FROM users;`

- 30살 이상의 평균 나이 구하기 | AVG(), MIN(), MAX(), SUM()

  `SELECT AVG(age) FROM users WHERE age>=30;`

- users에서 계좌 잔액(balance)이 가장 높은 사람의 이름과 잔액

  `SELECT first_name, MAX(balance) FROM users;`

##### Data 삭제(DELETE)

- 중복이 불가능한 rowid를 기준으로 삭제

  `DELETE FROM classmates WHERE rowid=4`

##### Data 수정(UPDATE)

- 특정 table에 특정한 레코드 수정

  `UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;`



SQLite 는 기본적으로 일부 행을 삭제하고 새 행을 입력하면 rowid 값을 그대로 재사용

ex) rowid 4인 데이터를 삭제하고 새로 입력하면 rowid 4 부여

==> 이전에 사용하지 않은 id 값 부여하고 싶다면? : **AUTOINCREMENT**

```text
sqlite> CREATE TABLE tests (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL
   ...> );
sqlite> INSERT INTO tests VALUES (1, '홍길동'), (2, '김철수');
sqlite> SELECT * FROM tests;
id          name
----------  ----------
1           홍길동
2           김철수
sqlite> DELETE FROM tests WHERE rowid=2;
sqlite> SELECT * FROM tests;
id          name
----------  ----------
1           홍길동
sqlite> INSERT INTO tests (name) VALUES ('최철순');
sqlite> SELECT * FROM tests;
id          name
----------  ----------
1           홍길동
3           최철순								==> id 값 3이 들어감
```

But, SQLite는 특정한 요구사항이 없다면 AUTOINCREMENT 쓰지 않는 것을 권장



##### LIKE (wild cards)

: 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환

```sqlite
SELECT * FROM 테이블 WHERE 열 LIKE '';
```

|  --  |    --     | --                                           |
| :--: | :-------: | -------------------------------------------- |
|  %   |    2%     | 2로 시작하는 값                              |
|      |    %2     | 2로 끝나는 값                                |
|      |    %2%    | 2가 들어가는 값                              |
|  _   |    _2%    | 아무값이나 들어가고 두번째가 2로 시작하는 값 |
|      |   1___    | 1로 시작하고 4자리인 값                      |
|      | 2 _ % _ % | 2로 시작하고 적어도 3자리인 값               |

- 나이가 '20대'인 사람들

  `SELECT * FROM users WHERE age LIKE '2_';`

- 전화번호 지역번호 '02'인 사람들

  `SELECT * FROM users WHERE phone LIKE '02-%';`

- 이름이 '-준'으로 끝나는 사람들

  `SELECT * FROM users WHERE first_name LIKE '%준';`

- 중간번호가 '5114'인 사람들

  `SELECT * FROM users WHERE phone LIKE '%5114%';`



##### 정렬 (ORDER)

```sqlite
SELECT 열 FROM 테이블 ORDER BY column1, column2 ASC | DESC;
```

▶ **ASC** 는 기본 설정 값 (디폴트)  ==> 안써도 OK

- 나이순으로 '오름차순' 정렬하여 '상위 10'개 데이터

  `SELECT * FROM users ORDER BY age ASC LIMIT 10;`

- 나이순, 성순으로 '오름차순' 정렬하여 '상위 10'개 데이터

  `SELECT * FROM users ORDER BY age, last_name LIMIT 10;`

- 계좌 잔액순으로 '내림차순' 정렬하여 '10'개의 사람 성, 이름

  `SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;`



##### 변경 (ALTER)

특정 테이블의 이름을 변경

```sqlite
ALTER TABLE 기존테이블 RENAME TO 새테이블;
```

특정 테이블에 새로운 컬럼 추가 (NOT NULL 설정 제외)

```sqlite
ALTER TABLE 테이블 ADD COLUMN 열 datatype;
```

또는 DEFAULT 값을 넣어서 추가 (NOT NULL 설정하고 싶을 때)

```sqlite
ALTER TABLE 테이블 ADD COLUMN 열 datatype NOT NULL DEFAULT 1;
```



```text
sqlite> CREATE TABLE articles (
   ...> title TEXT NOT NULL,
   ...> content TEXT NOT NULL)

sqlite> INSERT INTO articles VALUES ('1번제목', '1번내용');
sqlite> ALTER TABLE articles RENAME TO news;

sqlite> ALTER TABLE news ADD COLUMN created_at DATETIME NOT NULL;
Error: Cannot add a NOT NULL column with default value NULL

sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at DATETIME;

sqlite> INSERT INTO news VALUES ('title', 'content', datetime('now', 'localtime'));
sqlite> SELECT * FROM news;
title       content     created_at
----------  ----------  ----------
1번제목        1번내용
title       content     2019-10-10

sqlite> ALTER TABLE news
   ...> ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;
   
sqlite> SELECT * FROM news;
title       content     created_at  subtitle
----------  ----------  ----------  ----------
1번제목        1번내용                    1
title       content     2019-10-10  1
```

