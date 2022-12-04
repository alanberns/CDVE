import { defineStore } from "pinia";

export const useComprobanteStore = defineStore("comprobanteStore", {
  state: () => ({
    idComprobante: null,
    message: null,
  }),
  actions: {},
  getters: {},
});
