<template>
  <div>
    <NavOne />
    <PageHeader title="Contact" />
    <Contact />
    <Footer />
  </div>
</template>


<script>
  import NavTwo from "../components/NavOne";
  import PageHeader from "../components/PageHeader";
  import Contact from "../components/Contact";
  import Footer from "../components/Footer";
  export default {
    components: {
      NavOne,
      PageHeader,
      Contact,
      Footer,
    },
    head(){
      return {
        title: "Potisen | Contact"
      }
    }
  }
</script>
