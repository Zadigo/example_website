import Vue from 'vue'
import App from './App.vue'

import i18n from './plugins/i18n'

// Store + Router + Vuetify
import vuetify from './plugins/vuetify'
import globalPlugins from './plugins'
import router from './routes'
import store from './store'

// Styling
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Mixins
import globalMixin from './mixins'

// Plugins
import baselayouts from './components/baselayouts'

// Styling
require('../node_modules/bootstrap/dist/css/bootstrap.min.css')
require('../node_modules/bootstrap-vue/dist/bootstrap-vue.css')
require('./assets/mdb.css')
library.add(fas, fab)

// Plugins
Vue.use(globalPlugins)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

// import hero from './components/hero'
// import navs from './components/navs'
// import extended from './components/extended'
// Vue.use(hero)
// Vue.use(navs)
// Vue.use(extended)
Vue.use(baselayouts)

// components

// require('./components/navs')
// require('./components/hero')
Vue.component('font-awesome-icon', FontAwesomeIcon)

// Mixin
Vue.mixin(globalMixin)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  i18n,

  render: h => h(App),
}).$mount('#app')
