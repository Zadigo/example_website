import axios from 'axios'

var client = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/',
    // baseURL: 'https://jsonplaceholder.typicode.com/',
    withCredentials: true,
    responseType: 'json'
})

client.interceptors.request.use(
    request => {
        return request
    },

    error => {
        return Promise.reject(error)
    }
)

export default client
