<template>
  <div>
    <NavOne />
    <PageHeader title="Контакты" />
    <Contact />
    <Faq/>
    <Footer />
  </div>
</template>


<script>
  import NavOne from "../components/NavOne.vue";
  import Faq from "../components/Faq.vue";
  import PageHeader from "../components/PageHeader.vue";
  import Contact from "../components/Contact.vue";
  import Footer from "../components/Footer.vue";
  export default {
    components: {
      NavOne,
      Faq,
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
