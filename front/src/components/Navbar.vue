<template>
  <m-navbar
    :fixed-top="false"
    :fluid="true"
    theme="dark"
    :theme-shadow="false"
    :transparent="true"
    :isAuthenticated="userIsAuthenticated"
  >
    <template>
      <b-navbar-nav class="navbar-nav me-auto mb-2 mb-lg-0">
        <b-nav-item v-if="!userIsAuthenticated" :to="{ name: 'login' }">
          Login
        </b-nav-item>
        <b-nav-item @click="logoutUser" v-if="userIsAuthenticated" href="#">
          Logout
        </b-nav-item>
        <b-nav-item :to="{ name: 'pricing' }">
          Pricing
        </b-nav-item>
        <b-nav-item v-if="userIsAuthenticated" :to="{ name: 'profile' }">
          Profile
        </b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="d-flex flex-row">
        <b-nav-item
          class="me-3 me-lg-0"
          href="#"
        >
          <b-link class="nav-link">
            <font-awesome-icon :icon="['fab', 'facebook-f']" />
          </b-link>
        </b-nav-item>
        <b-nav-item
          class="me-3 me-lg-0"
          href="#"
        >
          <b-link class="nav-link">
            <font-awesome-icon :icon="['fab', 'instagram']" />
          </b-link>
        </b-nav-item>
      </b-navbar-nav>

      <base-i18n-selection class="pl-0" />
    </template>
  </m-navbar>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Navbar',
  computed: {
    ...mapGetters('authenticationModule', [
      'userIsAuthenticated'
    ])
  },

  methods: {
    logoutUser() {
      this.$store.commit('authenticationModule/resetAuthentication')
    }
  }
}
</script>
