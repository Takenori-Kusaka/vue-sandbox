<template>
  <v-card>

    <v-card-title>
      <h2>3d model</h2>
    </v-card-title>
    <!--<model-stl ref="model" src="/na.stl" @on-click="onClick"></model-stl>-->
    <model-collada src="/na.dae"></model-collada>
    <model-collada src="/na_freecad.dae"></model-collada>
    <v-card-actions>
    </v-card-actions>
    
  </v-card>
</template>

<script>
import { ModelCollada } from 'vue-3d-model'
import { ModelStl } from 'vue-3d-model'

export default {
    components: {
      ModelCollada,
      ModelStl
    },
    methods: {
      onClick ($event){
        console.log($event)
      }
    }
}
</script>
