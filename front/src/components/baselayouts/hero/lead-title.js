import Vue from 'vue'

var leadTitle = Vue.extend({
    props: {
        color: String,
        size: {
            type: Number,
            default: 4
        }
    },
    directives: {
        space: {
            inserted: (el) => {
                el.style.marginBottom = '3rem'
            }
        }
    },
    computed: {
        leadClasses() {
            return {
                class: ['font-weight-bold', 'text-white', this.color],
                style: {
                    'font-size': `${this.size}rem`
                },
                ref: 'leadTitle'
            }
        }
    },
    render(h) {
        return h('h1', this.leadClasses, [this.$slots.default])
    }
})

export {
    leadTitle
}
