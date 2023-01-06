import { createStore } from "vuex";

export default createStore({
  state: {
    isLogin: false,
  },
  getters: {},
  mutations: {
    // 로그인 상태를 변경합니다.
    changeLoginStatus(state, payload) {
      state.isLogin = payload;
    },
  },
  actions: {},
});
