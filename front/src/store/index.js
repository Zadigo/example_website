import Vue from 'vue'
import Vuex from 'vuex'

// Modules
import { authenticationModule } from './authentication'
import { messagesModule } from './messages'

Vue.use(Vuex)

var store = new Vuex.Store({
    state: () => ({}),

    modules: {
        authenticationModule,
        messagesModule
    }
})

export default store
