<template>
  <base-home-page>
    <template v-slot:navbar>
      <base-navbar />
    </template>

    <template v-slot:intro>
      <base-intro image="https://mdbootstrap.com/img/new/fluid/city/018.jpg">
        <template>
          <div class="text-white">
            <h1 class="mb-3">Learn Bootstrap 5 with MDB</h1>
            <h5 class="mb-4">Best & free guide of responsive web design</h5>
            <router-link :to="{ name: 'home' }" class="btn btn-outline-light btn-lg m-2">
              Start tutorial
            </router-link>
          </div>
        </template>
      </base-intro>
    </template>

    <template>
      <base-brands class="m-0" :items="companyDetails.partners" description="Trusted by product innovators around the world" />
      
      <!-- <base-section sectionId="section-id" color="blue darken-4">
        <h1 class="text-white">“Within two months of deploying Appcues, we improved first-week retention by nearly 20%.”</h1>
        <hr class="text-light my-5" >
        <b-btn :to="{ name: 'home' }" variant="primary" class="btn-lg btn-outline mt-4 text-white">Visit this</b-btn>
      </base-section> -->

      <!-- <benefits :items="companyDetails.benefits" sectionId="section-id" color="red darken-1" iconColor="text-red">
        <template v-slot:heading>
          <div class="col-10 offset-1">
            <h1 class="text-white mb-4">This is a great title</h1>
            <p class="text-white">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia sapiente possimus natus 
              fugiat tenetur placeat nihil quia optio, assumenda aliquam ipsam, eaque, dolores deserunt 
              laboriosam exercitationem quas doloribus ducimus accusantium!
            </p>
          </div>
        </template>
      </benefits>  -->
    </template>

  </base-home-page>
</template>

<script>
export default {
  name: 'Home',

  data() {
    return {
      footerColumns: [
        { title: 'Home', links: [{ title: 'Home', name: 'home' }, { title: 'Contact', name: 'home' }] },
        { title: 'Contact', links: [{ title: 'Contact', name: 'home' }] }
      ]
    }
  }
}
</script>

<style>
  /* .navbar .nav-link {
    color: #fff !important;
  }

  @media (min-width: 991.98px) {
    main {
      padding-left: 0px;
    }
  } */
</style>
