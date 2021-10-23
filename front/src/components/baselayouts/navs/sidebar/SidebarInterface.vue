<template>
  <header>
    <!-- Sidebar -->
    <slot name="side" />

    <!-- Nav/Heading -->
    <slot name="heading" />

    <!-- Content -->
    <div class="container">
      <div class="row">
        <div class="col-12">
          <slot />
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  // An interface that allows the user to
  // include the sidebar and the content
  // of the page -; with a slight modification
  // of the container to fit with the sidebar
  name: 'SidebarInterface',
  props: {
    navbarVisibility: {
      type: Boolean,
      default: true
    }
  }
}
</script>

<style scoped>
  .container {
    padding-left: 290px;
  }
</style>
