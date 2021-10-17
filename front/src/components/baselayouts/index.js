import { CTAInputGroup } from './extended'
import { BaseBenefit, BaseBenefits, BaseBrands, BaseCTA, BaseFullpageIntro, BaseHomePage, BaseIntro, BaseJumbotron, BaseModernBenefits, BasePricing, BaseSection, leadTitle, MapIntro } from './hero'
import { BaseFooter, BaseNavbar, BaseNavItem, BaseSidebar, SidebarInterface } from './navs'


export default {
    install: (Vue) => {
        Vue.component('base-intro', BaseIntro)
        Vue.component('base-fullpage-intro', BaseFullpageIntro),
        Vue.component('base-jumbotron', BaseJumbotron),
        Vue.component('base-home-page', BaseHomePage),
        Vue.component('base-brands', BaseBrands),
        Vue.component('base-section', BaseSection),
        Vue.component('base-benefits', BaseBenefits),
        Vue.component('base-benefit', BaseBenefit),
        Vue.component('base-modern-benefits', BaseModernBenefits),
        Vue.component('base-cta', BaseCTA),
        Vue.component('base-map-intro', MapIntro)
        Vue.component('base-pricing', BasePricing)

        // Navs
        Vue.component('base-navbar', BaseNavbar)
        Vue.component('base-footer', BaseFooter)

        // Utilities
        Vue.component('cta-input-group', CTAInputGroup)
        Vue.component('lead-title', leadTitle)

        // Sidebar
        Vue.component('base-sidebar', BaseSidebar)
        Vue.component('sidebar-interface', SidebarInterface)
        Vue.component('base-nav-item', BaseNavItem)

        // Mixins
        Vue.mixin({
            computed: {
                testMethod() {
                    return true
                }
            }
        })

        // Directives
        // Vue.directive('padding-one', {
        //     inserted: (el) => {
        //         el
        //     }
        // })
    }
}
