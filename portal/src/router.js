import { createRouter, createWebHistory } from 'vue-router'

// Componentes
import HelloWorld from './components/HelloWorld.vue'
import Disciplinas from './components/Disciplinas.vue';
import Usuario from './components/Usuario.vue'

// definir objeto rutas
const routes = [
    {
        path: '/',
        name: 'Home',
        component: HelloWorld
    },
    {
        path: '/disciplinas',
        component: Disciplinas
    },
    {
        path: '/user',
        component: Usuario
    }
]

// crear objeto rutas
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router