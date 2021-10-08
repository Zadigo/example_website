var client = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    headers: { 'Content-Type': 'application/json' },
    responseType: 'json',
    withCredentials: true
})


client.interceptors.request.use(
    request => {
        if (request.method == 'post') {
            request.headers['X-CSRFToken'] = PROJECT.init.getToken()
        }
        return request
    },

    error => {
        return Promise.reject(error)
    }
)

// client.defaults.headers.common['X-CSRFToken'] = "{{ csrf_token }}"
