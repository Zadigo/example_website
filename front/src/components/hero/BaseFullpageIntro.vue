<template>
  <header>
    <div ref="intro" id="intro" class="bg-image shadow-2-strong">
      <div class="mask d-flex align-items-center h-100">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-md-8 col-xl-5">
              <slot></slot>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'BaseFullPageIntro',
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
