<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <b-card class="position-relative">
          <b-img
            fluid
            :src="src"
          />

          <h1 class="font-weight-bold text-uppercase title position-absolute t-50 l-5">
            <slot />
          </h1>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'BaseErrorPage',
    props: {
      src: {
        type: String,
        default: null
      }
    }
}
</script>

<style scoped>
  h1 {
    font-size: 5rem;
    color: white;
  }
</style>
