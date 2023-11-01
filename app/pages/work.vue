<template>
  <div>
    <NavOne />
    <PageHeader title="History" />
    <History />
    <FunFactOne />
    <CallToActionOne />
    <Footer />
  </div>
</template>


<script>
  import NavOne from "../components/NavOne.vue";
  import PageHeader from "../components/PageHeader.vue";
  import History from "../components/History.vue";
  import CallToActionOne from "../components/CallToActionOne.vue";
  import Footer from "../components/Footer.vue";
  export default {
    components: {
      NavOne,
      PageHeader,
      History,
      CallToActionOne,
      Footer,
    },
    head(){
      return {
        title: "Potisen | History"
      }
    }
  }
</script>
