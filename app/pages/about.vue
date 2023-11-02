<template>
  <div>
    <NavOne />
    <PageHeader title="About" />
    <AboutOne />
    <AboutTwo />
    <CallToActionTwo />
    <TestimonialOne />
    <TeamOne />
    <CallToActionOne />
    <Footer />
  </div>
</template>


<script>
  import NavOne from "../components/NavOne.vue";
  import PageHeader from "../components/PageHeader.vue";
  import Footer from "../components/Footer.vue";
  import AboutOne from "../components/AboutOne.vue";
  import CallToActionTwo from "../components/CallToActionTwo.vue";
  import AboutTwo from "../components/AboutTwo.vue";
  import TestimonialOne from "../components/TestimonialOne.vue";
  import TeamOne from "../components/TeamOne.vue";
  import CallToActionOne from "../components/CallToActionOne.vue";
  export default {
    components: {
      AboutOne,
      NavOne,
      PageHeader,
      AboutTwo,
      CallToActionTwo,
      TestimonialOne,
      TeamOne,
      CallToActionOne,
      Footer,
    },
    head(){
      return {
        title: "JobAsk | О нас"
      }
    }
  }
</script>
