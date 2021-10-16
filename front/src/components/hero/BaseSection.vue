<template>
  <section ref="section" :class="sectionClasses" :id="sectionId">
    <div class="container">
      <slot></slot>
    </div>
  </section>
</template>

<script>
import { imageMixin, sectionMixin } from './mixins'

export default {
  // Represents a section of 
  // the Hero page

  name: 'BaseSection',
  mixins: [imageMixin, sectionMixin],
  props: {
    // color: {
    //   type: String,
    //   default: null
    // },
    // iconColor: {
    //   type: String,
    //   default: 'text-dark'
    // },
    // sectionId: {
    //   type: String,
    //   required: false
    // },
    // src: String,
    // theme: {
    //   type: String,
    //   default: 'light'
    // },
    // textWhite: Boolean
  },

  mounted() {
    if (this.hasImage) {
      this.$refs.section.style.backgroundImage = this.getBackgroundUrl(this.src)
    }
  },

  computed: {
    sectionClasses() {
      return [
        {
          'bg-image': this.hasImage,
          [`bg-${this.theme}`]: this.theme,
          'text-white': this.textWhite
        },
        this.color
      ]
    },

    hasImage() {
      return this.src != null
    }
  }
}
</script>

<style scoped>
  section {
    position: relative;
    text-align: center;
  }

  @media(min-width: 993px) {
    section {
      padding: 90px 45px 100px;
    }
  }
</style>
