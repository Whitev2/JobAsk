<template>
  <section class="testimonials-two">
    <div class="testimonials-two__carousel">
        <swiper :options="swiperOptions">

          <swiper-slide>
            <div class="testimonials-two__single"
                 style="background-image: url(/assets/images/testimonials/testimonials-1-bg.jpg);">
              <div class="container">
                <div class="row align-items-center">
                  <div class="col-lg-7">
                    <i class="potisen-icon-quote testimonials-two__icon"></i>
                    <h3 class="testimonials-two__text">This is due to their excellent service, competitive pricing and
                      customer support. It’s throughly refresing to get such a personal touch.</h3>
                    <p class="testimonials-two__name">Gary Hilk</p><!-- /.testimonials-two__name -->
                  </div><!-- /.col-lg-7 -->
                  <div class="col-lg-5 d-flex justify-content-xl-end justify-content-sm-start">
                    <div class="testimonials-two__btn-wrap">
                      <a href="https://www.youtube.com/watch?v=Get7rqXYrbQ" class="testimonials-two__btn glightbox2">
                        <i class="fa fa-play"></i>
                      </a>
                      <span class="testimonials-two__btn-tag-line">Watch Campaigns <img
                        src="/assets/images/resources/video-arrow.png" alt="Awesome Image"/></span>
                    </div><!-- /.testimonials-two__btn-wrap -->
                  </div><!-- /.col-lg-5 -->
                </div><!-- /.row -->
              </div><!-- /.container -->
            </div><!-- /.testimonials-two__single -->
          </swiper-slide>
          <swiper-slide>
            <div class="testimonials-two__single"
                 style="background-image: url(/assets/images/testimonials/testimonials-2-bg.jpg);">
              <div class="container">
                <div class="row align-items-center">
                  <div class="col-lg-7">
                    <i class="potisen-icon-quote testimonials-two__icon"></i>
                    <h3 class="testimonials-two__text">This is due to their excellent service, competitive pricing and
                      customer support. It’s throughly refresing to get such a personal touch.</h3>
                    <p class="testimonials-two__name">Naida Bowline</p><!-- /.testimonials-two__name -->
                  </div><!-- /.col-lg-7 -->
                  <div class="col-lg-5 d-flex justify-content-xl-end justify-content-sm-start">
                    <div class="testimonials-two__btn-wrap">
                      <a href="https://www.youtube.com/watch?v=Get7rqXYrbQ" class="testimonials-two__btn glightbox2">
                        <i class="fa fa-play"></i>
                      </a>
                      <span class="testimonials-two__btn-tag-line">Watch Campaigns <img
                        src="/assets/images/resources/video-arrow.png" alt="Awesome Image"/></span>
                    </div><!-- /.testimonials-two__btn-wrap -->
                  </div><!-- /.col-lg-5 -->
                </div><!-- /.row -->
              </div><!-- /.container -->
            </div><!-- /.testimonials-two__single -->
          </swiper-slide>
          <swiper-slide>
            <div class="testimonials-two__single"
                 style="background-image: url(/assets/images/testimonials/testimonials-3-bg.jpg);">
              <div class="container">
                <div class="row align-items-center">
                  <div class="col-lg-7">
                    <i class="potisen-icon-quote testimonials-two__icon"></i>
                    <h3 class="testimonials-two__text">This is due to their excellent service, competitive pricing and
                      customer support. It’s throughly refresing to get such a personal touch.</h3>
                    <p class="testimonials-two__name">Caroline Ocheltree</p><!-- /.testimonials-two__name -->
                  </div><!-- /.col-lg-7 -->
                  <div class="col-lg-5 d-flex justify-content-xl-end justify-content-sm-start">
                    <div class="testimonials-two__btn-wrap">
                      <a href="https://www.youtube.com/watch?v=Get7rqXYrbQ" class="testimonials-two__btn glightbox2">
                        <i class="fa fa-play"></i>
                      </a>
                      <span class="testimonials-two__btn-tag-line">Watch Campaigns <img
                        src="/assets/images/resources/video-arrow.png" alt="Awesome Image"/></span>
                    </div><!-- /.testimonials-two__btn-wrap -->
                  </div><!-- /.col-lg-5 -->
                </div><!-- /.row -->
              </div><!-- /.container -->
            </div><!-- /.testimonials-two__single -->
          </swiper-slide>
          <swiper-slide>
            <div class="testimonials-two__single"
                 style="background-image: url(/assets/images/testimonials/testimonials-4-bg.jpg);">
              <div class="container">
                <div class="row align-items-center">
                  <div class="col-lg-7">
                    <i class="potisen-icon-quote testimonials-two__icon"></i>
                    <h3 class="testimonials-two__text">This is due to their excellent service, competitive pricing and
                      customer support. It’s throughly refresing to get such a personal touch.</h3>
                    <p class="testimonials-two__name">Corey Gessner</p><!-- /.testimonials-two__name -->
                  </div><!-- /.col-lg-7 -->
                  <div class="col-lg-5 d-flex justify-content-xl-end justify-content-sm-start">
                    <div class="testimonials-two__btn-wrap">
                      <a href="https://www.youtube.com/watch?v=Get7rqXYrbQ" class="testimonials-two__btn glightbox2">
                        <i class="fa fa-play"></i>
                      </a>
                      <span class="testimonials-two__btn-tag-line">Watch Campaigns <img
                        src="/assets/images/resources/video-arrow.png" alt="Awesome Image"/></span>
                    </div><!-- /.testimonials-two__btn-wrap -->
                  </div><!-- /.col-lg-5 -->
                </div><!-- /.row -->
              </div><!-- /.container -->
            </div><!-- /.testimonials-two__single -->
          </swiper-slide>
          <div class="swiper-pagination" slot="pagination"></div>

        </swiper>
    </div><!-- /.testimonials-two__carousel -->

  </section>
</template>

<script>
  import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper';
  import 'swiper/css/swiper.css';

  export default {
    name: "TestimonialTwo",
    components: {
      Swiper,
      SwiperSlide
    },
    directives: {
      swiper: directive
    },
    mounted() {
      new GLightbox({
        selector: '.glightbox2',
        touchNavigation: true,
        loop: true,
        autoplayVideos: true
      });

    },
    data() {
      return {
        swiperOptions: {
          slidesPerView: 1,
          loop: true,
          speed: 1000,
          spaceBetween: 30,
          autoplay: {
            delay: 3000,
            disableOnInteraction: false
          },
          pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true
          },

          // Responsive breakpoints
          breakpoints: {
            1024: {
              slidesPerView: 1
            },
            768: {
              slidesPerView: 1
            },
            640: {
              slidesPerView: 1
            },
            320: {
              slidesPerView: 1
            }
          }
        }
      }
    },
  }
</script>

<style scoped>

</style>
