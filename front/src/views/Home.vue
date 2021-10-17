<template>
  <base-home-page>
    <template #navbar>
      <base-navbar :transparent="true" :themeShadow="false" :fixedTop="false" :fluid="true" theme="dark">
        <template>
          <b-navbar-nav class="navbar-nav me-auto mb-2 mb-lg-0">
            <b-nav-item :to="{ name: 'login' }">
              Login
            </b-nav-item>
            <b-nav-item href="#">
              Logout
            </b-nav-item>
            <b-nav-item :to="{ name: 'pricing' }">
              Pricing
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
      <base-intro :src="testImage" :mask="0.4" :correctionTop="74" flexPosition="center" textPosition="center">
        <div>
          <h1 class="lead-title mb-8">I love you <span class="hg-box pink darken-2 rounded">Kendall</span></h1>
          <!-- <lead-title>I love you Kendall</lead-title> -->
          <p class="lead-subtitle-half mb-9">
            An innovative website created with VueJS and Django
          </p>

          <cta-input-group :buttonFlat="true" :filled="true" class="mt-5" buttonName="Subscribe"  />
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
              <h1 class="lead-title">Kendall Jenner is a genius</h1>
              <p class="lead-subtitle">Get the best from her</p>
              <v-btn size="lg" color="light">Visit website</v-btn>
            </div>
          </div>
        </template>
      </base-section>

      <!-- Benefits -->
      <base-benefits :flat="true" :items="companyDetails.benefits" :textWhite="false" color="bg-light" iconColor="text-red lighten-1">
        <template #heading>
          <h1 class="fs-super">What we actually do</h1>
          <h1 class="fs-super mb-9">and what we can do</h1>
        </template>

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

      <!-- Benefit -->
      <base-benefit titleColor="text-pink darken-1" :orderReversed="true" :imageShadow="true" />
      <base-benefit titleColor="text-pink darken-1" :orderReversed="false" :bordered="false" :imageShadow="true" />
      
      <!-- FAQ -->
      <base-section color="blue darken-4">
        <template>
          <div class="row">
            <div class="col-8 offset-md-2">
              <h2 class="text-white fs-super mb-5">Got questions?</h2>
              <p class="mb-8 text-white-muted fw-300">Here are a few of our most frequently asked questions</p>

              <base-small-faq :items="faq" />
            </div>
          </div>
        </template>
      </base-section>

      <div class="container">
        <div class="row">
          <div class="col-12">
            <base-cta :isCard="true" :textWhite="true" buttonName="Subscribe" />
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
import faq from '../data/faq.json'

export default {
  name: 'Home',
  data() {
    return {
      faq: faq,
      footerItems: [

      ],
      testImage: 'https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=1200&w=940'
    }
  }
}
</script>
