<template>
  <section ref="cta" id="cta">
    <v-card :class="cardClasses" :color="color" v-if="isCard" class="text-center">
      <v-card-text>
        <div class="container">
          <div class="row">
            <div :class="contentClasses">
              <h2 class="mb-6">{{ title }}</h2>
              <v-text-field v-model="textFieldData" solo></v-text-field>
              <v-btn @click="$emit('textFieldValidated')" :to="{ name: to }" color="primary">Register yourself</v-btn>
            </div>
          </div>
        </div>
      </v-card-text>
    </v-card>

    <base-section v-else :color="color" class="text-center">
      <h2 class="mb-6">Don’t take our word for it. Try Appcues for free.</h2>
      <v-text-field solo></v-text-field>
      <v-btn color="primary">Register yourself</v-btn>
    </base-section>
  </section>
</template>

<script>
export default {
  name: 'SecondaryCTA',
  props: {
    absolute: Boolean,
    col: {
      type: Number,
      default: 8
    },
    color: {
      type: String,
      default: null
    },
    isCard: Boolean,
    right: {
      type: Number,
      default: 0
    },
    offset: {
      type: Number,
      default: 2
    },
    title: {
      type: String,
      default: 'Don’t take our word for it. Try Appcues for free.'
    },
    textWhite: Boolean,
    to: String,
    top: {
      type: Number,
      default: 0
    },
    marginTop: {
      type: Number,
      default: null
    }
  },

  data() {
    return {
      textFieldData: null
    }
  },

  mounted() {
  // if (this.isCard & this.absolute) {
  //   return this.getAbsoluteStyling()
  // } else {
  //   return null
  // }
    if (this.absolute) {
      this.$refs.cta.style.position = this.getAbsoluteStyling()
    }
  },

  computed: {
    cardClasses() {
      return [
        {
          'text-white': this.textWhite
        }
      ]
    },

    contentClasses() {
      return [
        'col-sm-12',
        {
          [`col-md-${this.col}`]: true,
          'offset-sm-0': true,
          [`offset-md-${this.offset}`]: true
        },
      ]
    }
  },

  methods: {
    getAbsoluteStyling() {
      return `position:absolute; top:${this.top}px; right:${this.right}px;`
    }
  }
}
</script>
