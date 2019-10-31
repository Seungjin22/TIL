EventListener

: 무엇을, 언제, 어떻게

ex) 버튼을, 누를때, 메세지'button clicked!'



Go LIve ==> console창 버튼 클릭



<script> 태그는 html의 다른 body 안 태그들 가장 아래에 작성해주기

DOM이 먼저 그려진 후에 script 코드가 와야 함



![image](https://user-images.githubusercontent.com/22102664/67913189-8a622280-fbcf-11e9-933a-c7b5cd22a4df.png)







## 동기식/blocking | 비동기식/non-blocking



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