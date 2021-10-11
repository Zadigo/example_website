var homeRoutes = [
    {
        name: 'home',
        path: '/',
        component: () => import(/* webpackChunkName: "home" */'../views/TestPage.vue')
    }
]

export default homeRoutes
