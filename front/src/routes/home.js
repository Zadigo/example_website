var homeRoutes = [
    {
        name: 'home',
        path: '/',
        component: () => import(/* webpackChunkName: "home" */'../views/Home.vue')
    }
]

export default homeRoutes
