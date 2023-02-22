import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
<<<<<<< HEAD
import RegisterView from "../views/RegisterView.vue";
=======
import System from '../views/system.vue'
import News from '../views/news.vue'
import Vote from '../views/Vote.vue'
import Order from '../views/Order.vue'
import Vermicelli from '../views/Vermicelli.vue'
import Assignment from '../views/Assignment.vue'


>>>>>>> 571ea31b028318ae3140b40c58bf103581891cb3

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
<<<<<<< HEAD
    path: "/register",
    name: "register",
    component: RegisterView,
  },
=======
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
  
>>>>>>> 571ea31b028318ae3140b40c58bf103581891cb3
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
