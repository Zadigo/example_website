// Vue JS for the special details
// section of the dashboard relevant
// to dealing with a user's profile

var sendmessage = {
    template: "\
    <div class='messages-section'>\
        <div class='messages'>\
            <div v-for='message in messages' :key='message.id' class='message'>\
                {{ message.text }}\
            </div>\
        </div>\
        <textarea v-model='newmessage' name='message' id='message' \
                cols='30' rows='30' placeholder='Message'></textarea>\
        <a @click='sendmessage' class='btn' :class='{disabled: hasnomessage}' \
            id='btn_envoyer_message'>Envoyer</a>\
    </div>\
    ",
    data() {
        return {
            newmessage: "",
            messages: []
        }
    },
    computed: {
        hasnomessage() {
            if (this.$data.newmessage === "") {
                return true
            }
            return false
        }
    },
    methods: {
        sendmessage: function() {
            this.$data.messages.push(
                {id: this.lastmessageid(), text: this.$data.newmessage}
            )
            this.$data.newmessage = ""

            $.ajax({
                type: "POST",
                url: "/api/v1/dashboard/users/1/3/message",
                data: {},
                dataType: "json",
                success: function (response) {}
            });
        },
        lastmessageid: function() {
            if (this.$data.messages.length > 0) {
                return 1
            } else {
                return _.maxBy(this.$data.messages, function(element) {
                    return element.id
                })
            } 
        }
    }
}

var scoreproposition = {
    template: "\
    <div>\
        <div v-if='!scored' class='stars'>\
            <i @click='selectedstar(star)' v-for='star in stars' :key='star' \
                class='material-icons' :class='activestars(star)'>star</i>\
        </div>\
        <p v-else>Score : {{ selected }}/5</p>\
    </div>\
    ",
    data() {
        return {
            stars: [1, 2, 3, 4, 5],
            selected: 0,
            scored: false
        }
    },
    methods: {
        selectedstar: function(star) {
            var self = this
            $.ajax({
                type: "POST",
                url: "/api/v1/dashboard/users/1/rate",
                data: {action: "rate", score: star},
                dataType: "json",
                success: function (response) {
                    self.$data.selected = star
                    self.$data.scored = true
                },
                error: function (response) {}
            });
        },
        activestars: function(n) {
            // Shows the selected star and
            // all stars before it in a
            // specified color
            // if (n <= this.$data.selected) {
            //     return "blue-text"
            // }
        }
    }
}

var actionbuttons = {
    template: "\
    <div class='card-panel center'>\
        <button v-if='!accepted' @click='accepted=true, runaction(\"accept\")' :disabled='refused' class='btn indigo lighten-1 waves-effect waves-light'><i class='material-icons left'>check</i>Accept</button>\
        <button v-else v-show='!hasmeeting' @click='openmodal' class='btn indigo lighten-1 waves-effect waves-light'><i class='material-icons left'>calendar_today</i>Prendre rendez-vous</button>\
        \
        <button v-show='hasmeeting' class='btn indigo lighten-1 waves-effect waves-light'><i class='material-icons left'>calendar_today</i>Bilan rendez-vous</button>\
        \
        <button @click='standby=true, runaction(\"standby\")' :disabled='accepted || refused' class='btn indigo lighten-1 waves-effect waves-light'><i class='material-icons left'>pause</i>Stand by</button>\
        <button @click='refused=true, runaction(\"refuse\")' :disabled='accepted || refused' class='btn red darken-1 waves-effect waves-light'><i class='material-icons left'>block</i>Refuse</button>\
    </div>\
    ",
    data() {
        return {
            accepted: false,
            refused: false,
            standby: false,
            hasmeeting: false
        }
    },
    mounted() {
        
    },
    methods: {
        openmodal: function() {
            // var elem = $(".meeting")
            // var instance = M.Modal.getInstance(elem)
            // instance.open()
        },
        runaction: function(name) {
            var data = {
                name: name
            }
            $.ajax({
                type: "POST",
                url: "/api/v1/dashboard/users/1/actions",
                data: data,
                dataType: "json",
                success: function (response) {},
                error: function (response) {}
            })
        }
    }
}

var userprofile = new Vue({
    el: "#vue_dashboard",
    components: {actionbuttons, scoreproposition, sendmessage}
})