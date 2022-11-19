import { createRouter, createWebHistory } from "vue-router";

// Componentes
import HelloWorld from "./components/HelloWorld.vue";
import Disciplinas from "./components/Disciplinas.vue";
import Usuario from "./components/Usuario.vue";
import Login from "./components/Login.vue";
import ListPagos from "./components/ListPagos.vue";
// definir objeto rutas
const routes = [
  {
    path: "/",
    name: "Home",
    component: HelloWorld,
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
  {
    path: "/pagos",
    component: ListPagos,
  },
];

// crear objeto rutas
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
