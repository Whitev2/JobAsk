<template>
  <div class="brand-one thm-gray-bg">
    <div class="container">
      <div class="brand-one__carousel">
        <no-ssr> <!-- important to add no-ssr-->
          <carousel :items="1" :autoplay="true" :margin="30" :dots="false" :nav="false"
                    :responsive="{0: {items: 1},640: {items: 2},992: {items: 3},1024: {items: 5}}">

            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->
            <div class="item">
              <img src="/assets/images/resources/brand-1-1.png" alt=""/>
            </div><!-- /.item -->

          </carousel>
        </no-ssr>

      </div><!-- /.brand-one__carousel owl-carousel owl-theme -->
    </div><!-- /.container -->
  </div>
</template>

<script>
  export default {
    name: "Brands",
  }
</script>

<style scoped>

</style>
