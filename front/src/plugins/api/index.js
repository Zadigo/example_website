export default ($axios) => ({
    getTodos: (limit, offset) => {
        limit = limit | 50
        offset = offset | 50

        return $axios({
            method: 'get',
            url: `/todos?limit=${limit}&offset=${offset}`
        })
    }
})
