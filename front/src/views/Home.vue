<template>
  <base-home-page>
    <template v-slot:navbar>
      <base-navbar :fixedTop="false" theme="red dark" />
    </template>

    <template v-slot:intro>
      <base-intro :image="images[0].url">
        <h2>This a great thing to do</h2>
      </base-intro>
    </template>

    <template>
      <div class="container">
        <div class="row">
          <div class="col-12">
            <modern-benefits />
          </div>
        </div>
      </div>
    </template>
  </base-home-page>

  <!-- <base-jumbotron lead="Learn Bootstrap 5 with MDB" subTitle="Best & free guide of responsive web design" color="blue">
    <template v-slot:navbar>
      <base-navbar :fixedTop="false" />
    </template>
  </base-jumbotron> -->

  <!-- <base-home-page>
    <template v-slot:navbar>
      <base-navbar />
    </template>

    <template v-slot:intro>
      <base-intro image="https://mdbootstrap.com/img/new/fluid/city/018.jpg">
      <base-intro image="https://picsum.photos/1200" :mask="0.5">
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
      
      <base-section sectionId="section-id" color="blue darken-4">
        <h1 class="text-white">“Within two months of deploying Appcues, we improved first-week retention by nearly 20%.”</h1>
        <hr class="text-light my-5" >
        <b-btn :to="{ name: 'home' }" variant="primary" class="btn-lg btn-outline mt-4 text-white">Visit this</b-btn>
      </base-section>

      <benefits :items="companyDetails.benefits" sectionId="section-id" color="red darken-1" iconColor="text-red">
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
      </benefits> 
    </template>

  </base-home-page> -->
</template>

<script>
export default {
  name: 'Home',

  data() {
    return {
      showSidebar: false,
      footerColumns: [
        { title: 'Home', links: [{ title: 'Home', name: 'home' }, { title: 'Contact', name: 'home' }] },
        { title: 'Contact', links: [{ title: 'Contact', name: 'home' }] }
      ],

      images: [
        {
          url: 'https://images.unsplash.com/photo-1432139555190-58524dae6a55?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fGZvb2R8ZW58MHwwfDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=60'
        },
        {
          url: 'https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjV8fGZvb2R8ZW58MHwwfDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=60'
        },
        {
          url: 'https://images.unsplash.com/photo-1561758033-d89a9ad46330?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDF8fGZvb2R8ZW58MHwwfDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=60'
        }
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
