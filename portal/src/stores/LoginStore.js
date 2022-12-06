import { defineStore } from "pinia";
import router from "../router";
export const useLoginStore = defineStore("loginStore", {
  state: () => ({
    isAuthenticated: false,
    token: null,
    tokenExpired: false,
    usuario: "",
  }),
  actions: {
    logOut() {
      localStorage.removeItem("token");
      this.token = null;
      this.isAuthenticated = false;
      this.usuario = "";
      router.push("/login");
    },
    signIn(token,usuario) {
      this.token = token;
      this.isAuthenticated = true;
      this.tokenExpired = false;
      this.usuario = usuario;
    },
    setTokenExpired(value) {
      this.tokenExpired = value;
    },
  },
  getters: {
    getToken: (state) => state.token,
  },
});
