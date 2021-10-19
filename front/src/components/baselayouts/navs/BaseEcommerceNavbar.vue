<template>
  <div class="ecommerce">
    <div class="p-3 blue">

    </div>
    
    <base-navbar> 
      <slot>
        <slot></slot>
      </slot>
    </base-navbar>

    <!-- collapse navbar-collapse navbar-1 -->
    <b-nav class="navbar navbar-lg d-lg-block p-3 blue" role="navigation">
      <div class="container">
        <b-nav-item-dropdown :lazy="true" id="my-nav-dropdown" text="Dropdown" menu-class="has-ecommerce-menu ecommerce-menu">
          <div class="row g-3" id="menu">
            <div class="col-lg-3 col-6">
              <div class="col-megamenu">
                <h6 class="title">Title Menu One</h6>
                <ul class="list-unstyled">
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                </ul>
              </div>
            </div>

            <div class="col-lg-3 col-6">
              <div class="col-megamenu">
                <h6 class="title">Title Menu Two</h6>
                <ul class="list-unstyled">
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                </ul>
              </div>
            </div>
            
            <div class="col-lg-3 col-6">
              <div class="col-megamenu">
                <h6 class="title">Title Menu Three</h6>
                <ul class="list-unstyled">
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                </ul>
              </div>
            </div>

            <div class="col-lg-3 col-6">
              <div class="col-megamenu">
                <h6 class="title">Title Menu Four</h6>
                <ul class="list-unstyled">
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                  <li><a href="#">Custom Menu</a></li>
                </ul>
              </div>
            </div>
          </div>
        </b-nav-item-dropdown>
      </div>
    </b-nav>
  </div>
</template>

<script>
import BaseNavbar from './BaseNavbar.vue'

export default {
  components: { BaseNavbar },
  
}
</script>

<style scoped>


@media all and (min-width: 992px) {
  .has-ecommerce-menu {
    position: static !important;
  }

  .ecommerce-menu #menu {
    /* left: 0;
    right: 0; */
    width: 100%;
    /* margin-top: 0; */
    padding: 2rem;
  }

  .ecommerce-menu.show {
    width: 1000px;
  }


  /* .navbar .has-megamenu{
    position: static !important;
  } */

  /* .secondary-navbar .ecommerce-navbar{
    left:0;
    right:0;
    width:100%;
    margin-top:0;
  } */
}
</style>
