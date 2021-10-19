<template>
  <!-- class="ml-auto" -->
  <b-navbar-nav>
    <b-nav-item-dropdown :text="lang">
      <b-dropdown-item @click="changeLanguage(lang)" v-for="(lang, index) in $i18n.availableLocales" :key="index">
        {{ lang }}
      </b-dropdown-item>
    </b-nav-item-dropdown>
  </b-navbar-nav>
</template>

<script>
export default {
  name: 'I18nSelection',
  
  data() {
    return {
      lang: null
    }
  },

  beforeMount() {
    this.lang = this.$i18n.locale
  },

  methods: {
    changeLanguage(lang) {
      this.lang = lang
      this.$router.push({ params: { 'lang': lang } })
    }
  }
}
</script>
