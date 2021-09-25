var profileApi = ($axios) => ({
    updatePreferences: (data) => {
        return $axios({
            method: 'post',
            url: '/accounts/profile/contact-preferences',
            data
        })
    }
})

var globalPlugin = {
    install: (Vue, options) => {
        var repositories = {
            profile: profileApi(client)
        }
        Vue.prototype.$api = repositories
    }
}
