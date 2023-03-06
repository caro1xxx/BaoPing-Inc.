import { createRouter, createWebHistory } from "vue-router";
import TemplateOneView from "../views/TemplateOneView.vue";
import TemplateTwoView from '../views/TemplateTwoView.vue'

const routes = [
  {
    path: "/one",
    name: "TemplateOneView",
    component: TemplateOneView,
  },
  {
    path: "/two",
    name: "TemplateTwoView",
    component: TemplateTwoView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
