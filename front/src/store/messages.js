var _ = require('lodash')

var messagesModule = {
    state: () => ({
        items: []
    }),

    mutations: {
        addMessage(state, message) {
            state.items.push(message)
        },

        clearStack(state) {
            state.items = []
        }
    },

    actions: {
        errorMessage({ commit }, message) {
            // Adds an error message to the stack -;
            // expects a text message
            var base = { type: 'danger', message: message }
            commit('addMessage', base)
        },

        formErrorMessages({ commit, dispatch }, payload) {
            commit('clearStack')
            // This special method deals with errors
            // that comes from forms since they return
            // dictionnaries as {field: [..., ...]}
            var keys = Object.keys(payload)
            var errors = []

            _.forEach(keys, (key) => {
                var values = payload[key]
                if (typeof(values) == 'string') {
                    errors.push(`${key}: ${values}`)
                } else {
                    _.forEach(values, (error) => {
                        errors.push(`${key}: ${error}`)
                    })
                }
            })

            _.forEach(errors, (error) => {
                dispatch('errorMessage', error)
            })
        }
    }
}

export {
    messagesModule
}
