<template>
  <div>
    <NavOne/>
    <SliderOne />
    <AboutFour />
    <Faq/>
    <Footer />
  </div>
</template>

<script>
  import NavOne from "../components/NavOne.vue";
  import Faq from "../components/Faq.vue";
  import SliderOne from "../components/SliderOne.vue";
  import AboutFour from "../components/AboutFour.vue";
  import Footer from "../components/Footer.vue";

  export default {
    components: {
      Faq,
      NavOne,
      SliderOne,
      Footer,
      AboutFour
    }
  }
</script>

