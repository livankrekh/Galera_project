<template>
  <div style="outline: none;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;" class="px-3 pb-4">
    <div class="d-flex flex-row">
      <!--Select file button-->
        <button class="btn btn-primary btn-big"
                @click="onPickFile"
                v-if="state === State.IDLE">ファイルを選択</button>
      <!--Image-->
    <div
        class="image-container text-center"
        v-else>
        <div class="preview-image full-width position-relative cursor-pointer">
          <div class="image-overlay position-relative full-width full-height"></div>
          <div class="image-overlay-details full-width full-height">
            <label
                class="cursor-pointer full-width full-height "
                :for="idEdit">
              <svg
                  class="icon-overlay centered"
                  xmlns="http://www.w3.org/2000/svg"
                  width="512"
                  height="512"
                  viewBox="0 0 512 512">
                <path d="M469.56 42.433C420.927-6.199 382.331-.168 378.087.68l-4.8.96L36.895 338.001 0 512l173.985-36.894 336.431-336.399.941-4.86c.826-4.257 6.65-42.984-41.797-91.414zM41.944 470.057L64.3 364.617c12.448 3.347 31.968 11.255 50.51 29.794 18.96 18.963 27.84 39.986 31.875 53.436l-104.741 22.21zm132.504-41.134c-6.167-16.597-17.199-37.794-36.775-57.371C119 352.88 99.435 342.57 83.739 336.879l155.156-155.15 97.066-97.051c11.069 2.074 34.864 8.95 57.253 31.338 22.708 22.708 30.95 48.358 33.734 60.428l-96.685 96.663-155.815 155.816zm278.41-278.383c-6.167-16.6-17.196-37.8-36.781-57.384-18.669-18.667-38.228-28.977-53.92-34.668l26.118-26.113c8.785.484 30.373 4.87 58.423 32.918l.001.002c28.085 28.074 32.467 49.675 32.946 58.463l-26.787 26.782z"></path>
              </svg>
            </label>
          </div>
            <img
                class="show-img img-responsive centered"
                :src="imagePreview"
                alt="image">
        </div>
    </div>
      <!--Do not touch -->
    <div>
      <input
          class="display-none"
          :id="idUpload"
          @change="uploadFieldChange"
          name="images"
          :accept="accept"
          type="file"
          ref="imageUpload"
          :disabled="disabled">
      <input
          class="display-none"
          :id="idEdit"
          @change="editFieldChange"
          name="image"
          :accept="accept"
          type="file"
          :disabled="disabled">
    </div>
      <div class="ml-3 p-2 position-relative  image-list container block-container" style="width: 500px"
           v-if="state === State.RECOGNITION_RESULT">
        <h3 class="text-center">認識結果</h3>
        <div class="d-flex text-left ">
          <div class="mr-3">
            <div>項目１</div>
            <div>項目２</div>
            <div>項目３</div>
            <div>項目４</div>
            <div>項目５</div>
          </div>
          <div class="flex-wrap">
            <div class="flex-grow-1">Brand</div>
            <div class="flex-grow-1">Branddsihviiubfsd</div>
            <div class="flex-grow-1">Brandsjndfkjsbfoiusdbj</div>
            <div class="flex-grow-1">Brand</div>
            <div class="flex-grow-1">Brand</div>
          </div>
        </div>
      </div>
      <div class="ml-3 p-2 position-relative image-list container block-container align-items-stretch"
           style="width: 500px; height: 300px; overflow-y: auto;"
           v-if="state === State.RERECOGNITION_RESULT">
        <h3 class="text-center">再認識結果</h3>
        <div v-for="item in items" class="d-flex text-left result_item mb-2"
             v-bind:class="{ item_selected: item.isActive }"
             @click="item.isActive=true; selectedItem.isActive=false; selectedItem=item">
          <div class="mr-3">
            <img class="show-img img-responsive p-2"
                 :src="imagePreview"
                 alt="image"/>
          </div>
          <div class="mr-3">
            <div>項目１</div>
            <div>項目２</div>
            <div>項目３</div>
            <div>項目４</div>
            <div>項目５</div>
          </div>
          <div class="flex-wrap">
            <div class="flex-grow-1">Brand</div>
            <div class="flex-grow-1">Branddsihvikjdf</div>
            <div class="flex-grow-1">Brandsjndfk</div>
            <div class="flex-grow-1">Brand</div>
            <div class="flex-grow-1">Brand</div>
          </div>
        </div>
      </div>
  </div>
