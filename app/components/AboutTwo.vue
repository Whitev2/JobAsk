<template>
  <section class="about-two">
    <div class="container">
      <div class="block-title text-center">
        <img src="/assets/images/resources/sec-title-star.png" alt="Awesome Image" class="wow rotateIn"
             data-wow-duration="1500ms">
        <p class="block-title__tag-line">Join Campaigns</p>
        <h2 class="block-title__title">We Will Make <br> History Together</h2><!-- /.block-title__title -->
      </div><!-- /.block-title -->
      <div class="row">
        <div class="col-lg-6">
          <div class="about-two__content">
            <div class="row">
              <div class="col-sm-4">
                <img src="/assets/images/resources/history-1-1.jpg" alt="" class="img-fluid"/>
              </div><!-- /.col-sm-4 -->
              <div class="col-sm-4">
                <img src="/assets/images/resources/history-1-2.jpg" alt="" class="img-fluid"/>
              </div><!-- /.col-sm-4 -->
              <div class="col-sm-4">
                <img src="/assets/images/resources/history-1-3.jpg" alt="" class="img-fluid"/>
              </div><!-- /.col-sm-4 -->
            </div><!-- /.row -->
            <p class="about-two__text">Lorem Ipsum is simply dummy text of the printing and type setting industry has
              been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
              type and scrambled to make a type specimen book. It has survived not only five centuries but also the leap
              into electronic type setting.</p><!-- /.about-two__text -->
          </div><!-- /.about-two__content -->
        </div><!-- /.col-lg-6 -->
        <div class="col-lg-6">
          <div class="accrodion-grp" data-grp-name="faq-accrodion">


            <div class="accordion-container-one">
              <div class="ac">
                <h2 class="ac-q accordion__title-text" tabIndex="0">Political organization that typically seeks</h2>
                <div class="ac-a accordion__content">
                  <p class="accordion__content-desc">It has survived not only five centuries but also the leap into
                    electronic type setting. when an
                    unknown printer took a galley of type and scrambled to make a type specimen book.
                  </p>
                </div>
              </div>

              <div class="ac accordion__content">
                <h2 class="ac-q accordion__title-text" tabIndex="0">Strong politics plan require experience</h2>
                <div class="ac-a">
                  <p class="accordion__content-desc">It has survived not only five centuries but also the leap into
                    electronic type setting. when an
                    unknown printer took a galley of type and scrambled to make a type specimen book.
                  </p>
                </div>
              </div>

              <div class="ac">
                <h2 class="ac-q accordion__title-text" tabIndex="0">Attract and retain quality high paying customers</h2>
                <div class="ac-a accordion__content">
                  <p class="accordion__content-desc">It has survived not only five centuries but also the leap into
                    electronic type setting. when an
                    unknown printer took a galley of type and scrambled to make a type specimen book.
                  </p>
                </div>
              </div>

            </div>

          </div>
        </div><!-- /.col-lg-6 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
  export default {
    name: "AboutTwo",
    mounted() {
      new Accordion('.accordion-container-one');
    }
  }
</script>

<style scoped>
  .ac {
    margin-top: 10px;
    padding: 10px;
    background: #eef1f6;
    box-sizing: border-box;
  }

  .ac > .ac-q {
    font: bold 15px Oswald, sans-serif;
    padding: 10px 30px 10px 10px;
    text-decoration: none;
    display: block;
    cursor: pointer;
    position: relative;
    margin: 0;
    color: #192437;
    font-size: 16px;
    font-weight: 400;
    text-transform: uppercase;
  }

  .ac.is-active .ac-q {
    color: #d41e44 !important;
  }

  .ac > .ac-q::after {
    content: '+';
    text-align: center;
    width: 15px;
    right: 10px;
    top: 50%;
    -webkit-transform: translate(0, -50%);
    transform: translate(0, -50%);
    position: absolute
  }

  .ac > .ac-a {
    overflow: hidden;
    -webkit-transition-property: all;
    transition-property: all;
    -webkit-transition-timing-function: ease;
    transition-timing-function: ease
  }

  .ac > .ac-a p {
    margin: 0;
    padding: 10px;
    color: #545764;
    font-size: 16px;
    line-height: 30px;
    font-weight: 300;
  }

  .ac.js-enabled > .ac-a {
    visibility: hidden
  }

  .ac.is-active > .ac-a {
    visibility: visible
  }

  .ac.is-active > .ac-q::after {
    content: '\2013';
    color: #d41e44;
  }
</style>

