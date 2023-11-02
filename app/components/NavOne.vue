<template>
  <div>

    <header class="site-header site-header__header-one ">
      <nav :class="`navbar navbar-expand-lg navbar-light header-navigation stricky ${sticky ? 'stricked-menu stricky-fixed' : ''}`">
        <div class="container clearfix">
          <!-- Brand and toggle get grouped for better mobile display -->
          <div class="logo-box clearfix">
            <nuxt-link class="navbar-brand" to="/">
              <img src="/assets/images/logo-dark-ja.PNG" class="main-logo" width="80" alt="Awesome Image"/>
            </nuxt-link>
            <button @click="mobileToggle = !mobileToggle" class="menu-toggler" data-target=".main-navigation">
              <span class="fa fa-bars"></span>
            </button>
          </div><!-- /.logo-box -->
          <!-- Collect the nav links, forms, and other content for toggling -->
          <div :class="`main-navigation ${mobileToggle ? 'showen' : ''}`" :style="`display: ${mobileToggle ? 'block' : 'none'}`">
            <ul class=" navigation-box">
              <li class="current">
                <nuxt-link to="/">Главная</nuxt-link>

              </li>
              <li>
                <nuxt-link to="/resident">ВНЖ</nuxt-link>
                <ul class="sub-menu">
                  <li>
                    <nuxt-link to="/resident#slovakii">Словакия</nuxt-link>
                  </li>
                  <li>
                    <nuxt-link to="/resident#ch">Чехия</nuxt-link>
                  </li>
                </ul><!-- /.sub-menu -->
              </li>
              <li>
                <nuxt-link to="/work">Работа</nuxt-link>
<!--                <ul class="sub-menu">-->
<!--                  <li>-->
<!--                    <nuxt-link to="/work">Вакансии</nuxt-link>-->
<!--                  </li>-->
<!--                  <li>-->
<!--                    <nuxt-link to="/work">Условия</nuxt-link>-->
<!--                  </li>-->
<!--                </ul>&lt;!&ndash; /.sub-menu &ndash;&gt;-->
              </li>

<!--              <li>-->
<!--                <nuxt-link to="/about">О нас</nuxt-link>-->
<!--              </li>-->

              <li>
                <nuxt-link to="/contact">Контакты</nuxt-link>
              </li>
            </ul>
          </div><!-- /.navbar-collapse -->
          <div class="right-side-box">
            <div class="header-social">
              <a href="#" class="fa fa-send"></a>
              <a href="#" class="fa fa-mail-forward"></a>
<!--              <a href="#" class="fa fa-pinterest-p"></a>-->
<!--              <a href="#" class="fa fa-instagram"></a>-->
            </div><!-- /.header-social -->
          </div><!-- /.right-side-box -->
        </div>
        <!-- /.container -->
      </nav>
    </header>
  </div>
</template>

<script>
  export default {
    name: "NavOne",
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

<style>
  .header-navigation .navigation-box > li > .sub-menu, .header-navigation .navigation-box > li > .sub-menu > li > .sub-menu {
    display: block;
  }
</style>
