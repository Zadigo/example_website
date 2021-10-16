// import Vue from 'vue'
import BaseFooter from './BaseFooter'
import BaseNavbar from './BaseNavbar.vue'

// Vue.component('base-footer', BaseFooter)
// Vue.component('base-navbar', BaseNavbar)


export default {
    install: (Vue) => {
        Vue.component('base-navbar', BaseNavbar)
        Vue.component('base-footer', BaseFooter)
    }
}
