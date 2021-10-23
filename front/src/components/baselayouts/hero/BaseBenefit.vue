<template>
  <base-section :class="sectionClasses">
    <div class="row">
      <div
        class="col-sm-12 col-md-6"
        :class="columnClasses"
      >
        <h1
          class="font-weight-bold"
          :class="titleClasses"
        >
          No more digging through Slack & email
        </h1>
        <p class="text-muted">
          See all activities, edits or mentions about every document and file, 
          in one central space. No matter if Slack, email or pigeons, 
          we will keep you up to date
        </p>
      </div>

      <div
        class="col-sm-12 col-md-6"
        :class="secondReverseClass"
      >
        <b-img
          class="rounded-lg"
          :class="imageClasses"
          :fluid="true"
          :src="require('@/assets/making_art.svg')"
          :width="imageWidth"
        />
      </div>
    </div>
  </base-section>
</template>

<script>
import BaseSection from './BaseSection.vue'

export default {
  name: 'BaseBenefit',
  components: { BaseSection },

  props: {
    bordered: Boolean,
    imageWidth: {
      type: Number,
      default: 500
    },
    imageShadow: Boolean,
    titleMargin: {
      type: Number,
      default: 100
    },
    orderReversed: Boolean,
    textPosition: {
      type: String,
      default: 'left'
    },
    titleColor: {
      type: String,
      default: null
    }
  },

  computed: {
    sectionClasses() {
      return [
        {
          'border-top': this.bordered,
          'border-bottom': this.bordered
        }
      ]
    },
    titleClasses() {
      return [
        'mt-6',
        'mb-5',
        this.titleColor
      ]
    },
    columnClasses() {
      return [
        'text-sm-center',
        {
          [`text-md-${this.textPosition}`]: true,
          'order-2': this.orderReversed
        }
      ]
    },
    imageClasses() {
      return [
        {
          'shadow-sm': this.imageShadow
        }
      ]
    },
    secondReverseClass() {
      return {
        'order-1': this.orderReversed
      }
    }
  },

  mounted() {

  }
}
</script>

<style scoped>
  @media(min-width: 993px) {
    .mt-6 {
      margin-top: 60px !important;
    }
  }
  
  p {
    font-weight: 300;
    font-size: 1.5rem;
  }
</style>
