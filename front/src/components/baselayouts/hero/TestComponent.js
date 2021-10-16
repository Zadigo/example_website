import Vue from 'vue'

export const TestComponent = Vue.extend({
    name: 'BaseHomePage',
    props: {
        color: {
            type: String,
            default: null
        }
    },
    mounted() {
        if (this.color != null) {
            this.$refs.linkSection.style.backgroundColor = this.color
        }
    },
    methods: {
        makeHeader(h) {
            const $header = h(
                'header', {
                    attrs: {
                        role: 'heading'
                    }
                }
            )
            return $header
        }
    },
    render(h) {
        return h(
            'section', 
            {
                attrs: { id: 'hero' }, 
                ref: 'linkSection'
            }, 
            [`${this.$slots}`]
        )
    }
})
