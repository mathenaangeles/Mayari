import Vue from "vue";
import Vuex from "vuex";

import {
  login,
  register,
  updateUser,
  fetchLoans,
  fetchLoan,
  updateLoan,
  postLoan,
} from "@/api";
import { isValidJwt, EventBus } from "@/utils";

Vue.use(Vuex);

const initialState = () => {
  return {
    loans: [],
    loan: {},
    user: {},
    jwt: "",
  };
};

const store = new Vuex.Store({
  state: initialState(),
  mutations: {
    setLoans(state, payload) {
      state.loans = payload.loans;
    },
    setLoan(state, payload) {
      state.loan = payload.loan;
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
			if(localStorage.getItem('store')) {
				this.replaceState(
					Object.assign(state, JSON.parse(localStorage.getItem('store')))
				);
			}
		}
  },
  actions: {
    fetchLoans(context, userId) {
      return fetchLoans(userId, context.state.jwt.token).then((response) => {
        context.commit("setLoans", { loans: response.data });
      });
    },
    fetchLoan(context, { loanId }) {
      return fetchLoan(loanId, context.state.jwt.token).then((response) => {
        context.commit("setLoan", { loan: response.data });
      });
    },
    updateLoan(context) {
      return updateLoan(context.state.loan, context.state.jwt.token);
    },
    postLoan(context, loan) {
      return postLoan(loan, context.state.user.id, context.state.jwt.token);
    },
    updateUser(context, user) {
      return updateUser(user, context.state.user.id, context.state.jwt.token);
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
        .then(context.dispatch("login", user))
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
  },
});

store.subscribe((mutation, state) => {
	localStorage.setItem('store', JSON.stringify(state));
});

export default store;