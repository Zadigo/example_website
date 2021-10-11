import defaultEndpoints from './api'
import client from '../axiosclient'

export default {
    install: (Vue) => {
        Vue.prototype.$api = {
            global: defaultEndpoints(client)
        }
    }
}