<!--    Buttons panel-->
    <div class="flex mt-4" v-if="images.length">
      <button
          v-if="state===State.IMAGE_SELECTED"
          type="button"
          class="btn btn-primary"
          v-on:click="upload">アップロード</button>
      <button
          v-if="state===State.RECOGNITION_RESULT || state===State.RERECOGNITION_RESULT"
          type="button"
          class="btn btn-primary"
          v-on:click="set">確定</button>
      <button
          v-if="state===State.RECOGNITION_IDLE"
          type="button"
          class="btn btn-primary"
          v-on:click="detect">認識</button>
      <button
          v-if="state===State.RECOGNITION_RESULT"
          type="button"
          class="btn btn-primary"
          v-on:click="redetect">再認識</button>
      <button
          v-if="state===State.RERECOGNITION_RESULT"
          type="button"
          class="btn btn-primary"
          v-on:click="redetect">手動入力</button>
      <button
          v-if="state===State.IMAGE_SELECTED ||
          state===State.RECOGNITION_RESULT ||
          state===State.RECOGNITION_IDLE||
          state===State.RERECOGNITION_RESULT"
          type="button"
          class="btn btn-primary"
          @click.prevent="deleteImage(currentIndexImage)">取り消し</button>
      <button
          v-if="state===State.RESULT"
          type="button"
          class="btn btn-primary"
          @click.prevent="deleteImage(currentIndexImage)">戻る</button>
    </div>
    <!--Alert-->
    <div class="processing-cover full-width full-height text-center text-primary position-fixed"
         v-if="state === State.IMAGE_UPLOADING || state === State.RECOGNITION || state === State.RERECOGNITION || state === State.MANUAL_INPUTING ||
