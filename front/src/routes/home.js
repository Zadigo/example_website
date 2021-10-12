var homeRoutes = [
    {
        name: 'home',
        path: '/',
        component: () => import(/* webpackChunkName: "home" */'../views/authentication/Login.vue'),
        meta: { requiresAuthentication: false }
    }
]

export default homeRoutes
