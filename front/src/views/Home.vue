<template>
  <base-home-page>
    <template #navbar>
      <base-navbar :fixedTop="true" :fluid="true" theme="dark">
        <template>
          <b-navbar-nav class="navbar-nav me-auto mb-2 mb-lg-0">
            <b-nav-item>
              Login
            </b-nav-item>
            <b-nav-item href="#">
              Logout
            </b-nav-item>
            <b-nav-item href="#">
              Profile
            </b-nav-item>
          </b-navbar-nav>

          <b-navbar-nav class="d-flex flex-row">
            <b-nav-item href="#" class="me-3 me-lg-0">
              <b-link class="nav-link">
                <font-awesome-icon :icon="['fab', 'facebook-f']" />
              </b-link>
            </b-nav-item>
            <b-nav-item href="#" class="me-3 me-lg-0">
              <b-link class="nav-link">
                <font-awesome-icon :icon="['fab', 'instagram']" />
              </b-link>
            </b-nav-item>
          </b-navbar-nav>
        </template>
      </base-navbar>  
    </template>

    <template #intro>
      <base-intro :src="testImage" :mask="0.4">
        <div>
          <h1 class="hero-lead mb-3">I love you Kendall</h1>
          <p class="hero-lead-300 mb-4">This is a great idea for a website</p>
        </div>
      </base-intro>
    </template>

    <template>
      <!-- Partners -->
      <base-brands :items="companyDetails.partners" />

      <!-- Benefits -->
      <div class="container">
        <base-modern-benefits />
      </div>

      <!-- Section -->
      <base-section class="px-sm-5" color="pink darken-1" :textWhite="true">
        <template>
          <div class="row">
            <div class="col-sm-12 col-md-12">
              <h1>Kendall Jenner is a Genius</h1>
              <p>Get the best from her</p>
              <v-btn size="lg" color="light">Visit website</v-btn>
            </div>
          </div>
        </template>
      </base-section>

      <!-- Benefits -->
      <base-benefits :items="companyDetails.benefits" :textWhite="false" color="bg-light" iconColor="text-red lighten-1">

        <template #footer>
          <div class="container">
            <div class="row">
              <div class="col-12">
                <h2 class="mb-3">Visit Kendall at that number</h2>
                <p class="mb-4">Lorem ipsum, dolor sit amet consectetur adipisicing elit. dit tenetur ea nam aliquam.</p>
                <v-btn size="lg" color="light">Visit website</v-btn>
              </div>
            </div>
          </div>
        </template>
      </base-benefits>
      
      <div class="container">
        <div class="row">
          <div class="col-12">
            <base-cta :isCard="true" :textWhite="true" />
          </div>
        </div>
      </div>
    </template>

    <template #footer>
      <base-footer :items="companyDetails.footer" :socials="companyDetails.socials" class="mt-5" color="bg-dark" />
    </template>
  </base-home-page>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      footerItems: [

      ],
      testImage: 'https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=1200&w=940'
    }
  }
}
</script>
