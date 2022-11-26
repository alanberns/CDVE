<template>
  <table class="responsive-table centered highlight">
    <thead>
      <tr>
        <th>Numero de Cuota</th>
        <th>Fecha</th>
        <th>Monto</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <RowCuotas
        v-for="cuota in cuotas"
        :key="cuota.id"
        :cuota="cuota"
      ></RowCuotas>
    </tbody>
  </table>
</template>

<script>
import RowCuotas from "./RowCuotas.vue";
export default {
  name: "ListCuotas",
  props: ["cuotas"],
  methods: {},
  components: {
    RowCuotas,
  },
};
</script>

<style></style>
