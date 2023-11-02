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
  import PageHeader from "../components/PageHeader.vue";
  import Donation from "../components/Donation.vue";
  import Footer from "../components/Footer.vue";
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
        title: "JobAsk | Контакты"
      }
    }
  }
</script>
