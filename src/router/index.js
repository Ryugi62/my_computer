import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import GameList from "../views/GameList.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/gameList",
    name: "gameList",
    component: GameList,
  },
  {
    path: "/:catchAll(.*)",
    name: "notFound",
    component: Home,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
