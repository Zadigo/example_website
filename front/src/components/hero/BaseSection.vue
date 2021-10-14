<template>
  <section ref="baseSection" :class="extraClass" :id="sectionId" :iconColor="iconColor">
    <div class="container">
      <slot></slot>
    </div>
  </section>
</template>

<script>
export default {
  // Represents a section of the Hero page
  name: 'BaseSection',
  props: {
    image: String,
    color: {
      type: String,
      default: 'bg-light'
    },
    iconColor: {
      type: String,
      default: 'text-dark'
    },
    sectionId: {
      type: String,
      required: false
    }
  },

  mounted() {
    if (this.image != null) {
      this.$refs.baseSection.style.backgroundImage = `url(${this.image})`
    }
  },

  computed: {
    extraClass() {
      if (this.image == undefined) {
        return this.color
      } else {
        return {
          'bg-image': this.image != undefined,
          // 'bg-light': this.color === 'light',
          // 'bg-dark text-white': this.color === 'dark',
        }
      }
    }
  }
}
</script>

<style scoped>
  section {
    position: relative;
    padding: 90px 45px 100px;
    text-align: center;
  }
</style>
