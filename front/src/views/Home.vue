<template>
  <base-home-page>
    <template #navbar>
      <navbar />  
    </template>

    <template #intro>
      <base-intro
        :correction-top="74"
        flex-position="center"
        :mask="0.4"
        :src="testImage"
        text-position="center"
      >
        <div>
          <h1 class="lead-title mb-8">
            I love you <span class="hg-box pink darken-2 rounded">Kendall</span>
          </h1>
          <!-- <lead-title>I love you Kendall</lead-title> -->
          <p class="lead-subtitle-half mb-9">
            An innovative website created with VueJS and Django
          </p>

          <cta-input-group
            :button-flat="true"
            button-name="Subscribe"
            class="mt-5"
            :filled="true"
          />
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
      <base-section
        class="px-sm-5"
        color="pink darken-1"
        :text-white="true"
      >
        <template>
          <div class="row">
            <div class="col-sm-12 col-md-12">
              <h1 class="lead-title">
                Kendall Jenner is a genius
              </h1>
              <p class="lead-subtitle">
                Get the best from her
              </p>
              <v-btn
                color="light"
                size="lg"
              >
                Visit website
              </v-btn>
            </div>
          </div>
        </template>
      </base-section>

      <!-- Benefits -->
      <base-benefits
        color="bg-light"
        :flat="true"
        icon-color="text-red lighten-1"
        :items="companyDetails.benefits"
        :text-white="false"
      >
        <template #heading>
          <h1 class="fs-super">
            What we actually do
          </h1>
          <h1 class="fs-super mb-9">
            and what we can do
          </h1>
        </template>

        <template #footer>
          <div class="container">
            <div class="row">
              <div class="col-12">
                <h2 class="mb-3">
                  Visit Kendall at that number
                </h2>
                <p class="mb-4">
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit. dit tenetur ea nam aliquam.
                </p>
                <v-btn
                  color="light"
                  size="lg"
                >
                  Visit website
                </v-btn>
              </div>
            </div>
          </div>
        </template>
      </base-benefits>

      <!-- Benefit -->
      <base-benefit
        :image-shadow="true"
        :order-reversed="true"
        title-color="text-pink darken-1"
      />
      <base-benefit
        :bordered="false"
        :image-shadow="true"
        :order-reversed="false"
        title-color="text-pink darken-1"
      />
      
      <!-- FAQ -->
      <base-section color="blue darken-4">
        <template>
          <div class="row">
            <div class="col-8 offset-md-2">
              <h2 class="text-white fs-super mb-5">
                Got questions?
              </h2>
              <p class="mb-8 text-white-muted fw-300">
                Here are a few of our most frequently asked questions
              </p>

              <base-small-faq :items="faq" />
            </div>
          </div>
        </template>
      </base-section>

      <div class="container">
        <div class="row">
          <div class="col-12">
            <base-cta
              button-name="Subscribe"
              :is-card="true"
              :text-white="true"
            />
          </div>
        </div>
      </div>
    </template>

    <template #footer>
      <base-footer
        class="mt-5"
        color="bg-dark"
        :items="footer"
        :socials="companyDetails.socials"
      />
    </template>
  </base-home-page>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import faq from '../data/faq.json'
import footer from '../data/footer.json'

export default {
  name: 'Home',
  components: { Navbar },
  data() {
    return {
      faq: faq,
      footer: footer,
      testImage: 'https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=1200&w=940'
    }
  }
}
</script>
