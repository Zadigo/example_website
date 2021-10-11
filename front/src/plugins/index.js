import defaultEndpoints from './api'
import client from '../axiosclient'

export default {
    install: (Vue) => {
        Vue.prototype.$api = {
            todos: defaultEndpoints(client)
        }
    }
}
