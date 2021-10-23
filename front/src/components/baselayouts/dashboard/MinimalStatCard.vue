<template>
  <div class="col-xl-3 col-sm-6 col-12 mb-4">
    <div class="card">
      <div class="card-body">
        <div class="d-flex justify-content-between px-md-1">
          <div class="align-self-center">
            <font-awesome-icon
              class="fa-3x"
              :class="`text-${color}`"
              :icon="icon"
            />
          </div>

          <div class="text-end">
            <h3>{{ value }}<span v-if="isPercentage">%</span></h3>
            <p class="mb-0">
              {{ title }}
            </p>
          </div>
        </div>
      
        <div
          v-if="shareValue != null"
          class="px-md-1"
        >
          <div
            class="progress mt-3 mb-1 rounded"
            style="height: 7px"
          >
            <div
              aria-valuemax="100"
              aria-valuemin="0"
              :aria-valuenow="shareValue"
              class="progress-bar"
              :class="`bg-${color}`"
              role="progressbar"
              style="width: 80%"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MinimalStatCard',
  props: {
    icon: {
      type: {
        type: String,
        default: null
      },
      default: null
    },
    color: {
      default: 'text-primary'
    },
    value: null,
    title: {
      type: String,
      default: null
    },
    isPercentage: Boolean,
    shareValue: {
      type: Number,
      default: null
    }
  }
}
</script>
