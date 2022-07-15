import { createRouter, createWebHistory } from "vue-router";
import NewFlow from "../views/NewFlow.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: NewFlow,
    },
  ],
});

export default router;
