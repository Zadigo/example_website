<template>
  <section ref="jumbotron" id="jumbotron">
    <!-- Navbar -->
    <slot name="navbar"></slot>

    <div :class="containerClasses">
      <div :class="introClasses" class="p-5 text-center" id="intro">
        
        <slot name="lead">
          <h1 class="mb-3 h2">{{ lead }}</h1>
          <p class="mb-3">{{ subTitle }}</p>
        </slot>

      </div>

      <!-- Content -->
      <slot></slot>
    </div>

    <!-- Footer -->
    <slot name="footer"></slot>
  </section>
</template>

<script>
import { imageMixin } from './mixins'

export default {
  name: 'BaseJumbotron',
  mixins: [imageMixin],
  props: {
    containerized: Boolean,
    color: String,
    src: String,
    lead: String,
    marginTop: {
      type: Number,
      default: 0
    },
    subTitle: String,
    theme: {
      type: String,
      default: 'light'
    }
  },

  mounted() {
    if (this.containerized) {
      this.$refs.jumbotron.style.marginTop = `${this.marginTop}px`
    }

    if (this.src != null) {
      document.getElementById('intro').style.backgroundImage = this.getBackgroundUrl(this.src)
    }
  },

  computed: {
    containerClasses() {
      return [
        { 'container': this.containerized }
      ]
    },
    introClasses() {
      // var attrs = {
      //   'container shadow-5 rounded-5 mb-5': this.containerized,
      //   'bg-image': this.hasImage,
      //   'bg-light': this.theme === 'light' | this.theme == null,
      //   'bg-dark': this.theme === 'dark'
      // }

      // attrs[this.color] = this.hasColor
      // attrs['text-white'] = this.hasColor | this.hasImage | this.darkTheme

      // return attrs
      return [
        {
          'container': this.containerized,
          'shadow-5': this.containerized,
          'rounded-5': this.containerized,
          'mb-5': this.containerized,
          'bg-image': this.hasImage,
          [this.color]: this.hasColor,
          [`bg-${this.theme}`]: true
        }
      ]
    },

    hasColor() {
      return this.color != null
    },

    hasImage() {
      return this.src != null
    },

    darkTheme() {
      return this.theme === 'dark'
    }
  }
}
</script>
