<template>
  <div class="container">
    <search-bar @inputChange="onInputChange"></search-bar>
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from "./components/SearchBar"
import VideoList from "./components/VideoList"
import VideoDetail from "./components/VideoDetail"

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'app',
  data() {
    return {
      videos: [],
      selectedVideo: null,
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    onVideoSelect(video) {
      console.log(video)
      this.selectedVideo = video
    },
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          //1. (required) 위에서 가져온 키
          key: API_KEY,
          //2. (option) 특정 리소스 유형만 검색(channel, playlist, video)
          type: 'video',
          //3. (required) API 응답이 포함하는 search 리소스 속성
          part: 'snippet',
          //4. (option) string -> 검색어(사용자에게 받은 input value)
          q: inputValue
        }
      })
      .then(response => {
        console.log(response)
        this.videos = response.data.items
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style>

</style>