state === State.IMAGE_UPLOADING_FAILED || state === State.RECOGNITION_FAILED || state === State.RERECOGNITION_FAILED || state === State.MANUAL_INPUTING_FAIL">
      <div class="centered">
        <div v-if="state === State.IMAGE_UPLOADING || state === State.RECOGNITION || state === State.RERECOGNITION || state === State.MANUAL_INPUTING">
          <img class="icon-drag-drop" src="img/icons/process.gif"/>
          <h4 class="drop-text-here" v-if="state === State.IMAGE_UPLOADING">アップロード中</h4>
          <h4 class="drop-text-here" v-if="state === State.RECOGNITION">認識中</h4>
          <h4 class="drop-text-here" v-if="state === State.RERECOGNITION">再認識中</h4>
          <h4 class="drop-text-here" v-if="state === State.MANUAL_INPUTING">手動入力中</h4>
        </div>
        <div class="alert alert-danger mt-4" v-if="state === State.IMAGE_UPLOADING_FAILED">アップロード失敗</div>
        <div class="alert alert-danger mt-4" v-if="state === State.RECOGNITION_FAILED">認識失敗</div>
        <div class="alert alert-danger mt-4" v-if="state === State.RERECOGNITION_FAILED">再認識失敗</div>
        <div class="alert alert-danger mt-4" v-if="state === State.MANUAL_INPUTING_FAIL">手動入力失敗</div>
      </div>
    </div>
    <div
        class="drag-upload-cover position-fixed full-height full-width"
        style="background: white"
        v-if="isDragover">
      <div class="centered full-width text-center text-primary">
        <svg
            class="icon-drag-drop"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512">
          <path d="M444.5 15C407.7 15 378 44.8 378 81.5s29.8 66.5 66.5 66.5S511 118.2 511 81.5 481.2 15 444.5 15zm29.4 72.4h-23.5l.1 25.9c0 3.2-2.6 5.8-5.8 5.9-3.2 0-5.8-2.6-5.8-5.8l-.1-26h-23.6c-3.2 0-5.8-2.6-5.8-5.8s2.6-5.8 5.8-5.8h23.5l-.1-25.9c0-3.2 2.6-5.8 5.8-5.9 3.2 0 5.8 2.6 5.8 5.8l.1 26h23.6c3.3 0 5.8 2.6 5.8 5.8s-2.6 5.8-5.8 5.8zM199.3 191.3c21.5 0 38.9 17.6 38.9 39.3s-17.4 39.3-38.9 39.3-38.9-17.6-38.9-39.3c0-21.7 17.5-39.3 38.9-39.3zm185.4 201.3H86.3c-6.5 0-11.9-5.3-11.9-11.9v-32.4c0-2.5.7-4.8 2.1-6.9l41.3-58.4c3.7-5.2 10.8-6.5 16.1-3.1l56.4 36.8c4.5 3 10.3 2.5 14.4-1L313 220.1c5.1-4.5 13.1-3.8 17.2 1.7l61.5 79.7c1.6 2 2.5 4.6 2.5 7.2v74.4c0 5.2-4.3 9.5-9.5 9.5zm7.9 117.6h-58.8v-12h58.8v12zm-78.4 0h-58.8v-12h58.8v12zm-78.5 0h-58.8v-12h58.8v12zm-78.4 0H98.4v-12h58.8v12h.1zm-78.5 0H57.7c-14.3 0-27.9-5.4-38.3-15.3l8.3-8.7c8.2 7.8 18.8 12 30.1 12h21.1l-.1 12zm333.6-.1l-.3-12c17.8-.4 33.4-11.5 39.8-28.2l11.2 4.3c-8.1 21.3-28 35.4-50.7 35.9zM6.8 477c-3.2-7.1-4.7-14.7-4.7-22.5v-38.2h12v38.2c0 6.1 1.3 12.1 3.7 17.6l-11 4.9zm459.9-24.1h-12v-58.8h12v58.8zM14.1 396.7h-12v-58.8h12v58.8zm452.6-22.3h-12v-58.8h12v58.8zM14.1 318.3h-12v-58.8h12v58.8zM466.7 296h-12v-58.8h12V296zM14.1 239.8h-12V181h12v58.8zm452.6-22.2h-12v-58.8h12v58.8zM14.1 161.4h-12v-58.8h12v58.8zm2.4-76.1L5.3 81.2C13 59.9 33.4 45.5 56.1 45.5h.2v12h-.2c-17.7 0-33.6 11.2-39.6 27.8zm353.6-27.8h-58.8v-12h58.8v12zm-78.5 0h-58.8v-12h58.8v12zm-78.4 0h-58.8v-12h58.8v12zm-78.5 0H75.9v-12h58.8v12z"></path>
        </svg>
        <h4 class="drop-text-here"><b>{{dropText}}</b></h4>
      </div>
    </div>
    </div>
</template>

