<template>
  <base-section :sectionId="sectionId" :color="color" :image="image" :iconColor="iconColor">
    <div class="row">

      <slot name="heading"></slot>

      <div v-for="(item, index) in items" :key="index" class="col-4">
        <v-card :class="{ 'border': bordered }" class="p-4" :flat="flat">
          <v-card-text>
            <font-awesome-icon v-if="isFontAwesomeIcon" :icon="item.icon" />
            <v-icon v-else :class="iconColor">mdi-{{ item.icon }}</v-icon>

            <h2 class="mt-4 mb-2 font-weight-bold">{{ item.title }}</h2>
            <p>{{ item.description }}</p>
          </v-card-text>
        </v-card>

        <slot name="footer"></slot>
      </div>

    </div>
  </base-section>
</template>

<script>
export default {
  name: 'Benefits',
  props: {
    sectionId: {
      type: String,
      required: true
    },
    items: {
      type: Array,
      default: () => []
    },
    color: {
      type: String,
      default: 'bg-light'
    },
    iconColor: {
      type: String,
      default: 'text-dark'
    },
    image: String,
    flat: Boolean,
    bordered: Boolean,
    isFontAwesomeIcon: Boolean
  }
}
</script>

<style scoped>
  .v-icon {
    font-size: 4rem;
  }
</style>
