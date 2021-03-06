import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Upload from "./views/Upload.vue";

Vue.use(Router);

export default new Router({
  linkExactActiveClass: "active",
  routes: [
    {
      path: "/",
      name: "upload",
      components: {
        header: AppHeader,
        default: Upload,
        footer: AppFooter
      }
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  }
});
