var homeRoutes = [
    {
        name: 'home',
        path: '/',
        component: () => import(/* webpackChunkName: "home" */'../views/TestPage.vue'),
        meta: { requiresAuthentication: false }
    }
]

export default homeRoutes
