/*
const nothing = () => {}

console.log('start')
setTimeout(nothing, 3000)
console.log('end')


function sleep_3s() {
  setTimeout(() =>{
    console.log('Wake up Javascript!!!')
  }, 3000)
}

console.log('Start Sleeping!!')
sleep_3s()
console.log('End of Program!!')


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
setTimeout(second, 1000)
third()
*/

console.log('Hello')

setTimeout(function cb1(){
  console.log('cb1')
}, 5000)

console.log('ByeBye')