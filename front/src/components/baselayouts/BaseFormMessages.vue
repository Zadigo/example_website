<template>
  <div class="row">
    <div v-for="(item, index) in formMessages" :key="index" class="col-12">
      <b-alert show :variant="item.type">
        {{ item.message }}
      </b-alert>
    </div>
  </div>
</template>

<script>
export default {
  // Use this component to display messages
  // that are a result of form requests
  name: 'BaseFormMessages',
  props: {
    formMessages: {
      type: Array,
      default: () => []
    }
  },

  computed: {
    hasMessages() {
      return this.formMessages.length > 0
    }
  }
}
</script>
