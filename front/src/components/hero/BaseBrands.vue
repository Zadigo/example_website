<template>
  <div class="partners p-5 bg-light" id="partners" aria-label="Partners">
    <small class="text-uppercase text-smaller m-0 text-muted">
      {{  description }}
    </small>

    <div class="brands">
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
  }
}
</script>

<style scoped>
  .brands {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: auto;
  }
</style>
