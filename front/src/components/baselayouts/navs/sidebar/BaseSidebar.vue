<template>
  <b-sidebar
    id="sidebar-1"
    :no-header="true"
    body-class="d-flex flex-column flex-shrink-0 p-4"
    title="Sidebar"
    :visible="visible"
    left
  >
    <ul class="nav nav-pills flex-column mb-auto">
      <slot name="navItems" />
    </ul>
    
    <hr>

    <b-dropdown
      id="dropdown-1"
      :lazy="true"
      class="d-flex align-items-center text-white text-decoration-none"
      text="Other"
      dropleft
    >
      <b-dropdown-item>New project...</b-dropdown-item>
      <b-dropdown-item>Settings</b-dropdown-item>
      <b-dropdown-item>Profile</b-dropdown-item>
      <b-dropdown-divider />
      <b-dropdown-item>Sign out</b-dropdown-item>
    </b-dropdown>
  </b-sidebar>
</template>

<script>
export default {
  name: 'BaseSidebar',
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped>  
  /* .bg-dark a, .bg-dark ul, .bg-dark li {
    color: #fff;
  } */

  /* .bg-light.text-dark {
    color: black;
  } */
</style>
