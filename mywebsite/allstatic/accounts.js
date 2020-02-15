var userform = {
    template: "\
    <form method='POST' enctype='multipart/form-data' id='base-profile-form'>\
        <div class='input-field'>\
            </div>\
        <button type='submit' class='btn waves-effect waves-light light-blue lighten-1'><i class='material-icons left'>check</i>Valider</button>\
    </form>\
    "
}

var profile = new Vue({
    el: "#app",
    components: {userform}
})