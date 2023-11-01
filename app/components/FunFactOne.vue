<template>
  <section class="fact-one" v-observe-visibility="onVisibilityChange">
    <div class="container text-center">
      <img src="/assets/images/resources/decor-star-1-1.png" class="fact-one__star-1" alt="">
      <h3 class="fact-one__title counter"><countTo :startVal='0' :endVal='startCounter ? 12327 : 0' :duration='5000'></countTo></h3>
      <p class="fact-one__text">Людей обратившийся к нам</p>
      <img src="/assets/images/resources/decor-star-1-1.png" class="fact-one__star-2" alt="">
    </div><!-- /.container -->
  </section>
</template>

<script>

  import countTo from 'vue-count-to';
  import { ObserveVisibility } from 'vue-observe-visibility'

  export default {
    name: "FunFactOne",
    components: { countTo },
    directives: {
      ObserveVisibility
    },
    data() {
      return{
        startCounter: false
      }
    },
    methods: {
      onVisibilityChange (isVisible) {
        if (isVisible){
          this.startCounter = true;
        }
      },
    },

  }
</script>

<style scoped>

</style>
