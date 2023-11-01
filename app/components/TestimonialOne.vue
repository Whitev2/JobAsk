<template>
  <section class="testimonials-one">
    <div class="container">
      <div class="testimonials-one__carousel">
        <no-ssr> <!-- important to add no-ssr-->
          <carousel :items="1" :autoplay="true" :margin="30" :dots="true" :nav="false"
                    :responsive="{0: {items: 1},640: {items: 1},992: {items: 1},1024: {items: 1}}">
            <div class="item">
              <div class="testimonials-one__single">
                <p class="testimonials-one__text">A Bill of Rights is what the people are entitled to against <strong><a
                  href="#">#politics</a></strong> every government, and what no just government should refuse, or rest
                  on inference. <a href="#">https://t.co/LpyuHZaOMK</a> <a href="#"> #ASMSG</a></p>
                <!-- /.testimonials-one__text -->
                <p class="testimonials-one__info">
                  <strong><a href="#">@potisentwitterfollow</a></strong> <span>10 minutes ago</span>
                </p><!-- /.testimonials-one__info -->
              </div><!-- /.testimonials-one__single -->
            </div><!-- /.item -->
            <div class="item">
              <div class="testimonials-one__single">
                <p class="testimonials-one__text">A Bill of Rights is what the people are entitled to against <strong><a
                  href="#">#politics</a></strong> every government, and what no just government should refuse, or rest
                  on inference. <a href="#">https://t.co/LpyuHZaOMK</a> <a href="#"> #ASMSG</a></p>
                <!-- /.testimonials-one__text -->
                <p class="testimonials-one__info">
                  <strong><a href="#">@potisentwitterfollow</a></strong> <span>10 minutes ago</span>
                </p><!-- /.testimonials-one__info -->
              </div><!-- /.testimonials-one__single -->
            </div><!-- /.item -->
            <div class="item">
              <div class="testimonials-one__single">
                <p class="testimonials-one__text">A Bill of Rights is what the people are entitled to against <strong><a
                  href="#">#politics</a></strong> every government, and what no just government should refuse, or rest
                  on inference. <a href="#">https://t.co/LpyuHZaOMK</a> <a href="#"> #ASMSG</a></p>
                <!-- /.testimonials-one__text -->
                <p class="testimonials-one__info">
                  <strong><a href="#">@potisentwitterfollow</a></strong> <span>10 minutes ago</span>
                </p><!-- /.testimonials-one__info -->
              </div><!-- /.testimonials-one__single -->
            </div><!-- /.item -->
          </carousel>
        </no-ssr>
      </div><!-- /.testimonials-one__carousel -->
    </div><!-- /.container -->
  </section>
</template>

<script>
  export default {
    name: "TestimonialOne"
  }
</script>

<style scoped>

</style>
