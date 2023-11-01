<template>
  <div>
    <div class="contact-info-one">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4562.753041141002!2d-118.80123790098536!3d34.152323469614075!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80e82469c2162619%3A0xba03efb7998eef6d!2sCostco+Wholesale!5e0!3m2!1sbn!2sbd!4v1562518641290!5m2!1sbn!2sbd"
        class="google-map__contact" allowfullscreen></iframe>
      <div class="container">
        <div class="inner-container wow fadeInUp" data-wow-duration="1500ms">
          <div class="row">
            <div class="col-xl-4">
              <div class="contact-info-one__single">
                <h4 class="contact-info-one__title">
                  <i class="potisen-icon-pin"></i>
                  22 Broklyn Street, USA
                </h4>
              </div><!-- /.contact-info-one__single -->
            </div><!-- /.col-xl-4 -->
            <div class="col-xl-4">
              <div class="contact-info-one__single">
                <h4 class="contact-info-one__title">
                  <i class="potisen-icon-phone"></i>
                  <a href="tel:666-888-000">666 888 000</a>
                </h4>
              </div><!-- /.contact-info-one__single -->
            </div><!-- /.col-xl-4 -->
            <div class="col-xl-4">
              <div class="contact-info-one__single">
                <h4 class="contact-info-one__title">
                  <i class="potisen-icon-mail"></i>
                  <a href="mailto:needhelp@potisen.com">needhelp@potisen.com</a>
                </h4>
              </div><!-- /.contact-info-one__single -->
            </div><!-- /.col-xl-4 -->
          </div><!-- /.row -->
        </div><!-- /.inner-container -->
      </div><!-- /.container -->
    </div><!-- /.contact-info-one -->
    <section class="contact-form-one">
      <div class="container">
        <div class="block-title text-center">
          <img src="/assets/images/resources/sec-title-star.png" alt="Awesome Image" class="wow rotateIn"
               data-wow-duration="1500ms">
          <p class="block-title__tag-line">Contact With Us</p>
          <h2 class="block-title__title">Leave a Message</h2><!-- /.block-title__title -->
        </div><!-- /.block-title -->
        <form class="contact-form-one__form contact-form-validated">
          <div class="row low-gutters">
            <div class="col-lg-6">
              <input type="text" name="name" placeholder="Your Name">
            </div><!-- /.col-lg-6 -->
            <div class="col-lg-6">
              <input type="text" name="email" placeholder="Email Address">
            </div><!-- /.col-lg-6 -->
            <div class="col-lg-12">
              <textarea name="message" placeholder="Write Message"></textarea>
              <div class="text-center">
                <button type="submit" class="thm-btn contact-form-one__btn">Send Message</button>
              </div><!-- /.text-center -->
            </div><!-- /.col-lg-12 -->
          </div><!-- /.row -->
        </form><!-- /.contact-form-one__form -->
        <div class="result"></div><!-- /.result -->
      </div><!-- /.container -->
    </section>

  </div>
</template>

<script>
  export default {
    name: "Contact",
  }
</script>

<style scoped>

</style>
