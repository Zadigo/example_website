<template>
  <div class="row">
    <div class="col-12">
      <!-- v-b-toggle.accordion-1 -->
      <div
        v-if="hasItems"
        class="accordion"
        role="tablist"
      >
        <b-card
          v-for="(item, index) in items"
          :key="index"
          class="mb-1"
          no-body
        >
          <b-card-header
            class="p-1"
            header-tag="header"
            role="tab"
          >
            <b-button
              v-b-toggle="`accordion-${index}`"
              block
              class="shadow-none d-flex justify-content-between"
              variant="white"
              @hidden="item.visible=false"
              @shown="item.visible=true"
            >
              <p class="h6 m-0 text-reset">
                {{ item.question }}
              </p>
              <font-awesome-icon
                v-if="!item.visible"
                class="fa-2x"
                icon="times-circle"
              />
              <font-awesome-icon
                v-else
                class="fa-2x text-success"
                icon="check-circle"
              />
            </b-button>
          </b-card-header>

          <b-collapse
            :id="`accordion-${index}`"
            accordion="my-accordion"
            role="tabpanel"
            visible
          >
            <b-card-body>
              <b-card-text>
                {{ item.answer }}
              </b-card-text>
            </b-card-body>
          </b-collapse>
        </b-card>
      </div>

      <div
        v-else
        class="row"
      >
        <div class="col-12">
          <h1>FAQ coming soon</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var _ = require('lodash')

export default {
  name: 'BaseSmallFAQ',
  props: {
    items: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      opened: null
    }
  },

  computed: {
    hasItems() {
      return this.items.length > 0
    }
  },
  
  beforeMount() {
    if (this.hasItems) {
      _.forEach(this.items, (item) => {
        item['visible'] = false
      })
    }
  }
}
</script>
