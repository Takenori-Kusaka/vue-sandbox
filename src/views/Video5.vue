<template>
  <v-card  flat>

    <v-card-title>
      <h2>video example</h2>
    </v-card-title>
    <video ref="myvideo"
    src="file_example_MP4_480_1_5MG.mp4"
    type="video/mp4"
    width="400"></video>

    <v-card-actions>
      <v-btn color=success :disabled="isPlaying" @click="play">Play</v-btn>
      <v-btn flat color=primary :disabled="!isPlaying" @click="stop">Stop</v-btn>
      <v-spacer></v-spacer>
      <v-btn icon><v-icon>bookmark</v-icon></v-btn>
    </v-card-actions>
    
  </v-card>
</template>

<script>
export default {
  name: "VideoExample",
  components: {
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
    play() {
      this.$refs.myvideo.play()
      this.isPlaying = true
    },
    stop() {
      this.$refs.myvideo.pause()
      this.isPlaying = false
    }
  }
}