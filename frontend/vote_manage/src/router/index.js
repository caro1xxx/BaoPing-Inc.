import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

// 系统管理板块
import AuthView from "../views/AuthView.vue";
import SystemUserView from "../views/SystemUserView.vue";
import SystemSettingView from "../views/SystemSettingView.vue";
import GlobalDomainView from "../views/GlobalDomainView.vue";
import AuthGroupView from "../views/AuthGroupView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  // 登录注册
  {
    path: "/auth",
    name: "auth",
    component: AuthView,
  },
  // 系统用户
  {
    path: "/systemuser",
    name: "systemuser",
    component: SystemUserView,
  },
  // 系统设置
  {
    path: "/systemsetting",
    name: "systemsetting",
    component: SystemSettingView,
  },
  // 全局域名
  {
    path: "/globaldomain",
    name: "globaldomain",
    component: GlobalDomainView,
  },
  // 权限分支
  {
    path: "/authgroup",
    name: "authgroup",
    component: AuthGroupView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
