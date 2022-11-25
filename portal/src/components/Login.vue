<template>
  <div class="container">
    <p
      class="center-align flow-text token-expired-message"
      v-if="loginStore.tokenExpired"
    >
      Token expirado, por favor inicie sesion nuevamente
    </p>
    <div class="row">
      <form
        @submit.prevent="login"
        class="col s12 m8 l8 offset-l2 offset-m4 m4 offset-s3 s6"
      >
        <div class="row">
          <h3>Iniciar Sesion</h3>
        </div>
        <div class="row">
          <div class="input-field">
            <input
              id="first_name"
              type="text"
              class="validate center-align"
              v-model="user"
            />
            <label for="first_name">Email</label>
          </div>
        </div>
        <div class="row">
          <div class="input-field">
            <input
              id="password"
              type="password"
              class="validate center-align"
              v-model="password"
            />
            <label for="password">Contraseña</label>
          </div>
        </div>
        <div class="row">
          <button
            class="btn waves-effect waves-light"
            type="submit"
            name="action"
          >
            Iniciar Sesion
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import router from "@/router";
import { apiService } from "../apiService";
import { useLoginStore } from "../stores/LoginStore.js";

export default {
  name: "Login",
  setup() {
    const loginStore = useLoginStore();
    return { loginStore };
  },
  data() {
    return {
      info: null,
      user: "",
      password: "",
    };
  },
  methods: {
    async login() {
      await apiService
        .post(
          "/login",
          {},
          {
            auth: {
              username: this.user,
              password: this.password,
            },
          }
        )
        .then((response) => {
          localStorage.setItem("token", response.data.token);
          this.loginStore.signIn(response.data.token);
        })
        .catch((error) => console.log(error));
      router.push("/pagos");
    },
  },
};
</script>

<style>
.token-expired-message {
  color: #d50000;
}
</style>
