<template>
  <b-card :class="formClasses">
    <template #header>
      <slot name="authFormHeader">
        <h1 class="h3">
          <span v-if="login">Login</span>
          <span v-else>Signup</span>
        </h1>
      </slot>
    </template>
    
    <b-form class="p-4">
      <base-form-messages :form-messages="formMessages" />

      <div
        v-for="(field, index) in fields"
        :key="index"
        class="form-group"
      >
        <b-input
          v-model="credentials[field.name]"
          :autocomplete="field.autocomplete"
          class="my-2"
          :name="field.name"
          :placeholder="field.placeholder"
          :type="field.type"
        /> 
      </div>
    </b-form>
    
    <slot name="policy" />

    <!-- <div class="form-group p-1">
      <b-form-checkbox id="consent" name="consent">
        I authorize whatever to happen
      </b-form-checkbox>
    </div> -->

    <template
      #footer
      class="text-right"
    >
      <b-btn
        variant="primary"
        @click="authenticateUser"
      >
        <span v-if="login">Login</span>
        <span v-else>Signup</span>
      </b-btn>
    </template>
  </b-card>
</template>

<script>
import BaseFormMessages from './BaseFormMessages.vue'
var _ = require('lodash')

export default {
  name: 'AuthenticationForm',
  components: { BaseFormMessages },
  props: {
    fieldType: {
      type: String,
      default: 'email'
    },
    login: {
      type: Boolean,
      default: true
    },
    transparent: {
      type: Boolean,
      default: true
    },
    formMessages: {
      type: Array,
      default: () => []
    }
  },

  data() {
    return {
      credentials: {},
      baseFields: [
        [
          { type: 'email', name: 'email', placeholder: 'Email', autocomplete: 'email' },
          { type: 'text', name: 'username', placeholder: 'Username', autocomplete: 'username' }
        ],
        { type: 'password', name: 'password', placeholder: 'Password', autocomplete: 'current-password' }
      ]
    }
  },

  computed: {
    formClasses() {
      return [
        {
          'card-transparent': this.transparent
        }
      ]
    },

    fields() {
      if (this.login) {
        return [
          this.requiresEmail ? this.baseFields[0][0] : this.baseFields[0][1],
          this.baseFields[1]
        ]
      } else {
        // The form can display either the username 
        // or email field or both
        if (this.requiresEmail) {
          return [
            this.baseFields[0][0],
            ...this.passwordFields()
          ]
        } else if (this.requiresUsername) {
          return [
            this.baseFields[0][1],
            ...this.passwordFields()
          ]
        } else if (this.requiresBoth) {
          return [
            this.baseFields[0][0],
            this.baseFields[0][1],
            ...this.passwordFields()
          ]
        } else {
          return []
        }
      }
    },

    requiresUsername() {
      return this.fieldType === 'username'
    },

    requiresEmail() {
      return this.fieldType === 'email'
    },
    
    requiresBoth() {
      return this.fieldType === 'both'
    },
  },

  methods: {
    passwordFields() {
      var fields = []
      var field = _.filter(this.baseFields, ['name', 'password'])[0]
      field['autocomplete'] = 'new-password'

      var field1 = {...field}
      var field2 = {...field}
      field1['name'] = 'password1'
      field2['name'] = 'password2'
      
      fields.push(field1)
      fields.push(field2)
      return fields
    },

    authenticateUser() {
      this.$emit('authenticateUser', this.credentials)
      this.credentials = {}
    }
  }
}
</script>

<style scoped>
  .card-transparent {
    background-color: rgb(255, 255, 255, .3)
  }
</style>
