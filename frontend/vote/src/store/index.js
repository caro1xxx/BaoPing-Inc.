import { createStore } from "vuex";

export default createStore({
  // 全局设置
  state: {
    settings: {},
  },
  getters: {
  },
  mutations: {
    changeSettings(state, payload) {
      state.settings = payload;
    },
  },
  actions: {
    changeSettingsActions(context, payload) {
      context.commit("changeSettings", payload);
    },
  },
  modules: {},
});
