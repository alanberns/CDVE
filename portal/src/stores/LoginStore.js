import { defineStore } from "pinia";

export const useLoginStore = defineStore("loginStore", {
  state: () => ({
    isAuthenticated: false,
    token: null,
  }),
  actions: {
    signIn(token) {
      (this.token = token), (this.isAuthenticated = true);
    },
  },
});
