var secondsettings = {
    template: "\
    <div class='settings-group'>\
        <ul class='collapsible'>\
            <li>\
                <div class='collapsible-header'><i class='material-icons'>person</i>First</div>\
                <div class='collapsible-body'><span>Lorem ipsum dolor sit amet.</span></div>\
            </li>\
            <li>\
                <div class='collapsible-header'><i class='material-icons'>filter_drama</i>First</div>\
                <div class='collapsible-body'><span>Lorem ipsum dolor sit amet.</span></div>\
            </li>\
        </ul>\
    </div>\
    "
}

var firstsettings = {
    props: ["options"],
    template: "\
    <div class='settings-group'>\
        <div v-for='option in options' :key='option.id' class='setting'>\
            <div class='switch'>\
                <label>\
                    <input v-model='option.selected' @click='applysetting(option.title), option.selected=!option.selected' \
                        type='checkbox' :name='option.title' :id='option.title'>\
                    <span class='lever'></span>\
                    {{ option.title }}\
                </label>\
            </div>\
        </div>\
    </div>\
    ",
    data() {
        return  {
            // options: [
            //     {id: 1, title: "Night mode", selected: false, type: "lever"},
            //     {id: 2, title: "Notifications", selected: false, type: "lever"},
            // ]
        }
    },
    computed: {
        selectedoptions() {
            return this.$data.options.filter(option => {
                return option.selected === true
            })
        }
    },
    methods: {
        applysetting: function(optiontitle) {
            this.$emit("applysetting", optiontitle)
        }
    }
}

var settingstemplate = {
    // The base component for the settings
    // page of the dashboard
    components: {firstsettings, secondsettings},
    template: "\
        <div>\
            <firstsettings @applysetting='sendrequest' v-bind:options='usersettings[1]' />\
            <secondsettings @applysetting='sendrequest' />\
        </div>\
    ",
    data() {
        return {
            usersettings: []
        }
    },
    beforeMount() {
        var self = this
        $.ajax({
            type: "GET",
            url: "/api/v1/dashboard/settings",
            dataType: "json",
            success: function (response) {
                self.$data.usersettings = response
            },
            error: function(response) {
                console.log("An error occured")
            }
        });
    },
    methods: {
        sendrequest: function(optiontitle) {
            $.ajax({
                type: "POST",
                url: "/api/v1/dashboard/settings",
                data: {setting: optiontitle},
                dataType: "json",
                success: function (response) {},
                error: function(response) {
                    console.log("An error occured")
                }
            })
        }
    }
}