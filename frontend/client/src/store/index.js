import Vue from "vue";
import Vuex from "vuex";

import { login, register } from "@/api";
import { isValidJwt, EventBus } from "@/utils";

Vue.use(Vuex);

const initialState = () => {
  return {
    loans: [],
    user: {},
    jwt: "",
  }
}

const state = initialState()

const mutations = {
  setUser(state, payload) {
    state.user = payload.user;
  },
  setJwtToken(state, payload) {
    localStorage.token = payload.jwt.token;
    state.jwt = payload.jwt;
  },
  resetState (state) {
    Object.assign(state, initialState())
  }
};

const actions = {
  login(context, user) {
    context.commit("setUser", { user });
    return login(user)
      .then((response) => context.commit("setJwtToken", { jwt: response.data }))
      .catch((error) => {
        console.log("Authentication Error: ", error);
        EventBus.$emit("failedLogin", error);
      });
  },
  register(context, user) {
    context.commit("setUser", { user });
    return register(user)
      .then(context.dispatch("login", user))
      .catch((error) => {
        console.log("Registration Error: ", error);
        EventBus.$emit("failedRegister: ", error);
      });
  },
  logout(context) {
    context.commit("resetState");
  }
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
