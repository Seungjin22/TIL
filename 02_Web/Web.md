# 190729~ | Web



Web Site를 만든다? -> Web Service를 만든다

-> *우리는 서버 컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.*



 World Wide Web (WWW, W3)



웹의 시작과 최초의 메세지



#### Web Service란?

고객 (요쳥하는 컴퓨터)  --------------요청(request)----------------> 해주는 컴퓨터

 클라이언트(Client)		<-----------응답(response)----------------  서버(Server)



우리는 브라우저(Browser) 통해서 요청 보냄

- #### 요청의 종류

1. 줘라(Get) __주소 창에 입력하는건 모두 Get 방식
2. 받아라(Post) 처리해줘!



## Static Web

정말 단순한 웹 서비스

주어진 일만 할 수 있음(아무것도 변하지 않음)

​	ex) 학교 홈페이지, 댓글 기능이 없는 블로그(GitHub IO)

클라이언트가 요청을 보내면 서버가 응답한다. (request & response)



172.217.27.78 : Google의 주소

##### - IP(Internet Protocol)

​	172.217.27.78

##### - 도메인(Domain)

​	google.com

##### - URL(Uniform Resource Locator)

​	https://www.google.co.kr/search?q=구글



## Dynamic Web	Web Application Program (Web APP)

접속할 때마다 변해야 할 필요가 있는 사이트

일반적인 웹사이트(댓글 기능)



**URI** : URL보다 더 상위의 개념

요즘은 원하는게 딱 그 자리에 있지 않음(URLocator 보다 URIdentificator_식별자 사용)



웹 표준 지정하는 곳

W3C(3W Consortium)    VS    WHATWG(Web Hypertext Application Technology Working Group)___승리!!!



- #### HTML(Hyper Text Markup Language)

  : 웹 페이지를 작성하기 위한 역할 표시 언어

  - HTTP(S) : S는 Secure. 더 보안에 강화된

  - Hyper Text란 선형적이 아닌 비 선형적으로 이루어진 텍스트

    Hyper Link를 통해 텍스트를 이동

  - Markup 역할을 줌



- #### CSS(Cascading Style Sheet)

  - HTML을 꾸며주는 친구



- #### JS(Java Script)

  - 활기를 불어넣어주는 친구 



---



## HTML



#### 1. HTML 문서의 기본 구조

- head 요소는 브라우저에 나타나지 않음

  head 안 meta 태그 : Facebook에서 개발  ex) 카카오 링크 보내면 사진도 딱 같이 뜨는 것

  - Meta : 메타 정보는 '정보의 정보'  -> HTML 정보에 대한 정보

- body 요소 : 브라우저에 나타나는 부분

  

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Hello World!</title>
    </head>
    <body>
         <!--이거슨 주석입니다. 화면에 나오지 않쥬-->
        <h1>Hi, There! I'm Marlene :-)</h1>
        <h2>My favorite food is pizza!</h2>
    </body>
