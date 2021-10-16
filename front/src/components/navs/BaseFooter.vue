<template>
  <footer ref="footer" :class="footerClasses" class="text-lg-start">
    <div v-show="items.length > 0" class="py-4 text-center">
      <div class="row">

        <div v-for="(item, index) in items" :key="index" class="col-sm-12 col-md-2">
          <p class="font-weight-bold text-uppercase">{{ item.title }}</p>
          
          <div v-for="(link, index) in item.links" :key="index">
            <router-link :to="{ name: link.name }">
              {{ link.title }}
            </router-link>
          </div>
        </div>

      </div>
    </div>

    <hr class="m-0" />

    <div class="text-center py-4 align-items-center">
      <b-button v-for="(social, index) in socials" :key="index" :href="social.url" style="min-width: 62px;" variant="primary" class="m-1" rel="nofollow" target="_blank">
        <font-awesome-icon :icon="['fab', social.icon]" />
      </b-button>
    </div>

    <div ref="copyright" class="text-center p-3" id="copyright">
      ©{{ currentYear }} Copyright: {{ companyDetails.legalName }}
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
  .bg-dark a, .bg-dark p, .bg-dark #copyright {
    --bs-text-opacity: 1;
    color: rgba(var(--bs-light-rgb),var(--bs-text-opacity)) !important;
  }

  #copyright {
    background-color: rgba(0, 0, 0, 0.2)
  }
</style>
