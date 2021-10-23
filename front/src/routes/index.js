import Vue from 'vue'
import Router from 'vue-router'
import i18n from '../plugins/i18n'
import store from '../store'
// import client from '../axiosclient'

// Routes
import homeRoutes from './home'

Vue.use(Router)

var router = new Router({
    mode: 'history',
    routes: [
        ...homeRoutes,

        // Test for i18n
        // {
        //     path: '/',
        //     redirect: `/${i18n.locale}`
        // },
        // {
        //     path: '/:lang',
        //     component: {
        //         render(c) { return c('router-view') }
        //     },
        //     children: [
        //         // ...homeRoutes,
        //         {
        //             path: 'about',
        //             name: 'about',
        //             component: () => import('../views/TestLang.vue')
        //         }
        //     ]
        // },
        {
            path: '*',
            // alias: '/404',
            component: () => import(/* webpackChunkName: "error" */'../views/404.vue')
        }
    ],
    scrollBehavior: () => { window.scroll(0, 0) }
})

router.beforeEach((to, from, next) => {
    // Set the default language for the app
    // on each requests. English being the
    // default language to use
    var language = to.params['lang']
    if (!language) { language = 'en' }
    i18n.locale = language

    // Views that require authentication where
    // the user is not logged in should return
    // to the login page
    if (to.meta.requiresAuthentication && !store.getters['authenticationModule/userIsAuthenticated']) {
        console.log(to.meta.requiresAuthentication && !store.getters['authenticationModule/userIsAuthenticated'])
        next({ name: 'login' })
    }

    // If the user is already authenticated and the token has
    // expired, we need to refresh the access token from 
    // the backend and receive a new one
    // if (to.meta.requiresAuthentication && store.getters['authenticationModule/userIsAuthenticated']) {
    //     client({
    //         method: 'post',
    //         url: '/token/refresh'
    //     })
    //     .then((response) => {
    //         store.commit('authenticationModule/setTokens', response.data)
    //     })
    //     .catch((error) => {
    //         next({ name: 'login' })
    //     })
    // }

    next()
})

export default router
