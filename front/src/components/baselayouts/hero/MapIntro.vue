<template>
  <div
    id="map"
    :class="extraClass"
    class="map-container mb-4"
  >
    <iframe
      :src="locationUrl"
      frameborder="0"
    />
  </div>
</template>

<script>
export default {
  name: 'MapIntro',
  props: {
    locationUrl: {
      type: String,
      default: 'https://maps.google.com/maps?q=Manhatan&t=&z=15&ie=UTF8&iwloc=&output=embed'
    },
    shadow: {
      type: Boolean,
      default: true
    }
  },

  computed: {
    extraClass() {
      return {
        'z-depth-1-half': this.shadow
      }
    }
  }
}
</script>

<style scoped>
  .map-container {
    overflow: hidden;
    height: 500px;
    /* padding-bottom: 56.25%; */
    position: relative;
  }

  .z-depth-1-half {
    -webkit-box-shadow: 0 5px 11px 0 rgb(0 0 0 / 18%), 0 4px 15px 0 rgb(0 0 0 / 15%) !important;
    box-shadow: 0 5px 11px 0 rgb(0 0 0 / 18%), 0 4px 15px 0 rgb(0 0 0 / 15%);
  }

  .map-container iframe {
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;
    position: absolute;
    border: 0;
  }
</style>
