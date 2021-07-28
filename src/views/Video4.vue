<template>
  <v-card  flat>

    <v-card-title>
      <h2>video example</h2>
    </v-card-title>
    <video-player :options="videoOptions"></video-player>
    <v-card-actions>
      <v-btn color=success>Click #1</v-btn>
      <v-btn flat color=primary>Click #2</v-btn>
      <v-spacer></v-spacer>
      <v-btn icon><v-icon>bookmark</v-icon></v-btn>
    </v-card-actions>
    
  </v-card>
</template>

<script>
import VideoPlayer from "@/components/VideoPlayer.vue";

export default {
	name: "VideoExample",
	components: {
		VideoPlayer
	},
	data() {
		return {
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
	}
}