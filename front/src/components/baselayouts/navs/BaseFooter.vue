<template>
  <footer
    ref="footer"
    class="text-lg-start"
    :class="footerClasses"
  >
    <div
      v-show="items.length > 0"
      class="py-4 text-center"
    >
      <div class="row p-5">
        <!-- Links -->
        <div
          v-for="(item, index1) in items"
          :key="index1"
          class="col-sm-12 col-md-2 text-md-left"
        >
          <p class="font-weight-bold text-uppercase">
            {{ item.title }}
          </p>
          
          <div
            v-for="(link, index2) in item.links"
            :key="index2"
          >
            <router-link :to="{ name: link.name }">
              {{ link.title }}
            </router-link>
          </div>
        </div>

        <div class="col-sm-12 col-md-2 text-md-left">
          <p class="font-weight-bold text-uppercase">
            {{ $t('address') }}
          </p>
          <p>
            <span class="d-block">15, rue du Château</span>
            <span class="d-block">75001 Paris, France</span>
          </p>
          <p>
            <span class="d-block">info@monsite.fr</span>
            <span class="d-block">Tél : 01 23 45 67 89</span>
          </p>
        </div>

        <div
          v-if="linkToAppStore != undefined || linkToPlayStore != undefined"
          class="col-sm-auto col-md-2"
        >
          <p class="font-weight-bold text-uppercase">
            Our apps
          </p>

          <div class="d-flex flex-column justify-content-center align-items-center">
            <b-link
              aria-label="App Store"
              :href="linkToAppStore"
              target="_blank"
            >
              <b-img
                class="mb-3"
                :src="require('@/assets/appstore.png')"
                width="100"
              />
            </b-link>
            
            <b-link
              aria-label="Play store"
              :href="linkToPlayStore"
              target="_blank"
            >
              <b-img
                :src="require('@/assets/playmarket.png')"
                width="100"
              />
            </b-link>
          </div>
        </div>
      </div>
    </div>

    <hr class="m-0">

    <div class="text-center py-4 align-items-center">
      <p class="mt-3 mb-1">
        Suivez-nous sur les réseaux sociaux
      </p>
      <b-button
        v-for="(social, index) in socials"
        :key="index"
        class="m-1 transparent shadow-none"
        :href="social.url"
        rel="nofollow"
        style="min-width: 62px;"
        target="_blank"
        variant="primary"
      >
        <font-awesome-icon
          class="fa-2x"
          :icon="['fab', social.icon]"
        />
      </b-button>
    </div>

    <div
      id="copyright"
      ref="copyright"
      class="text-center p-3"
    >
      ©{{ currentYear }} {{ $t('copyright') }}: {{ companyDetails.legalName }}
    </div>
  </footer>
</template>

<script>
export default {
  name: 'BaseFooter',
  props: {
    color: {
      type: String,
      default: null
    },
    items: {
      type: Array,
      default: () => { return [] }
    },
    socials: {
      type: Array,
      default: () => { return [] }
    },
    linkToAppStore: {
        type: String,
        default: null
    },
    linkToPlayStore: {
        type: String,
        default: null
    },
    theme: {
      type: String,
      default: 'bg-dark'
    }
  },

  computed: {
    footerClasses() {
      return [
        this.color,
        this.theme
      ]
    }
  }
}
</script>

<style scoped>
  .fa-2x {
    font-size: 18px;
  }

  .bg-dark a, .bg-dark p, .bg-dark #copyright {
    --bs-text-opacity: 1;
    color: rgba(var(--bs-light-rgb),var(--bs-text-opacity)) !important;
  }

  #copyright {
    background-color: rgba(0, 0, 0, 0.2)
  }
</style>
