(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pricing"],{d4e9:function(e,t,s){"use strict";s.r(t);var a=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("base-home-page",{scopedSlots:e._u([{key:"intro",fn:function(){return[s("base-intro",{attrs:{"is-full-page":!0,mask:.5,src:"https://images.pexels.com/photos/762084/pexels-photo-762084.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=1200","text-white":!0}},[[s("authentication-form",{attrs:{"field-type":"email","form-messages":e.formMessages,login:!0},on:{authenticateUser:e.authenticateUser}}),s("div",{staticClass:"text-separator my-4"},[s("span",[e._v("Or")])]),s("v-btn",{attrs:{block:""}},[s("font-awesome-icon",{staticClass:"mr-3",attrs:{icon:["fas","google"]}}),e._v("Google ")],1)]],2)]},proxy:!0}])})},i=[],r=s("2f62"),o={name:"Login",data(){return{fields:[{type:"email",placeholder:"Email"},{type:"password",placeholder:"Password"}]}},computed:{...Object(r["e"])({formMessages:e=>e.messagesModule.items})},methods:{...Object(r["d"])("authenticationModule",["setTokens","clearStack"]),...Object(r["b"])(["formErrorMessages"]),authenticateUser(e){let{email:t,password:s}=e;this.$api.auth.login(t,s).then(e=>{this.setTokens(e.data),this.clearStack(),this.$router.push({name:"home"})}).catch(e=>{this.formErrorMessages(e.response.data)})}}},u=o,n=s("2877"),p=Object(n["a"])(u,a,i,!1,null,null,null);t["default"]=p.exports},dbc9:function(e,t,s){"use strict";s.r(t);var a=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("base-jumbotron",{attrs:{color:"pink darken-2",lead:"Learn Bootstrap 5 with MDB","sub-title":"Best & free guide of responsive web design","text-white":!0},scopedSlots:e._u([{key:"navbar",fn:function(){return[s("base-navbar",{attrs:{theme:"light"}})]},proxy:!0},{key:"footer",fn:function(){return[s("base-footer")]},proxy:!0}])},[[s("base-pricing",{attrs:{items:e.companyDetails.pricing,lead:"Pricing for all our products",shadow:!1,"sub-title":"Best & free guide of responsive web design"}}),s("div",{staticClass:"container"}),s("base-section",{attrs:{color:"pink darken-3"}},[[s("h1",{staticClass:"fs-super text-center text-white"},[e._v(" Got questions? ")]),s("p",{staticClass:"text-white-muted text-center h5 mb-8"},[e._v(" Commonly asked questions ")]),s("base-small-faq",{attrs:{items:e.faq}})]],2)]],2)},i=[],r=s("f6a8"),o={name:"Pricing",data(){return{faq:r}}},u=o,n=s("2877"),p=Object(n["a"])(u,a,i,!1,null,null,null);t["default"]=p.exports},f6a8:function(e){e.exports=JSON.parse('[{"question":"How much does Jetty Protect cost?","answer":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio tempora repellat quisquam expedita quasi voluptatum ipsam ea  asperiores, eius qui provident corrupti eaque veniam, ducimus  necessitatibus id nulla atque est!"},{"question":"Am I required to have renters insurance?","answer":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio tempora repellat quisquam expedita quasi voluptatum ipsam ea  asperiores, eius qui provident corrupti eaque veniam, ducimus  necessitatibus id nulla atque est!"},{"question":"How long are plans valid?","answer":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio tempora repellat quisquam expedita quasi voluptatum ipsam ea  asperiores, eius qui provident corrupti eaque veniam, ducimus  necessitatibus id nulla atque est!"},{"question":"Can I change my coverage once a policy is in place?","answer":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio tempora repellat quisquam expedita quasi voluptatum ipsam ea  asperiores, eius qui provident corrupti eaque veniam, ducimus  necessitatibus id nulla atque est!"},{"question":"Where is Jetty Protect available?","answer":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio tempora repellat quisquam expedita quasi voluptatum ipsam ea  asperiores, eius qui provident corrupti eaque veniam, ducimus  necessitatibus id nulla atque est!"}]')}}]);
//# sourceMappingURL=pricing.ada8ef95.js.map