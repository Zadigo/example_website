import client from '../axiosclient'

import companyDetails from '../data/company.json'

import defaultEndpoints from './api'
import authentication from './api/authentication'
import profile from './api/profile'

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
            todos: defaultEndpoints(client),
            auth: authentication(client),
            profile: profile(client)
        }
        
        Vue.mixin(globalMixin)
    }
}