<script>
import { forEach, findIndex, cloneDeep } from 'lodash'
import Popper from 'vue-popperjs'
import 'vue-popperjs/dist/css/vue-popper.css'
import axios from "axios";
const State= Object.freeze({
  IDLE: 1,
  IMAGE_SELECTED: 2,
  IMAGE_UPLOADING:3,
  IMAGE_UPLOADING_FAILED: 4,
  RECOGNITION_IDLE: 5,
  RECOGNITION: 6,
  RECOGNITION_FAILED: 7,
  RECOGNITION_RESULT: 8,
  RERECOGNITION: 9,
  RERECOGNITION_FAILED: 10,
  RERECOGNITION_RESULT: 11,
  MANUAL_INPUT_FORM: 12,
  MANUAL_INPUTING: 13,
  MANUAL_INPUTING_FAIL: 14,
  RESULT: 15,
})
export default {

  name: 'VueUploadMultipleImage',

  props: {
    dragText: {
      type: String,
      default: '画像をドラッグ'
    },
    browseText: {
      type: String,
      default: 'または選択'
    },
    dropText: {
      type: String,
      default: 'ファイルをこちらにドロップしてください。'
    },
    accept: {
      type: String,
      default: 'image/gif,image/jpeg,image/png,image/bmp,image/jpg'
    },
    dataImages: {
      type: Array,
      default: () => {
        return []
      }
    },
    multiple: {
      type: Boolean,
      default: true
    },
    showPrimary: {
      type: Boolean,
      default: true
    },
    maxImage: {
      type: Number,
      default: 5
    },
    idUpload: {
      type: String,
      default: 'image-upload'
    },
    idEdit: {
      type: String,
      default: 'image-edit'
    },
    disabled: {
      type: Boolean,
      default: false
    },
  },
  data () {
    return {
      currentIndexImage: 0,
      images: [],
      formData: null,
      lastTarget: null,
      isDragover: false,
      State,
      state: State.IDLE,
      items: [
        { message: 'Foo', isActive: true },
        { message: 'Bar', isActive: false },
        { message: 'Foo', isActive: false },
        { message: 'Bar', isActive: false }
      ],
      selectedItem: 0
    }
  },
  components: {
    Popper,
  },
  computed: {
    imagePreview () {
      let index = findIndex(this.images, { highlight: 1 })
      if (index > -1) {
        return this.images[index].path
      } else {
        return this.images.length ? this.images[0].path : ''
      }
    },
    // eslint-disable-next-line vue/return-in-computed-property
    imageDefault () {
      if (this.images[this.currentIndexImage]) {
        return this.images[this.currentIndexImage].default
      }
    }
  },
  methods: {
    onPickFile () {
      console.log(this.$refs.imageUpload)
      this.$refs.imageUpload.click()
    },
    onDragEnter(e) {
      this.lastTarget = e.target;
      console.log("onDragEnter")
      this.isDragover = true;
    },
    onDragLeave(e) {
      if (e.target === this.lastTarget) {
        console.log("onDragLeave")
        this.isDragover = false;
      }
    },
    onDragOver(e) {
      e.preventDefault();
    },
    selectItem(e) {

    },
    upload() {
      this.state=State.IMAGE_UPLOADING
      console.log('upload', this.images)
      // Upload image api
      let image = this.formData
      axios.post('http://localhost/api/predict', { image }).then(response => {
        // console.log(response)
        if(true) {
          console.log("成功")
          this.state=State.RECOGNITION_IDLE
        }
        else {
          console.log("失敗")
          this.state=State.IMAGE_UPLOADING_FAILED
          setTimeout(() => {
            this.state = State.IMAGE_SELECTED
          }, 2000)
        }
      })
      //FOR TEST
      setTimeout(() => {
      if(true) {
        console.log("成功")
        this.state=State.RECOGNITION_IDLE
      }
      else {
        console.log("失敗")
        this.state=State.IMAGE_UPLOADING_FAILED
        setTimeout(() => {
            this.state = State.IMAGE_SELECTED
           }, 2000)
      } }, 2000);
    },
    detect() {
      this.state=State.RECOGNITION
      console.log('upload', this.images)
      // Detection image api
      axios.post('localhost:5000/predict', { data: this.images }).then(response => {
        this.isUploading = false
        // console.log(response)
        if(true) {
          console.log("成功")
          this.state=State.RECOGNITION_RESULT
        }
        else {
          console.log("失敗")
          this.state=State.RECOGNITION_FAILED
              setTimeout(() => {
                this.state=State.RECOGNITION_IDLE
              }, 2000)
        }
      })
      //FOR TEST
      // setTimeout(() => {
      //   if(true) {
      //     console.log("成功")
      //     this.state=State.RECOGNITION_RESULT
      //   }
      //   else {
      //     console.log("失敗")
      //     this.state=State.RECOGNITION_FAILED
      //     setTimeout(() => {
      //       this.state=State.RECOGNITION_IDLE
      //     }, 2000)
      //   } }, 2000);
    },
    set() {
      this.state=State.RESULT
    },
    redetect() {
      this.state=State.RERECOGNITION
      setTimeout(() => {
        if(true) {
          console.log("成功")
          this.state=State.RERECOGNITION_RESULT
        }
        else {
          console.log("失敗")
          this.state=State.RERECOGNITION_FAILED
          setTimeout(() => {
            this.state=State.RECOGNITION_RESULT
          }, 2000)
        } }, 2000);
    },

    preventEvent (e) {
      e.preventDefault()
      e.stopPropagation()
    },
    onDrop (e) {
      console.log("onDrop")
      this.isDragover = false
      e.stopPropagation()
      e.preventDefault()
      let files = e.dataTransfer.files
      if (!files.length) {
        return false
      }
      // eslint-disable-next-line no-unused-vars
      forEach(files, (value, index) => {
        this.createImage(value)
        if (!this.multiple) {
          return false
        }
      })
      if (document.getElementById(this.idUpload)) {
        document.getElementById(this.idUpload).value = []
      }
    },
    onDragover () {
      console.log("onDragover")
      this.isDragover = true
    },
    createImage (file) {
      if (this.disabled) return
      let reader = new FileReader()
      let formData = new FormData()
      formData.append('file', file)
      this.formData = formData
      reader.onload = (e) => {
        let dataURI = e.target.result
        if (dataURI) {
          if (!this.images.length) {
            this.images.push({ name: file.name, path: dataURI, highlight: 1, default: 1 })
            this.currentIndexImage = 0
          } else {
            this.images.push({ name: file.name, path: dataURI, highlight: 0, default: 0 })
          }
          this.state = State.IMAGE_SELECTED
          this.$emit('upload-success', formData, this.images.length - 1, this.images)
        }
      }
      reader.readAsDataURL(file)
    },
    editImage (file) {
      if (this.disabled) return
      let reader = new FileReader()
      let formData = new FormData()
      formData.append('file', file)
      reader.onload = (e) => {
        let dataURI = e.target.result
        if (dataURI) {
          if (this.images.length && this.images[this.currentIndexImage]) {
            this.images[this.currentIndexImage].path = dataURI
            this.images[this.currentIndexImage].name = file.name
          }
        }
      }
      reader.readAsDataURL(file)
      this.$emit('edit-image', formData, this.currentIndexImage, this.images)
    },
    uploadFieldChange (e) {
      let files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return false
      }
      // eslint-disable-next-line no-unused-vars
      forEach(files, (value, index) => {
        this.createImage(value)
      })
      if (document.getElementById(this.idUpload)) {
        document.getElementById(this.idUpload).value = []
      }
    },
    editFieldChange (e) {
      let files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return false
      }
      forEach(files, (value, index) => {
        this.editImage(value)
      })
      if (document.getElementById(this.idEdit)) {
        document.getElementById(this.idEdit).value = ''
      }
    },
    deleteImage (currentIndex) {
      let r = confirm("画像を取り消しますか？")
      if (r === true) {
        if (this.images[currentIndex].default === 1) {
          this.images[0].default = 1
        }
        this.images.splice(currentIndex, 1)
        this.currentIndexImage = 0
        if (this.images.length) {
          this.images[0].highlight = 1
        }
        this.state = State.IDLE
      } else {
      }
    },
  },
  watch: {
    dataImages: {
      handler: function (newVal) {
        this.images = cloneDeep(newVal)
      },
      deep: true
    }
  },
  mounted () {
    window.addEventListener('dragenter', this.onDragEnter);
    window.addEventListener('dragleave', this.onDragLeave);
    window.addEventListener('dragover', this.onDragOver);
    window.addEventListener('drop', this.onDrop);
    this.selectedItem = this.items[0]
  },
  beforeDestroy() {
    window.removeEventListener('dragenter', this.onDragEnter);
    window.removeEventListener('dragleave', this.onDragLeave);
    window.removeEventListener('dragover', this.onDragOver);
    window.removeEventListener('drop', this.onDrop);
  },
  created () {
    this.images = []
    this.images = cloneDeep(this.dataImages)
  }
}
</script>

