<template>
  <v-app>
    <v-system-bar
      app
      color="primary"
    >
      <v-spacer></v-spacer>
      <v-icon>mdi-wifi-strength-4</v-icon>
      <v-icon>mdi-signal-cellular-outline</v-icon>
      <v-icon>mdi-battery</v-icon>
      <span>12:30</span>
    </v-system-bar>

    <v-navigation-drawer app flat dark v-model="drawer" stateless  absolute clipped>
      <v-list>
        <v-list-item class="px-2">
          <v-list-item-avatar>
            <v-img src="https://randomuser.me/api/portraits/men/11.jpg"></v-img>
          </v-list-item-avatar>

          <v-list-item-title>John Doe</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item v-for="item in navbarlist" :key="item.route" :to="item.route">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>{{ item.title }}</v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      color="deep-purple accent-4"
      dense
      clipped-left flat
      dark
    >
      <v-app-bar-nav-icon  @click.stop="drawer=!drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Sandbox</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-menu
        left
        bottom
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <template v-slot:extension>
        <v-tabs align-with-title fixed-tabs color="white">
          <v-tabs-slider color="yellow"></v-tabs-slider>
          <v-tab><v-icon>mdi-home</v-icon></v-tab>
          <v-tab><v-icon>mdi-magnify</v-icon></v-tab>
          <v-tab><v-icon>mdi-account</v-icon></v-tab>
        </v-tabs>
      </template>
    </v-app-bar>

    <v-main app>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>

        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>
    <v-footer app>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  components: {
  },

  data: () => ({
    drawer: false,
    navbarlist: [
        {icon: 'mdi-home', title:'Home', route:'/'},
        {icon: 'mdi-table', title:'Cgrid', route:'/cgrid'},
        {icon: 'mdi-video', title:'Video', route:'/video'},
        {icon: 'mdi-text', title:'Search Word', route:'/search_word'},
        {icon: 'mdi-graph', title:'ApexGraph', route:'/graph'},
        {icon: 'mdi-square-wave', title:'WaveDrom', route:'/wave'},
        {icon: 'mdi-cube-outline', title:'3DModel', route:'/3DModel'},
    ],
    //
  }),
};
</script>
