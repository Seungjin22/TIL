/*
// Object & Array

// Array

const numbers = [1, 2, 3, 4]

console.log(numbers[0]) // 1
console.log(numbers[-1]) // undefined
console.log(numbers.length) // 4

// 원본 파괴
console.log(numbers.reverse()) // .reverse()는 원본을 바꿈
console.log(numbers)
console.log(numbers.reverse())
console.log(numbers)

// push - 배열의 길이를 return
// 배열 끝에 push

console.log(numbers.push('a')) // 5
console.log(numbers)

// pop - 배열의 가장 마지막 요소를 제거 후 return
console.log(numbers.pop())
console.log(numbers)

// unshift - 배열의 가장 앞에 요소를 추가 -> 배열의 길이를 return
console.log(numbers.unshift('a')) // 5
console.log(numbers) // 'a'가 첫번째 요소로 push된 배열

// shift - 배열 가장 첫번째 요소를 제거하고 return
console.log(numbers.shift())
console.log(numbers)

// 복사본 or 다른값을 return
console.log(numbers.includes(1)) // true
console.log(numbers.includes(0)) // false

console.log(numbers.push('a')) // 5
console.log(numbers.push('a')) // 6
console.log(numbers)
console.log(numbers.indexOf('a')) // 처음 만나는 값의 배열 인덱스를 return
console.log(numbers.indexOf('b')) // 찾고자 하는 배열의 요소가 없으면 -1

// join - 
console.log(numbers.join())
console.log(numbers.join('-'))

// 배열의 원본은 변하지 않음
console.log(numbers)


// Object - 객체(오브젝트)

const me = {
  name: 'ssafy', // key가 1개의 단어
  'phone number': '01012345678', // key가 여러 개 단어로 이루어지면 스트링으로 처리
  appleProducts: {
    ipad: '2018pro',
    iphone: '6s+',
    macbook: '2018pro',
  }
}

console.log(me.name) // value를 얻어내는 첫번째 방법
console.log(me['name']) // value를 얻어내는 두번째 방법
console.log(me['phone number']) // 주의! 2개 이상의 단어로 구성된 key는 []로 접근

console.log(me.appleProducts)
console.log(typeof me.appleProducts)

// Object Literal (추가된 오브젝트 표현법: ES6+)

const books = ['사서삼경', '천자문']

const movies = {
  'Horror': ['곤지암', '겟아웃'],
  'SF': ['인셉션', '마션', '인터스텔라', '그레비티']
}

const magazines = null

// ES5
const bookShop = {
  books: books,
  movies: movies,
  magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[1])

// ES6+
// object의 key, value가 똑같다면 마치 배열처럼 한 번만 작성이 가능
const books = ['사서삼경', '천자문']

const movies = {
  'Horror': ['곤지암', '겟아웃'],
  'SF': ['인셉션', '마션', '인터스텔라', '그레비티']
}

const magazines = null

const bookShop = {
  books,
  movies,
  magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[1])
*/

// JSON <-> Object
// Json -> JS의 object 형태와 유사한 문자열!!
// 실제 모습만 비슷하고 JS Object로 사용하기 위해서는 변환이 필요하다.

// Object -> String(json)
const jsonData = JSON.stringify({
  coffee: 'Americano',
  icecream: 'Cookie and Cream'
})
console.log(jsonData)
console.log(typeof jsonData) // string

// String -> Object
const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData) // object

// Object <-> Json의 차이
// Object: JS의 Key-Value pair의 자료 구조
// Json: JS의 Object와 비스무리하게 생긴 단순 String(그냥 문자열!!)
