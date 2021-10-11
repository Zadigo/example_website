import defaultEndpoints from './api'
import client from '../axiosclient'

var globalMixin = {
    data() {
        return {
            currentYear: null
        }
    }
}

export default {
    install: (Vue) => {
        Vue.prototype.$api = {
            todos: defaultEndpoints(client)
        }
        
        Vue.mixin(globalMixin)
    }
}
