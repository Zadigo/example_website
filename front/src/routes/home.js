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
    }
]

export default homeRoutes
