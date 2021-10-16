<template>
  <base-home-page>
    <template v-slot:navbar>
      <base-navbar :fixedTop="false" theme="bg-secondary dark" />
    </template>

    <template v-slot:intro>
      <base-intro :image="'https://picsum.photos/1200'">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <h1 class="hero-lead text-white">This a great thing to do</h1>
              <p class="hero-lead-300 text-white">What can we do today for you</p>
              <b-btn v-b-modal.modal-1 size="lg">Visit website</b-btn>

              <!-- <b-modal modalClass="right" dialogClass="modal-side modal-top-right" :hideFooter="true" :hideHeader="true" :centered="false" size="md" id="modal-1" title="BootstrapVue">
                Show something here
              </b-modal> -->
              <extended-modal positionY="top" :hideFooter="true" :hideHeader="true" :centered="false" size="md" id="modal-1" title="BootstrapVue">
              </extended-modal>
            </div>
          </div>
        </div>
      </base-intro>
    </template>

    <template>
      <div class="container">
        <div class="row">
          <div class="col-12">
            <modern-benefits />
          </div>
        </div>
      </div>

      <!-- <image-grid :items="[{ url: 'https://picsum.photos/600' }, { url: 'https://picsum.photos/800' }, { url: 'https://picsum.photos/900' }, { url: 'https://picsum.photos/950' }, { url: 'https://picsum.photos/810' }, { url: 'https://picsum.photos/890' }]" /> -->
    </template>
  </base-home-page>
</template>

<script>
import ExtendedModal from "../components/navs/ExtendedModal.vue"

export default {
  components: { ExtendedModal },
  name: 'Home',

  data() {
    return {
      showSidebar: false,
      footerColumns: [
        { title: 'Home', links: [{ title: 'Home', name: 'home' }, { title: 'Contact', name: 'home' }] },
        { title: 'Contact', links: [{ title: 'Contact', name: 'home' }] }
      ]
    }
  }
}
</script>

<style>
  /* .navbar .nav-link {
    color: #fff !important;
  }

  @media (min-width: 991.98px) {
    main {
      padding-left: 0px;
    }
  } */

</style>
