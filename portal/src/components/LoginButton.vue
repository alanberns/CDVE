<template>
  <a
    href="#"
    class="waves-effect waves-light btn red darken-2"
    v-if="loginStore.isAuthenticated"
    @click="signOut()"
    >Cerrar Sesion
  </a>
  <router-link
    v-if="!loginStore.isAuthenticated"
    class="waves-effect waves-light btn blue darken-3 valign-wrapper"
    to="/login"
    >Iniciar Sesion</router-link
  >
</template>

<script>
import { useLoginStore } from "../stores/LoginStore";

export default {
  name: "LoginButton",
  setup() {
    const loginStore = useLoginStore();
    return { loginStore };
  },
  methods: {
    signOut() {
      this.loginStore.setTokenExpired(null);
      this.loginStore.logOut();
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
