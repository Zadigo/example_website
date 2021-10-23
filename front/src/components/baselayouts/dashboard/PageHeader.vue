<template>
  <b-card class="my-3">
    <h2>
      <router-link
        class="text-primary"
        :to="{ name: 'home' }"
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
