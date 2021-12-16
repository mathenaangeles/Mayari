import Vue from "vue";
import { BootstrapVue } from "bootstrap-vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import VuePageTransition from 'vue-page-transition'

Vue.use(VuePageTransition)
Vue.config.productionTip = false;
Vue.use(BootstrapVue);
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
