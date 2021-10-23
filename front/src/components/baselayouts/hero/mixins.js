var imageMixin = {
    methods: {
        getBackgroundUrl(url) {
            return `url(${url})`
        }
    }
}

var sectionMixin = {
    props: {
        color: {
            type: String,
            default: null
        },
        sectionId: {
            type: String,
            default: 'base--section'
        },
        src: {
            type: String,
            default: null
        },
        theme: {
            type: String,
            default: 'light'
        },
        textWhite: Boolean
    }
}

export {
    imageMixin,
    sectionMixin
}