<style lang="css" scoped>
.text-small {
  font-size: 11px;
}
.position-relative {
  position: relative;
}
.position-absolute {
  position: absolute;
}
.text-center {
  text-align: center;
}
.text-primary {
  color: #2fa3e6;
}
.btn-primary {
  color: #312A15;
  background-color: #FFD86D;
  opacity: 0.84;
}
.display-flex {
  display: flex;
}
.flex-column {
  flex-direction: column;
}
.flex-wrap {
  flex-wrap: wrap;
}
.justify-content-center {
  justify-content: center;
}
.justify-content-between {
  justify-content: space-between;
}
.justify-content-end {
  justify-content: flex-end;
}
.align-items-center {
  align-items: center;
}
.full-width {
  width: 100%;
}
.full-height {
  height: 100%;
}
.cursor-pointer {
  cursor: pointer;
}
.centered {
  left: 50%;
  transform: translate(-50%, -50%);
  top: 50%;
  position: absolute;
  display: block;
}
.image-container {
  width: 200px;
  height: 200px;
  border-radius: 5px;
  background-color: #fff;
}
.block-container {
  border: 1px solid #d6d6d6;
  border-radius: 4px;
  background-color: #fff;
}
.btn-big {
  width: 260px;
  height: 75px;
  font-size: 28px;
  margin-top: 100px;
}
.image-center {
  width: 100%;
  height: 100%;
}
.image-icon-drag {
  fill: #c9c8c8;
  height: 50px;
  width: 50px;
}
.drag-text {
  padding-top: 5px;
  color: #777;
  font-weight: 400;
  line-height: 1.5;
}
.browse-text {
  font-size: 86%;
  color: #206ec5;
  text-decoration: none;
}
.image-input {
  overflow: hidden;
  opacity: 0;
  top: 0;
  left: 0;
  bottom: 0;
}
.image-input label {
  display: block;
}
.drag-upload-cover {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: #fcfeff;
  opacity: 0.9;
  z-index: 10;
  margin: 5px;
  border: 2px dashed #268ddd;
}
.processing-cover {
  background: #fcfeff;
  opacity: 0.9;
  z-index: 20;
}
.drag-upload-cover {
  font-weight: 400;
  font-size: 20px;
}
.icon-drag-drop {
  height: 50px;
  width: 50px;
  fill: #2fa3e6;
}
.drop-text-here {
  margin: 0;
  line-height: 1.5;
}
.display-none {
  display: none;
}

