<template>
  <br />
  <div class="container">
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

    <SubirArchivo v-if="selected"></SubirArchivo>
  </div>
</template>

<script>
import SubirArchivo from "./SubirArchivo.vue";
import { apiService } from "../apiService";

export default {
  name: "ImportarPago",
  data() {
    return {
      myOptions: [],
      selected: null,
    };
  },
  mounted() {
    this.getDisciplinas();
  },
  components: {
    SubirArchivo,
  },
  methods: {
    mySelectEvent(e) {
      this.selected = e.text;
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
