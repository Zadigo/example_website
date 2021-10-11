export default ($axios) => ({
    testApi: () => {
        return $axios({
            method: 'get',
            url: null
        })
    }
})
