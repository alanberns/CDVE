import { defineStore } from "pinia";

export const useConfigStore = defineStore("configStore", {
  state: () => ({
    config: {},
  }),
  actions: {},
  getters: {
    showListPagos(state) {
      return state.config.tabla_pagos;
    },
  },
});
