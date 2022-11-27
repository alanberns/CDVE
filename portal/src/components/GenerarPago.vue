<template>
  <br />
  <div class="container modal-vue">
    <h2>Pago de Disciplinas</h2>
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <div class="row valign-wrapper">
      <div class="col l6">
        <p class="flow-text">Seleccione la disciplina que desea pagar</p>
      </div>
      <div class="col l6">
        <Select2
          v-model="selected"
          :options="myOptions"
          :settings="{ width: '50%' }"
          @select="mySelectEvent($event)"
        />
      </div>
    </div>
    <div class="row valign-wrapper">
      <p v-if="!has_cuotas && has_cuotas != null" class="flow-text">
        No hay cuotas para pagar
      </p>
      <ListCuotas v-else-if="has_cuotas" :cuotas="cuotas"></ListCuotas>
    </div>
    <ModalPago v-if="has_cuotas"></ModalPago>
  </div>
</template>

<script>
import ListCuotas from "./ListCuotas.vue";
import { apiService } from "../apiService";
import { useCuotaPickedStore } from "../stores/CuotaPickedStore";
import ModalPago from "./ModalPago.vue";

export default {
  name: "ImportarPago",
  data() {
    return {
      myOptions: [],
      selected: null,
      cuotas: [],
      has_cuotas: null,
      loading: true,
    };
  },
  setup() {
    const cuotaPickedStore = useCuotaPickedStore();
    return { cuotaPickedStore };
  },
  mounted() {
    this.getDisciplinas();
  },
  // beforeUnmount() {
  //   this.cuotaPickedStore.resetDisciplina();
  // },
  components: {
    ListCuotas,
    ModalPago,
  },
  methods: {
    mySelectEvent(e) {
      this.cuotaPickedStore.resetCuotasSelected();
      this.selected = e.text;
      this.cuotaPickedStore.setDisciplina(this.selected);
      this.getCuotas();
    },
    async getCuotas() {
      await apiService
        .get("/me/cuotas", {
          params: {
            disciplina: this.selected,
          },
          headers: {
            Authorization: `${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          this.cuotas = [];
          const data = response.data.cuotas;
          Object.values(data).forEach((item) => this.cuotas.push(item));
          this.has_cuotas = this.cuotas.length > 0 ? true : false;
          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
        });
    },
    async getDisciplinas() {
      await apiService
        .get("/me/disciplines", {
          headers: {
            Authorization: `${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          const data = response.data.data;
          Object.values(data).forEach((item) => this.myOptions.push(item.name));
          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
        });
    },
  },
};
</script>

<style>
.modal-vue {
  margin-bottom: 1rem;
}
</style>
