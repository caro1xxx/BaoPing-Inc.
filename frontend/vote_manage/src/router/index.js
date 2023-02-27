import { createRouter, createWebHistory } from "vue-router";

// 系统管理板块
import AuthView from "../views/AuthView.vue";
import SystemUserView from "../views/SystemUserView.vue";
import SystemSettingView from "../views/SystemSettingView.vue";
import DataOverview from "../views/DataOverview.vue";
import ActivityStatusView from "../views/ActivityStatusView.vue";
import GloablDomainView from "../views/GloablDomainView.vue";
import AuthGroupView from "../views/AuthGroupView.vue";
import FeedbackView from "../views/FeedbackView.vue";
import PrizeApplicationView from "../views/PrizeApplicationView.vue";
import ActivityView from "../views/ActivityView.vue";
import VoteUserView from "../views/VoteUserView.vue";
import VoteRecordView from "../views/VoteRecordView.vue";
import PaymentRecordView from "../views/PaymentRecordView.vue";
import OverViewView from "../views/OverViewView.vue";

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
  // 反馈信息
  {
    path: "/message/feedback",
    name: "feedback",
    component: FeedbackView,
  },
  // 奖品申请
  {
    path: "/message/prizeapplication",
    name: "prizeapplication",
    component: PrizeApplicationView,
  },
  // 投票活动
  {
    path: "/vote/activity",
    name: "ActivityView",
    component: ActivityView,
  },
  // 投票用户
  {
    path: "/vote/voteuser",
    name: "VoteUserView",
    component: VoteUserView,
  },
  // 投票记录
  {
    path: "/vote/voterecord",
    name: "VoteRecordView",
    component: VoteRecordView,
  },
  // 概括
  {
    path: "/order/paymentrecord",
    name: "PaymentRecordView",
    component: PaymentRecordView,
  },
  // 概括
  {
    path: "/order/overview",
    name: "OverViewView",
    component: OverViewView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
