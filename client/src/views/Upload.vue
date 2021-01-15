<template>
    <section class="section section-shaped section-lg my-0">
        <div class="shape shape-style-1 bg-gradient-default">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
        <div class="container pt-lg-md">
            <div class="row justify-content-center">
                <div class="col-lg-5">
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
</style>
