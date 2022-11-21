<template>
  <div>
    <table>
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
import axios from "axios";
export default {
  name: "ListPagos",
  data() {
    return {
      pagos: [],
    };
  },
  created() {
    let url = "http://127.0.0.1:5000/api/me/payments";
    axios
      .get(url, {
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
