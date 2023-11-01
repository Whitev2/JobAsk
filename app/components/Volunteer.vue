<template>
    <div>
      <section class="volunteer-gallery">
        <div class="container">
          <div class="row">
            <div class="col-lg-6">
              <img src="/assets/images/resources/volun-1-1.jpg" alt="" class="img-fluid wow fadeInUp animated" data-wow-duration="1500ms" style="visibility: visible; animation-duration: 1500ms; animation-name: fadeInUp;">
            </div><!-- /.col-lg-6 -->
            <div class="col-lg-6">
              <img src="/assets/images/resources/volun-1-2.jpg" alt="" class="img-fluid wow fadeInUp animated" data-wow-duration="1500ms" style="visibility: visible; animation-duration: 1500ms; animation-name: fadeInUp;">
            </div><!-- /.col-lg-6 -->
          </div><!-- /.row -->
        </div><!-- /.container -->
      </section>
      <section class="contact-form-one">
        <div class="container">
          <div class="block-title text-center">
            <img src="/assets/images/resources/sec-title-star.png" alt="Awesome Image" class="wow rotateIn animated" data-wow-duration="1500ms" style="visibility: visible; animation-duration: 1500ms; animation-name: rotateIn;">
            <p class="block-title__tag-line">Become a Volunteer </p>
            <h2 class="block-title__title">Apply &amp; Join Us Today</h2><!-- /.block-title__title -->
          </div><!-- /.block-title -->
          <form class="contact-form-one__form contact-form-validated" novalidate="novalidate">
            <div class="row low-gutters">
              <div class="col-lg-6">
                <input type="text" name="name" placeholder="Your Name">
              </div><!-- /.col-lg-6 -->
              <div class="col-lg-6">
                <input type="text" name="email" placeholder="Email Address">
              </div><!-- /.col-lg-6 -->
              <div class="col-lg-6">
                <input type="text" name="phone" placeholder="Phone">
              </div><!-- /.col-lg-6 -->
              <div class="col-lg-6">
                <input type="text" name="address" placeholder="Address">
              </div><!-- /.col-lg-6 -->
              <div class="col-lg-12">
                <textarea name="message" placeholder="Describe Yourself"></textarea>
                <div class="text-center">
                  <button type="submit" class="thm-btn contact-form-one__btn">Send Request</button>
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
        name: "Volunteer"
    }
</script>

<style scoped>

</style>
