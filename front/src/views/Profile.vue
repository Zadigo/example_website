<template>
  <section>
    My profile
  </section>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Profile',
  beforeMount() {
    this.$api.profile.get(this.userId)
    .then((response) => {
      this.$store.commit('authenticationModule/setUserProfile', response.data)
    })
    .catch((error) => {
      console.error(error)
    })
  },

  computed: {
    ...mapState('authenticationModule', [
      'userProfile', 'userId'
    ])
  }
}
</script>
