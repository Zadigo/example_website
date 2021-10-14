<template>
  <footer :class="`bg-${ color }`" class="text-lg-start">
    <div v-show="items.length > 0" class="py-4 text-center">
      <div class="row">

        <div v-for="(item, index) in items" :key="index" class="col-2">
          <p>{{ item.title }}</p>
          
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
      <b-button v-for="(social, index) in companyDetails.socials" :key="index" :href="social.url" style="min-width: 62px;" variant="primary" class="m-1" rel="nofollow" target="_blank">
        <font-awesome-icon :icon="['fab', social.icon]" />
      </b-button>
      <!-- <a href="https://www.youtube.com/channel/UC5CF7mLQZhvx8O5GODZAhdA" class="btn btn-primary m-1" role="button"
        rel="nofollow" target="_blank">
        <i class="fab fa-youtube"></i>
      </a>
      <a href="https://www.facebook.com/mdbootstrap" class="btn btn-primary m-1" role="button" rel="nofollow"
        target="_blank">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a href="https://twitter.com/MDBootstrap" class="btn btn-primary m-1" role="button" rel="nofollow"
        target="_blank">
        <i class="fab fa-twitter"></i>
      </a>
      <a href="https://github.com/mdbootstrap/mdb-ui-kit" class="btn btn-primary m-1" role="button" rel="nofollow"
        target="_blank">
        <i class="fab fa-github"></i>
      </a> -->
    </div>

    <div class="text-center p-3" id="copywrite" style="background-color: rgba(0, 0, 0, 0.2);">
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
      default: 'dark'
    },
    items: {
      type: Array,
      default: () => { return [] }
    }
  }
}
</script>

<style scoped>
  .bg-dark a, .bg-dark p, .bg-dark #copywrite {
    --bs-text-opacity: 1;
    color: rgba(var(--bs-light-rgb),var(--bs-text-opacity))!important;
  }
</style>
