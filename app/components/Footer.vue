<template>
  <div>
    <footer class="site-footer">

      <div class="site-footer__upper">
        <div class="container">
          <div class="row">
            <div class="col-xl-4 col-lg-6 col-md-6 col-sm-12">
              <div class="footer-widget">
                <h3 class="footer-widget__title">О нас</h3><!-- /.footer-widget__title -->
                <p class="footer-widget__text">Занимаемся оформлением виз в Европу <br> помогаем найти работу и сделать ВНЖ</p><!-- /.footer-widget__text -->
<!--                <div class="footer-widget__social">-->
<!--                  <a href="#" class="fa fa-twitter"></a>&lt;!&ndash; /.fa fa-twitter &ndash;&gt;-->
<!--                  <a href="#" class="fa fa-facebook-square"></a>&lt;!&ndash; /.fa fa-facebook-square &ndash;&gt;-->
<!--                  <a href="#" class="fa fa-pinterest-p"></a>&lt;!&ndash; /.fa fa-pinterest-p &ndash;&gt;-->
<!--                  <a href="#" class="fa fa-instagram"></a>&lt;!&ndash; /.fa fa-instagram &ndash;&gt;-->
<!--                </div>&lt;!&ndash; /.footer-widget__social &ndash;&gt;-->
              </div><!-- /.footer-widget -->
            </div><!-- /.col-lg-3 -->
            <div class="col-xl-2 col-lg-6 col-md-6 col-sm-12">
              <div class="footer-widget footer-widget__links">
                <h3 class="footer-widget__title">Поиск</h3><!-- /.footer-widget__title -->
                <ul class="list-unstyled footer-widget__links-list">
                  <li><a href="/">Главная</a></li>
                  <li><a href="/resident">ВНЖ</a></li>
                  <li><a href="/work">Работа</a></li>
                  <li><a href="/contact">Контакты</a></li>
                </ul><!-- /.list-unstyled footer-widget__links-list -->
              </div><!-- /.footer-widget -->
            </div><!-- /.col-lg-3 -->

            <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12">
              <div class="footer-widget footer-widget__contact">
                <h3 class="footer-widget__title">Контакты</h3><!-- /.footer-widget__title -->
                <ul class="list-unstyled footer-widget__contact-list">
                  <li>
                    <i class="potisen-icon-phone"></i><!-- /. -->
                    <a href="tel:+79999971903">Whats App</a>
                  </li>
                  <li>
                    <i class="potisen-icon-mail"></i><!-- /. -->
                    <a href="mailto:pro_visa_agency@gmail.com">Email</a>
                  </li>
                  <li>
                    <i class="potisen-icon-pin"></i><!-- /. -->
                    <a href="https://t.me/job_ask">Telegram</a>
                  </li>
                </ul><!-- /.list-unstyled footer-widget__post-list -->
              </div><!-- /.footer-widget -->
            </div><!-- /.col-lg-3 -->
          </div><!-- /.row -->
        </div><!-- /.container -->
      </div><!-- /.site-footer__upper -->
      <div class="site-footer__bottom">
        <div class="container">
          <div class="inner-container text-center">
            <p class="site-footer__copy">&copy; copyright 2023 by <a href="#">jobask.ru</a></p>
            <!-- /.site-footer__copy -->
          </div><!-- /.inner-container -->
        </div><!-- /.container -->
      </div><!-- /.site-footer__bottom -->
    </footer>

    <a href="#" @click="scrollTop" data-target="html" class="scroll-to-target scroll-to-top"
       :style="`display: ${scrollBtn ? 'inline' : 'none'}`"><i class="fa fa-angle-up"></i></a>
  </div>
</template>

<script>
  export default {
    name: "Footer",
    data() {
      return {
        scrollBtn: false
      }
    },
    mounted() {
      window.addEventListener('scroll', this.handleScroll);
    },

    methods: {
      handleScroll() {
        if (window.scrollY > 70) {
          this.scrollBtn = true
        } else if (window.scrollY < 70) {
          this.scrollBtn = false
        }
      },

      scrollTop() {
        window.scrollTo(0, 0);
      }

    }
  }
</script>

<style scoped>

</style>
