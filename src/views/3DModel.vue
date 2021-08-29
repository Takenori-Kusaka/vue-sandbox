<template>
  <v-card>

    <v-card-title>
      <h2>3d model</h2>
    </v-card-title>
    <model-stl src="/na.stl"></model-stl>
    <v-card-actions>
    </v-card-actions>
    
  </v-card>
</template>

<script>
import { ModelStl } from 'vue-3d-model'

export default {
    components: {
        ModelStl
    }
}
</script>
