<template>
  <v-card>

    <v-card-title>
      <h2>video example</h2>
    </v-card-title>
    <v-divider/>
    <v-select
      v-model="target_video"
      :items="target_video_list"
      label="Select video"
      outlined
    ></v-select>
    <vue-core-video-player-myself
      ref="vplayer1"
      style="height=30vh;width=30vw"
      :src="target_video"
      :controls="false"
      :autoplay="false"
      :muted="true"
      :loop="false"
      @loadeddata="getDuration"
      @timeupdate="timeUpdate"
      >
    </vue-core-video-player-myself>
    <vue-core-video-player
      ref="vplayer2"
      style="height=30vh;width=30vw"
      :src="target_video"
      :controls="false"
      :autoplay="false"
      :muted="true"
      :loop="false"
      @loadeddata="getDuration"
      @timeupdate="timeUpdate"
      >
    </vue-core-video-player>

    <v-card-actions>
      <v-btn v-if="!isPlaying" color=success @click="play">Play</v-btn>
      <v-btn v-else color=primary @click="stop">Stop</v-btn>
      <v-btn @click="debug">debug</v-btn>
      <v-slider
        v-model="seak"
        hint="Seak bar"
        :max="seak_max"
        :min="0"
        :step="0.1"
        @change="updateCurrenttime"
      ></v-slider>
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
      isPlaying: false,
      seak_max: 0.0,
      seak: 0.0,
      target_video: 'video_files/file_example_MP4_480_1_5MG.mp4',
      target_video_list: [
        'video_files/file_example_MP4_480_1_5MG.mp4',
        'video_files/Sample MP4 Video File for Testing.mp4',
        'video_files/sample_640x360.mp4',
        'video_files/sample-mp4-file.mp4',
      ]
    }
  },
  methods: {
    play($event) {
      console.log($event)
      this.isPlaying=true
      this.$refs.vplayer1.play()
      this.$refs.vplayer2.play()
    },
    stop($event) {
      console.log($event)
      this.$refs.vplayer1.pause()
      this.$refs.vplayer2.pause()
      this.isPlaying=false
    },
    getDuration($event) {
      console.log($event)
      this.seak_max = $event.target.duration
    },
    updateCurrenttime($event) {
      console.log($event)
      console.log(this.$refs.vplayer)
      this.$refs.vplayer.videoCore.$video.currentTime = this.seak
    },
    timeUpdate($event) {
      console.log($event)
      this.seak = $event.target.currentTime
    },
    debug() {
      console.log(this.$refs.vplayer1)
      console.log(this.$refs.vplayer2)
    }
  }
}
</script>
