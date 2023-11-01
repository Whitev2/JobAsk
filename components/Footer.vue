<template>
  <div>
    <footer class="site-footer">
      <div class="site-footer__logo text-center">
        <nuxt-link to="/"><img src="/assets/images/logo-light.png" alt="" width="174"></nuxt-link>
      </div><!-- /.site-footer__logo -->
      <div class="site-footer__upper">
        <div class="container">
          <div class="row">
            <div class="col-xl-4 col-lg-6 col-md-6 col-sm-12">
              <div class="footer-widget">
                <h3 class="footer-widget__title">About</h3><!-- /.footer-widget__title -->
                <p class="footer-widget__text">Lorem ipsum is simply dolor sit ametcn <br> sectetur adipiscing
                  elit.
                  Phasellus vehic <br> sagittis euismod.</p><!-- /.footer-widget__text -->
                <div class="footer-widget__social">
                  <a href="#" class="fa fa-twitter"></a><!-- /.fa fa-twitter -->
                  <a href="#" class="fa fa-facebook-square"></a><!-- /.fa fa-facebook-square -->
                  <a href="#" class="fa fa-pinterest-p"></a><!-- /.fa fa-pinterest-p -->
                  <a href="#" class="fa fa-instagram"></a><!-- /.fa fa-instagram -->
                </div><!-- /.footer-widget__social -->
              </div><!-- /.footer-widget -->
            </div><!-- /.col-lg-3 -->
            <div class="col-xl-2 col-lg-6 col-md-6 col-sm-12">
              <div class="footer-widget footer-widget__links">
                <h3 class="footer-widget__title">Explore</h3><!-- /.footer-widget__title -->
                <ul class="list-unstyled footer-widget__links-list">
                  <li><a href="#">About Potisen</a></li>
                  <li><a href="#">Volunteering</a></li>
                  <li><a href="#">Contribute</a></li>
                  <li><a href="#">Join Our Community</a></li>
                  <li><a href="#">Latest News</a></li>
                </ul><!-- /.list-unstyled footer-widget__links-list -->
              </div><!-- /.footer-widget -->
            </div><!-- /.col-lg-3 -->
            <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12">
              <div class="footer-widget footer-widget__posts">
                <h3 class="footer-widget__title">Updates</h3><!-- /.footer-widget__title -->
                <ul class="list-unstyled footer-widget__posts-list">
                  <li>
                    <div class="footer-widget__posts-image">
                      <img src="/assets/images/resources/footer-post-1-1.png" alt="">
                    </div><!-- /.footer-widget__posts-image -->
                    <div class="footer-widget__posts-content">
                      <h4 class="footer-widget__posts-title">
                        <nuxt-link to="/news-details">International
                          conference
                        </nuxt-link>
                      </h4><!-- /.footer-widget__posts-title -->
                      <p class="footer-widget__posts-date">20 Oct, 2021</p>
                      <!-- /.footer-widget__posts-date -->
                    </div><!-- /.footer-widget__posts-content -->
                  </li>
                  <li>
                    <div class="footer-widget__posts-image">
                      <img src="/assets/images/resources/footer-post-1-2.png" alt="">
                    </div><!-- /.footer-widget__posts-image -->
                    <div class="footer-widget__posts-content">
                      <h4 class="footer-widget__posts-title">
                        <nuxt-link to="/news-details">The strength of
                          democracy
                        </nuxt-link>
                      </h4><!-- /.footer-widget__posts-title -->
                      <p class="footer-widget__posts-date">20 Oct, 2019</p>
                      <!-- /.footer-widget__posts-date -->
                    </div><!-- /.footer-widget__posts-content -->
                  </li>
                </ul><!-- /.list-unstyled footer-widget__posts-list -->
              </div><!-- /.footer-widget -->
            </div><!-- /.col-lg-3 -->
            <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12">
              <div class="footer-widget footer-widget__contact">
                <h3 class="footer-widget__title">Contact</h3><!-- /.footer-widget__title -->
                <ul class="list-unstyled footer-widget__contact-list">
                  <li>
                    <i class="potisen-icon-phone"></i><!-- /. -->
                    <a href="tel:666-888-000">666 888 000</a>
                  </li>
                  <li>
                    <i class="potisen-icon-mail"></i><!-- /. -->
                    <a href="mailto:needhelp@example.com">needhelp@example.com</a>
                  </li>
                  <li>
                    <i class="potisen-icon-pin"></i><!-- /. -->
                    22 Broklyn Street 30 Road. New <br> York United States
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
            <p class="site-footer__copy">&copy; copyright 2021 by <a href="#">Layerdrops.com</a></p>
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
