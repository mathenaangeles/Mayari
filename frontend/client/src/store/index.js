import Vue from "vue";
import Vuex from "vuex";

import { login, register } from "@/api";
import { isValidJwt, EventBus } from "@/utils";

Vue.use(Vuex);

const state = {
  loans: [],
  user: {},
  jwt: "",
};

const mutations = {
  setUserData(state, payload) {
    console.log("setUserData payload = ", payload);
    state.userData = payload.userData;
  },
  setJwtToken(state, payload) {
    console.log("setJWTToken payload = ", payload);
    localStorage.token = payload.jwt.token;
    state.jwt = payload.jwt;
  },
};

const actions = {
  login(context, userData) {
    context.commit("setUserData", { userData });
    return login(userData)
      .then((response) => context.commit("setJwtToken", { jwt: response.data }))
      .catch((error) => {
        console.log("Error Authenticating: ", error);
        EventBus.$emit("failedAuthentication", error);
      });
  },
  register(context, userData) {
    context.commit("setUserData", { userData });
    return register(userData)
      .then(context.dispatch("login", userData))
      .catch((error) => {
        console.log("Error Registering: ", error);
        EventBus.$emit("failedRegistering: ", error);
      });
  },
};

const getters = {
  isAuthenticated(state) {
    return isValidJwt(state.jwt.token);
  },
};

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
});
