import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import VideoPlayer from 'vue-videojs7'
import VueCoreVideoPlayer from 'vue-core-video-player'

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

Vue.use(VideoPlayer)
Vue.use(VueCoreVideoPlayer)