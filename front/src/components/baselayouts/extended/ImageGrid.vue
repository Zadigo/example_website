<template>
  <div ref="link" class="images">
    <transition-group tag="div" class="images-grid" name="image-transition">
      <div v-for="item in items" :key="item.url" id="grid-image bg-image" :style="`background-color: red`">
        <!-- <b-img :fluid="true" :lazy="true" :src="item.url" class="grid-item"></b-img> -->
      </div>
    </transition-group>
  </div>
</template>

<script>
export default {
  name: 'ImageGrid',
  props: {
    items: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<style scoped>
  .images-grid {
    position: relative;
    height: auto;
    width: 100%;
    min-height: 100%;
    display: grid;
    grid-template-columns: repeat(4, 300px);
    grid-template-rows: 1fr 300px;
    grid-column-gap: .3rem;
    grid-row-gap: .3rem;
  }

  .grid-image {
    height: 100%;
    width: 100%;
  }

  .grid-item:hover {
    transform: scale(.8s, .8s);
  }

  .image-transition-enter-active,
  .image-transition-leave-active {
    transition: all .5s ease;
  }

  .image-transition-enter,
  .image-transition-leave-to {
    opacity: 0;
  }

  .image-transition-leave,
  .image-transition-enter-to {
    opacity: 1;
  }
</style>
