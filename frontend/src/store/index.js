import { createStore } from "vuex";

export default createStore({
  state: {
    isAdmin: false,
  },
  getters: {},
  mutations: {
    setAdmin(state, payload) {
      state.isAdmin = payload;
    },
  },
  actions: {},
});
