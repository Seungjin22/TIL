const axios = require('axios')

axios.get('https://jsonplaceholder.typicode.com/posts')

.then(res => {
  console.log(res)
})
.catch(err => {
  console.log(err)
})