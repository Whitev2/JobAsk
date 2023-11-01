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
  import NavOne from "../components/NavOne";
  import PageHeader from "../components/PageHeader";
  import History from "../components/History";
  import CallToActionOne from "../components/CallToActionOne";
  import Footer from "../components/Footer";
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
