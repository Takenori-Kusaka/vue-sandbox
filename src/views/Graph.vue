<template>
  <v-card>

    <v-card-title>
      <h2>apex graph example</h2>
    </v-card-title>

    <apexchart width="500" type="bar" :options="options" :series="series"></apexchart>
    <v-card-actions>
      <v-btn v-if="!isPlaying" color=success @click="play">Play</v-btn>
      <v-btn v-else color=primary @click="stop">Stop</v-btn>
      <v-slider
        v-model="seak"
        hint="Seak bar"
        :max="100"
        :min="0"
        :step="1"
      ></v-slider>
    </v-card-actions>
    
  </v-card>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
export default {
  name: "ApexGraphExample",
  components: {
    apexchart: VueApexCharts
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
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
        }
      },
      series: [{
        name: 'series-1',
        data: [30, 40, 45, 50, 49, 60, 70, 91]
      }]
    }
  },
  methods: {
    play($event) {
      console.log($event)
      this.isPlaying=true
    },
    stop($event) {
      console.log($event)
      this.isPlaying=false
    }
  }
}
</script>
