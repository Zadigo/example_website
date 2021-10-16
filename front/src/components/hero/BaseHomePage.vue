<template>
  <section id="hero">
    <header role="heading">
      <!-- Navbar -->
      <slot name="navbar"></slot>

      <!-- Intro -->
      <slot name="intro"></slot>
    </header>

    <!-- Content -->
    <slot></slot>

    <!-- Footer -->
    <slot name="footer"></slot>
  </section>
</template>

<script>
export default {
  // This is a skeleton for a website's
  // home page. Can be extended or impleted
  // for home page view
  name: 'BaseHomePage'
}
</script>

<style scoped>
  @media (min-width: 991.98px) {
    main {
      padding-left: 0px;
    }
  }
</style>
