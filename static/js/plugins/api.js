var profileApi = ($axios) => ({
    updatePreferences: (data) => {
        return $axios({
            method: 'post',
            url: '/accounts/profile/contact-preferences',
            data
        })
    }
})

var Api = {
    install: (Vue, options) => {
        var repositories = {
            profile: profileApi(axiosClient)
        }
        Vue.prototype.$api = repositories
    }
}
