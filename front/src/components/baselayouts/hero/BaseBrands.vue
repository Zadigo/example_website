<template>
  <div class="partners bg-light" id="partners" aria-label="Partners">
    <div class="wrapper">
      <div class="text-uppercase text-smaller ml-md-5 text-muted">
        {{  description }}
      </div>

      <div ref="brands" class="brands">
        <b-img v-for="(item, index) in items" :key="index" :src="item.image" :height="imageHeight" :alt="item.name" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseBrands',
  props: {
    description: {
      type: String,
      default: 'Trusted by product-led innovators around the world'
    },
    items: {
      type: Array
    },
    imageHeight: {
      type: Number,
      default: 50
    }
  },
  mounted() {
    // Set the grid template dynamically based on the
    // number of items in the list
    // this.$refs.brands.style.gridTemplateColumns = `repeat(${this.items.length}, 1fr)`
  }
}
</script>

<style scoped>
  .partners .wrapper {
    padding: 1rem;
  }

  .brands {
    display: grid;
    grid-template-rows: auto;
  }

  .text-smaller {
    font-size: .7rem;
  }

  @media(min-width: 320px) {
    .brands {
      padding: 1rem;
      grid-template-columns: repeat(2, 1fr);
      text-align: center;
      vertical-align: middle;
    }

    .brands img {
      margin: .75rem;
    }

    /* .text-sm-center {
      text-align: center;
    } */
  }

  @media(min-width: 993px) {
    .brands {
      padding: 0 0 1rem 0;
      grid-template-columns: repeat(8, 1fr);
    }
  }
</style>
