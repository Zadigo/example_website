import Vue from 'vue'
import Vuetify from 'vuetify'

// Styling
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'

// Colors
// import colors from 'vuetify/lib/util/color'

Vue.use(Vuetify)

export default new Vuetify({
    icons: {
        iconfont: 'mdi'
    }
})
