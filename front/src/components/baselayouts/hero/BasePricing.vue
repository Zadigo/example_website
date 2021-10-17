<template>
  <div class="container">

    <section class="text-center" id="pricing">
      <h4 class="mb-4"><strong>Pricing</strong></h4>

      <!-- Selection -->
      <div v-if="hasChoices & !hasOneBilling" class="btn-group mb-4" role="group" aria-label="Billing selection">
        <b-btn @click="monthly = true" :class="{ active: billedMonthly }" variant="primary">
          Monthly billing
        </b-btn>

        <b-btn @click="monthly = false" :class="{ active: billedAnnually }" variant="primary">
          Annual billing <small>(2 months FREE)</small>
        </b-btn>
      </div>

      <!-- Pricing -->
      <div v-if="hasChoices" class="row gx-lg-5">
        <div v-for="(choice, index) in currentChoices.choices" :key="index" class="col-lg-3 col-md-6 mb-4">

          <div :class="customCardClasses(choice)" :aria-label="choice.title" class="card">
            <div class="card-header bg-white py-3">
              <p class="text-uppercase small mb-2"><strong>{{ choice.title }}</strong></p>
              <h5 class="mb-0">{{ choice.price|priceFilter|currencyFilter }}{{ priceSuffix(choice) }}</h5>
            </div>

            <div class="card-body">
              <ul class="list-group list-group-flush">
                <li v-for="(feature, index) in choice.features" :key="index" class="list-group-item">
                  {{ feature }}
                </li>
              </ul>
            </div>

            <div class="card-footer bg-white py-3">
              <b-btn @click="$emit('updateBillingPlan', selectedBillingPlan(choice))" :to="getRoute(choice)" :variant="customButtonVariant(choice)" class="btn-sm">
                Get it
              </b-btn>
            </div>

          </div>
        </div>

      </div>

      <div v-else class="row gx-lg-5">
        <b-card>
          <h1>Coming soon</h1>
        </b-card>
      </div>
    </section>

  </div>
</template>

<script>
var _ = require('lodash')

export default {
  name: 'BasePricing',
  props: {
    shadow: {
      type: Boolean,
      default: true
    },
    isAuthenticated: Boolean,
    notAuthenticatedRouteName: {
      type: String,
      default: 'login'
    },
    items: {
      type: Array,
      default: () => []
    },
    lead: String,
    subTitle: String,
  },

  data() {
    return {
      monthlyBillingChoices: [],
      annualBillingChoices: [],
      monthly: true
    }
  },

  beforeMount() {
    if (this.hasChoices) {
      // If we have more than on billing options at our
      // disposal, pick the last one of the list. This
      // prevents raising an error to the user
      this.monthlyBillingChoices = _.last(_.filter(this.items, ['monthly', true]))
      this.annualBillingChoices = _.last(_.filter(this.items, ['monthly', false]))
    }
  },

  computed: {
    currentChoices() {
      if (this.billedMonthly) {
        return this.monthlyBillingChoices
      } else {
        return this.annualBillingChoices
      }
    },

    billedMonthly() {
      return this.monthly == true
    },

    billedAnnually() {
      return !this.billedMonthly
    },

    hasChoices() {
      return this.items.length > 0
    },

    hasOneBilling() {
      // If we pass only one billing method,
      // consider that we only have one choice
      // and should not show the selection buttons
      return this.items.length == 1
    },

  },

  methods: {
    selectedBillingPlan(choice) {
      // Resumes the billing plan selected
      // by the user
      return { plan: choice.title, monthly: this.monthly }
    },
    getRoute(choice) {
      // Depdending on whether the user is authenticated
      // or not, go to a specific route. Generally, it is
      // the signup oute. NOTE: The programmer should implement
      // the logic for keeping track of the plan that was
      // selected by the user in the rest of the app
      var route = { name: null, query: this.selectedBillingPlan(choice)}
      if (this.isAuthenticated) {
        route['name'] = 'home'
        return route
      } else {
        route['name'] = this.notAuthenticatedRouteName
        return route
      }
    },
    priceSuffix(choice) {
      if (choice.price == null) {
        return null
      } else {
        return this.monthly ? '/month' : '/year'
      }
    },
    customCardClasses(choice) {
      return [
        {
          'border border-primary': choice.highlighted,
          'shadow-none': !this.shadow && !choice.highlighted,
          'border': !this.shadow && !choice.highlighted
        }
      ]
    },

    customButtonVariant(choice) {
      if (choice.title === 'Free') {
        return 'success'
      } else if (choice.highlighted) {
        return 'primary'
      } else {
        return 'info'
      }
    }
  },

  filters: {
    priceFilter(value) {
      if (value == null) {
        return 'Free'
      } else {
        return value
      }
    },
    currencyFilter(value) {
      if (value === 'Free') {
        return value
      }
      return `$${ value }`
    }
  }
}
</script>


<style scoped>
  .v-application a {
    color: white;
  }
</style>
