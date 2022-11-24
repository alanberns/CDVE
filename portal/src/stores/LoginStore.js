import { defineStore } from "pinia";
import router from "../router";
export const useLoginStore = defineStore("loginStore", {
  state: () => ({
    isAuthenticated: false,
    token: null,
    tokenExpired: false,
  }),
  actions: {
    logOut() {
      localStorage.removeItem("token");
      this.token = null;
      this.isAuthenticated = false;
      router.push("/login");
    },
    signIn(token) {
      this.token = token;
      this.isAuthenticated = true;
      this.tokenExpired = false;
    },
    setTokenExpired(value) {
      this.tokenExpired = value;
    },
  },
});
