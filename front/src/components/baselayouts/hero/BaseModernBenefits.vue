<template>
  <section class="text-center card p-5">
    <div class="row">
      <div class="col-lg-3 col-md-6 mb-4 mb-lg-0 position-relative">
        <font-awesome-icon icon="cubes" class="fa-3x text-theme mb-4" />
        <h4 class="text-theme fw-bold mb-3">5000+</h4>
        <h5 class="fw-normal mb-0">Components</h5>
        <hr class="divider-vertical  d-none d-md-block">
      </div>

      <div class="col-lg-3 col-md-6 mb-4 mb-lg-0 position-relative">
        <font-awesome-icon icon="layer-group" class="fas fa-layer-group fa-3x text-theme mb-4" />
        <h4 class="text-theme fw-bold mb-3">150+</h4>
        <h5 class="fw-normal mb-0">Design blocks</h5>
        <hr class="divider-vertical d-none d-lg-block">
      </div>

      <div class="col-lg-3 col-md-6 mb-4 mb-lg-0 position-relative">
        <font-awesome-icon icon="image" class="fa-3x text-theme mb-4" />
        <h4 class="text-theme fw-bold mb-3">100+</h4>
        <h5 class="fw-normal mb-0">Templates</h5>
        <hr class="divider-vertical d-none d-md-block">
      </div>

      <div class="col-lg-3 col-md-6 mb-4 mb-lg-0 position-relative">
        <font-awesome-icon icon="plug" class="fa-3x text-theme mb-4" />
        <h4 class="text-theme fw-bold mb-3">28</h4>
        <h5 class="fw-normal mb-0">Plugins</h5>
      </div>

    </div>
  </section>
</template>

<script>
export default {
  name: 'BaseModernBenefits'
}
</script>

<style scoped>
  .text-theme {
    color: #7446ac !important;
  }

  hr.divider-vertical {
    position: absolute;
    background-color: transparent;
    height: 100%;
    right: 0;
    top: 0;
    width: 1px;
    background-image: linear-gradient(180deg, transparent, rgba(0, 0, 0, 0.4), transparent);
  }

  .fw-bold {
    font-weight: 700!important;
  }

  .fw-normal {
    font-weight: 400!important;
  }
</style>
