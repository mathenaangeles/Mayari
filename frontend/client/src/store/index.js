import Vue from "vue";
import Vuex from "vuex";

import {
  login,
  register,
  updateUser,
  uploadProfilePhoto,
  fetchLoans,
  fetchAllLoans,
  fetchLoan,
  updateLoan,
  postLoan,
  postArticle,
  fetchArticles,
  fetchArticle,
  fetchAllArticles,
  updateArticle,
  deleteArticle,
} from "@/api";
import { isValidJwt, EventBus } from "@/utils";

Vue.use(Vuex);

const initialState = () => {
  return {
    loans: [],
    loan: {},
    business: {},
    user: {},
    jwt: "",
    articles: [],
    article: {},
  };
};

const store = new Vuex.Store({
  state: initialState(),
  mutations: {
    setArticles(state, payload) {
      state.articles = payload.articles;
    },
    setArticle(state, payload) {
      state.article = payload.article;
    },
    setLoans(state, payload) {
      state.loans = payload.loans;
    },
    setLoan(state, payload) {
      state.loan = payload.loan;
    },
    setBusiness(state, payload) {
      state.business = payload.business;
    },
    setUser(state, payload) {
      state.user = payload.user;
    },
    setJwtToken(state, payload) {
      state.jwt = payload.jwt;
      localStorage.token = payload.jwt;
    },
    resetState(state) {
      Object.assign(state, initialState());
    },
    initializeStore(state) {
      if (localStorage.getItem("store")) {
        this.replaceState(
          Object.assign(state, JSON.parse(localStorage.getItem("store")))
        );
      }
    },
  },
  actions: {
    deleteArticle(context, articleId) {
      return deleteArticle(articleId, context.state.jwt).then(() => {
        context.commit("setArticle", { article: {} });
      });
    },
    updateArticle(context, { article, articleId }) {
      return updateArticle(article, articleId, context.state.jwt);
    },
    fetchAllArticles(context) {
      return fetchAllArticles(context.state.jwt).then((response) => {
        context.commit("setArticles", { articles: response.data });
      });
    },
    fetchArticle(context, { articleId }) {
      return fetchArticle(articleId).then((response) => {
        context.commit("setArticle", { article: response.data });
      });
    },
    fetchArticles(context) {
      return fetchArticles().then((response) => {
        context.commit("setArticles", { articles: response.data });
      });
    },
    postArticle(context, article) {
      return postArticle(article, context.state.jwt);
    },
    updateLoan(context, loan) {
      return updateLoan(loan, context.state.jwt);
    },
    fetchAllLoans(context) {
      return fetchAllLoans(context.state.jwt).then((response) => {
        context.commit("setLoans", { loans: response.data });
      });
    },
    fetchLoan(context, { loanId }) {
      return fetchLoan(loanId, context.state.jwt).then((response) => {
        context.commit("setLoan", { loan: response.data[0] });
        context.commit("setBusiness", { business: response.data[1] });
      });
    },
    fetchLoans(context) {
      return fetchLoans(context.state.user.id, context.state.jwt).then(
        (response) => {
          context.commit("setLoans", { loans: response.data });
        }
      );
    },
    postLoan(context, loan) {
      return postLoan(loan, context.state.jwt);
    },
    uploadProfilePhoto(context, image) {
      return uploadProfilePhoto(
        image,
        context.state.user.id,
        context.state.jwt
      ).then((response) => {
        context.commit("setUser", { user: response.data });
      });
    },
    updateUser(context, user) {
      return updateUser(user, context.state.user.id, context.state.jwt).then(
        (response) => {
          context.commit("setUser", { user: response.data });
        }
      );
    },
    login(context, user) {
      return login(user)
        .then((response) => {
          context.commit("setJwtToken", { jwt: response.data.token });
          context.commit("setUser", { user: response.data.user });
        })
        .catch((error) => {
          console.log("Authentication Error: ", error);
          EventBus.$emit("failedLogin", error);
        });
    },
    register(context, user) {
      return register(user)
        .then((response) => {
          console.log(response);
          context.dispatch("login", user);
        })
        .catch((error) => {
          console.log("Registration Error: ", error);
          EventBus.$emit("failedRegister: ", error);
        });
    },
    logout(context) {
      localStorage.removeItem("token");
      context.commit("resetState");
    },
  },
  getters: {
    isAuthenticated() {
      return isValidJwt(localStorage.getItem("token"));
    },
    isAdminAuthenticated(state) {
      return (
        isValidJwt(localStorage.getItem("token")) && state.user.role == "admin"
      );
    },
  },
});

store.subscribe((mutation, state) => {
  localStorage.setItem("store", JSON.stringify(state));
});

export default store;
