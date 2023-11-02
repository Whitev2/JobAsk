<template>

  <section class="inner-banner">
    <div class="container">
      <h2 class="inner-banner__title">Работа</h2><!-- /.inner-banner__title -->
      <ul class="list-unstyled thm-breadcrumb">
        <li>
          <nuxt-link to="/">Главная</nuxt-link>
        </li>
        <li>Работа</li>
      </ul><!-- /.list-unstyled -->
    </div><!-- /.container -->
  </section>

</template>

<script>
  export default {
    name: "PageHeader",
    props: {
      title: {
        type: String
      }
    }

  }
</script>

<style scoped>

</style>
