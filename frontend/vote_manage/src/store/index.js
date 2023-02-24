import { createStore } from "vuex";
export default createStore({
  state: {
    globalMessage: "",
    loadingState: false,
    userInfo: {
      name: "",
      username: "",
      email: "",
      last_login_time: "",
      create_time: "",
      auth: "",
      avator: "",
      token: "",
      status: "",
    },
  },
  getters: {},
  mutations: {
    closeGlobalMessage(state) {
      setTimeout(() => {
        state.globalMessage = "";
      }, 2000);
    },
    saveUserInfo(state, payload) {
      state.userInfo = payload;
    },
    updateGlobalMessage(state, payload) {
      state.globalMessage = payload;
    },
    noticifyLoading(state, payload) {
      state.loadingState = payload;
    },
  },
  actions: {
    UserActions(context, payload) {
      context.commit("closeGlobalMessage");
      context.commit("saveUserInfo", payload);
    },
    GlobalMessageActions(context, payload) {
      context.commit("closeGlobalMessage");
      context.commit("updateGlobalMessage", payload);
    },
    NoticifyActions(context, payload) {
      context.commit("noticifyLoading", payload);
    },
  },
  modules: {},
});
