var formbutton = {
    props: ["formbuttonname"],
    template: "\
    <button type='submit' class='btn-large indigo lighten-1 waves-effect waves-light'>\
        <i class='material-icons left'>create</i>{{ formbuttonname }}\
    </button>\
    "
}

var updateform = {
    components: {formbutton},
    template: "\
    <form @submit.prevent='updateitem'>\
        <div class='row'>\
            <div v-for='field in fields' :key='field.name' :class='\"input-field col s12 \" + field.size'>\
                <input :type='field.type' :name='field.name' :id='field.name' :placeholder='field.placeholder'>\
            </div>\
        </div>\
        <formbutton v-bind:formbuttonname='formbuttonname' />\
    </form>\
    ",
    data() {
        return {
            fields: [
                {type: "text", name: "name", placeholder: "Name", size: "m12 l12"},
                {type: "text", name: "category", placeholder: "Category", size: "m4 l4"},
            ],
            productid: undefined,
            formbuttonname: "Update"
        }
    },
    beforeMount() {
        var self = this
        var url = new URLSearchParams(window.location.search)
        var product = url.get("product")
        if (product) {
            // $.ajax({
            //     type: "GET",
            //     url: "http://example.com",
            //     success: function (response) {
            //         self.$data.product = product
            //     }
            // })
        }
    },
    methods: {
        updateitem: function() {
            window.location.href = "/materialize_for_startups/templates2/dashboard/products2.html"
        }
    }
}

var createform = {
    components: {formbutton},
    template: "\
    <form @submit.prevent='createitem'>\
        <div class='row'>\
            <div v-for='field in fields' :key='field.name' :class='\"input-field col s12 \" + field.size'>\
                <input :type='field.type' :name='field.name' :id='field.name' :placeholder='field.placeholder'>\
            </div>\
        </div>\
        <formbutton v-bind:formbuttonname='formbuttonname' />\
    </form>\
    ",
    data() {
        return {
            fields: [
                {type: "text", name: "name", placeholder: "Name", size: "m12 l12"},
                {type: "text", name: "category", placeholder: "Category", size: "m4 l4"},
                {type: "number", name: "price", placeholder: "Price", size: "m4 l4"}
            ],
            formbuttonname: "Create",
            // testfields: {
            //     "1": [
            //         {type: "text", name: "name", placeholder: "Name", size: "m12 l12"},
            //         {type: "text", name: "category", placeholder: "Category", size: "m4 l4"},
            //         {type: "number", name: "price", placeholder: "Price", size: "m4 l4"}
            //     ],
            //     "2": [
            //         {type: "text", name: "skill", placeholder: "Skill", size: "m12 l12"}
            //     ]
            // },
            // w: []
        }
    },
    // beforeMount() {
    //     var self = this
    //     var params = new URLSearchParams(window.location.search)
    //     var currentstep = params.get("step")

    //     if (currentstep === "" | ! currentstep) {
    //         // Assume that we are at the first
    //         // step directly
    //     }
    //     if (currentstep === "1") {
    //         self.$data.w = self.$data.testfields["1"]
    //     }
    //     if (currentstep === "2") {
    //         self.$data.w = self.$data.testfields["2"]
    //     }
    // },
    methods: {
        createitem: function() {
            window.location.href = "/materialize_for_startups/templates2/dashboard/products2.html"
        },
        // changestep: function() {
        //     var params = new URL(window.location.href)
        //     params.searchParams.set("step", 2)
        // }
    }
}