<template>
  <section id="hero">
    <header>
      <!-- Navbar -->
      <general-navbar />

      <!-- Intro -->
      <base-intro image="https://mdbootstrap.com/img/new/fluid/city/018.jpg">
        <template>
          <div class="text-white">
            <h1 class="mb-3">Learn Bootstrap 5 with MDB</h1>
            <h5 class="mb-4">Best & free guide of responsive web design</h5>
            <router-link :to="{ name: 'home' }" class="btn btn-outline-light btn-lg m-2">
              Start tutorial
            </router-link>
          </div>
        </template>
      </base-intro>

    </header>

    <!-- <main class="mt-5">
      <div class="container">
        
      </div>
    </main> -->

    <!-- Footer -->
    <base-footer :items="footerColumns" color="dark" />
  </section>
</template>

<script>
import BaseIntro from "../components/home/BaseIntro.vue"

export default {
  components: { BaseIntro },
  name: 'Home',

  data() {
    return {
      footerColumns: [
        { title: 'Home', links: [{ title: 'Home', name: 'home' }, { title: 'Contact', name: 'home' }] },
        { title: 'Contact', links: [{ title: 'Contact', name: 'home' }] }
      ]
    }
  }
}
</script>

<style>
  .navbar .nav-link {
    color: #fff !important;
  }

  @media (min-width: 991.98px) {
    main {
      padding-left: 0px;
    }
  }
</style>
