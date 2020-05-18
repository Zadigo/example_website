// $(document).ready(function () {
//     $("#trigger-for-sidebar").on("click", function() {
//         // $(".dashboard .wrapper").toggle(".show-side-bar")
//         $(".dashboard .wrapper").toggle("hide")
//     })    
// });

// UTILITIES

var productdetailsurl = window.location.origin + "/dashboard/products/"

var constructurl = function(id, slug) {
    return  productdetailsurl + id + "/" + slug
}

// var filterproducts = {
//     template: "\
//     <select id='filter_products'>\
//         <option @click='doselect(option.value)' v-for='option in options' :key='option.value' :value='option.value'>{{ option.name }}</option>\
//     </select>\
//     ",
//     data() {
//         return {
//             options: [
//                 {value: "all", name: "-----", selected: true},
//                 {value: "croissant", name: "Croissant", selected: false},
//                 {value: "decroissant", name: "Décroissant", selected: false},
//             ]
//         }
//     },
//     methods: {
//         doselect: function(value) {
//             this.$data.options.forEach(option => {
//                 option.selected = false
//                 if (option.value === value) {
//                     option.selected = true
//                 }
//             })
//         }
//     },
//     computed: {
//         selectedfilter() {
//             return this.$data.options.filter(option => {
//                 return option.selected === true
//             })
//         }
//     }
// }

// LISTS

var vuecards = {
    props: ["products"],
    template: "\
    <div class='row'>\
        <div class='col s12 m12 l12'>\
            <div class='col s3 m3 l3'>\
                <select v-model='selectedoption' name='card-filter' id='card-filter'>\
                    <option v-for='option in items' :key='option.value' :value='option.value'>{{ option.name }}</option>\
                </select>\
            </div>\
        </div>\
        <div class='col s12 m12 l12'>\
            <transition-group name='card_items'>\
                <div v-for='card in productlist' :key='card.name' class='col s12 m4 l4'>\
                    <div class='card'>\
                        <div class='card-content'>\
                            <span class='card-title'>{{ card.name }}</span>\
                            <p>{{ card.content }}</p>\
                        </div>\
                        <div class='card-action'>\
                            <a href='' class='btn'><i class='material-icons left'>watch</i>Details</a>\
                        </div>\
                    </div>\
                </div>\
            </transition-group>\
        </div>\
    </div>\
    ",
    data() {
        return {
            items: [
                {value: "all", name: "-----"},
                {value: "first", name: "First"},
                {value: "second", name: "Second"}
            ],
            selectedoption: "all"
        }
    },
    computed: {
        productlist() {
            // Returns a list of products that were
            // previously filtered by other methods
            if (this.$data.selectedoption === "all") {
                return this.$props.products
            }
            if (this.$data.selectedoption === "first") {
                return this.filternames
            }
            if (this.$data.selectedoption === "second") {
                return this.filterprices
            }
        },
        filterprices() {
            // Method to filter prices which avoids
            // messing up the original values
            var products = []
            var productcopy = {}
            this.$props.products.forEach(product => {
                products.push(Object.assign(productcopy, product))
                productcopy = {}
            })
            return products.sort(function (a, b) {
                return b.price - a.price
            })
        },
        filternames() {
            return this.$props.products.filter(product => {
                return product.name === "Kendall"
            })
        }
    }
}

var deletebutton = {
    // This commponent allows the user to
    // delete an item from the database
    // after having selected them

    props: ["selectedproducts"],
    template: "\
        <a @click='deleteitems' class='btn-large waves-effect waves-light' id='delete_product' :disabled='showdeletebutton'>\
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
            // Defines if the delete button should be enabled
            // or not --; true if products are selected,
            // otherwise false
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


// DASHBOARD

var dashboard = new Vue({
    el: "#vue_dashboard",
    components: {vuetable_one, vuetable_two, deletebutton, createform, 
                    updateform, messages, vuecards, settingstemplate},
    data() {
        return {
            products: [],
            showsidebar: true
        }
    },
    beforeMount() {
        var self = this
        $.ajax({
            type: "GET",
            url: "/api/v1/products",
            dataType: "json",
            success: function (response) {
                // response.forEach(product => {
                //     product["deleted"] = false
                // })
                self.$data.products = response
            }
        });
    },
    computed: {
        selectedproducts() {
            // Returns a list of selected products that
            // were also marked as not deleted
            return this.$data.products.filter(product => {
                return product.selected === true && product.deleted === false
            })
        }
    },
    methods: {
        doselect: function(index) {
            // Selects a product in the table using
            // a selectio checkbox
            this.$data.products[index].selected = !this.$data.products[index].selected
        },
        getall: function() {
            // Selects all the products in the
            // table by using the selection
            // checkboxes
            this.$data.products.forEach(product => {
                product.checked = !product.checked
                product.selected = !product.selected
            })
        },
        applydeletemultiple: function() {
            // Deletes multiple items using the selection
            // checkboxes in the table
            var productstodelete  = this.$data.products.filter(product => {
                return product.selected === true
            })
            if (productstodelete.length === 0) {
                return
            }
            var productsarray = []
            productstodelete.forEach(product => {
                productsarray.push(product.id)
            })
            console.log(productsarray)
            
            $.ajax({
                type: "POST",
                url: "/api/v1/product/1/delete",
                data: {products: productsarray, multiple: true},
                dataType: "json",
                success: function (response) {
                    console.log(response)
                    productstodelete.forEach(product => {
                        product["deleted"] = true
                    })
                },
                error: function(response) {
                    console.log("An error occured")
                }
            });
        },
        applydeletesingle: function(productid) {
            var self = this
            $.ajax({
                type: "POST",
                url: "/api/v1/product/1/delete",
                data: {csrfmiddlewaretoken: "", reference: ""},
                dataType: "json",
                success: function (response) {
                    console.log(response)
                    // ALlows the deletionf of a single
                    // item from the table without going
                    // through the selection
                    self.$data.products.forEach(product => {
                        if (product.id === productid) {
                            product.deleted = !product.deleted
                        }
                    })
                },
                error: function(response) {
                    console.log("An error occured")
                }
            });
        },
        togglesidebar: function() {
            this.$data.showsidebar = !this.$data.showsidebar
        }
    },
})