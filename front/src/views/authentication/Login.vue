<template>
  <base-fullpage-intro image="https://mdbootstrap.com/img/new/fluid/city/018.jpg">
    <template>
      <b-card>
        <b-form>
          <div v-for="(field, index) in fields" :key="index" class="form-group">
            <b-input :type="field.type" :placeholder="field.placeholder" class="my-2"></b-input>
          </div>
        </b-form>

        <template class="text-right" footer>
          <b-button>Login</b-button>
        </template>
      </b-card>
    </template>
  </base-fullpage-intro>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      fields: [
        { type: 'email', placeholder: 'Email' },
        { type: 'password', placeholder: 'Password' },
      ]
    }
  }
}
</script>
