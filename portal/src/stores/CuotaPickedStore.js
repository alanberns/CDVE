import { defineStore } from "pinia";

export const useCuotaPickedStore = defineStore("cuotaPickedStore", {
  state: () => ({
    cuotas: [],
  }),
  actions: {
    addCuota(cuota) {
      this.cuotas.push(cuota);
    },
    removeCuota(cuota) {
      const index = this.cuotas.indexOf(cuota);
      if (index > -1) {
        this.cuotas.splice(index, 1); // 2nd parameter means remove one item only
      }
    },
    resetCuotasSelected() {
      this.cuotas = [];
    },
  },
  getters: {
    getCuotas: (state) => state.cuotas,
    getMontoTotal: (state) =>
      state.cuotas.reduce((acc, cuota) => acc + cuota.monto, 0),
  },
});
