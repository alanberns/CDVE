import { createRouter, createWebHistory } from "vue-router";

// Componentes
import Home from "./components/Home.vue";
import Disciplinas from "./components/Disciplinas.vue";
import Usuario from "./components/Usuario.vue";
import Login from "./components/Login.vue";
import ListPagos from "./components/ListPagos.vue";
import SociosPorDisciplina from "./components/SociosPorDisciplina.vue";

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
  {
    path: "/pagos",
    component: ListPagos,
  },
  {
    path: "/statistics/sociosPorDisciplina",
    component: SociosPorDisciplina,
  }
];

// crear objeto rutas
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
