<template>
    <div class="navbar-fixed">
      <nav>
        <div class="nav-wrapper blue-grey darken-4">
          <a
            href="#"
            class="brand-logo right"
            v-if="loginStore.isAuthenticated"
            @click="loginStore.logOut"
            >Cerrar Sesion</a
          >
          <ul id="nav-mobile" class="left hide-on-med-and-down">
            <li><router-link to="/"><strong>Home</strong></router-link></li>
            <li><router-link to="/disciplinas">Disciplinas</router-link></li>
            <li><router-link to="/user">User</router-link></li>
            <li><router-link to="/login">Login</router-link></li>
            <li><router-link to="/pagos">Pagos</router-link></li>
          </ul>
        </div>
      </nav>
    </div>
  </template>
  
  <script>
  import { useLoginStore } from "@/stores/LoginStore";
  
  export default {
    name: "NavbarComponent",
    setup() {
      const loginStore = useLoginStore();
      return { loginStore };
    },
  };
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .navbar-fixed {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
  }
  </style>
  