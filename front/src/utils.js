var parsePaginationUrl = (url) => {
    // Takes a url that includes pagination
    // e.g. ?limit=100&offset=100 and parses
    // it in order to get the limit and offset
    // parameters
    if (url == undefined) {
        return { limit: 50, offset: 50, hasNext: false }
    }

    var obj = new URL(url)
    var hasNext = false

    return {
        limit: obj.searchParams.get('limit'), 
        offset: obj.searchParams.get('offset'),
        hasNext: hasNext
    }
}



export {
    parsePaginationUrl
}
