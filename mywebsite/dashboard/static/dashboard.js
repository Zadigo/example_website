// $(document).ready(function () {
//     $("#trigger-for-sidebar").on("click", function() {
//         // $(".dashboard .wrapper").toggle(".show-side-bar")
//         $(".dashboard .wrapper").toggle("hide")
//     })    
// });


var productdetailsurl = window.location.origin + "/dashboard/products/"

var constructurl = function(id, slug) {
    return  productdetailsurl + id + "/" + slug
}

var updateform = {
    template: "\
    <form @submit.prevent='updateitem'>\
        <div class='row'>\
            <div v-for='field in fields' :key='field.name' :class='\"input-field col s12 \" + field.size'>\
                <input :type='field.type' :name='field.name' :id='field.name' :placeholder='field.placeholder'>\
            </div>\
        </div>\
        <button type='submit' class='btn-large red darken-1'>Update</button>\
    </form>\
    ",
    data() {
        return {
            fields: [
                {type: "text", name: "name", placeholder: "Name", size: "m12 l12"},
                {type: "text", name: "category", placeholder: "Category", size: "m4 l4"},
            ],
            productid: undefined
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
            window.location.href = "/dashboard/list/"
        }
    }
}

var createform = {
    template: "\
    <form @submit.prevent='createitem'>\
        <div class='row'>\
            <div v-for='field in fields' :key='field.name' :class='\"input-field col s12 \" + field.size'>\
                <input :type='field.type' :name='field.name' :id='field.name' :placeholder='field.placeholder'>\
            </div>\
        </div>\
        <button class='btn-large indigo lighten-1 waves-effect waves-light'>Create</button>\
    </form>\
    ",
    data() {
        return {
            fields: [
                {type: "text", name: "name", placeholder: "Name", size: "m12 l12"},
                {type: "text", name: "category", placeholder: "Category", size: "m4 l4"},
                {type: "number", name: "price", placeholder: "Price", size: "m4 l4"}
            ]
        }
    },
    methods: {
        createitem: function() {
            window.location.href = "/dashboard/list/"
        }
    }
}

var messages = {
    template: "\
        <transition name='show_message'>\
            <div v-if='show'>Supprimer un cours est une action irréversible.</div>\
        </transition>\
    ",
    data() {
        return {
            show: false
        }
    }
}

var deletebutton = {
    // This commponent allows the user to
    // delete an item from the database
    // after having selected them

    props: ["selectedproducts"],
    template: "\
        <a @click='deleteitems' class='btn-large' id='delete_product' :disabled='showdeletebutton'>\
            <i class='material-icons left'>delete</i>\
            {{ title }}\
        </a>\
    ",
    data() {
        return {
            title: "Delete"
        }
    },
    computed: {
        showdeletebutton() {
            if (this.$props.selectedproducts.length > 0) {
                return false
            } else {
                return true
            }
        }
    },
    methods: {
        deleteitems: function() {
            this.$emit('deleteitems')
        }
    }
}

var filterproducts = {
    template: "\
    <select id='filter_products'>\
        <option @click='doselect(option.value)' v-for='option in options' :key='option.value' :value='option.value'>{{ option.name }}</option>\
    </select>\
    ",
    data() {
        return {
            options: [
                {value: "all", name: "-----", selected: true},
                {value: "croissant", name: "Croissant", selected: false},
                {value: "decroissant", name: "Décroissant", selected: false},
            ]
        }
    },
    methods: {
        doselect: function(value) {
            this.$data.options.forEach(option => {
                option.selected = false
                if (option.value === value) {
                    option.selected = true
                }
            })
        }
    },
    computed: {
        selectedfilter() {
            return this.$data.options.filter(option => {
                return option.selected === true
            })
        }
    }
}

var vuetable = {
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
                    <th v-for='title in titles' :key='title'>{{ title|capitalize }}</th>\
                </tr>\
            </thead>\
            <tbody>\
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
                    <td><a :href='\"/dashboard/list/\" + product.id + \"/update/\"'><i class='material-icons'>create</i></a></td>\
                </tr>\
            </tbody>\
        </table>\
    ",
    data() {
        return {
            titles: ["iD", "name", "surname", "price", "update"],
        }
    },
    methods: {
        selectitem: function(index) {
            this.$emit('selectitem', index)
        },
        selectall: function(index) {
            this.$emit('selectall')
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

var dashboard = new Vue({
    el: "#vue_dashboard",
    components: {vuetable, deletebutton, filterproducts, createform, 
                    updateform, messages},
    data() {
        return {
            products: [
                {id: 1, name: "Kendall", surname: "Jenner", price: 145, selected: false, checked: false, deleted: false},
                {id: 2, name: "Hailey", surname: "Baldwin", price: 345, selected: false, checked: false, deleted: false},
                {id: 3, name: "Taylor", surname: "Swift", price: 175, selected: false, checked: false, deleted: false}
            ],
            showsidebar: true
        }
    },
    computed: {
        selectedproducts() {
            return this.$data.products.filter(product => {
                return product.selected === true && product.deleted === false
            })
        }
    },
    methods: {
        doselect: function(index) {
            this.$data.products[index].selected = !this.$data.products[index].selected
        },
        getall: function() {
            this.$data.products.forEach(product => {
                product.checked = !product.checked
                product.selected = !product.selected
            })
        },
        applydelete: function() {
            this.selectedproducts.forEach(product => {
                this.$data.products.forEach((actualproduct, index) => {
                    if (product.id === actualproduct.id) {
                        product.deleted = !product.deleted
                    }
                })
            })

            // A method that iterates through the
            // the iDs of the products and creates
            // an AJAX request to delete them
            $.ajax({
                type: "DELETE",
                url: "http://example.com",
                data: self.$props.selectedproducts,
                dataType: "json",
                success: function (response) {
                    console.log(response)
                }
            });
        },
        togglesidebar: function() {
            this.$data.showsidebar = !this.$data.showsidebar
        }
    },
})