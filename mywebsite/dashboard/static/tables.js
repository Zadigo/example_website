var vuetable_two = {
    props: ["products"],
    template: "\
    <div class='card-table'>\
        <table>\
            <thead>\
                <tr>\
                    <th @click='dosort(title.name)' v-if='title.sortable' v-for='title in titles' :key='title.id' class='sortable' :class='{sorted: title.sorted}'>{{ title.name|capitalize }}</th>\
                    <th v-else>{{ title.name|capitalize }}</th>\
                </tr>\
            </thead>\
            <tbody>\
                <tr v-if='!product.deleted' v-for='(product, index) in sortedproducts' :key='product.id'>\
                    <td><a :href='\"./details.html?product=\" + product.id'>{{ product.id }}</a></td>\
                    <td>{{ product.name }}</td>\
                    <td>{{ product.surname }}</td>\
                    <td>{{ product.price|euros }}</td>\
                    <td>\
                        <a :href='\"/dashboard/list/\" + product.id + \"/update/\"'><i class='material-icons'>create</i></a>\
                    </td>\
                    <td>\
                        <a @click='deletesingleitem(product.id)'><i class='material-icons'>delete</i></a>\
                    </td>\
                </tr>\
            </tbody>\
        </table>\
    </div>\
    ",
    data() {
        return {
            titles: [
                {id: 1, name: "id", sortable: true, sorted: false},
                {id: 2, name: "name", sortable: true, sorted: false},
                {id: 3, name: "surname", sortable: true, sorted: false},
                {id: 4, name: "price", sortable: true, sorted: false},
                {id: 5, name: "", sortable: false, sorted: false},
                {id: 6, name: "", sortable: false, sorted: false}
            ],
            currentsort: ""
        }
    },
    computed: {
        columncss() {
            var self = this
            self.$data.titles.forEach(title => {
                title.sorted = false
                if (title.name === self.$data.currentsort) {
                    title.sorted = true
                }
            })
        },
        sortbyid() {
            return this.productlist.sort((a, b) => {
                return a - b
            })
        },
        sortbyword() {
            var self = this
            return self.productlist.sort(function(a, b) {
                if (a[self.$data.currentsort] < b[self.$data.currentsort]) {
                    return -1
                }
                if (a[self.$data.currentsort] > b[self.$data.currentsort]) {
                    return 1
                }
                return 0
            })
        },
        productlist() {
            return [...this.$props.products]
        },
        sortedproducts() {
            var self = this
            if (self.$data.currentsort === "") {
                return self.productlist
            }
            if (self.$data.currentsort === "iD") {
                return self.sortbyid
            } else {
                return self.sortbyword
            }
        }
    },
    methods: {
        dosort: function(filtername) {
            var self = this
            self.$data.currentsort = filtername
        },
        selectitem: function(index) {
            this.$emit('selectitem', index)
        },
        selectall: function(index) {
            this.$emit('selectall')
        },
        deletesingleitem: function(productid) {
            this.$emit('deletesingleitem', productid)
        }
    },
    filters: {
        capitalize: function(value) {
            // Capitalize the first
            // letter of the title
            return value.toUpperCase()
        },
        slugify: function(value) {
            // Transforms words such as
            // 'eugenie bouchard' becomes
            // 'eugenie_bouchard'
            value.toLowerCase().replace(" ", "_")
        },
        euros: function(value) {
            return value + "€"
        }
    }
}

var vuetable_one = {
    props: ["products"],
    template: "\
    <table class='highlight responsive-table'>\
        <thead>\
            <tr>\
                <th>\
                    <label>\
                        <input @click='selectall' type='checkbox' name='select_all' id='selct_all' />\
                        <span></span>\
                    </label>\
                </th>\
                <th v-for='title in titles' :key='title.id'>{{ title.name|capitalize }}</th>\
            </tr>\
        </thead>\
        <tbody v-if='nondeletedproducts==0'>Vous n'avez aucun produits</tbody>\
        <tbody v-else>\
            <tr v-if='!product.deleted' v-for='(product, index) in products' :key='product.id'>\
                <td>\
                    <p>\
                        <label>\
                            <input @click='selectitem(index)' type='checkbox' :name='product.name|slugify' :id='product.name|slugify' :checked='product.checked'>\
                            <span></span>\
                        </label>\
                    </p>\
                </td>\
                <td><a :href='\"/dashboard/list/\" + product.id'>{{ product.id }}</a></td>\
                <td>{{ product.name }}</td>\
                <td>{{ product.surname }}</td>\
                <td>{{ product.price|euros }}</td>\
                <td>\
                    <a :href='\"/dashboard/list/\" + product.id + \"/update/\"'><i class='material-icons'>create</i></a>\
                </td>\
                <td>\
                    <a @click='deletesingleitem(product.id)'><i class='material-icons'>delete</i></a>\
                </td>\
            </tr>\
        </tbody>\
    </table>\
    ",
    data() {
        return {
            // titles: ["iD", "name", "surname", "price", "update"]
            titles: [
                {id: 1, name: "id", sortable: true, sorted: false},
                {id: 2, name: "name", sortable: true, sorted: false},
                {id: 3, name: "surname", sortable: true, sorted: false},
                {id: 4, name: "price", sortable: true, sorted: false},
                {id: 5, name: "", sortable: false, sorted: false},
                {id: 6, name: "", sortable: false, sorted: false}
            ],
        }
    },
    methods: {
        selectitem: function(index) {
            this.$emit('selectitem', index)
        },
        selectall: function(index) {
            this.$emit('selectall')
        },
        deletesingleitem: function(productid) {
            this.$emit('deletesingleitem', productid)
        }
    },
    computed: {
        nondeletedproducts() {
            // Keeps track of the products that are
            // not marked as deleted in order to
            // to perform certain actions
            var self = this
            var numberofproducts = self.$props.products.length

            self.$props.products.forEach(product => {
                if (product.deleted === true) {
                    numberofproducts -= 1
                }
            })
            return numberofproducts
        }
    },
    filters: {
        capitalize: function(value) {
            // Capitalize the first
            // letter of the title
            return value.toUpperCase()
        },
        slugify: function(value) {
            // Transforms words such as
            // 'eugenie bouchard' becomes
            // 'eugenie_bouchard'
            value.toLowerCase().replace(" ", "_")
        },
        euros: function(value) {
            return value + "€"
        }
    }
}