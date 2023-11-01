<template>
  <div>
    <div class="topbar-two">
      <div class="container">
        <div class="topbar-two__left">
          <a href="mailto:needhelp@potisen.com">needhelp@potisen.com</a>
          <a href="tel:666-888-0000">666 888 0000</a>
        </div><!-- /.topbar-two__left -->
        <div class="topbar-two__logo">
          <nuxt-link to="/index-2">
            <img src="/assets/images/logo-full-light.png" width="177" alt="Awesome Image"/>
          </nuxt-link>
        </div><!-- /.topbar-two__logo -->
        <div class="topbar-two__social">
          <a href="#" class="fa fa-twitter"></a>
          <a href="#" class="fa fa-facebook-square"></a>
          <a href="#" class="fa fa-pinterest-p"></a>
          <a href="#" class="fa fa-instagram"></a>
        </div><!-- /.topbar-two__social -->
      </div><!-- /.container -->
    </div><!-- /.topbar-two -->
    <header class="site-header site-header__header-one site-header__header-two ">
      <nav :class="`navbar navbar-expand-lg navbar-light header-navigation stricky ${sticky ? 'stricked-menu stricky-fixed' : ''}`">
        <div class="container clearfix">
          <!-- Brand and toggle get grouped for better mobile display -->
          <div class="logo-box clearfix">
            <button @click="mobileToggle = !mobileToggle" class="menu-toggler" data-target=".main-navigation">
              <span class="fa fa-bars"></span>
            </button>
          </div><!-- /.logo-box -->
          <!-- Collect the nav links, forms, and other content for toggling -->
          <div :class="`main-navigation ${mobileToggle ? 'showen' : ''}`" :style="`display: ${mobileToggle ? 'block' : 'none'}`">
            <ul class=" navigation-box">
              <li class="current">
                <nuxt-link to="/">Home</nuxt-link>
                <ul class="sub-menu">
                  <li>
                    <nuxt-link to="/">Home 01</nuxt-link>
                  </li>
                  <li>
                    <nuxt-link to="/index-2">Home 02</nuxt-link>
                  </li>
                  <li>
                    <nuxt-link to="#">Header Versions</nuxt-link>
                    <ul class="sub-menu">
                      <li>
                        <nuxt-link to="/">Header 01</nuxt-link>
                      </li>
                      <li>
                        <nuxt-link to="/index-2">Header 02</nuxt-link>
                      </li>
                    </ul><!-- /.sub-menu -->
                  </li>
                </ul><!-- /.sub-menu -->
              </li>
              <li>
                <nuxt-link to="/about">About</nuxt-link>
                <ul class="sub-menu">
                  <li>
                    <nuxt-link to="/about">About Us</nuxt-link>
                  </li>
                  <li>
                    <nuxt-link to="/history">History</nuxt-link>
                  </li>
                </ul><!-- /.sub-menu -->
              </li>
              <li>
                <nuxt-link to="/donation">Contribute</nuxt-link>
                <ul class="sub-menu">
                  <li>
                    <nuxt-link to="/donation">Donations</nuxt-link>
                  </li>
                  <li>
                    <nuxt-link to="/volunteer">Volunteer</nuxt-link>
                  </li>
                </ul><!-- /.sub-menu -->
              </li>
              <li>
                <a href="#">Pages</a>
                <ul class="sub-menu">
                  <li>
                    <nuxt-link to="/event">Events</nuxt-link>
                  </li>
                  <li>
                    <nuxt-link to="/event-details">Event Details</nuxt-link>
                  </li>
                </ul><!-- /.sub-menu -->
              </li>

              <li>
                <a href="#news">News</a>
                <ul class="sub-menu">
                  <li>
                    <nuxt-link to="/news">News Page</nuxt-link>
                  </li>
                  <li>
                    <nuxt-link to="/news-details">News Details</nuxt-link>
                  </li>
                </ul><!-- /.sub-menu -->
              </li>
              <li>
                <nuxt-link to="/contact">Contact</nuxt-link>
              </li>
            </ul>
          </div><!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
      </nav>
    </header>
  </div>
</template>

<script>
  export default {
    name: "NavTwo",
    data() {
      return {
        sticky: false,
        mobileToggle: false
      }
    },
    mounted() {
      window.addEventListener('scroll', this.handleScroll);
    },
    methods: {

      handleScroll() {
        if (window.scrollY > 70) {
          this.sticky = true
        } else if (window.scrollY < 70) {
          this.sticky = false
        }
      },
    }
  }
</script>

<style scoped>

</style>