</html>
```



#### 2. Tag와 DOM Tree

- 주석(Comment) : 주석으로 처리된 부분은 브라우저에서 보이지 않음

  `<!-- 주석 -->`

- 요소(Element) : HTML의 요소는 태그와 내용(Contents)으로 구성  `<h1> 내용 </h1>`
  - 태그는 대소문자를 구별하지 X, But **소문자**로 써야!!
  - 요소간의 중첩도 가능 (태그 안에 태그 가능)
  - Self-closing element : 닫는 태그 없음
  
- 속성(Attribute) `<a href="google.com">` 앵커 태그 -> get 요청 보낼 때만 사용 가능
  - 태그에는 속성이 지정될 수 있다.
  - =""사이 띄우면 X
  - "" 이걸로 사용! NOT SINGLE QUOTATION
  - 아래의 속성은 HTML 전역 속성 중 일부로 모든 태그에서 사용 가능
    - id
    - class
    - style

- DOM 트리

  - **중첩되어 사용 가능**하며 '**관계**'를 가짐

    ```html
    <body>
        <h1>웹문서</h1>
          <ul>
              <li>HTML</li>
              <li>CSS</li>
          </ul>
    </body>
    ```

    - body 태그와 h1 태그는 부모(parent)-자식(child) 관계
    - li 태그는 형제 관계(sibling)
    - h1 태그와 ul 태그는 형제 관계(sibling)

- 시맨틱 태그

  | 태그        |                             설명                             |
| ----------- | :----------------------------------------------------------: |
  | **header**  |                헤더 (문서 전체나 섹션의 헤더)                |
  | **nav**     |                          네비게이션                          |
  | **aside**   | 사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용 |
| **section** | 문서의 일반적인 구분으로 컨텐츠의 그룹을 표현하며, 일반적으로 h1~h6 요소를 가짐 |
  | **article** | 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역(포럼/신문 등의 글 또는 기사) |
| **footer**  |                푸터 (문서 전체나 섹션의 푸터)                |
  
- 컨텐츠의 의미를 설명하는 태그, HTML5에 새롭게 추가된 태그
  
    ```html
    <div>이거슨 공간</div> ==> division ==> 공간 분할
    ```
  
  - 하지만 ''공간'' 자체에 대한 어떠한 의미도 가지고 있지 않음
  
  - but, Why?
  
    - 개발자가 의도한 요소의 의미가 명확히 보임 == 코드의 가독성 높이고 유지보수 쉬움
    - 웹에 존재하는 수많은 웹페이지들에 '메타데이터'를 부여하여 기존의 잡다한 데이터의 집합을 '의미'와 '관련성'을 가지는 거대한 데이터의 집합으로 구축하고자 하는 발상
    - 개발자 및 사용자 뿐만 아니라 검색엔진(구글, 네이버) 등에 의미 있는 
    - SEO(Search Engine Optimization) : 웹 페이지 검색 엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성해 검색 결과를 상위에 노출될 수 있도록 하는 작업



#### 3. Markup - Tag의 종류__어떤 역할 / 어떤 종류

- 텍스트 태그
  - 단순히 글자 크기 크게 쓰고 싶어서 쓰지 말자! ==> 다 역할이 있음 `<h1></h1>`~`<h6></h6>`
  - 본문 작성 `<p>본문</p>` 
  - 글자 강조 `<b>contents</b>`  `<strong>semantic contents</strong>`
  - ordered list `<ol>순서가 있는</ol>`,  unordered list `<ul>순서가 없는</ul>` 
- 레이아웃 태그

  - semantic 태그 `<header>누가 봐도 헤더!</header>` `<footer>누가 봐도 푸터!</footer>` 
  - non-semantic 태그 `<div>의미 없는 블록</div>` `<span>의미 없는 인라인</span>`
- 미디어 태그

  - image 태그 : `<img src="/profile.jpg" alt="">`
    - `alt=""`이건 이미지가 뜨지 않을 경우 뜨게 되는 글. 웹 접근성을 위해 읽어줄 때 이걸 읽음
  - video 태그 : 
  - iframe 태그 : `<iframe src="https://www.w3schools.com"></iframe>`
    - width : IFrame 창의 가로 길이 결정
    - hight : IFrame 창의 세로 길이 결정



---



## CSS(Cascading Style Sheet)

HTML은 정보와 구조화

CSS는 Styling 정의

==> 각자는 문법이 다른 별개의 언어!



1. 단순선택자(기본)  - 전체 선택자



2. 단순 선택자(기본) - 태그 선택자
   - ol, ul {list-style-type}



3. 단순 선택자(기본) - 클래스 선택자
   - .class {color: blue;}



4. 단순 선택자(기본) - 아이디 선택자
   - #id {colkr: blue;}



5. 단순 선택자(기본) - 후손 / 자식 셀렉터

   - 자식 셀렉터(공백) -> 해당 태그 내에 있는 직계 자식 요소만 선택

   - 후손 셀렉터(>) -> 해당 태그 내의 모든 요소를 선택



- 프로퍼티 값의 단위

  h1{color: blue; font-size: 150px;}



- em

  : 상대 단위

  1em = 100%

  상속의 영향을 받음. 



- rem

  : em의 기준은 상속의 영향으로 바뀔 수 있음

  즉, 상황에 따라 1.2em은 각기 다른 값을 가질 수 있다.

  rem은 최상위 요소(html)의 사이즈를 기준으로 삼는다.

  rem의 r은 root를 의미

  

- Viewport 단위

  : 디바이스마다 다른 크기의 화면을 가지고 있기 때문에 상대적인 단위인 viewport를 기준으로 만든 단위



색상 표현 단위

HEX : red=(ff0000)

RGB : red=(255, 0, 0)

RGBA : red=(255, 0, 0, 0.2)



기본 픽셀 16px



---



## Box Model

모든 태그는 다 박스

Margin : 테두리 바깥의 외부 여백 배경색을 지정할 수 없다

Border : 테두리 영역

Padding : 테두리 안쪽의 내부 여백 요소에 적용된 배경의 컬러, 이미지는 패딩까지 적용

Content : 실제 내용이 위치



1.1 기본 박스모델 활용 - margin

```html
.margin{
	margin-top: 10px;
	margin-right: 20px;
	margin-bottom: 30px;
	margin-left: 40px;
}
```

```html
/*상, 하, 좌, 우: 10px*/
.margin-1 {	margin: 10px;}
/*상, 하: 10px, 좌, 우: 20px*/
.margin-2 {	margin: 10px 20px;}
/*상: 10px, 하: 20px, 좌, 우: 30px*/
.margin-3 {	margin: 10px 20px 30px;}
/*상: 10px, 하: 20px, 좌: 30px, 우: 40px*/
.margin-4 {	margin: 10px 20px 30px 40px;}
```



1.2 기본 박스모델 활용- padding

```html
.margin-padding {
    margin: 10px;
    padding: 20px;
}
```

1.3 -border

```html
.border{
    border-width: 2px;
    border-style: dashed;
	border-color: black;
}
```

1.4 -shorthand





2.display 속성 `06_box_model_2`

- block

  - 항상 새로운 라인에서 시작
  - 화면 크기 전체의 가로폭 차지(width: 100%)
  - block 레벨 요소 내에 inline 레벨 요소 포함 가능
  - ex) `div`

- inline

  - 새로운 라인에서 시작X 문장의 중간에 들어갈 수 있음
  - content의 너비만큼 가로폭 차지
  - width, height, margin-top, margin-bottom 프로퍼티를 지정할 수 없다.
  - 상, 하 여백은 line-height로 지정
  - ex) `span` `a` `strong` `img` `br` `input` `select` `textarea` `button`

- inline-block

  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline 레벨 요소처럼 한 줄에 표시
  - block에서의 width, height, margin(top, bottom) 속성 모두 지정 가능

- None

  - 해당 요소를 화면에 표시하지 않음(**공간(영역)조차 사라진다**)

  > display: none    VS    visibility: hidden

- background

  - background-image : url('')
  - background-color



#### Position

1. 기본 위치(static)

2. 상대 위치(relative)

   : 기본 위치(static으로 지정되었을 때의 위치)를 기준으로 좌표 프로퍼티를 사용하여 위치 이동(음수 가능)

   - 잠시 집을 비움. (집의 빈자리가 남아있음)

   - relative의 static간 중복 불가

   ```css
   .relative {
       position: relative;
       top: 100px;
       left: 100px;
   }
   ```

3. 절대 위치(absolute)

   : 부모 요소 또는 가장 가까운 상대 위치(relative)를 기준으로 

   - 완전히 집을 나감(원래 있던 자리 비어있음)

   ```css
   .parent {
       position: relative;
   }
   
   .absolute-child {
       position: absolute;
       top: 50px;
       left: 50px
   }
   ```

   

4. 고정 위치(fixed)

   부모 요소와 관계없이 좌표 프로퍼티를 사용하여 위치 이동

   ```css
   .fixed {
       position: fixed;
       bottom: 0;
       right: 0
   }
   ```



```html
<body>
    <!--1. 기본위치(static)-->
    <div>
        static
    </div>

    <!---2. 상대위치(relative): 기본위치(static)일 때를 기준으로 삼음-->
    <div class="relative">
        relative
    </div>

    <!--3. 절대위치(absolute)-->
    <div class="parent">
        부모
        <div class="absolute-child">
            자식
        </div>
    </div>

    <!--4. 고정위치(fixed)-->
    <div class="fixed">
        fixed
    </div>
