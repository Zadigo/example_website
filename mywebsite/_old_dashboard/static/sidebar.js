// $(document).ready(function () {
//     var dashboard = $(".dashboard")
//     var currentwidth = document.body.clientWidth
//     var showsidebar = true
//     // localStorage.setItem("sidebar", showsidebar)

//     if (currentwidth < 420) {
//         dashboard.find(".side").addClass("hide")
//         dashboard.find(".wrapper").addClass("show-side-bar")
//     }

//     if (showsidebar === false) {
//         dashboard.find(".side").toggleClass("hide")
//         dashboard.find(".wrapper").toggleClass("show-side-bar")
//         return
//     }
    
//     $(".topnav").find("#trigger-for-sidebar").on("click", function() {
//         showsidebar = localStorage.getItem("sidebar")
//         localStorage.setItem("sidebar", !showsidebar)

//         dashboard.find(".side").toggleClass("hide")
//         dashboard.find(".wrapper").toggleClass("show-side-bar")
//     }) 
// });


$(document).ready(function () {
    sessionStorage.setItem("sidebartoggle", false)

    var sideBar = (function(initial) {
        var dashboard = $(".dashboard")
        var currentstate = localStorage.getItem("sidebartoggle")

        
    
        var currentwidth = function() {
            return document.body.clientWidth
        }
    
        var managestorage = function() {
            var state = localStorage.getItem("sidebar")
            localStorage.setItem("sidebar", !state)
        }

        var triggersidebar = function() {
            dashboard.find(".side").toggleClass("hide")
            dashboard.find(".wrapper").toggleClass("show-side-bar")
            managestorage()
        }
    
        var togglesidebar = function() {
            $(".topnav").find("#trigger-for-sidebar").on("click", triggersidebar)
        }
    
        var init = function() {
            togglesidebar()
            
            if (currentstate === undefined || currentstate === null) {
                localStorage.setItem("sidebar", true)
            }

            if (currentstate === false) {
                dashboard.find(".side").addClass("hide")
                dashboard.find(".wrapper").addClass("show-side-bar")
            }        

            if (currentwidth < 420) {
                toggle()
            }
        }
        
        return {
            init: init
        }
    })
    
    sideBar().init()
});