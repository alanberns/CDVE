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
            <router-link to="/user">Perfil</router-link>
          </li>
          <!-- <li><router-link to="/login">Login</router-link></li> -->
          <li v-if="loginStore.isAuthenticated && configStore.showListPagos">
            <router-link to="/pagos">Pagos</router-link>
          </li>
          <li v-if="loginStore.isAuthenticated">
            <router-link to="/pagar">Pagar</router-link>
          </li>
        </ul>
        <ul id="nav-mobile2" class="right left hide-on-med-and-down">
          <li v-if="loginStore.isAuthenticated">
            <i class="material-icons">perm_identity</i>
          </li>
          <li v-if="loginStore.isAuthenticated">
            {{usuario}}
          </li>
          <li>
            <LoginButton></LoginButton>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
import { useLoginStore } from "../stores/LoginStore";
import { useConfigStore } from "../stores/ConfigStore";
import LoginButton from "./LoginButton.vue";
export default {
  name: "NavbarComponent",
  components: {
    LoginButton,
  },
  data() {
    return {
      usuario: "",
    }
  },
  setup() {
    const loginStore = useLoginStore();
    const configStore = useConfigStore();
    return { loginStore, configStore };
  },
  mounted() {
    this.usuario = this.loginStore.usuario
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
