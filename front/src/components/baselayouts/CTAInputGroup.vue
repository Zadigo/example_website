<template>
  <b-input-group :class="inputGroupClasses">
    <b-form-input
      v-model="email"
      :placeholder="placeholder"
      :type="inputType"
    />
    <b-btn
      :class="buttonClasses"
      :variant="buttonColor"
      @click="$emit('ctaButtonClick', email), email = null"
    >
      {{ buttonName }}
    </b-btn>
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
      buttonColor: {
        type: String,
        default: null 
      },
      filled: Boolean,
      inputType: {
        type: String,
        default: null
      },
      placeholder: {
        type: String,
        default: null
      }
    },

    data() {
      return {
        email: null
      }
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
