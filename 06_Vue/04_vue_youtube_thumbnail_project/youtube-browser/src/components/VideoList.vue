<template>
  <ul class="col-lg-4 list-group">
    <video-list-item
    v-for="video in videos"
    :key="video.etag"
    :video="video"
    @videoSelect="onVideoSelect"
    >
    </video-list-item>
  </ul>
</template>

<script>
import VideoListItem from "./VideoListItem"

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    onVideoSelect(video) {
      this.$emit('videoSelect', video)
    }
  }
}
</script>

<style>

</style>