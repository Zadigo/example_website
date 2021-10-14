<template>
  <div ref="intro" :class="{ 'shadow-2-strong': shadow }" id="intro" class="bg-image">
    <div class="mask">
      <div :class="containerClass" class="container d-flex h-100">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // Represents the image and the mask element
  // used for the hero. The user has to implement
  // the rest of the elements (lead, call to action...)
  
  name: 'BaseIntro',
  props: {
    image: String,
    mask: {
      type: Number,
      default: 0.8
    },
    isFullPage: Boolean,
    shadow: Boolean,
    containerClass: {
      type: String,
      default: 'align-items-center justify-content-center text-center'
    }
  },

  mounted() {
    // Set the background image dynamically here -;
    // also the mask that helps darken the image
    this.$refs.intro.style.backgroundImage = `url(${this.image})`
    var maskDiv = this.$refs.intro.getElementsByClassName('mask')[0]
    maskDiv.style.backgroundColor = `rgba(0, 0, 0, ${this.mask})`
  },

  computed: {
    extraClass() {
      return {
        'd-flex align-items-center h-100':  this.isFullPage
      }
    }
  }
}
</script>

<style scoped>
  #intro {
    height: 100vh;
  }

  @media (min-width: 992px) {
    #intro {
      margin-top: -73px;
    }
  }
</style>
