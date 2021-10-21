<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <b-card class="position-relative">
          <b-img :src="src" fluid />

          <h1 class="font-weight-bold text-uppercase title position-absolute t-50 l-5">
            <slot></slot>
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
      src: String
    }
}
</script>

<style scoped>
  h1 {
    font-size: 5rem;
    color: white;
  }
</style>
