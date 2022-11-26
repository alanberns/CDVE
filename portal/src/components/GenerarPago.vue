<template>
  <br />
  <div class="container modal-vue">
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
    <SubirArchivo v-if="!selected"></SubirArchivo>
  </div>
</template>

<script>
import SubirArchivo from "./SubirArchivo.vue";
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
    };
  },
  setup() {
    const cuotaPickedStore = useCuotaPickedStore();
    return { cuotaPickedStore };
  },
  mounted() {
    this.getDisciplinas();
  },
  components: {
    SubirArchivo,
    ListCuotas,
    ModalPago,
  },
  methods: {
    mySelectEvent(e) {
      this.cuotaPickedStore.resetCuotasSelected();
      this.selected = e.text;
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
          console.log(data);
          Object.values(data).forEach((item) => this.cuotas.push(item));
          this.has_cuotas = this.cuotas.length > 0 ? true : false;
        })
        .catch((error) => console.log(error));
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
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style></style>
