<template>
  <div>
    <input @change="onInput" type="text">
  </div>
</template>

<script>
//1. 트리거: input값 변경(@input)
// - 인자: event(e)
// - 실행 함수: onInput

//2. 트리거: input 내 $emit(inputChange)
// - 인자: 변경된 input 값(inputValue)
// - 실행 함수: onInputChange

export default {
  name: 'SearchBar',
  methods: {
    onInput(e) {
      // console.log(e.target.value)
      this.$emit('inputChange', e.target.value)
    }
  }
}
</script>

<style scoped>
  input {
    width: 75%;
  }
  div {
    text-align: center;
    margin: 20px;
  }
</style>