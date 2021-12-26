import Vue from "vue";
import { BootstrapVue } from "bootstrap-vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import AOS from 'aos'
import 'aos/dist/aos.css'
import VuePageTransition from "vue-page-transition";
import "vue2-animate/dist/vue2-animate.min.css";
Vue.use(VuePageTransition);
Vue.config.productionTip = false;
Vue.use(BootstrapVue);
new Vue({
  router,
  store,
  created () {
    AOS.init()
  },
  render: (h) => h(App),
}).$mount("#app");
