<template>
  <base-jumbotron lead="Learn Bootstrap 5 with MDB" subTitle="Best & free guide of responsive web design">
    <template #navbar>
      <base-navbar theme="light">

      </base-navbar>
    </template>

    <template>
      <base-pricing :shadow="false" :items="companyDetails.pricing" lead="Pricing for all our products" subTitle="Best & free guide of responsive web design">
      </base-pricing>
    </template>

     <template #footer>
      <base-footer>

      </base-footer>
    </template>
  </base-jumbotron>
</template>

