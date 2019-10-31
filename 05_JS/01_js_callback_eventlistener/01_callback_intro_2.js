/*
// JS에서는 아래의 3가지 조건을 만족하기 때문에 1급 객체(first class object)다.
//1. 변수에 담을 수 있다.
//2. 인자로 전달할 수 있다.
//3. 반환값(return)으로 전달할 수 있다.

const fco = function () { //1. 변수 fco에 함수 저장
  return n => n + 1 //3. return 값이 함수
}

console.log(fco) //2. fco가 console.log() 함수의 인자로 전달

// 도전과제 -> num_101 변수에 101을 담아야 한다.
const num_101 = fco()(100)
console.log(num_101) // 101
*/

