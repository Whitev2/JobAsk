<template>
  <section class="fact-two" v-observe-visibility="onVisibilityChange">
    <div class="container">
      <div class="row">
        <div class="col-lg-3 col-md-6">
          <div class="fact-two__single text-center wow fadeInLeft" data-wow-duration="1500ms">
            <h3 class="fact-two__count counter"><countTo :startVal='0' :endVal='startCounter ? 2340 : 0' :duration='3000'></countTo></h3><!-- /.fact-two__count -->
            <p class="fact-two__text">Total Volunteer</p><!-- /.fact-two__text -->
          </div><!-- /.fact-two__single -->
        </div><!-- /.col-lg-3 col-md-6 -->
        <div class="col-lg-3 col-md-6">
          <div class="fact-two__single text-center wow fadeInLeft" data-wow-duration="1500ms" data-wow-delay="100ms">
            <h3 class="fact-two__count counter"><countTo :startVal='0' :endVal='startCounter ? 1403 : 0' :duration='3000'></countTo></h3><!-- /.fact-two__count -->
            <p class="fact-two__text">Campaigns</p><!-- /.fact-two__text -->
          </div><!-- /.fact-two__single -->
        </div><!-- /.col-lg-3 col-md-6 -->
        <div class="col-lg-3 col-md-6">
          <div class="fact-two__single text-center wow fadeInLeft" data-wow-duration="1500ms" data-wow-delay="200ms">
            <h3 class="fact-two__count counter"><countTo :startVal='0' :endVal='startCounter ? 8400 : 0' :duration='3000'></countTo></h3><!-- /.fact-two__count -->
            <p class="fact-two__text">Issues Solved</p><!-- /.fact-two__text -->
          </div><!-- /.fact-two__single -->
        </div><!-- /.col-lg-3 col-md-6 -->
        <div class="col-lg-3 col-md-6">
          <div class="fact-two__single text-center wow fadeInLeft" data-wow-duration="1500ms" data-wow-delay="300ms">
            <h3 class="fact-two__count counter"><countTo :startVal='0' :endVal='startCounter ? 3240 : 0' :duration='3000'></countTo></h3><!-- /.fact-two__count -->
            <p class="fact-two__text">Party Workers</p><!-- /.fact-two__text -->
          </div><!-- /.fact-two__single -->
        </div><!-- /.col-lg-3 col-md-6 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
  import countTo from 'vue-count-to';
  import {ObserveVisibility} from 'vue-observe-visibility'

  export default {
    name: "FunFactTwo",
    components: {countTo},
    directives: {
      ObserveVisibility
    },
    data() {
      return {
        startCounter: false
      }
    },
    methods: {
      onVisibilityChange(isVisible) {
        if (isVisible) {
          this.startCounter = true;
        }
      },
    },
  }
</script>

<style scoped>

</style>
