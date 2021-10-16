<template>
  <div class="input-group">
    <b-input @update="updateData" v-for="(item, index) in items" :key="index" :type="item.type"></b-input>
  </div>
</template>

<script>
export default {
  name: 'InputGroup',
  props: {
    items: {
      type: Array,
      required: true,
      default: () => []
    }
  },

  data() {
    return {
      newData: {}
    }
  },

  methods: {
    updateData(value) {
      this.newData[value]
    }
  }
}
</script>

<style scoped>
  .input-group {
    display: flex;
    background-color: white;
    padding: 1rem;
    border-radius: .5rem;
    width: auto;
    margin: 0 auto;
    /* align-items: center; */
    /* justify-content: center; */
    box-shadow: 0 10px 15px -3px rgb(0 0 0 / 7%), 0 4px 6px -2px rgb(0 0 0 / 5%);
  }

  .input-group .v-input {
    max-width: 20%;
  }

  .input-group .v-input:not(:last-child) {

  }
</style>
