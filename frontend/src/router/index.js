import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import GameList from "../views/GameList.vue";
import Admin from "../views/Admin.vue";
import AdminLogin from "../views/AdminLogin.vue";
import Notice from "../views/Notice.vue";
import Post from "../views/Post.vue";

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
    path: "/admin",
    name: "admin",
    component: Admin,
  },
  {
    path: "/adminLogin",
    name: "adminLogin",
    component: AdminLogin,
  },
  {
    path: "/notice",
    name: "notice",
    component: Notice,
  },
  {
    path: "/post",
    name: "post",
    component: Post,
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
