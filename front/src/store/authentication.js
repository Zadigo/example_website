var _ = require('lodash')

var authenticationModule = {
    namespaced: true,
    
    state: () => ({
        accessToken: null,
        refreshToken: null,
        userId: null,

        isAuthenticated: false,
        isAdmin: false,
        isActive: false,
        isSuperUser: false,
        isStaff: false,

        userProfile: {}
    }),

    mutations: {
        setTokens(state, payload) {
            // Sets the necessary tokens for
            // indicating that the user 
            // is authenticated
            state.accessToken = payload.access
            state.refreshToken = payload.refresh
            state.isAuthenticated = true
            state.userId = payload.user_id
            state.userProfile = {}
            localStorage.setItem('crd', JSON.stringify(payload))
        },

        resetAuthentication(state) {
            // Logs out the user by removing resetting
            // the necessary fields in the module
            state.accessToken = null
            state.refreshToken = null
            state.isAuthenticated = false
            state.userId = null
            localStorage.removeItem('crd')
        },

        setUserProfile(state, payload) {
            state.userProfile = payload
        }
    },

    getters: {
        userIsAuthenticated(state) {
            // Returns a boolean that indicates
            // whether a user is authenticated by
            // checking if there an access token,
            // a refresh token and that isAuthenticated
            // is set to true
            var logic = [
                state.isAuthenticated,
                !_.isNull(state.accessToken),
                !_.isNull(state.refreshToken)
            ]
            return _.every(logic, (item) => {
                return item == true
            })
        }
    }
}

export {
    authenticationModule
}
