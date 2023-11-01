<template>
  <section class="social-shares">
    <div class="container">
      <div class="row">
        <div class="col-lg-4">
          <div class="social-shares__facebook thm-base-bg text-center">
            <i class="fa fa-facebook-square"></i>
            <p class="social-shares__facebook-name">Facebook</p><!-- /.social-shares__facebook-name -->
            <h3 class="social-shares__facebook-count">280,366</h3><!-- /.social-shares__facebook-count -->
            <a href="#" class="social-shares__facebook-link">#potisenfacebook</a>
          </div><!-- /.social-shares__facebook -->
        </div><!-- /.col-lg-4 -->
        <div class="col-lg-8">
          <div class="social-shares__twitter thm-base-bg-2">
            <h3 class="social-shares__twitter-title">Latest Tweets</h3><!-- /.social-shares__twitter-title -->
            <div class="social-shares__twitter-carousel">
              <no-ssr> <!-- important to add no-ssr-->
                <carousel :items="1" :autoplay="true" :margin="30" :dots="true" :nav="false"
                          :responsive="{0: {items: 1},640: {items: 1},992: {items: 1},1024: {items: 1}}">
              <div class="item">
                <div class="social-shares__twitter-single">
                  <p class="social-shares__twitter-text">A Bill of Rights is what the people are entitled to against <a href="#"><strong>#politics</strong></a> every government, and what no just government should refuse, or rest on inference. <a href="#">https://t.co/LpyuHZaOMK</a> <a href="#">#ASMSG</a></p><!-- /.social-shares__twitter-text -->
                  <div class="social-shares__twitter-info">
                    <p class="social-shares__twitter-info-text">
                      <a href="#">@potisentwitterfollow</a>
                      <span>5 minutes ago</span>
                    </p><!-- /.social-shares__twitter-info-text -->
                    <i class="fa fa-twitter"></i>
                  </div><!-- /.social-shares__twitter-info -->
                </div><!-- /.social-shares__twitter-single -->
              </div><!-- /.item -->
              <div class="item">
                <div class="social-shares__twitter-single">
                  <p class="social-shares__twitter-text">A Bill of Rights is what the people are entitled to against <a href="#"><strong>#politics</strong></a> every government, and what no just government should refuse, or rest on inference. <a href="#">https://t.co/LpyuHZaOMK</a> <a href="#">#ASMSG</a></p><!-- /.social-shares__twitter-text -->
                  <div class="social-shares__twitter-info">
                    <p class="social-shares__twitter-info-text">
                      <a href="#">@potisentwitterfollow</a>
                      <span>5 minutes ago</span>
                    </p><!-- /.social-shares__twitter-info-text -->
                    <i class="fa fa-twitter"></i>
                  </div><!-- /.social-shares__twitter-info -->
                </div><!-- /.social-shares__twitter-single -->
              </div><!-- /.item -->
              <div class="item">
                <div class="social-shares__twitter-single">
                  <p class="social-shares__twitter-text">A Bill of Rights is what the people are entitled to against <a href="#"><strong>#politics</strong></a> every government, and what no just government should refuse, or rest on inference. <a href="#">https://t.co/LpyuHZaOMK</a> <a href="#">#ASMSG</a></p><!-- /.social-shares__twitter-text -->
                  <div class="social-shares__twitter-info">
                    <p class="social-shares__twitter-info-text">
                      <a href="#">@potisentwitterfollow</a>
                      <span>5 minutes ago</span>
                    </p><!-- /.social-shares__twitter-info-text -->
                    <i class="fa fa-twitter"></i>
                  </div><!-- /.social-shares__twitter-info -->
                </div><!-- /.social-shares__twitter-single -->
              </div><!-- /.item -->
                </carousel>
              </no-ssr>
            </div><!-- /.social-shares__twitter-carousel -->
          </div><!-- /.social-shares__twitter -->
        </div><!-- /.col-lg-8 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
    export default {
        name: "SocialShare"
    }
</script>

<style scoped>

</style>
