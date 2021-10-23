export default ($axios) => ({
    get(userId) {
        return $axios({
            method: 'get',
            url: `/profile/${userId}/`
        })
    },
})
