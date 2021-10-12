<template>
  <div ref="intro" id="intro" class="bg-image shadow-2-strong">
    <div class="mask">
      <div class="container d-flex align-items-center justify-content-center text-center h-100">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseIntro',
  props: {
    image: String,
    mask: {
      type: Number,
      default: 0.8
    }
  },

  mounted() {
    this.$refs.intro.style.backgroundImage = `url(${this.image})`
    var maskDiv = this.$refs.intro.getElementsByClassName('mask')[0]
    maskDiv.style.backgroundColor = `rgba(0, 0, 0, ${this.mask})`
  }
}
</script>

<style scoped>
  #intro {
    height: 100vh;
  }

  @media (min-width: 992px) {
    #intro {
      /* margin-top: -58.59px; */
      margin-top: -72px;
    }
  }
</style>
