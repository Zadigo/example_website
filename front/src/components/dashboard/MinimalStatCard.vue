<template>
  <div class="col-xl-3 col-sm-6 col-12 mb-4">
    <div class="card">
      <div class="card-body">

        <div class="d-flex justify-content-between px-md-1">
          <div class="align-self-center">
            <font-awesome-icon :icon="icon" :class="`text-${color}`" class="fa-3x"></font-awesome-icon>
          </div>

          <div class="text-end">
            <h3>{{ value  }}<span v-if="isPercentage">%</span></h3>
            <p class="mb-0">
              {{ title }}
            </p>
          </div>
        </div>
      
        <div v-if="shareValue != null" class="px-md-1">
          <div class="progress mt-3 mb-1 rounded" style="height: 7px">
            <div :aria-valuenow="shareValue" :class="`bg-${color}`" class="progress-bar" role="progressbar" style="width: 80%" aria-valuemin="0" aria-valuemax="100"></div>
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
    icon: String,
    color: {
      default: 'text-primary'
    },
    value: null,
    title: String,
    isPercentage: Boolean,
    shareValue: {
      type: Number,
      default: null
    }
  }
}
</script>
