var PROJECT = PROJECT || (function () {
    var token = null

    var setToken = (token) => {
        this.token = token
    }

    var getToken = () => {
        return this.token
    }

    var init = {
        setToken,
        getToken
    }

    return {
        init
    }
})()
