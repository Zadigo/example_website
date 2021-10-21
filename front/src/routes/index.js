import Vue from 'vue'
import Router from 'vue-router'
import i18n from '../plugins/i18n'

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
    var language = to.params['lang']
    if (!language) {
        language = 'en'
    }
    i18n.locale = language

    if (to.meta.requiresAuthentication) {
        next()
    } else {
        next()
    }
})

export default router
