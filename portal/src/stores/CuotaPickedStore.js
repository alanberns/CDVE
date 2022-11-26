import { defineStore } from "pinia";

export const useCuotaPickedStore = defineStore("cuotaPickedStore", {
  state: () => ({
    cuotasSelected: [],
  }),
  actions: {
    addCuota(nro_cuota) {
      this.cuotasSelected.push(nro_cuota);
    },
    removeCuota(nro_cuota) {
      const index = this.cuotasSelected.indexOf(nro_cuota);
      if (index > -1) {
        this.cuotasSelected.splice(index, 1); // 2nd parameter means remove one item only
      }
    },
    resetCuotasSelected() {
      this.cuotasSelected = [];
    },
  },
  getters: {
    getCuotas: (state) => state.cuotasSelected,
  },
});
