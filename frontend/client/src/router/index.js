import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import NotFound from "../views/NotFound.vue";
import FAQ from "../views/FAQ.vue";
import Register from "../views/auth/Register.vue";
import Login from "../views/auth/Login.vue";
import Dashboard from "../views/Dashboard.vue";
import AdminDashboard from "../views/admin/AdminDashboard.vue";
import AdminLoanForm from "../views/admin/AdminLoanForm";
import LoanForm from "../views/LoanForm.vue";
import Loan from "../views/Loan.vue";
import EditProfile from "../views/EditProfile.vue";
import Blog from "../views/Blog.vue";
import Article from "../views/Article.vue";
import AdminBlog from "../views/admin/AdminBlog.vue";
import AdminArticleForm from "../views/admin/AdminArticleForm.vue";

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
    component: Blog,
  },
  {
    path: "/article/:id",
    name: "article",
    component: Article,
  },
  {
    path: "/faq/:amount?/:term?",
    name: "faq",
    component: FAQ,
  },
  {
    path: "/register/:email?/:mobile?",
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
  {
    path: "/admin/dashboard",
    name: "admin_dashboard",
    component: AdminDashboard,
    meta: {
      requiresAdminAuthentication: true,
    },
  },
  {
    path: "/admin/blog",
    name: "admin_blog",
    component: AdminBlog,
    meta: {
      requiresAdminAuthentication: true,
    },
  },
  {
    path: "/admin/article/:id?",
    name: "admin_article",
    component: AdminArticleForm,
    meta: {
      requiresAdminAuthentication: true,
    },
  },
  {
    path: "/apply",
    name: "apply",
    component: LoanForm,
    meta: {
      requiresAuthentication: true,
      hideNavbar: true,
    },
  },
  {
    path: "/admin/loan/:id",
    name: "admin",
    component: AdminLoanForm,
    meta: {
      requiresAdminAuthentication: true,
    },
  },
  {
    path: "/loan/:id",
    name: "loan",
    component: Loan,
    meta: {
      requiresAuthentication: true,
    },
  },
  {
    path: "/profile/:id",
    name: "profile",
    component: EditProfile,
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
  if (to.matched.some((record) => record.meta.requiresAdminAuthentication)) {
    if (!store.getters.isAdminAuthenticated) {
      next({ name: "home" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
