export default ($axios) => ({
    // Endpoints for login in, signing up
    // or x a given user
    
    login(email, password) {
        return $axios({
            method: 'post',
            url: '/token',
            data: {
                email: email,
                password: password
            }
        })
    },

    refreshToken() {
        // When the access token expires,
        // we need to get a new pair of
        // tokens for the user
        return $axios({
            method: 'post',
            url: '/token/refresh'
        })
    }
})
