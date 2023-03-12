import { createStore } from "vuex";

export default createStore({
  // 全局设置
  state: {
    settings: {},
    currentClickAlht:0,
  },
  getters: {
  },
  mutations: {
    changeSettings(state, payload) {
      state.settings = payload;
    },
    changeCurrentClick(state,payload){
      if(!payload)return;
      state.currentClickAlht = payload
    }
  },
  actions: {
    changeSettingsActions(context, payload) {
      context.commit("changeSettings", payload);
    },
  },
  modules: {},
});
