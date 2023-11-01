<template>
  <section class="countdown-one thm-gray-bg countdown-one__home-one">
    <div class="container">
      <div class="inner-container">
        <div class="row align-items-xl-center align-items-lg-center">
          <div class="col-xl-6">
            <h3 class="countdown-one__title">Our new campaign starts in:</h3><!-- /.countdown-one__title -->
          </div><!-- /.col-lg-6 -->

          <client-only>
            <Countdown end="August 22, 2022"></Countdown>
          </client-only>
          <div class="col-xl-6 d-flex justify-content-xl-end justify-content-lg-center justify-content-sm-center">
            <div class="countdown-one__right">

            </div><!-- /.countdown-one__right -->
          </div><!-- /.col-lg-6 -->
        </div><!-- /.row -->
      </div><!-- /.inner-container -->
    </div><!-- /.container -->
  </section>
</template>

<script>
  import Countdown from 'vuejs-countdown'
  export default {
    name: "CountdownOne",
    components: { Countdown }
  }
</script>

<style scoped>

</style>
