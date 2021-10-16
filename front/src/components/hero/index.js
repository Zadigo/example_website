import BaseIntro from './BaseIntro'
import BaseFullpageIntro from './BaseFullpageIntro.vue'
import BaseJumbotron from './BaseJumbotron.vue'
import BaseHomePage from './BaseHomePage.vue'
import BaseBrands from './BaseBrands.vue'
import BaseSection from './BaseSection.vue'
import BaseBenefits from './BaseBenefits.vue'
import BaseModernBenefits from './BaseModernBenefits.vue'
import BaseCTA from './BaseCTA.vue'
import MapIntro from './MapIntro.vue'

// import CarouselIntro from './CarouselIntro.vue'
// import InputGroup from './InputGroup.vue'
// import ImageGrid from './ImageGrid.vue'

// import { TestComponent  } from "./TestComponent"

export default {
    install: (Vue) => {
        Vue.component('base-section', BaseSection)
        Vue.component('base-intro', BaseIntro)
        Vue.component('base-fullpage-intro', BaseFullpageIntro)
        Vue.component('base-jumbotron', BaseJumbotron)
        Vue.component('base-home-page', BaseHomePage)
        Vue.component('map-intro', MapIntro)

        Vue.component('base-brands', BaseBrands)
        Vue.component('base-cta', BaseCTA)
        Vue.component('base-modern-benefits', BaseModernBenefits)
        Vue.component('base-benefits', BaseBenefits)

        
        // Vue.component('carousel-intro', CarouselIntro)
        // Vue.component('input-group', InputGroup)
        // Vue.component('image-grid', ImageGrid)
    }
}
