import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AuthView from "../views/AuthView.vue";
import System from "../views/system.vue";
import News from "../views/news.vue";
import Vote from "../views/Vote.vue";
import Order from "../views/Order.vue";
import Vermicelli from "../views/Vermicelli.vue";
import Assignment from "../views/Assignment.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/auth",
    name: "auth",
    component: AuthView,
  },
  {
    path: "/system",
    name: "system",
    component: System,
  },
  {
    path: "/news",
    name: "news",
    component: News,
  },
  {
    path: "/vote",
    name: "vote",
    component: Vote,
  },
  {
    path: "/order",
    name: "order",
    component: Order,
  },
  {
    path: "/vermicelli",
    name: "vermicelli",
    component: Vermicelli,
  },
  {
    path: "/assignment",
    name: "assignment",
    component: Assignment,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
