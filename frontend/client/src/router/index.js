import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import NotFound from "../views/NotFound.vue";
import FAQ from "../views/FAQ.vue";
import Register from "../views/auth/Register.vue";
import Login from "../views/auth/Login.vue";
import Dashboard from "../views/Dashboard.vue";

import store from "../store/index.js";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/about",
    name: "about",
    component: About,
  },
  {
    path: "/404",
    name: "404",
    component: NotFound,
  },
  {
    path: "/blog",
    name: "blog",
    component: NotFound,
  },
  {
    path: "/faq/:amount?/:term?",
    name: "faq",
    component: FAQ,
  },
  {
    path: "/register",
    name: "register",
    component: Register,
    meta: {
      hideForAuthenticated: true,
    },
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: {
      hideForAuthenticated: true,
    },
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: Dashboard,
    meta: {
      requiresAuthentication: true,
    },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuthentication)) {
    if (!store.getters.isAuthenticated) {
      next({ name: "login" });
    } else {
      next();
    }
  } else {
    next();
  }
  if (to.matched.some((record) => record.meta.hideForAuthenticated)) {
    if (store.getters.isAuthenticated) {
      next({ name: "dashboard" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
