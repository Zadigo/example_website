import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

var router = new Router({
    mode: 'history',
    routes: [

    ],
    scrollBehavior: () => { window.scroll(0, 0) }
})

export default router
