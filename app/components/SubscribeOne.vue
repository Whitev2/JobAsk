<template>
  <section class="mailchimp-one">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-5">
          <h3 class="mailchimp-one__title">Don't miss our monthly updates</h3><!-- /.mailchimp-one__title -->
        </div><!-- /.col-lg-5 -->
        <div class="col-lg-7">
          <form class="mailchimp-one__form mc-form">
            <input placeholder="Email Address" type="email" required="required" class="formInput" name="EMAIL">
            <button type="submit" class="thm-btn mailchimp-one__form-btn">Subscribe</button>
          </form>
          <div class="mc-form__response"></div><!-- /.mc-form__response -->
        </div><!-- /.col-lg-7 -->
      </div><!-- /.row -->
    </div><!-- /.container -->
  </section>
</template>

<script>
    export default {
        name: "SubscribeOne"
    }
</script>

<style scoped>

</style>