</body>
```



#### 실습(위치위치위치위치위치_네모네모 옮기기)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>BOX</title>
    <link rel="stylesheet" href="09_position_2.css">
</head>
<body>
  <div class="big-box"> <!--부모 네모-->
    <div class="small-box" id="red"></div>	<!--자식 네모-->
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green"></div>
    <div class="small-box" id="blue"></div>
    <div class="small-box" id="pink"></div>
  </div>
</body>
</html>
```









##### ol > li: nth-child(4) {}

4번쨰가 li가 아니면 적용하지 않음

```css
ol > li:nth-child(4) {
    background: lemonchiffon;
}
```

![](noteimage/nthchild.PNG)



##### ol > li: nth-of-type(4) {}

4번째의 li를 찾아서 적용시킴

```css
ol > li:nth-of-type(4) {
    background: lemonchiffon;
}
```

![](noteimage/nthoftype.PNG)





---





# 190731 | Bootstrap

기본 틀

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```





### CDN(Content Delivery(Distribution) Network)

CDN 활용을 통해 Bootstrap에 작성된 CSS, JS를 활용하자!



컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템



개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)

외부 서버를 활용함으로써 본인 서버의 부하가 적어짐.

CDN은 보통 적절한 수준의 캐시 설정으로 빠르게 로딩할 수 있음.





Spacing

margin: 0!

```html

```



.py-0? 패딩



.mt-1

margin-top: 0.25rem



mt-2? 0.5rem 8px!

mt-3? 1rem 16px!





Border

radius!

.rounded-circle



display:block



.d-none



1-5. Position

1.6. Text

​	text-align : center

​	.text-center



컴포넌트는 공식 문서로 확인 > 앞으로도 많이 활용, 직접 들어가서 코드 찾아야하니!



2. Grid System

grid: 격자, 모눈

디자인 요소를 일렬 배열할 수 있는 패턴을 만드는 가로 및 세로 선 컬렉션

12개의 열을 한 줄에 표현할 때 몇 개씩 차지하게 할거냐!



```html
<!--1. Grid 기본-->
    <div class="container-fluid">  ==> fluid 붙이면 여백 다 없이 꽉 참
        <div class="row">
            <div class="square col-4">
                One of three columns
            </div>
            <div class="square col-4">
                One of three columns
            </div>
             <div class="square col-4">
                One of three columns
            </div>
        </div>
    </div>
```



ml : margin left









```html
display: flex;
flex-direction: row;
				row-reverse;
				column;
				column-reverse;

flex-wrap: wrap; ==> 창 줄이면 아래로 쌓임		(기본 설정은 nowrap)
		   wrap-reverse; ==> 위로 쌓임
```



!important 는 최강자! 다 비켜!!



반응형 웹 : 사이즈 줄이면 화면 구성 변화