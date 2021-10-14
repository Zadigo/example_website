<template>
  <v-card :style="extraStyle" v-if="isCard" class="text-center p-3">
    <v-card-text>
      <div class="container">
        <div class="row">
          <div class="col-8 offset-md-2">
            <h2 class="mb-6">Don’t take our word for it. Try Appcues for free.</h2>
            <v-text-field solo></v-text-field>
            <v-btn color="primary">Register yourself</v-btn>
          </div>
        </div>
      </div>
    </v-card-text>
  </v-card>

  <base-section v-else class="text-center">
    <h2 class="mb-6">Don’t take our word for it. Try Appcues for free.</h2>
    <v-text-field solo></v-text-field>
    <v-btn color="primary">Register yourself</v-btn>
  </base-section>
</template>

<script>
export default {
  name: 'SecondaryCTA',
  props: {
    isCard: Boolean,
    absolute: Boolean,
    top: {
      type: Number,
      default: 0
    },
    right: {
      type: Number,
      default: 0
    }
  },

  computed: {
    extraStyle() {
      if (this.isCard & this.absolute) {
        return this._getAbsoluteStyling()
      } else {
        return null
      }
    }
  },

  methods: {
    _getAbsoluteStyling() {
      return `position: absolute; top: ${this.top}px; right:${this.right}px;`
    }
  }
}
</script>
