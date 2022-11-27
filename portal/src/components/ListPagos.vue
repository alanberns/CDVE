<template>
  <div>
    <br />
    <p
      class="center-align flow-text pago-confirm-message"
      v-if="cuotaPickedStore.pagoIsConfirmed"
    >
      Su pago fue realizado con exito
    </p>
    <table class="responsive-table centered highlight">
      <thead>
        <tr>
          <th>Monto</th>
          <th>Fecha</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="pago in pagos" :key="pago.id">
          <td>{{ pago.monto }}</td>
          <td>{{ pago.fecha }}</td>
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
</template>

<script>
import { apiService } from "../apiService";
import { useCuotaPickedStore } from "../stores/CuotaPickedStore";
export default {
  name: "ListPagos",
  setup() {
    const cuotaPickedStore = useCuotaPickedStore();
    return { cuotaPickedStore };
  },
  data() {
    return {
      pagos: [],
      current_page: 1,
      pages: 1,
    };
  },
  async mounted() {
    await this.nextPage();
  },
  beforeUnmount() {
    this.cuotaPickedStore.pagoIsConfirmed = false;
  },
  methods: {
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
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
.pago-confirm-message {
  color: #2e7d32;
}
</style>
