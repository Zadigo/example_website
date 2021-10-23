<template>
  <!-- <sidebar-interface>
    <template v-slot:side>
      <base-sidebar :navbarVisibility="true">
        <template v-slot:navItems>
          <base-nav-item name="Home" linkName="home" icon="home" />
          <base-nav-item name="Users" linkName="products" icon="users" />
        </template>
      </base-sidebar>
    </template>

    <template v-slot:heading>
      <v-toolbar maxWidth="100%" class="border-bottom mb-2" style="margin-left:320px;" flat extended>
        <v-toolbar-title>Your Dashboard</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-logout</v-icon>
        </v-btn>

        <template v-slot:extension>
          <v-tabs>
            <v-tab>Item One</v-tab>
            <v-tab>Item Two</v-tab>
            <v-tab>Item Three</v-tab>
          </v-tabs>
        </template>
      </v-toolbar>
    </template>
    
    <template>
      <div class="row">
        <div class="col-6">
          <v-card>
            <v-card-title>Profile</v-card-title>
            <v-card-text class="d-flex justify-content-left">
              <b-avatar size="70" src="http://via.placeholder.com/100" avatar></b-avatar>
              <div class="ml-5">
                <label class="mt-2">Name</label>
                <b-form-input></b-form-input>

                <label class="mt-4">Job</label>
                <v-combobox :items="[1, 2, 3]" class="border" flat solo></v-combobox>
              </div>
            </v-card-text>

            <v-card-actions>
              <v-btn class="text-right" color="primary">Save</v-btn>
            </v-card-actions>
          </v-card>
        </div>
        <div class="col-6">
          <v-card>
            <v-card-title>
              Account settings
            </v-card-title>

            <v-card-text>
              <div class="form-group">
                <label for="">Company name</label>
                <b-form-input></b-form-input>
              </div>

              <div class="form-group">
                <label for="">Account ID</label>
                <b-form-input></b-form-input>
              </div>

              <div class="form-group">
                <label for="">Web application domain</label>
                <b-form-input></b-form-input>
              </div>

            </v-card-text>

            <v-card-actions>
              <v-btn class="text-right" color="primary">Save</v-btn>
            </v-card-actions>
          </v-card>
        </div>
      </div>
    </template>
  </sidebar-interface> -->

  <base-ecommerce-navbar />
</template>

<script>
// import BaseNavItem from '../components/sidebar/BaseNavItem.vue'
// import BaseSidebar from '../components/sidebar/BaseSidebar.vue'
// import SidebarInterface from '../components/sidebar/SidebarInterface.vue'

export default {
  name: 'TestPage',
  // components: { BaseSidebar, SidebarInterface, BaseNavItem }
  }
</script>
