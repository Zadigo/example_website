<template>
  <base-home-page>
    <template #intro>
      <base-intro :isFullPage="true" :textWhite="true" :mask="0.5" src="https://images.pexels.com/photos/762084/pexels-photo-762084.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=1200">
        <template>
          <authentication-form @authenticateUser="authenticateUser" fieldType="email" :login="true" />

          <div class="text-separator my-4">
            <span>Or</span>
          </div>

          <v-btn block>
            <font-awesome-icon :icon="['fas', 'google']" class="mr-3" />Google
          </v-btn>
        </template>
      </base-intro>
    </template>
  </base-home-page>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'
export default {
  name: 'Login',
  data() {
    return {
      fields: [
        { type: 'email', placeholder: 'Email' },
        { type: 'password', placeholder: 'Password' },
      ]
    }
  },

  methods: {
    ...mapMutations('authenticationModule', [
      'setTokens'
    ]),
    ...mapActions([
      'formErrorMessages'
    ]),
    authenticateUser(credentials) {
      let { email, password } = credentials
      // Authenticate a user on the backend
      // by logging them in. This receives
      // an access token and a refresh token
      // that can be persisted in the header
      this.$api.auth.login(email, password)
      .then((response) => {
        this.setTokens(response.data)
        // this.$router.push({ name: 'home' })
      })
      .catch((error) => {
        this.formErrorMessages(error.response.data)
      })
    }
  }
}
</script>
