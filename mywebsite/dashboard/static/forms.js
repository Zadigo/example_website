var currentpagefields = [
    {page: 1, fields: [
            {type: "text", name: "name", placeholder: "Name", size: "m12 l12"},
            {type: "text", name: "category", placeholder: "Category", size: "m4 l4"},
            {type: "number", name: "price", placeholder: "Price", size: "m4 l4"}
        ]
    },
    {page: 2, fields: [
        {type: "text", name: "domaine", placeholder: "Domaine", size: "m12 l12"}
    ]},
    {page: 3, fields: [
        {type: "text", name: "domaine", placeholder: "Element", size: "m12 l12"}
    ]}
]

var linkbutton = {
    props: ["formbuttonname", "icon"],
    template: "\
    <a @click='saveasdraft' class='btn-large red lighten-1 waves-effect waves-light'>\
        <i class='material-icons left'>{{ icon }}</i>{{ formbuttonname }}\
    </a>\
    ",
    methods: {
        saveasdraft: function() {
            $.ajax({
                type: "POST",
                url: "/api/v1/product/create",
                data: {draft: true},
                dataType: "json",
                success: function (response) {
                    window.location.href = "/dashboard/list/"
                },
                error: function() {
                    console.log("An error occured")
                }
            });
        }
    }
}

var formbutton = {
    props: ["formbuttonname", "icon"],
    template: "\
    <button type='submit' class='btn-large indigo lighten-1 waves-effect waves-light'>\
        <i class='material-icons left'>{{ icon }}</i>{{ formbuttonname }}\
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
                {type: "number", name: "price", placeholder: "Price", size: "m4 l4"},
            ],
            productid: undefined,
            formbuttonname: "Update"
        }
    },
    beforeMount() {
        var self = this
        var url = new URL(window.location)
        var product = url.pathname
        var r = /^\/dashboard\/list\/(\d+)\/update\/$/g
        var regexmatch = r.exec(window.location.pathname)
        $.ajax({
            type: "GET",
            url: "/api/v1/product/" + regexmatch[1],
            data: "json",
            success: function (response) {
                console.log(response)
            }
        });
        
    },
    methods: {
        updateitem: function() {
            window.location.href = "/dashboard/list"
        }
    }
}

var createform = {
    components: {formbutton, linkbutton},
    template: "\
    <form @submit.prevent='createitem'>\
        <div class='row'>\
            <div v-for='field in currentfields' :key='field.name' class='input-field col s12' :class='field.size'>\
                <input v-model='completedfields[field.name]' :type='field.type' :name='field.name' :id='field.name' :placeholder='field.placeholder'>\
            </div>\
        </div>\
        <linkbutton v-if='currentstep >= 2' v-bind:formbuttonname='\"Save to draft\"' v-bind:icon='\"watch_later\"' />\
        <formbutton v-bind:formbuttonname='formbuttonname' v-bind:icon='icon' />\
    </form>\
    ",
    data() {
        return {
            fields: [],
            formbuttonname: "Continuer",
            icon: "create",
            completedfields: {},
            currentstep: 1,
            maxsteps: 3,
            created: false,
            productid: undefined
        }
    },
    beforeMount() {
        var fields = currentpagefields.filter(field => {
            return field.page == 1
        })
        this.$data.fields = fields[0].fields
    },
    computed: {
        isfinalstep() {
            return this.$data.currentstep == this.$data.maxsteps
        },
        currentfields() {
            var self = this
            var fields = currentpagefields.filter(field => {
                return field.page == self.$data.currentstep
            })
            return fields[0].fields
        }
    },
    methods: {
        createitem: function() {
            var self = this
            var data = {
                newitem: self.$data.newitem,
                update: false
            }
            if (self.$data.created) {
                data["update"] = true
            }
            if (self.$data.productid !== undefined) {
                data["product_id"] = self.$data.productid
            }
            $.ajax({
                type: "POST",
                url: "/api/v1/product/create",
                data: data,
                dataType: "json",
                success: function (response) {
                    self.$data.productid = response.product_id
                    self.changestep()
                    // window.location.href = "/dashboard/list"
                },
                error: function (response) {
                    console.log("An error occured")
                }
            })
        },
        changestep: function() {
            if (this.$data.currentstep * 1 == 1) {
                this.$data.created = true
            }

            // Change button name on the before last step
            if (this.$data.currentstep == this.$data.maxsteps - 1) {
                this.$data.icon = "done"
                this.$data.formbuttonname = "Terminer"
            }

            if (this.$data.currentstep === this.$data.maxsteps) {
                window.location.href = "/dashboard/list/"
            } else {
                this.$data.completedfields = {}
                this.$data.currentstep = this.$data.currentstep + 1
            }
        }
    }
}