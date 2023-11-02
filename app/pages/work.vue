<template>
  <div>
    <NavOne />
    <PageHeader title="Работа" />
    <History />
    <Faq />
    <Footer />

  </div>
</template>


<script>
  import NavOne from "../components/NavOne.vue";
  import Faq from "../components/Faq.vue";
  import PageHeader from "../components/PageHeader.vue";
  import History from "../components/History.vue";
  import Footer from "../components/Footer.vue";
  export default {
    components: {
      NavOne,
      PageHeader,
      History,
      Faq,
      Footer,
    },
    head(){
      return {
        title: "JobAsk | Работа"
      }
    }
  }
</script>
