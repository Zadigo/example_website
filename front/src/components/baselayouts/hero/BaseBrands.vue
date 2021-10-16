<template>
  <div class="partners bg-light" id="partners" aria-label="Partners">
    <small class="text-uppercase text-smaller m-0 text-muted">
      {{  description }}
    </small>

    <div ref="brands" class="brands">
      <b-img v-for="(item, index) in items" :key="index" :src="item.image" :height="imageHeight" :alt="item.name" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseBrands',
  props: {
    description: String,
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
  .brands {
    display: grid;
    grid-template-rows: auto;
  }

  @media(min-width: 320px) {
    .brands {
      padding: 1.5rem;
      grid-template-columns: repeat(2, 1fr);
      text-align: center;
      vertical-align: middle;
    }

    .brands img {
      margin: .75rem;
    }
  }

  @media(min-width: 993px) {
    .brands {
      padding: 2rem;
      grid-template-columns: repeat(8, 1fr);
    }
  }

</style>
