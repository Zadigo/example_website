<template>
  <base-section :class="sectionClasses" :sectionId="sectionId" :color="color" :src="src" :textWhite="textWhite">
    <div class="row">
      <div class="col-12">
        <slot name="heading"></slot>
      </div>

      <div v-for="(item, index) in items" :key="index" class="col-sm-12 col-md-4">
        
        <v-card :class="benefitClasses" :flat="flat" class="p-4">
          <v-card-text>
            <font-awesome-icon v-if="isFontAwesomeIcon" :icon="item.icon" :class="iconColor" />
            <v-icon v-else :class="iconColor">mdi-{{ item.icon }}</v-icon>

            <h2 class="mt-4 mb-2 font-weight-bold">{{ item.title }}</h2>
            <p>{{ item.description }}</p>
          </v-card-text>
        </v-card>
        
      </div>

      <div class="col-12">
        <slot name="footer"></slot>
      </div>
    </div>
  </base-section>
</template>

<script>
import { sectionMixin } from './mixins'

export default {
  name: 'BaseBenefits',
  mixins: [sectionMixin],
  props: {
    bordered: Boolean,
    flat: Boolean,
    iconColor: {
      type: String,
      default: 'text-dark'
    },
    isFontAwesomeIcon: Boolean,
    items: {
      type: Array,
      default: () => []
    },
    rounded: Boolean
  },

  computed: {
    sectionClasses() {
      return [
        {
          'rounded': this.rounded,
          [`rounded-lg`]: this.rounded
        }
      ]
    },
    benefitClasses() {
      return [
        {
          'border': this.bordered
        }
      ]
    }
  }
}
</script>

<style scoped>
  .v-icon {
    font-size: 4rem;
  }
</style>
