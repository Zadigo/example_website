<template>
  <base-jumbotron
    :text-white="true"
    color="pink darken-2"
    lead="Learn Bootstrap 5 with MDB"
    sub-title="Best & free guide of responsive web design"
  >
    <template #navbar>
      <base-navbar theme="light" />
    </template>

    <template>
      <base-pricing
        :shadow="false"
        :items="companyDetails.pricing"
        lead="Pricing for all our products"
        sub-title="Best & free guide of responsive web design"
      />

      <div class="container">
        <!-- <div class="row">
          <div class="col-12">
            <b-card class="p-5 blue darken-4">
              <b-card-text>
                <h1 class="fs-super text-center text-white">Got questions?</h1>
                <p class="text-white-muted text-center h5 mb-8">Commonly asked questions</p>
                <base-small-faq :items="faq" />
              </b-card-text>
            </b-card>
          </div>
        </div> -->
      </div>

      <base-section color="pink darken-3">
        <template>
          <h1 class="fs-super text-center text-white">
            Got questions?
          </h1>
          <p class="text-white-muted text-center h5 mb-8">
            Commonly asked questions
          </p>
          <!-- Faq -->
          <base-small-faq :items="faq" />
        </template>
      </base-section>
    </template>

    <template #footer>
      <base-footer />
    </template>
  </base-jumbotron>
</template>

<script>
import faq from '../data/faq.json'

export default {
  name: 'Pricing',
  data() {
    return {
      faq: faq
    }
  }
}
</script>
