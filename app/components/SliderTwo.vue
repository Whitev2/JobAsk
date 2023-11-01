<template>
  <div class="banner-wrapper" id="home">
    <div class="banner-one__nav">
      <a href="#" class="banner-one__nav-left"><i class="fa fa-angle-left"></i><!-- /.fa fa-angle-left --></a>
      <a href="#" class="banner-one__nav-right"><i class="fa fa-angle-right"></i><!-- /.fa fa-angle-right --></a>
    </div><!-- /.banner-one__nav -->
    <section class="banner-one banner-carousel__one">
      <swiper :options="swiperOptions">

        <swiper-slide>
          <div class="item">
            <div class="banner-one__slide  banner-one__slide-1"
                 style="background-image: url(/assets/images/slider/slider-1-1.jpg);">
              <div class="container">
                <div class="row">
                  <div class="col-lg-12 text-center">
                    <h3 class="banner-one__title banner-one__light-color">Building A Future
                      <br/> For <span>America</span></h3>
                    <div class="banner-one__btn-block">
                      <a href="#" class="thm-btn banner-one__btn">Discover More</a>
                    </div><!-- /.btn-block -->
                  </div><!-- /.col-lg-12 -->
                </div><!-- /.row -->
              </div><!-- /.container -->
            </div><!-- /.banner-one__slide -->
          </div><!-- /.item -->
        </swiper-slide>
        <swiper-slide>
          <div class="item">
            <div class="banner-one__slide  banner-one__slide-2"
                 style="background-image: url(/assets/images/slider/slider-1-2.jpg);">
              <div class="container">
                <div class="row">
                  <div class="col-lg-12 text-center">
                    <h3 class="banner-one__title banner-one__light-color">Building A Future
                      <br/> For <span>America</span></h3>
                    <div class="banner-one__btn-block">
                      <a href="#" class="thm-btn banner-one__btn">Discover More</a>
                    </div><!-- /.btn-block -->
                  </div><!-- /.col-lg-12 -->
                </div><!-- /.row -->
              </div><!-- /.container -->
            </div><!-- /.banner-one__slide -->
          </div><!-- /.item -->
        </swiper-slide>
        <swiper-slide>
          <div class="item">
            <div class="banner-one__slide  banner-one__slide-3"
                 style="background-image: url(/assets/images/slider/slider-1-3.jpg);">
              <div class="container">
                <div class="row">
                  <div class="col-lg-12 text-center">
                    <h3 class="banner-one__title banner-one__light-color">Building A Future
                      <br/> For <span>America</span></h3>
                    <div class="banner-one__btn-block">
                      <a href="#" class="thm-btn banner-one__btn">Discover More</a>
                    </div><!-- /.btn-block -->
                  </div><!-- /.col-lg-12 -->
                </div><!-- /.row -->
              </div><!-- /.container -->
            </div><!-- /.banner-one__slide -->
          </div><!-- /.item -->
        </swiper-slide>
        </swiper>
    </section><!-- /.banner-one -->
  </div>
</template>

<script>
  import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper';
  import 'swiper/css/swiper.css';

  export default {
    name: "SliderTwo",
    components: {
      Swiper,
      SwiperSlide
    },
    directives: {
      swiper: directive
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
          navigation: {
            nextEl: '.banner-one__nav-right',
            prevEl: '.banner-one__nav-left',
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
