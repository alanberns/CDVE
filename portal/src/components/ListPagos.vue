<template>
  <div>
    <br /><br />
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
  </div>
</template>

<script>
import { apiService } from "../apiService";
export default {
  name: "ListPagos",
  data() {
    return {
      pagos: [],
    };
  },
  created() {
    apiService
      .get("/me/payments", {
        headers: {
          Authorization: `${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.pagos = response.data.payments;
        console.log(response.data);
      })
      .catch((error) => console.log(error));
  },
};
</script>

<style></style>
