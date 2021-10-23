import axios from 'axios'
import store from './store'
var _ = require('lodash')

var client = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/',
    headers: {
        'Content-Type': 'application/json'
    },  
    // baseURL: 'https://jsonplaceholder.typicode.com/',
    withCredentials: true,
    responseType: 'json'
})

client.interceptors.request.use(
    request => {
        var accessToken = store.state.authenticationModule.accessToken
        if (!_.isNull(accessToken)) {
            request.headers['Authorization'] = `Token ${accessToken}`
        }
        return request
    },

    error => {
        // TODO: Integrate a code for
        // forbidden requests here?
        return Promise.reject(error)
    }
)

client.interceptors.response.use(
    response => {
        return response
    },

    error => {
        // On the slightest response error
        // in such as 401 (Unauthorized) or 403
        // (forbidden), completly log off the user
        // to eventually protect against a non
        // authenticated request
        var errors = [401, 403]
        if (errors.includes(error.request.status)) {
            store.commit('authenticationModule/resetAuthentication')
        }
        return Promise.reject(error)
    }
)

export default client
