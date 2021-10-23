<template>
  <div
    id="intro"
    ref="intro"
    :class="introClasses"
  >
    <div class="mask">
      <div
        ref="container"
        class="container"
        :class="containerClasses"
      >
        <div
          ref="wrapper"
          class="wrapper"
          :class="wrapperClasses"
        >
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { imageMixin } from './mixins'

export default {
  // Represents the image and the mask element
  // used for the hero. The user has to implement
  // the rest of the elements (lead, call to action...)
  
  name: 'BaseIntro',
  mixins: [imageMixin],
  props: {
    // height: {
    //   type: String,
    //   default: '100'
    // },
    color: {
      type: String,
      default: 'blue'
    },
    containerClass: {
      type: String,
      default: null
    },
    correctionTop: {
      type: Number,
      default: null
    },
    flexPosition: {
      type: String,
      default: 'center'
    },
    introClass: {
      type: String,
      default: null
    },
    isFullPage: Boolean,
    mask: {
      type: Number,
      default: 0.8
    },
    shadow: Boolean,
    src: String,
    textWhite: {
      type: Boolean,
      default: true
    },
    textPosition: {
      type: String,
      default: 'center'
    },
    wrapperClass: {
      type: String,
      default: null
    }
  },

  computed: {
    introClasses() {
      return [
        {
          [`${this.color}`]: true,
          'bg-image': this.hasImage,
          'shadow-2-strong': this.shadow,
        },
        this.introClass
      ]
    },
    containerClasses() {
      return [
        'd-flex', 
        'h-100',
        'align-items-center',
        {
          [`justify-content-${this.flexPosition}`]: true,
          [`text-${this.textPosition}`]: true,
          'text-white': this.textWhite
        },
        this.containerClass
      ]
    },
    wrapperClasses() {
      return [
        this.wrapperClass
      ]
    },
    // extraClass() {
    //   return {
    //     'd-flex align-items-center h-100':  this.isFullPage
    //   }
    // },

    hasImage() {
      return this.src != null
    }
  },

  mounted() {
    if (this.hasImage) {
      // Sets the intro's height
      // this.$refs.intro.style.height = `${this.height}vh`

      // Set the background image dynamically here
      // this.$refs.intro.style.backgroundImage = `url(${this.src})`
      this.$refs.intro.style.backgroundImage = this.getBackgroundUrl(this.src)

      // Add a mask to darken the image
      var maskDiv = this.$refs.intro.getElementsByClassName('mask')[0]
      maskDiv.style.backgroundColor = `rgba(0, 0, 0, ${this.mask})`
    }

    // Applies a correction to intro when there is a Navbar
    // on the page (generally between 50/73 pixels)
    if (!this.isFullPage) {
      this.$refs.intro.style.marginTop = `-${this.correctionTop}px`
    }
  }
}
</script>

<style scoped>
  #intro {
    height: 100vh;
  }
</style>