/* list images*/
.image-list {
  border: 1px solid #d6d6d6;
}
.preview-image {
  height: 200px;
  width: 200px;
  border-radius: 15px;
  box-sizing: border-box;
}

.image-overlay {
  background: rgba(0, 0, 0, 0.7);
  z-index: 10;
  border-radius: 5px;
  opacity: 0;
  transition: all 0.3s ease-in-out 0s;
}
.image-overlay-details {
  position: absolute;
  z-index: 11;
  opacity: 0;
  transform: translate(0, -50%);
  top: 50%;
}
.icon-overlay {
  width: 40px;
  height: 40px;
  fill: #fff;
}
.preview-image:hover .image-overlay,
.preview-image:hover .image-overlay-details {
  opacity: 1;
}
.img-responsive {
  display: block;
  max-width: 100%;
  height: auto;
}
.show-img {
  max-height: 200px;
  max-width: 200px;
  display: block;
  vertical-align: middle;
}
/*image bottom*/
.image-bottom {
  bottom: 0;
  left: 0;
  height: 40px;
  padding: 5px 10px;
  box-sizing: border-box;
}
.image-primary {
  border-radius: 4px;
  background-color: #e3edf7;
  padding: 3px 7px;
  font-size: 11px;
  margin-right: 5px;
}
.image-icon-primary {
  width: 10px;
  height: 10px;
  margin-right: 2px;
}
.image-icon-delete {
  height: 14px;
  width: 14px;
  fill: #222;
}
.image-edit {
  margin-right: 10px;
}
.image-icon-edit {
  height: 14px;
  width: 14px;
  fill: #222;
}
.image-list-container {
  max-width: 190px;
  min-height: 50px;
  margin-top: 10px;
}
.image-list-container .image-list-item {
  height: 32px;
  width: 32px;
  border-radius: 4px;
  border: 1px solid #d6d6d6;
}
.image-list-container .image-list-item:not(:last-child) {
  margin-right: 5px;
  margin-bottom: 5px;
}
.image-list-container .image-list-item .show-img {
  max-width: 25px;
  max-height: 17px;
}
.image-list-container .image-highlight {
  border: 1px solid #2fa3e7;
}
.add-image-svg {
  width: 12px;
  height: 12px;
  fill: #222;
}
.input-add-image {
  overflow: hidden;
  opacity: 0;
  top: 0;
  left: 0;
  bottom: 0;
  z-index: 11;
}
.input-add-image label {
  display: block;
}
.image-icon-info {
  width: 14px;
  height: 14px;
  fill: #222;
}
.mark-text-primary {
  color: #034694;
}
.popper-custom {
  background: #000;
  padding: 10px;
  border: none;
  box-shadow: none;
  color: white;
  text-align: left;
  font-size: 12px;
}

.result_item {
  border-radius: 25px;
  border: 2px solid #444;
}

.item_selected {
  border: 4px solid #24b47e;
}
</style>
<style lang="css">
.popper-custom .popper__arrow {
  border-color: #000 transparent transparent transparent !important;
}
</style>
