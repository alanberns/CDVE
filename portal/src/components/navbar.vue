<template>
  <div class="navbar-fixed">
    <nav>
      <div class="nav-wrapper blue-grey darken-4">
        <ul id="nav-mobile" class="left hide-on-med-and-down">
          <li>
            <router-link to="/"><strong>Home</strong></router-link>
          </li>
          <li><router-link to="/disciplinas">Disciplinas</router-link></li>
          <li v-if="loginStore.isAuthenticated">
            <router-link to="/user">User</router-link>
          </li>
          <!-- <li><router-link to="/login">Login</router-link></li> -->
          <li v-if="loginStore.isAuthenticated">
            <router-link to="/pagos">Pagos</router-link>
          </li>
        </ul>
        <ul id="nav-mobile2" class="right left hide-on-med-and-down">
          <li>
            <a
              href="#"
              class="waves-effect waves-light btn red darken-2"
              v-if="loginStore.isAuthenticated"
              @click="loginStore.logOut"
              >Cerrar Sesion
            </a>
          </li>
          <li v-if="!loginStore.isAuthenticated">
            <router-link
              class="waves-effect waves-light btn blue darken-3 valign-wrapper"
              to="/login"
              >Iniciar Sesion</router-link
            >
          </li>
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
