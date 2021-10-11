import Vue from 'vue'
import App from './App.vue'

// Store + Router + Vuetify
import vuetify from './plugins/vuetify'
import globalPlugins from './plugins'
import router from './routes'
import store from './store'

// Mixins
import globalMixin from './mixins'

// Styling
require('../node_modules/bootstrap/dist/css/bootstrap.min.css')

// Plugins
Vue.use(globalPlugins)

// Mixin
Vue.mixin(globalMixin)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,

  render: h => h(App),
}).$mount('#app')
