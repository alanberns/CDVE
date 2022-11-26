<template>
  <tr>
    <td hidden>{{ cuota.id }}</td>
    <td>{{ cuota.nro_cuota }}</td>
    <td>{{ cuota.fecha }}</td>
    <td>{{ cuota.monto }}</td>
    <td>
      <form action="#">
        <p>
          <label>
            <input type="checkbox" />
            <span></span>
          </label>
        </p>
      </form>
    </td>
  </tr>
</template>

<script>
export default {
  name: "RowCuotas",
  props: {
    cuota: Object,
  },
  methods: {},
};
</script>

<style></style>
