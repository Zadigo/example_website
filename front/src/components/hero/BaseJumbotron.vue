<template>
  <section>
    <header>
      <router-view name="nav" />
    </header>

    <main class="my-5">
      <div class="container">
        <section>
          <div id="intro" class="p-5 text-center bg-light shadow-5 rounded-5 mb-5">
            <h1 class="mb-3 h2">Learn Bootstrap 5 with MDB</h1>
            <p class="mb-3">Best & free guide of responsive web design</p>
            <a class="btn btn-primary m-2" href="https://www.youtube.com/watch?v=c9B4TPnak1A" role="button" rel="nofollow" target="_blank">Start tutorial</a>
            <a class="btn btn-primary m-2" href="https://mdbootstrap.com/docs/standard/" target="_blank" role="button">Download MDB UI KIT</a>
          </div>
        </section>

        <slot></slot>
      </div>
    </main>
  </section>
</template>

<script>
export default {
  name: 'BaseJumbotron',
  props: {
    hasContainer: Boolean
  }
}
</script>

<style scoped>
  #intro {
    margin-top: 100px;
  }
</style>
