<template>
  <section ref="link" id="jumbotron">
    <!-- Navbar -->
    <slot name="navbar"></slot>

    <div :class="{ 'container': containerized }">
      <div :class="extraClass" class="p-5 text-center" id="intro">
        <slot name="lead">
          <h1 class="mb-3 h2">{{ lead }}</h1>
          <p class="mb-3">{{ subTitle }}</p>
        </slot>
      </div>

      <!-- Content -->
      <slot></slot>
    </div>

    <!-- Footer -->
    <slot name="footer"></slot>
  </section>
</template>

<script>
export default {
  name: 'BaseJumbotron',
  props: {
    containerized: Boolean,
    lead: String,
    subTitle: String,
    marginTop: {
      type: Number,
      default: 0
    },
    image: String,
    color: String
  },

  mounted() {
    if (this.containerized) {
      this.$refs.link.style.marginTop = `${this.marginTop}px`
    }

    if (this.image != null) {
      document.getElementById('intro').style.backgroundImage = `url(${this.image})`
    }
  },

  computed: {
    extraClass() {
      var attrs = {
        'container shadow-5 rounded-5 mb-5': this.containerized,
        'bg-image': this.hasImage,
        'bg-light': this.theme === 'light' | this.theme == null,
        'bg-dark': this.theme === 'dark'
      }

      attrs[this.color] = this.hasColor
      attrs['text-white'] = this.hasColor | this.hasImage | this.darkTheme

      return attrs
    },

    hasColor() {
      return this.color != null
    },

    hasImage() {
      return this.image != null
    },

    darkTheme() {
      return this.theme === 'dark'
    }
  }
}
</script>
