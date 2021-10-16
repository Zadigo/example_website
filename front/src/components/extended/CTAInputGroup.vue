<template>
  <b-input-group :class="inputGroupClasses">
    <b-form-input @change="$emit('ctaInputChange')" :placeholder="placeholder"></b-form-input>
    <b-btn @click="$emit('ctaButtonClick')" :class="buttonClasses" :variant="buttonColor">{{ buttonName }}</b-btn>
  </b-input-group>
</template>

<script>
export default {
    name: 'CTAInputGroup',
    props:{
      buttonFlat: Boolean,
      buttonName: {
        type: String,
        required: true
      },
      buttonColor: String,
      filled: Boolean,
      placeholder: String
    },

    computed: {
      inputGroupClasses() {
        return [
          'cta-input-group',
          {
            'filled': this.filled
          }
        ]
      },

      buttonClasses() {
        return [
          {
            'shadow-none': this.buttonFlat
          },
          this.buttonColor
        ]
      }
    }
}
</script>

<style scoped>
  .cta-input-group.filled {
    padding: 1rem;
    background-color: white;
    border-radius: 8px;
  }

  .cta-input-group>.form-control {
    min-height: calc(3.08rem + 2px);
    height: calc(3.08rem + 2px);
    font-weight: 600;
    font-size: 16px;
    border-radius: 8px;
  }
</style>
