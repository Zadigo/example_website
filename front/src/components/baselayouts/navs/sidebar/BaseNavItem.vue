<template>
  <li class="nav-item">
    <router-link
      aria-current="page"
      class="nav-link"
      :to="{ name: linkName, params: linkParams }"
    >
      <font-awesome-icon
        class="mr-3"
        :icon="icon"
      /> {{ name }}
    </router-link>

    <hr v-if="divider">
  </li>
</template>

<script>
export default {
  name: 'BaseNavItem',
  props: {
    name: {
      type: String,
      default: null
    },
    linkName: {
      type: String,
      default: null
    },
    linkParams: {
      type: Object,
      default: () => {}
    },
    icon: String,
    divider: Boolean
  }
}
</script>

<style scoped>
  .router-link-exact-active,
  .router-link-active {
    color: #fff;
    background-color: #1266f1;
    box-shadow: 0 2px 5px 0 rgb(0 0 0 / 20%), 0 2px 10px 0 rgb(0 0 0 / 10%);
  }
</style>
