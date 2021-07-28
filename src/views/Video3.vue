<template>
  <v-card  flat>

    <v-card-title>
      <h2>video example</h2>
    </v-card-title>
    <video class="video" ref="video">
      <source src="file_example_AVI_480_750kB.avi" type="video/avi">
    </video>
    <video class="video" ref="video">
      <source src="file_example_MP4_480_1_5MG.mp4" type="video/mp4">
    </video>
    <v-card-actions>
      <v-btn color=success>Click #1</v-btn>
      <v-btn flat color=primary>Click #2</v-btn>
      <v-spacer></v-spacer>
      <v-btn icon><v-icon>bookmark</v-icon></v-btn>
    </v-card-actions>
    
  </v-card>
</template>
<script>
export default {
  name: 'service',
  components: {
  },
  mounted() {
    console.log('this is current player instance object', this.player)
  },
  computed: {
  },
  data () {
    return {
      video: {
        sources: [{
        src: 'file_example_MP4_480_1_5MG.mp4',
        type: 'video/mp4'
      }],
      options: {
        autoplay: true,
        volume: 0.6,
        poster: 'http://covteam.u.qiniudn.com/poster.png'
        }
      }
    }
  },
  methods: {
    // listen event
    onPlayerPlay(player) {
      console.log('player play!', player)
    },
    onPlayerPause(player) {
      console.log('player pause!', player)
    },
    // ...player event

    // or listen state event
    playerStateChanged(playerCurrentState) {
      console.log('player current update state', playerCurrentState)
    },

    // player is ready
    playerReadied(player) {
      console.log('the player is readied', player)
      // you can use it to do something...
      // player.[methods]
    }
  }
}
</script>