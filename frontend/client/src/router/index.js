import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import ErrorPage from "../views/ErrorPage.vue";
import FAQ from "../views/FAQ.vue";
import Register from "../views/auth/Register.vue";
import Login from "../views/auth/Login.vue";
import UserDashboard from "../views/auth/UserDashboard.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/404",
    name: "404",
    component: ErrorPage,
  },
  {
    path: "/blog",
    name: "blog",
    component: ErrorPage,
  },
  {
    path: "/faq/:amount?/:term?",
    name: "faq",
    component: FAQ,
  },
  {
    path: "/contact",
    name: "contact",
    component: ErrorPage,
  },
  {
    path: "/register",
    name: "register",
    component: Register,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: UserDashboard,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
