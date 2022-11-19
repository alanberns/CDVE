import { createRouter, createWebHistory } from "vue-router";

// Componentes
import Home from "@/components/Home.vue";
import Disciplinas from "@/components/Disciplinas.vue";
import Usuario from "@/components/Usuario.vue";
import Login from "@/components/Login.vue";
// definir objeto rutas
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/disciplinas",
    component: Disciplinas,
  },
  {
    path: "/user",
    component: Usuario,
  },
  {
    path: "/login",
    component: Login,
  },
];

// crear objeto rutas
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
