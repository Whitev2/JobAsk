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
  import NavOne from "../components/NavOne";
  import PageHeader from "../components/PageHeader";
  import Footer from "../components/Footer";
  import AboutOne from "../components/AboutOne";
  import CallToActionTwo from "../components/CallToActionTwo";
  import AboutTwo from "../components/AboutTwo";
  import TestimonialOne from "../components/TestimonialOne";
  import TeamOne from "../components/TeamOne";
  import CallToActionOne from "../components/CallToActionOne";
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
        title: "Potisen | About"
      }
    }
  }
</script>
