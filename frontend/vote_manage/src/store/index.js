
import { createStore } from "vuex";
export default createStore({
  state: {
    // 二级路由列表
    subNavBarList: [],
    // 全局提示消息
    globalMessage: "",
    // 错误刷新按钮
    errorRefresh: false,
    freshFlag: 0,
    // 是否登录
    isAuth: true,
    // 加载状态
    loadingState: false,
    // 编辑框
    editPopProps: {
      name: "",
      status: 1,
      pwd: "",
      auth: 1,
      username: "",
    },
    // 用户是否点击编辑保存按钮
    isUserEditSave: 1,
    // 用户信息
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
<<<<<<< HEAD
    // 活动管理编辑框
    voteManagePopup: { state: false, target: "" },
    // 活动管理添加框
    voteManageAddPopup: false,
    // 活动管理修改数据
    voteManageData: {},
=======
    // 全局域名管理编辑弹窗是否开启
    isRealmUpdata: false,
    // 全局域名保存数据
    realmData: {
      domain_name: '',
      // 默认为1
      status: 1,
      expire_time: undefined,
      key: undefined,
    },
    // 奖品申请编辑弹窗是否开启
    isPrizeUpdate: false,
    // 奖品申请保存数据
    prizeData: {
      wx_username: '',
      name: '',
      phone_number: '',
      create_time: '',
      status: undefined,
      index: undefined,
      pk: undefined
    }
>>>>>>> c8f51597dfe950d85a4cc8fd5a754a6f10de88b8
  },
  getters: {},
  mutations: {
    // 用户修改信息后点击保存出发
    changeSubNavBarList(state, payload) {
      state.subNavBarList = payload;
    },
    // 错误刷新状态
    reFreshState(state) {
      state.errorRefresh = true;
    },
    // 错误刷新重试
    reFresh(state) {
      state.errorRefresh = false;
      state.freshFlag += 1;
    },
    // 全局信息自动关闭
    closeGlobalMessage(state) {
      setTimeout(() => {
        state.globalMessage = "";
      }, 2000);
    },
    // 保存用户信息
    saveUserInfo(state, payload) {
      state.userInfo = payload;
    },
    // 修改提示消息
    updateGlobalMessage(state, payload) {
      state.globalMessage = payload;
    },
    // 修改加载状态
    noticifyLoading(state, payload) {
      state.loadingState = payload;
    },
    // 保存修改的用户信息
    editUserInfo(state, payload) {
      state.editPopProps.name = payload.name;
      state.editPopProps.status = payload.status;
      state.editPopProps.pwd = payload.pwd;
      state.editPopProps.auth = payload.auth;
      state.editPopProps.username = payload.username;
    },
    // 用户修改信息后点击保存出发
    editUserInfoSave(state, payload) {
      state.isUserEditSave += payload;
    },
    // 修改登录状态
    editUserInfoSave(state, payload) {
      state.isAuth = payload;
    },
<<<<<<< HEAD
    // 修改活动管理编辑框状态
    edidVoteManageSave(state, payload) {
      if (payload.type === "post") {
        state.voteManageAddPopup = !state.voteManageAddPopup;
      } else {
        state.voteManagePopup.state = !state.voteManagePopup.state;
        state.voteManagePopup.target = payload.target;
      }
    },
=======
    // 全局域名编辑弹窗开启或关闭状态
    undateRealmStatus(state, payload) {
      state.isRealmUpdata =!state.isRealmUpdata;
      if (payload.key !== undefined) {
        // 编辑
        if (payload.key) {
          state.realmData.expire_time = payload.expire_time;
          state.realmData.status = payload.status;
          state.realmData.domain_name = payload.domain_name;
          state.realmData.key = payload.key;
          state.realmData.index = payload.index;
        // 新增
        } else if (!payload.key) {
          state.realmData.expire_time = payload.expire_time;
          state.realmData.status = 1;
          state.realmData.domain_name = payload.domain_name;
          state.realmData.key = payload.key;
          state.realmData.index = undefined;
        }
      }
    },
    // 保存全局域名新增数据
    preserveRealmData(state, payload) {
      state.realmData.domain_name =  payload.domain_name;
      state.realmData.expire_time =  payload.expire_time;
      if (payload.index) {
        state.realmData.status = payload.status,
        state.realmData.index = payload.index
      }
    },
    // 改变奖品申请编辑弹窗开启或关闭
    changePrizeStatus(state, payload) {
      state.isPrizeUpdate =!state.isPrizeUpdate;
      if (payload) {
        state.prizeData.wx_username = payload.wx_username;
        state.prizeData.name = payload.name;
        state.prizeData.phone_number = payload.phone_number;
        state.prizeData.status = payload.status;
        state.prizeData.create_time = payload.create_time;
        state.prizeData.index = payload.index;
        state.prizeData.pk = payload.pk
      }
    }
>>>>>>> c8f51597dfe950d85a4cc8fd5a754a6f10de88b8
  },
  actions: {
    SubNavBarActions(context, payload) {
      context.commit("changeSubNavBarList", payload);
    },
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
    editUserActions(context, payload) {
      context.commit("editUserInfo", payload);
    },
    handleUserEditActions(context, payload) {
      context.commit("editUserInfoSave", payload);
    },
    refreshErroActions(context) {
      context.commit("reFreshState");
    },
    authActions(context, payload) {
      context.commit("editUserInfoSave", payload);
    },
    voteManagerActions(context, payload) {
      context.commit("edidVoteManageSave", payload);
    },
  },
  modules: {},
});
