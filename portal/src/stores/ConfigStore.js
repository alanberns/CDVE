import { defineStore } from "pinia";

export const useConfigStore = defineStore("configStore", {
  state: () => ({
    config: [],
  }),
  actions: {},
  getters: {},
});
