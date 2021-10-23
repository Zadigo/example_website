<template>
  <div id="app">
    <v-app>
      <transition
        name="general-transition"
        mode="out-in"
      >
        <router-view :key="$route.name" />
      </transition>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App',

  mounted() {
    var body = document.getElementsByTagName('body').item(0)
    body.style.backgroundColor = '#fbfbfb'
    body.style.color = '#4f4f4f'
    body.style.lineHeight = 1.6
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900');
/* @import url('https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.6.0/mdb.min.css'); */
@import url('./assets/style.css');
@import url('./assets/dashboard.css');
</style>
