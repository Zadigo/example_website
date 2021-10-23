<template>
  <nav
    id="sidebarMenu"
    class="collapse d-lg-block sidebar collapse bg-white"
  >
    <div class="position-sticky">
      <div class="list-group list-group-flush mx-3 mt-4">
        <!-- <b-link v-for="(link, index) in links" :key="index" :to="{ name: 'home' }" class="list-group-item list-group-item-action py-2 ripple">
          <font-awesome-icon :icon="link.icon" class="fa-fw me-3"></font-awesome-icon>
          <span>{{ link.name }}</span>
        </b-link> -->

        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
          aria-current="true"
        >
          <i class="fas fa-tachometer-alt fa-fw me-3" /><span>Main dashboard</span>
        </a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple active"
        >
          <i class="fas fa-chart-area fa-fw me-3" /><span>Webiste traffic</span>
        </a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        ><i class="fas fa-lock fa-fw me-3" /><span>Password</span></a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        ><i class="fas fa-chart-line fa-fw me-3" /><span>Analytics</span></a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        >
          <i class="fas fa-chart-pie fa-fw me-3" /><span>SEO</span>
        </a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        ><i class="fas fa-chart-bar fa-fw me-3" /><span>Orders</span></a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        ><i class="fas fa-globe fa-fw me-3" /><span>International</span></a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        ><i class="fas fa-building fa-fw me-3" /><span>Partners</span></a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        ><i class="fas fa-calendar fa-fw me-3" /><span>Calendar</span></a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        ><i class="fas fa-users fa-fw me-3" /><span>Users</span></a>
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 ripple"
        ><i class="fas fa-money-bill fa-fw me-3" /><span>Sales</span></a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'BaseSidebar',
  data() {
    return {
      links: [
        { name: 'Main dashboard', icon: 'tachometer'},
        { name: 'Website traffic', icon: 'chart-area'},
        { name: 'Password', icon: 'lock'},
      ]
    }
  }
}
</script>

<style scoped>
  /* .list-group-item {
    position: relative;
    display: block;
    padding: .5rem 1.5rem;
    color: #262626;
    text-decoration: none;
    background-color: #fff;
    border: 1px solid rgba(0,0,0,.125);
  }

  .sidebar .active, .sidebar .router-link-exact-active, .sidebar .router-link-active {
    border-radius: 5px;
    box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
  }

  .list-group-item + .list-group-item.active + .list-group.router-link-exact-active + .list-group.router-link-active {
    margin-top: -1px;
    border-top-width: 1px;
  } */
</style>
