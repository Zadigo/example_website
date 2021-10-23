<template>
  <b-card class="my-3">
    <h2>
      <router-link
        :to="{ name: 'home' }"
        class="text-primary"
      >
        Home
      </router-link> / {{ currentPage }}
    </h2>
  </b-card>
</template>

<script>
export default {
  name: 'PageHeader',
  props: {
    currentPage: {
      type: String,
      required: true
    }
  }
}
</script>
