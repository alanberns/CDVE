<template>
  <div>
    <p class="center-align flow-text" v-if="comprobanteStore.message">
      {{ comprobanteStore.message }}
    </p>
    <h1>Mis pagos</h1>
    <p
      class="center-align flow-text pago-confirm-message"
      v-if="cuotaPickedStore.pagoIsConfirmed"
    >
      Su pago fue realizado con exito
    </p>
    <div v-if="configStore.showListPagos">
      <div v-if="loading" class="progress">
        <div class="indeterminate"></div>
      </div>
      <table class="responsive-table centered highlight">
        <thead>
          <tr>
            <th>Monto</th>
            <th>Fecha</th>
            <th>Comprobante</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="pago in pagos" :key="pago.id">
            <td>{{ pago.monto }}</td>
            <td>{{ formatDate(pago.fecha) }}</td>
            <td v-if="pago.comprobante">
              <button
                @click="showComprobante(pago.id)"
                class="btn waves-effect green accent-4"
              >
                ver<i class="material-icons right">photo_library</i>
              </button>
            </td>
            <td v-else>
              <button
                @click="uploadComprobante(pago.id)"
                class="btn waves-effect red accent-4"
              >
                Subir<i class="material-icons right">cloud_upload</i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="container">
        <ul class="pagination">
          <li
            v-for="page in pages"
            v-bind:key="page"
            v-bind:class="{ active: page == current_page }"
            class="waves-effect"
          >
            <a @click="nextPage(page)" href="#">{{ page }}</a>
          </li>
        </ul>
      </div>
    </div>
    <div v-else>
      <p class="center-align flow-text">
        La tabla de pagos se encuentra deshabilitada por el momento
      </p>
    </div>
  </div>
</template>

<script>
import { apiService } from "../apiService";
import { useCuotaPickedStore } from "../stores/CuotaPickedStore";
import { useComprobanteStore } from "../stores/ComprobanteStore";
import { useConfigStore } from "../stores/ConfigStore";

import router from "@/router";
import moment from "moment";

export default {
  name: "ListPagos",
  setup() {
    const cuotaPickedStore = useCuotaPickedStore();
    const comprobanteStore = useComprobanteStore();
    const configStore = useConfigStore();
    return { cuotaPickedStore, comprobanteStore, configStore };
  },
  data() {
    return {
      pagos: [],
      current_page: 1,
      pages: 1,
      loading: true,
    };
  },
  async mounted() {
    await this.getConfig();
    await this.nextPage();
  },
  beforeUnmount() {
    this.cuotaPickedStore.pagoIsConfirmed = false;
    this.comprobanteStore.message = null;
  },
  methods: {
    formatDate(value) {
      return moment(value).format("DD-MM-YYYY");
    },
    uploadComprobante(idComprobante) {
      this.comprobanteStore.idComprobante = idComprobante;
      router.push("/comprobante");
    },
    showComprobante(idComprobante) {
      this.comprobanteStore.idComprobante = idComprobante;
      router.push("/comprobante/show");
    },
    async nextPage(page) {
      page = page || this.current_page;
      apiService
        .get("/me/payments", {
          params: {
            page: page,
          },
          headers: {
            Authorization: `${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          this.pagos = response.data.payments;
          this.pages = response.data.pages;
          this.current_page = response.data.current_page;
          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
        });
      router.push("/pagos");
    },
    async getConfig() {
      let url = "club/config";
      apiService
        .get(url)
        .then((response) => (this.configStore.config = response.data))
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.pago-confirm-message {
  color: #2e7d32;
}
.check-icon {
  color: #2e7d32;
}
.comprobante-done {
  display: flex;
  justify-content: center;
}
</style>
