var csrf = function() {
    return $(".csrf").find("input").val()
}

var checkboxcomponent = {
    props: ["checkboxtext"],
    template: "\
    <p>\
        <label>\
            <input @click='docheck' v-model='currentstate' type='checkbox'>\
            <span>{{ checkboxtext }}</span>\
        </label>\
    </p>\
    ",
    data() {
        return {
            currentstate: false
        }
    },
    methods: {
        docheck: function() {
            this.$emit("docheck", this.$data.currentstate)
        }
    }
}

var registrationform = {
    props: ["fields"],
    components: {checkboxcomponent},
    template: "\
    <form @submit.prevent='submitform'>\
        <div v-for='field in fields' :key='field.id' class='input-field'>\
            <input v-model='datatosubmit[field.name]' :type='field.text' :name='field.name' id='field.name'\
                :autocomplete='field.autocomplete' :placeholder='field.placeholder'>\
        </div>\
        <checkboxcomponent @docheck='' v-bind:checkboxtext='checkboxtext' />\
        <button type='submit' class='btn-large' :class='{\"disabled\": hasdata}'>\
            <i class='material-icons left'>done</i>S'enregistrer\
        </button>\
    </form>\
    ",
    data() {
        return {
            datatosubmit: {},
            checkboxtext: "Je ne souhaites être contacté"
        }
    },
    computed: {
        hasdata() {
            var keyslength = Object.keys(this.$data.datatosubmit).length > 0
            if (keyslength === true) {
                return false
            } else {
                return true
            }
        }
    },
    methods: {
        dosubmit: function() {
            this.$emit("dosubmit", this.$data.datatosubmit)
        }
    }
}

var contactform = {
    props: ["fields"],
    template: "\
    <form @submit.prevent='dosubmit'>\
        <div v-for='field in fields' :key='field.id' class='input-field'>\
            <input v-model='datatosubmit[field.name]' :type='field.text' :name='field.name' id='field.name'\
                :autocomplete='field.autocomplete' :placeholder='field.placeholder'>\
        </div>\
        <div class='input-field'>\
            <textarea v-model='datatosubmit[\"message\"]' id='textarea1'\
                    class='materialize-textarea' placeholder='Message'></textarea>\
        </div>\
        <button type='submit' class='btn-large' :class='{\"disabled\": hasdata}'>\
            <i class='material-icons left'>done</i>Valider\
        </button>\
    </form>\
    ",
    data() {
        return {
            datatosubmit: {},
            messagetext: ""
        }
    },
    computed: {
        hasdata() {
            var keyslength = Object.keys(this.$data.datatosubmit).length > 0
            if (keyslength === true) {
                return false
            } else {
                return true
            }
        }
    },
    methods: {
        dosubmit: function() {
            this.$emit("dosubmit", this.$data.datatosubmit)
        }
    }
}

var profileapp = new Vue({
    el: '#app',
    components: {contactform, registrationform},
    data() {
        return {
            fields: [
                {id: 1, type: "text", name: "name", autocomplete: "name", placeholder: "Nom"},
                {id: 2, type: "email", name: "email", autocomplete: "email", placeholder: "Email"},
            ],
        }
    },
    methods: {
        submitform: function(data) {
            var self = this
            var formdata = new FormData()
            formdata.append("csrfmiddlewaretoken", csrf())

            Object.keys(data).forEach(key => {
                formdata.append(key, self.$data.datatosubmit[key])
            })

            var promise = new Promise((resolve, reject) => {
                var xhr = new XMLHttpRequest()
                xhr.onloadend = function(response) {
                    if (xhr.status === 200) {
                        
                    }
                }
                xhr.open("POST", window.location.href)
                xhr.send(formdata)
                resolve(xhr.response)
            })
            promise.then(response => {
                console.log(response)
            })
        }
    }
})