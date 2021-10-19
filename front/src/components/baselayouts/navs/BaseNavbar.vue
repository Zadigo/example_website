<template>
  <nav :class="navClasses" class="navbar">
    <div :class="containerClasses">
      
      <!-- Navbar brand -->
      <router-link :to="{ name: 'home' }" class="navbar-brand nav-link">
        <strong>{{ companyDetails.legalName }}</strong>
      </router-link>

      <b-btn @click="$emit('toggleNavigation')" variant="light shadow-none" class="navbar-toggler" aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
        <font-awesome-icon icon="bars" />
      </b-btn>
      
      <!-- Links -->
      <div class="collapse navbar-collapse">
        <slot></slot>
      </div>
    </div>
  </nav>
</template>


<script>
export default {
  name: 'BaseNavbar',
  props: {
    color: {
      type: String,
      default: null
    },
    fixedTop: Boolean,
    fluid: Boolean,
    isAuthenticated: Boolean,
    socials: {
      type: Array,
      default: () => []
    },
    themeShadow: Boolean,
    transparent: Boolean,
    theme: {
      type: String,
      default: 'light'
    }
  },

  computed: {
      navClasses() {
        return [
          'navbar-expand-lg',
          'd-lg-block',
          {
            'fixed-top': this.fixedTop,
            'scrolling-navbar': this.fixedTop,
            [`navbar-${this.theme}`]: true,
            'on-top': !this.fixedTop,
            'navbar-transparent': this.transparent,
            'shadow-none': this.transparent,
            'theme-shadow': this.themeShadow
          },
          this.color
        ]
      },

      containerClasses() {
        return [
          {
            'container': !this.fluid,
            'container-fluid': this.fluid
          }
        ]
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
  .navbar.theme-shadow {
    box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
  }

  .on-top {
    z-index: 1010;
  }
</style>
