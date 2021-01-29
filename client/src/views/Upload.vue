<template>
    <section class="section-shaped my-0 screen-height screen-section">
        <div class="shape shape-style-1 background-gradient"/>
            <div class="justify-content-center substrate">
                <div id="uploadPanel" class="container text-center">
<!--                  <div class="col-lg-7 text-center pt-lg">-->
                    <h1 class="mt-4 mb-5 caption">オンライン商品認識システム</h1>
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
@font-face {
  font-family: "Yu Mincho Light";
  src: local("Yu Mincho Light"),
  url("/src/assets/yuminl.ttf") format("truetype");
}
body {
  background-image: url("/img/BG_.png");
  background-size: cover;
}
.background-gradient {
  background-color: #213058;
  opacity: 0.66;
}
.screen-section {
  padding-top: 3.5rem;
  padding-bottom: 5rem;
}
.substrate {
  background-color: #fff;
  opacity: 0.64;
  border-radius: 21px;
  margin: 0 10vmin;
  height: 100%;
}
.caption {
  color: #29528F;
  font-family: "Yu Mincho Light", serif;
  font-size: 4em;
  line-height: 1.7;
  margin-top: 1.5rem;
  padding-top: 3vmin;
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
