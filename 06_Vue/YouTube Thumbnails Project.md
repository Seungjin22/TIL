# YouTube Thumbnails Project





![image](https://user-images.githubusercontent.com/22102664/68562531-76e76f00-048d-11ea-874b-0e60c1b4fb17.png)

![image](https://user-images.githubusercontent.com/22102664/68562700-1d337480-048e-11ea-95bc-39ed55a3da1b.png)

![1573461158386](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1573461158386.png)

```text
$ vue create youtube-browser

? Please pick a preset: default (babel, eslint)
```



데이터는 단방향으로만 흐른다.

부모에서 업데이트가 되면 자식 데이터는 자동 갱신



console.developers.google.com

새 프로젝트 만들기

YouTube Data API v3

사용자 인증 정보 ==> 사용자 인증 정보 만들기 ==> API  키



```text
$ touch .env.local
```

`.env.local`에서

```text
VUE_APP_YOUTUBE_API_KEY=키값
```

```vue
<script>
  // App.vue

  const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
</script>
```



VideoDetail에서는 props에 required = true, 생략