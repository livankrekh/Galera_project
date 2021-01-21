<template>
    <section class="section section-shaped section-lg my-0">
        <div class="shape shape-style-1 background-gradient">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
            <div class="row justify-content-center">
                <div id="uploadPanel" class="col-lg-5 text-center">
<!--                  <div class="col-lg-7 text-center pt-lg">-->
                    <p class="caption text-white mt-4 mb-5">オンライン商品認識システム</p>
<!--                  </div>-->
                    <card type="secondary" shadow
                          header-classes="bg-white pb-5"
                          body-classes="px-lg-5 py-lg-5"
                          class="border-0">
                       <vue-upload-multiple-image
                           style="display: flex;
                           justify-content: center;
                           flex-direction: column;
                           align-items: center;"/>
                    </card>
                </div>
            </div>
    </section>
</template>
<script>
import VueUploadMultipleImage from '@/views/components/VueUploadMultipleImage.vue'
export default {
  components: {VueUploadMultipleImage}
};
</script>
<style>
.background-gradient {
  background: linear-gradient(87deg, #9E0329 0, #44111B 100%) !important
}
.caption {
  font-size: 2rem;
  font-weight: 300;
  line-height: 1.7;
  margin-top: 1.5rem;
}
.blur {
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px);
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(5px);
  background-color: #ccc;
}
</style>
