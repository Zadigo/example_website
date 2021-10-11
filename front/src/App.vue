<template>
  <div id="app">
    <v-app>

      <transition name="general-transition" mode="out-in">
        <router-view :key="$route.name" />
      </transition>
    
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900');
@import url('./assets/style.css')
</style>
