<template>
  <!-- <b-carousel-slide v-for="(image, index) in images" :key="index" :img-src="image.url" /> -->
    
  <!-- <div class="mask" style="background-color: rgba(0, 0, 0, 0.6);z-index:9999;">
      <b-carousel @sliding-start="onSlideStart" @sliding-end="onSlideEnd" v-model="slide" :interval="4000" controls indicators class="carousel-fade shadow-2-strong" id="carousel-intro">
        <b-carousel-slide v-for="(image, index) in images" :key="index">
          <template #img>
            <img :src="image.url" class="d-block img-fluid w-100" alt="image slot">
          </template>
        </b-carousel-slide>
      </b-carousel>
    </div> -->

  <div
    id="carousel-intro"
    class="carousel slide carousel-fade shadow-2-strong"
  >
    <ol class="carousel-indicators">
      <li
        v-for="i in images.length"
        :key="i"
        :class="isActive(i)"
        @click="slide=i"
      />
    </ol>

    <div class="carousel-inner">
      <div
        v-for="(image, index) in images"
        :key="index"
        class="carousel-item"
        :class="isActive(index)"
      >
        <div
          class="mask"
          style="background-color: rgba(0, 0, 0, 0.6);"
        >
          <div class="d-flex justify-content-center align-items-center h-100">
            <slot />
          </div>
        </div>
      </div>
    </div>

    <a
      class="carousel-control-prev"
      role="button"
      @click="goToPrevious"
    >
      <span
        aria-hidden="true"
        class="carousel-control-prev-icon"
      />
      <span class="sr-only">Previous</span>
    </a>

    <a
      class="carousel-control-next"
      role="button"
      @click="goToNext"
    >
      <span
        aria-hidden="true"
        class="carousel-control-next-icon"
      />
      <span class="sr-only">Next</span>
    </a>
  </div>
</template>

<script>
export default {
  name: 'CarouselIntro',
  props: {
    images: {
      type: Array,
      required: true
    }
  },

  data() {
    return {
      slide: 1,
      sliding: null
    }
  },

  computed: {
    numSlides() {
      return this.images.length
    }
  },

  methods: {
    onSlideStart(slide) {
      slide
      this.sliding = true
    },
    onSlideEnd(slide) {
      slide
      this.sliding = false
    },
    goToPrevious() {
      var result = this.slide - 1
      if (result < 1) {
        this.slide = this.images.length
      } else {
        this.slide = result
      }
    },
    goToNext() {
      var result = this.slide + 1
      if (result > this.images.length) {
        this.slide = 1
      } else {
        this.slide = result
      }
    },
    isActive(index) {
      return { 'active': this.slide === index }
    }
  }
}
</script>

<style scoped>
  #carousel-intro,
  .carousel-inner,
  .carousel-item,
  .carousel-item.active {
    height: 100vh;
  }
</style>
