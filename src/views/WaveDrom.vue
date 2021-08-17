<template>
  <v-card>

    <v-card-title>
      <h2>wavedrom example</h2>
    </v-card-title>
    <script type="WaveDrom">
        {{ signal }}
        </script>
    <v-card-actions>
    </v-card-actions>
    
  </v-card>
</template>

<script>
export default {
  name: "WaveDrom",
  components: {
  },
  mounted () {
    WaveDrom.ProcessAll()
  },
  computed: {
  },
  watch: {
    signal: {
      handler: function () {
        WaveDrom.ProcessAll()
      },
      deep: true
    }
  },
  data() {
    return {
      intarval: 0,
      external: '',
      signal: { signal : [
        { name: "clk",  wave: "p......" },
        { name: "wire", wave: "0.1..0." },
      ]}
    }
  },
  methods: {
  }
}
</script>
