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
          no-body
          class="mb-1"
        >
          <b-card-header
            header-tag="header"
            class="p-1"
            role="tab"
          >
            <b-button
              v-b-toggle="`accordion-${index}`"
              block
              class="shadow-none d-flex justify-content-between"
              variant="white"
              @shown="item.visible=true"
              @hidden="item.visible=false"
            >
              <p class="h6 m-0 text-reset">
                {{ item.question }}
              </p>
              <font-awesome-icon
                v-if="!item.visible"
                icon="times-circle"
                class="fa-2x"
              />
              <font-awesome-icon
                v-else
                icon="check-circle"
                class="fa-2x text-success"
              />
            </b-button>
          </b-card-header>

          <b-collapse
            :id="`accordion-${index}`"
            visible
            accordion="my-accordion"
            role="tabpanel"
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
