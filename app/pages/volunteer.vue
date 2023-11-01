<template>
  <div>
    <NavTwo />
    <PageHeader title="Volunteer" />
    <Volunteer />
    <CallToActionOne />
    <Footer />
  </div>
</template>


<script>
  import NavTwo from "../components/NavTwo.vue";
  import PageHeader from "../components/PageHeader.vue";
  import Volunteer from "../components/Volunteer.vue";
  import CallToActionOne from "../components/CallToActionOne.vue";
  import Footer from "../components/Footer.vue";
  export default {
    components: {
      NavTwo,
      PageHeader,
      Volunteer,
      CallToActionOne,
      Footer,
    },
    head(){
      return {
        title: "Potisen | Volunteer"
      }
    }
  }
</script>
