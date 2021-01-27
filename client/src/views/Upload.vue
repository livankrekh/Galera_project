<template>
    <section class="section section-shaped section-lg my-0 screen-height">
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
                <div id="uploadPanel" class="container text-center">
<!--                  <div class="col-lg-7 text-center pt-lg">-->
                    <h1 class="text-white mt-4 mb-5">オンライン商品認識システム</h1>
<!--                  </div>-->
                       <vue-upload-multiple-image
                           class="px-lg-5 py-lg-5"
                           style="display: flex;
                           justify-content: center;
                           flex-direction: column;
                           align-items: center;"/>
                </div>
            </div>
    </section>
</template>
<script>
// import * as Vibrant from 'node-vibrant'
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
.screen-height {
  height: 100vh;
}
</style>
