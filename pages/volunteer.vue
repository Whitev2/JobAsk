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
  import NavTwo from "../components/NavTwo";
  import PageHeader from "../components/PageHeader";
  import Volunteer from "../components/Volunteer";
  import CallToActionOne from "../components/CallToActionOne";
  import Footer from "../components/Footer";
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
