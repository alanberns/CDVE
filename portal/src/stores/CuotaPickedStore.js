import { defineStore } from "pinia";

export const useCuotaPickedStore = defineStore("cuotaPickedStore", {
  state: () => ({
    cuotas: [],
    disciplina: null,
    pagoIsConfirmed: null,
  }),
  actions: {
    addCuota(cuota) {
      this.cuotas.push(cuota);
    },
    setDisciplina(nombre_disciplina) {
      this.disciplina = nombre_disciplina;
    },
    resetDisciplina() {
      this.disciplina = null;
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
