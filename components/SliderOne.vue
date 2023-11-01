<template>
  <section class="static-banner-one">
    <div class="static-banner-one__bg">
      <div class="static-banner-one__bg-inner" style="background-image: url(assets/images/background/inner-banner-bg.jpg);"></div><!-- /.static-banner-one__bg-inner -->
    </div><!-- /.static-banner-one__bg -->
    <div class="container">
      <vue-typed-js :loop="true" :strings="['Ждет', 'Нанимает', 'Приглашает']">
        <h2 class="static-banner-one__title">
          Работа это просто <br />
          Европа <span class="typed-effect typing"></span>
        </h2>
      </vue-typed-js>

      <div class="mc-form__response"></div><!-- /.mc-form__response -->
    </div><!-- /.container -->
  </section>
</template>

<script>
    export default {
        name: "SliderOne"
    }
</script>

<style scoped>

</style>
