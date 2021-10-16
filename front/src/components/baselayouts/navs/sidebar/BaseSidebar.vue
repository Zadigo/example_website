<template>
  <b-sidebar :noHeader="true" bodyClass="d-flex flex-column flex-shrink-0 p-4" id="sidebar-1" title="Sidebar" :visible="visible" left>
    <ul class="nav nav-pills flex-column mb-auto">
      <slot name="navItems"></slot>
    </ul>
    
    <hr>

    <b-dropdown :lazy="true" class="d-flex align-items-center text-white text-decoration-none" id="dropdown-1" text="Other" dropleft>
      <b-dropdown-item>New project...</b-dropdown-item>
      <b-dropdown-item>Settings</b-dropdown-item>
      <b-dropdown-item>Profile</b-dropdown-item>
      <b-dropdown-divider></b-dropdown-divider>
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
