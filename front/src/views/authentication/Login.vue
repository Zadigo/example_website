<template>
  <base-home-page>
    <template #intro>
      <base-intro
        :is-full-page="true"
        :mask="0.5"
        src="https://images.pexels.com/photos/762084/pexels-photo-762084.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=1200"
        :text-white="true"
      >
        <template>
          <authentication-form field-type="email" :form-messages="formMessages" :login="true" @authenticateUser="authenticateUser" />

          <div class="text-separator my-4">
            <span>Or</span>
          </div>

          <v-btn block>
            <font-awesome-icon
              class="mr-3"
              :icon="['fas', 'google']"
            />Google
          </v-btn>
        </template>
      </base-intro>
    </template>
  </base-home-page>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'
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

  computed: {
    ...mapState({
      formMessages: (state) => { return state.messagesModule.items }
    }),
  },

  methods: {
    ...mapMutations('authenticationModule', [
      'setTokens', 'clearStack'
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
        this.clearStack()
        this.$router.push({ name: 'home' })
      })
      .catch((error) => {
        this.formErrorMessages(error.response.data)
      })
    }
  }
}
</script>
