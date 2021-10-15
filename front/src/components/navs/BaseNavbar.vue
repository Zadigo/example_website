<template>
  <!-- <nav class="navbar navbar-expand-lg navbar-dark d-none d-lg-block" style="z-index: 2000;"> -->
  <nav ref="link" :class="extraClass" class="navbar navbar-expand-lg">
    <div :class="{ 'container': !fluid, 'container-fluid': fluid }">
      <!-- Navbar brand -->
      <a class="navbar-brand nav-link" target="_blank" href="https://mdbootstrap.com/docs/standard/">
        <strong>{{ companyDetails.legalName }}</strong>
      </a>

      <button class="navbar-toggler" type="button" aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
        <font-awesome-icon icon="bars" />
      </button>
      
      <div class="collapse navbar-collapse" id="navbarExample01">
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

        <!-- <ul class="navbar-nav d-flex flex-row">
          <li class="nav-item me-3 me-lg-0">
            <a class="nav-link" href="https://www.youtube.com/channel/UC5CF7mLQZhvx8O5GODZAhdA" rel="nofollow"
              target="_blank">
              <i class="fab fa-youtube"></i>
            </a>
          </li>
          <li class="nav-item me-3 me-lg-0">
            <a class="nav-link" href="https://www.facebook.com/mdbootstrap" rel="nofollow" target="_blank">
              <i class="fab fa-facebook-f"></i>
            </a>
          </li>
          <li class="nav-item me-3 me-lg-0">
            <a class="nav-link" href="https://twitter.com/MDBootstrap" rel="nofollow" target="_blank">
              <i class="fab fa-twitter"></i>
            </a>
          </li>
          <li class="nav-item me-3 me-lg-0">
            <a class="nav-link" href="https://github.com/mdbootstrap/mdb-ui-kit" rel="nofollow" target="_blank">
              <i class="fab fa-github"></i>
            </a>
          </li>
        </ul> -->
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
    scrollingNavbar: Boolean
  },

  created() {
    // When the user scrolls to a certain level,
    // animate the navbar (size + color)
    window.addEventListener('scroll', () => {
      if (this.scrollingNavbar) {
        // var defaultColor = 'red'

        if (window.scrollY > 30) {
          this.$refs.link.classList.add('scrolling-navbar', 'top-nav-collapse', 'red')
        } else {
          this.$refs.link.classList.remove('top-nav-collapse', 'red')
        }
      }
    })
  },

  destroyed() {
    if (this.scrollingNavbar) {
      window.removeEventListener('scroll', this.$refs.link.classList.remove('scrolling-navbar', 'top-nav-collapse', 'red'))
    }
  },

  computed: {
      extraClass() {
        var attrs = {
          'fixed-top': this.fixedTop | this.scrollingNavbar ? true : false,
          'navbar-light': this.lightTheme,
          'navbar-dark': this.darkTheme,
          'scrolling-navbar': this.scrollingNavbar
        }
        return attrs
      },

      lightTheme() {
        return !this.darkTheme
      },

      darkTheme() {
        return this.theme === 'dark' | this.fixedTop ? true : false
      }
  }
}
</script>

<style scoped>
  .scrolling-navbar {
    padding-top: 12px;
    padding-bottom: 12px;
    transition: background 0.5s ease-in-out, padding 0.5s ease-in-out;
  }

  @media (min-width: 600px) {
    .navbar.scrolling-navbar.top-nav-collapse {
        padding-top: 5px;
        padding-bottom: 5px;
    }
  }
</style>
