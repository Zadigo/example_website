<template>
  <!-- <nav class="navbar navbar-expand-lg navbar-dark d-none d-lg-block" style="z-index: 2000;"> -->
  <nav :class="extraClass" class="navbar navbar-expand-lg">
    <div :class="{ 'container': !fluid, 'container-fluid': fluid }">
      
      <!-- Navbar brand -->
      <router-link :to="{ name: 'home' }" class="navbar-brand nav-link">
        <strong>{{ companyDetails.legalName }}</strong>
      </router-link>

      <b-btn @click="$emit('toggleNavigation')" variant="light shadow-none" class="navbar-toggler" aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
        <font-awesome-icon icon="bars" />
      </b-btn>
      
      <div class="collapse navbar-collapse" id="navbarExample01">
        <slot></slot>
        
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item active">
            <a class="nav-link" aria-current="page" href="#intro">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://www.youtube.com/channel/UC5CF7mLQZhvx8O5GODZAhdA" rel="nofollow"
              target="_blank">Learn Bootstrap 5</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://mdbootstrap.com/docs/standard/" target="_blank">Download MDB UI KIT</a>
          </li>
        </ul>

        <b-navbar-nav class="d-flex flex-row">
          <b-nav-item href="#" class="me-3 me-lg-0">
            <b-link class="nav-link">
              <font-awesome-icon :icon="['fab', 'facebook-f']" />
            </b-link>
          </b-nav-item>
        </b-navbar-nav>
      </div>
    </div>
  </nav>
</template>


<script>
export default {
  name: 'BaseNavbar',
  props: {
    fixedTop: Boolean,
    fluid: Boolean,
    theme: {
      type: String,
      default: 'light'
    },
    socials: {
      type: Array,
      default: () => []
    }
  },

  computed: {
      extraClass() {
        var attrs = {
          'fixed-top scrolling-navbar': this.fixedTop,
          'navbar-light': this.theme.includes('light') | !this.fixedTop,
          'navbar-dark': this.theme.includes('dark')
        }

        attrs[this.theme] = true
        attrs['on-top'] = !this.fixedTop

        return attrs
      },

      lightTheme() {
        return this.theme === 'light' | !this.fixedTop
      },

      darkTheme() {
        return this.theme === 'dark'
      }
  }
}
</script>

<style scoped>
  /* .navbar {
    box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
  } */

  /* .navbar .nav-link {
    color: white;
  } */

  .on-top {
    z-index: 2000;
  }
</style>
