import { createRouter, createWebHistory } from "vue-router";

// Componentes
import Home from "./components/Home.vue";
import Disciplinas from "./components/Disciplinas.vue";
import Usuario from "./components/Usuario.vue";
import Login from "./components/Login.vue";
import ListPagos from "./components/ListPagos.vue";
import SociosPorDisciplina from "./components/SociosPorDisciplina.vue";
import Genero from "./components/Genero.vue";
import Concurrencia from "./components/Concurrencia.vue";
import SubirComprobante from "./components/SubirComprobante";
import GenerarPago from "./components/GenerarPago.vue";
import ShowComprobante from "./components/ShowComprobante.vue";
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
    path: "/pagar",
    component: GenerarPago,
  },
  {
    path: "/statistics/sociosPorDisciplina",
    component: SociosPorDisciplina,
  },
  {
    path: "/statistics/genero",
    component: Genero,
  },
  {
    path: "/statistics/concurrencia",
    component: Concurrencia,
  },
  {
    path: "/comprobante",
    component: SubirComprobante,
  },
  {
    path: "/comprobante/show",
    component: ShowComprobante,
  },
];

// crear objeto rutas
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
