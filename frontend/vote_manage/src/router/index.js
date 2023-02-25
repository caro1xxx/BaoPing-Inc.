import { createRouter, createWebHistory } from "vue-router";

// 系统管理板块
import AuthView from "../views/AuthView.vue";
import SystemUserView from "../views/SystemUserView.vue";
import SystemSettingView from "../views/SystemSettingView.vue";
import DataOverview from "../views/DataOverview.vue";
import ActivityStatusView from "../views/ActivityStatusView.vue";
import GloablDomainView from "../views/GloablDomainView.vue";
import AuthGroupView from "../views/AuthGroupView.vue";

const routes = [
  // 登录注册
  {
    path: "/auth",
    name: "auth",
    component: AuthView,
  },
  // 数据概括
  {
    path: "/",
    name: "home",
    component: DataOverview,
  },
  // 活动状态
  {
    path: "/activitystatus",
    name: "activitystatus",
    component: ActivityStatusView,
  },
  // 系统用户
  {
    path: "/system/systemuser",
    name: "systemuser",
    component: SystemUserView,
  },
  // 系统设置
  {
    path: "/system/systemsetting",
    name: "systemsetting",
    component: SystemSettingView,
  },
  // 全局域名
  {
    path: "/system/gloabldomain",
    name: "gloabldomain",
    component: GloablDomainView,
  },
  // 权限分组
  {
    path: "/system/authgroup",
    name: "authgroup",
    component: AuthGroupView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
