<template>
  <section class="video-one">
    <div class="container">
      <div class="block-title text-center">
        <img src="/assets/images/resources/sec-title-star.png" alt="Awesome Image" class="wow rotateIn"
             data-wow-duration="1500ms">
        <p class="block-title__tag-line">Watch us Live</p>
        <h2 class="block-title__title">Campaign Videos</h2><!-- /.block-title__title -->
      </div><!-- /.block-title -->
      <div class="video-one__carousel wow fadeInUp" data-wow-duration="1500ms">
        <no-ssr> <!-- important to add no-ssr-->
          <carousel :items="1" :autoplay="true" :margin="30" :dots="false" :nav="true"
                    :responsive="{0: {items: 1},640: {items: 1},992: {items: 1},1024: {items: 1}}">
        <div class="item">
          <div class="video-one__box">
            <img src="/assets/images/resources/video-1-1.jpg" alt="Awesome Image"/>
            <a href="https://www.youtube.com/watch?v=Get7rqXYrbQ" class="video-one__btn"><i class="fa fa-play"></i></a>
          </div><!-- /.video-one__box -->
        </div><!-- /.item -->
        <div class="item">
          <div class="video-one__box">
            <img src="/assets/images/resources/video-1-1.jpg" alt="Awesome Image"/>
            <a href="https://www.youtube.com/watch?v=Get7rqXYrbQ" class="video-one__btn"><i class="fa fa-play"></i></a>
          </div><!-- /.video-one__box -->
        </div><!-- /.item -->
        <div class="item">
          <div class="video-one__box">
            <img src="/assets/images/resources/video-1-1.jpg" alt="Awesome Image"/>
            <a href="https://www.youtube.com/watch?v=Get7rqXYrbQ" class="video-one__btn"><i class="fa fa-play"></i></a>
          </div><!-- /.video-one__box -->
        </div><!-- /.item -->
          </carousel>
        </no-ssr>
      </div><!-- /.video-one__carousel owl-carousel owl-theme -->
    </div><!-- /.container -->
  </section>
</template>

<script>
  import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper';
  import 'swiper/css/swiper.css';

  export default {
    name: "VideoTwo",
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

    mounted() {
      new GLightbox({
        selector: '.glightbox2',
        touchNavigation: true,
        loop: true,
        autoplayVideos: true
      });

    },
  }
</script>

<style scoped>

</style>
