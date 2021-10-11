export default ($axios) => ({
    getTodos: () => {
        return $axios({
            method: 'get',
            url: '/todos'
        })
    }
})
