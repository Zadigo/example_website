<template>
  <section
    id="hero"
    :class="bodyColor"
  >
    <header role="heading">
      <!-- Navbar -->
      <slot name="navbar" />

      <!-- Intro -->
      <slot name="intro" />
    </header>

    <!-- Content -->
    <slot />

    <!-- Footer -->
    <slot name="footer" />
  </section>
</template>

<script>
export default {
  // This is a skeleton for a website's
  // home page. Can be extended or impleted
  // for home page view
  
  name: 'BaseHomePage',
  props: {
    bodyColor: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped>
  @media (min-width: 991.98px) {
    main {
      padding-left: 0px;
    }
  }
</style>
