<template>
  <div>
    <NavOne />
    <Donation/>
    <Faq/>
    <Footer />
  </div>
</template>


<script>
  import NavOne from "../components/NavOne.vue"
  import Faq from "../components/Faq.vue"
  import PageHeader from "../components/PageHeader";
  import Donation from "../components/Donation";
  import Footer from "../components/Footer";
  export default {
    components: {
      NavOne,
      PageHeader,
      Donation,
      Faq,
      Footer,
    },
    head(){
      return {
        title: "ВНЖ"
      }
    }
  }
</script>
