const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')

module.exports = {
  mode: 'development',
  // entry: 여러 개의 js 파일의 시작점 (웹팩이 파일을 읽기 시작하는 지점)
  entry: {
    app: path.join(__dirname, 'src', 'main.js')
  },
  // module: 웹팩은 js만 변환이 가능하기 때문에 html, css 같은 모듈을 통해서 웹팩이 이해할 수 있는 것으로 변환을 해주는 곳
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader',
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader']
      }
    ]
  },
  // plugins: 웹팩을 통해서 번들된 결과물을 추가적으로 처리하는 부분(옵션)
  plugins: [
    new VueLoaderPlugin(),
  ],
  // output: 여러 개의 js 파일을 하나로 만들어낸 결과물
  output: {
    filename: 'app.js',
    path: path.join(__dirname, 'dist')
  },
}