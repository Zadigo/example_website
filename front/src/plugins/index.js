import defaultEndpoints from './api'
import client from '../axiosclient'
import companyDetails from '../data/company.json'

var globalMixin = {
    data() {
        return {
            currentYear: null,
            companyDetails: companyDetails
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
