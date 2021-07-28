<template>
  <video-player  class="video-player vjs-custom-skin"
                  ref="videoPlayer"
                  :playsinline="true"
                  :options="videoPlayerOptions"
                  @play="onPlayerPlay($event)"
                  @pause="onPlayerPause($event)"
                  @ended="onPlayerEnded($event)"
                  @waiting="onPlayerWaiting($event)"
                  @playing="onPlayerPlaying($event)"
                  @loadeddata="onPlayerLoadeddata($event)"
                  @timeupdate="onPlayerTimeupdate($event)"
                  @canplay="onPlayerCanplay($event)"
                  @canplaythrough="onPlayerCanplaythrough($event)"
                  @statechanged="playerStateChanged($event)"
                  @ready="playerReadied"
  ></video-player>
</template>

<script>
     // Import components
  import {videoPlayer} from 'vue-video-player'

  export default {
    name: 'VideoPlayer',
    components: {
      videoPlayer
    },
    data () {
      return {
        video:'', //Specific video
        fileType: 'mp4', // resource type
        videoUrl: 'file_example_MP4_480_1_5MG.mp4', // The path address of the resource
        posterUrl:''    //Cover address
      }
    },
    mounted(){
      
    },
    methods:{
             // Play callback
      onPlayerPlay(player) {
        console.log('player play!', player)
      },

             // Pause callback
      onPlayerPause(player) {
        console.log('player pause!', player)
      },

             // Callback after the video is played
      onPlayerEnded($event) {
        console.log($event)
        this.$refs.videoPlayer.player.src(this.fileUrl)
      },

             // ReadyState changes on DOM elements cause playback to stop
      onPlayerWaiting($event) {
        console.log($event)
      },

             // has started playing callback
      onPlayerPlaying($event) {
        console.log($event)
      },

             // Triggered when the player downloads data at the current playback position
      onPlayerLoadeddata($event) {
        console.log($event)
      },

             // Triggered when the current playback position changes.
      onPlayerTimeupdate($event) {
        console.log($event)
      },

             //The readyState of the media is HAVE_FUTURE_DATA or higher
      onPlayerCanplay(player) {
        console.log('player Canplay!', player)
      },

             //The readyState of the media is HAVE_ENOUGH_DATA or higher. This means that the entire media file can be played without buffering.
      onPlayerCanplaythrough(player) {
        console.log('player Canplaythrough!', player)
      },

             //Playback status change callback
      playerStateChanged(playerCurrentState) {
        console.log('player current update state', playerCurrentState)
      },

             // Bind the listener to the ready state of the component. The difference with the event listener is that if the ready event has occurred, it will immediately trigger the function. .
      playerReadied(player) {
        console.log('example player 1 readied', player);
      },
    },
    computed: {
      videoPlayerOptions () {
        const videoPlayerOptions = {
          playbackRates: [0.75, 1.0, 1.25, 1.5,2.0], //Play speed 
                     autoplay: false, // Whether to play automatically.
                     muted: false, // Whether to mute the playback, by default any audio will be eliminated.
                     loop: false, // Whether to play in a loop.
          preload: 'auto', // It is recommended that the browser<video>Whether the video data should be downloaded after loading the element. The auto browser chooses the best behavior and starts loading the video immediately (if supported by the browser)
          language: 'zh-CN',
          aspectRatio: '3:1', // Put the player in smooth mode and use this value when calculating the dynamic size of the player. The value should represent a ratio-two numbers separated by a colon (e.g."16:9"or"4:3"）
                     fluid: true, // Whether the fluid is scaled proportionally to fit its container.
          flash:{hls:{withCreadentials:false}},//Can play rtmp video
          html5:{hls:{withCreadentials:false}},//Can play m3u8 video
          sources: [{
            type: 'video/' + this.fileType,
                         src: this.videoUrl // video url address
          }],
                     poster: this.posterUrl, // cover address
          width: '100%',
          notSupportedMessage: 'This video is temporarily unavailable...', // Allow to overwrite Video.js and display the default information when it cannot be played.
          controlBar: {
            timeDivider: true,
            durationDisplay: true,
            remainingTimeDisplay: false,
            fullscreenToggle: true
          }
        }
        return videoPlayerOptions
      }
    },
  }
</script>
<style>
  .my_video{
    width: 100%;
    height: calc(100vh - 100px);
    background-color: white;
  }
  .video-js .vjs-big-play-button{
         /*Set the style of the play button*/
    width: 100%;
    height: 100%;
    border-radius: 50%;
  }
</style>