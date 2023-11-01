<template>
  <section class="countdown-one thm-base-bg">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <h3 class="countdown-one__title">Our new campaign <br> starts in:</h3><!-- /.countdown-one__title -->
        </div><!-- /.col-lg-6 -->
        <div class="col-lg-6 d-flex justify-content-end">
          <client-only>
            <Countdown end="August 22, 2022"></Countdown>
          </client-only>
        </div><!-- /.col-lg-6 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
  import Countdown from 'vuejs-countdown'

  export default {
    name: "CountdownTwo",
    components: {Countdown}
  }
</script>

<style scoped>

</style>
