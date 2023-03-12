import { createStore } from "vuex";

export default createStore({
  // 全局设置
  state: {
    settings: {},
    currentClickAlht:0,
    // 通用弹窗开启或关闭属性
    publicData: {
      status: false,
      value: ''
    }
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
    },
    chengePublicData(state, payload) {
      if (payload) {
        state.publicData.status = true;
        state.publicData.value = payload
      } else {
        state.publicData.status = false;
      }
    }
  },
  actions: {
    changeSettingsActions(context, payload) {
      context.commit("changeSettings", payload);
    },
  },
  modules: {},
});
