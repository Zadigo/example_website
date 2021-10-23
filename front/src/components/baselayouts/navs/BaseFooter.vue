<template>
  <footer
    ref="footer"
    :class="footerClasses"
    class="text-lg-start"
  >
    <div
      v-show="items.length > 0"
      class="py-4 text-center"
    >
      <div class="row p-5">
        <!-- Links -->
        <div
          v-for="(item, index) in items"
          :key="index"
          class="col-sm-12 col-md-2 text-md-left"
        >
          <p class="font-weight-bold text-uppercase">
            {{ item.title }}
          </p>
          
          <div
            v-for="(link, index) in item.links"
            :key="index"
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
              :href="linkToAppStore"
              target="_blank"
              aria-label="App Store"
            >
              <b-img
                :src="require('@/assets/appstore.png')"
                width="100"
                class="mb-3"
              />
            </b-link>
            
            <b-link
              :href="linkToPlayStore"
              target="_blank"
              aria-label="Play store"
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
        :href="social.url"
        style="min-width: 62px;"
        variant="primary"
        class="m-1 transparent shadow-none"
        rel="nofollow"
        target="_blank"
      >
        <font-awesome-icon
          :icon="['fab', social.icon]"
          class="fa-2x"
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
    linkToAppStore: String,
    linkToPlayStore: String,
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
