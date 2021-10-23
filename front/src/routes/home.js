var homeRoutes = [
    {
        name: 'home',
        path: '/',
        component: () => import(/* webpackChunkName: "home" */'../views/Home.vue')
    },
    {
        name: 'pricing',
        path: '/pricing',
        component: () => import(/* webpackChunkName: "pricing" */'../views/Pricing.vue')
    },
    {
        name: 'login',
        path: '/login',
        component: () => import(/* webpackChunkName: "pricing" */'../views/authentication/Login.vue'),
    },
    {
        name: 'profile',
        path: '/profile',
        component: () => import(/* webpackChunkName: "profile" */'../views/Profile.vue'),
        meta: { requiresAuthentication: true }
    },
    {
        name: 'test_page',
        path: '/tests',
        component: () => import(/* webpackChunkName: "tests" */'../views/TestPage.vue')
    }
]

export default homeRoutes
