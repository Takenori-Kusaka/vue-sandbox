<template>
    <VideoPlayer ref="videoPlayer"
                  class="vjs-custom-skin"
                  :options="videoOptions"
                  @play="onPlayerPlay($event)"
                  @ready="onPlayerReady($event)">
    </VideoPlayer>
</template>

<script>
import {VideoPlayer} from 'vue-videojs7'
export default {
  name: "VideoExample",
  components: {
    VideoPlayer
  },
  mounted () {
    const src = "file_example_MP4_480_1_5MG.mp4"
    this.playVideo(src)
  },
  computed: {
    player () {
      return this.$refs.videoPlayer.player
    }
  },
  data() {
    return {
      isPlaying: false,
      videoOptions: {
        autoplay: true,
        controls: true,
        mute: true,
        sources: [
          {
            src: "file_example_MP4_480_1_5MG.mp4",
            type: "video/mp4"
          }
        ]
      }
    }
  },
  methods: {
    onPlayerPlay($event) {
      console.log($event)
    },
    onPlayerReady($event) {
      console.log($event)
    },
    playVideo: function (source) {
      const video = {
        withCredentials: false,
        type: 'application/x-mpegurl',
        src: source
      }
      // this.player.reset() // in IE11 (mode IE10) direct usage of src() when <src> is already set, generated errors,
      this.player.src(video)
      // this.player.load()
      this.player.play()
    }
  }
}
</script>
<style scoped>
  .player {
    position: absolute !important;
    width: 100%;
    height: 60%;
  }
  .vjs-custom-skin {
    height: 60% !important;
  }

  .vjs-custom-skin /deep/ .video-js {
    height: 60%;
  }
</style>