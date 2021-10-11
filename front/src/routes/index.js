import Vue from 'vue'
import Router from 'vue-router'

// Routes
import homeRoutes from './home'

Vue.use(Router)

var router = new Router({
    mode: 'history',
    routes: [
        ...homeRoutes
    ],
    scrollBehavior: () => { window.scroll(0, 0) }
})

export default router
