import { createRouter, createWebHistory } from "vue-router";

// 系统管理板块
import AuthView from "../views/AuthView.vue";
import SystemUserView from "../views/SystemUserView.vue";
import SystemSettingView from "../views/SystemSettingView.vue";
import DataOverview from "../views/DataOverview.vue";
import GloablDomainView from "../views/GloablDomainView.vue";
import FeedbackView from "../views/FeedbackView.vue";
import PrizeApplicationView from "../views/PrizeApplicationView.vue";
import ActivityView from "../views/ActivityView.vue";
import VoteRecordView from "../views/VoteRecordView.vue";
import PaymentRecordView from "../views/PaymentRecordView.vue";
import VoteParentView from "../views/VoteParentView.vue";
import PrizeView from "../views/PrizeView.vue";

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
  // 投票记录
  {
    path: "/vote/voterecord",
    name: "VoteRecordView",
    component: VoteRecordView,
  },
  // 礼物管理
  {
    path: "/vote/prize",
    name: "PrizeView",
    component: PrizeView,
  },
  // 支付
  {
    path: "/order/paymentrecord",
    name: "PaymentRecordView",
    component: PaymentRecordView,
  },
  // 选手
  {
    path: "/parent/voteparent",
    name: "VoteParentView",
    component: VoteParentView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
