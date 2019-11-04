# var, let, const 차이점은?

- `var`는 `function-scoped`이고, `let`, `const`는 `block-scoped`입니다.
- `function-scoped`와 `block-scoped`가 무슨말이냐?

## var(function-scoped)

```
// var는 function-scope이기 때문에 for문이 끝난다음에 i를 호출하면 값이 출력이 잘 된다.
// 이건 var가 hoisting이 되었기 때문이다.
for(var j=0; j<10; j++) {
  console.log('j', j)
}
console.log('after loop j is ', j) // after loop j is 10


// 아래의 경우에는 에러가 발생한다.
function counter () {
  for(var i=0; i<10; i++) {
    console.log('i', i)
  }
}
counter()
console.log('after loop i is', i) // ReferenceError: i is not defined
```

그럼 항상 function을 만들어서 호출해야 할까? 그건 아니다.

javascript에서는 `immediately-invoked function expression (or IIFE, pronounced "iffy")`라는것이 있다.

`IIFE`로 `function-scope`인거 처럼 만들 수가 있다.

```
// IIFE를 사용하면
// i is not defined가 뜬다.
(function() {
  // var 변수는 여기까지 hoisting이 된다.
  for(var i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // ReferenceError: i is not defined
```

근데 javascript는 여기서 좀 웃긴 부분이 있다.

위에서 잠깐 말했지만 `IIFE`는 `function-scope`처럼 보이게 만들어주지만 `결과가 같지는 않다.`

```
// 이 코드를 실행하면 에러없이 after loop i is 10이 호출된다.
(function() {
  for(i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // after loop i is 10
```

위에 코드가 아무 에러 없이 실행되는 이유는 `i`가 hoisting이 되어서 `global variable`이 되었기 때문이다.

그래서 아래와 같이 된 것이다.

```
var i
(function() {
  for(i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // after loop i is 10
```

`IIFE`는 쓰는데 이렇게 hoisting이 된다면 무슨 소용이 있겠는가?!

그래서 이런 `hoisting`을 막기 위해 `use strict`를 사용한다.

```
// 아까랑 다르게 실행하면 i is not defined라는 에러가 발생한다.
(function() {
  'use strict'
  for(i=0; i<10; i++) {
    console.log('i', i)
  }
})()
console.log('after loop i is', i) // ReferenceError: i is not defined
```

어떤가? 뭔가 변수 선언때문에 너무 많은 일을 한다고 생각하지 않는가?

그럼 `let`, `const`에 대해서 알아보자.

## let, const(block-scoped)

- es2015에서는 `let`, `const`가 추가 되었다.

javascipt에는 그동안 `var`만 존재했기 때문에 아래와 같은 문제가 있었다.

```
// 이미 만들어진 변수이름으로 재선언했는데 아무런 문제가 발생하지 않는다.
var a = 'test'
var a = 'test2'

// hoisting으로 인해 ReferenceError에러가 안난다.
c = 'test'
var c
```

위와 같은 문제점으로 인해 javascript를 욕 하는 사람이 참 많았다.

하지만 `let`, `const`를 사용하면 `var`를 사용할때보다 상당히 이점이 많다.

두개의 공통점은 var와 다르게 `변수 재선언 불가능`이다.

`let`과 `const`의 차이점은 변수의 `immutable`여부이다.

`let`은 변수에 재할당이 가능하지만,

`const`는 변수 재선언, 재할당 모두 불가능하다.

```
// let
let a = 'test'
let a = 'test2' // Uncaught SyntaxError: Identifier 'a' has already been declared
a = 'test3'     // 가능

// const
const b = 'test'
const b = 'test2' // Uncaught SyntaxError: Identifier 'a' has already been declared
b = 'test3'    // Uncaught TypeError:Assignment to constant variable.
```

`let`, `const`가 hoisting이 발생하지 않는건 아니다.

`var`가 `function-scoped`로 hoisting이 되었다면

`let`, `const`는 `block-scoped`단위로 hoisting이 일어나는데

```
c = 'test' // ReferenceError: c is not defined
let c
```

위에 코드에서 `ReferenceError`가 발생한 이유는 `tdz(temporal dead zone)`때문이다.

`let은 값을 할당하기전에 변수가 선언 되어있어야 하는데 그렇지 않기 때문에` 에러가 난다.

이건 `const`도 마찬가지인데 좀 더 엄격하다.

```
// let은 선언하고 나중에 값을 할당이 가능하지만
let dd
dd = 'test'

// const 선언과 동시에 값을 할당 해야한다.
const aa // Missing initializer in const declaration
```

이렇게 javascript에 `tdz`가 필요한 이유는 동적언어이다 보니깐 `runtime type check` 가 필요해서이다.



---

**switch**

##### while loop, for loop 등





### EventListener

: 무엇을, 언제, 어떻게

ex) 버튼을, 누를때, 메세지'button clicked!'



Go LIve ==> console창 버튼 클릭



<script> 태그는 html의 다른 body 안 태그들 가장 아래에 작성해주기

DOM이 먼저 그려진 후에 script 코드가 와야 함



![image](https://user-images.githubusercontent.com/22102664/67913189-8a622280-fbcf-11e9-933a-c7b5cd22a4df.png)







### callback function

항상 콜백이 비동기는 아님

콜백의 방법 중 하나가 비동기식



### 동기식/blocking | 비동기식/non-blocking



동기식은 blocking

```python
# python

from time import sleep

def sleep_3s():
    sleep(3)
    print('Wake up Python!!')

print('Start Sleeping!!')
sleep_3s()
print('End of Program!!')
```

```text
$ python 00_blocking.py
Start Sleeping!!
Wake up Python!!
End of Program!!
```





비동기식은 non-blocking / 막지 않고 뒷 일이 계속 쭉-

JavaScript는 비동기식으로 작동(non-blocking)_다른 일의 동작을 막지 않음

```javascript
// javascript

function sleep_3s() {
  setTimeout(() =>{
    console.log('Wake up Javascript!!!')
  }, 3000)
}

console.log('Start Sleeping!!')
sleep_3s()
console.log('End of Program!!')
```

```text
$ node 01_non_blocking.js
Start Sleeping!!
End of Program!!
Wake up Javascript!!!
```

```javascript
function first() {
  console.log('first')
}

function second() {
  console.log('second')
}

function third() {
  console.log('third')
}

first()
setTimeout(second, 1000) // 이게 0초여도 결과는 같음
third()
```

```text
$ node 01_non_blocking.js
first
third
second
```



axios

: 그냥 요청 보내주는!

**npm** (python에서 pip)

`$ npm install axios`

**cdn** Content Delivery Network(bootstrap)



