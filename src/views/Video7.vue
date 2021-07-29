<template>
  <v-card>

    <v-card-title>
      <h2>video example</h2>
    </v-card-title>
    <vue-core-video-player
      ref="vplayer"
      src="file_example_MP4_480_1_5MG.mp4"
      :controls="false"
      :autoplay="false"
      :muted="true"
      :loop="false"
      >
    </vue-core-video-player>

    <v-card-actions>
      <v-btn color=success :disabled="isPlaying" @click="play">Play</v-btn>
      <v-btn color=primary :disabled="!isPlaying" @click="stop">Stop</v-btn>
    </v-card-actions>
    
  </v-card>
</template>

<script>
export default {
  name: "VideoExample",
  components: {
  },
  mounted () {
  },
  computed: {
  },
  data() {
    return {
      isPlaying: false
    }
  },
  methods: {
    play($event) {
      console.log($event)
      this.$refs.vplayer.play()
    },
    stop($event) {
      console.log($event)
      this.$refs.vplayer.pause()
    },
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