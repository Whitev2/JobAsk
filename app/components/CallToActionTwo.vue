<template>
  <section class="cta-two cta-two__home-one">
    <div class="container">
      <p class="cta-two__tag-line">Join the Fight for Freedom</p><!-- /.cta-two__tag-line -->
      <h3 class="cta-two__title">Help us Bring <br> the Change we Need</h3><!-- /.cta-two__title -->
      <a href="#" class="thm-btn cta-two__btn">Become a Volunteer</a>
    </div><!-- /.container -->
    <div class="donation-contribute wow fadeInUp" data-wow-duration="1500ms">
      <div class="container">
        <div class="inner-container thm-base-bg-2">
          <div class="row align-items-center">
            <div class="col-lg-5">
              <h3 class="donation-contribute__title">Contribute to help us win</h3><!-- /.donation-contribute__title -->
            </div><!-- /.col-lg-5 -->
            <div class="col-lg-7">
              <form class="donation-contribute__form">
                <div class="donation-contribute__amount">
                  <div class="dropdown bootstrap-select">
                    <div class="btn dropdown-toggle btn-light" data-toggle="dropdown" role="button" title="$">
                      <div class="filter-option">
                        <div class="filter-option-inner">
                          <div class="filter-option-inner-inner">$</div>
                        </div>
                      </div>
                    </div>
                    <div class="dropdown-menu">
                      <div class="inner show">
                        <ul class="dropdown-menu inner show"></ul>
                      </div>
                    </div>
                  </div>
                  <input type="text" name="donation-money" value="5.00">
                </div><!-- /.donation-contribute__amount -->
                <button type="submit" class="thm-btn donation-contribute__btn">Donate</button>
              </form>
            </div><!-- /.col-lg-7 -->
          </div><!-- /.row -->
        </div><!-- /.inner-container -->
      </div><!-- /.container -->
    </div><!-- /.donation-contribute -->
  </section>
</template>

<script>
  export default {
    name: "CallToActionTwo"
  }
</script>

<style scoped>

</style>
