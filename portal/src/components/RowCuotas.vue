<template>
  <tr>
    <td>{{ cuota.nro_cuota }}</td>
    <td>{{ cuota.fecha }}</td>
    <td>{{ cuota.monto }}</td>
    <td>
      <form action="#">
        <p>
          <label>
            <input
              type="checkbox"
              :value="cuota.nro_cuota"
              v-model="checkedCuotas"
              @change="check($event)"
            />
            <span></span>
          </label>
        </p>
      </form>
    </td>
  </tr>
</template>

<script>
import { useCuotaPickedStore } from "../stores/CuotaPickedStore";

export default {
  name: "RowCuotas",
  data() {
    return {
      checkedCuotas: null,
    };
  },
  setup() {
    const cuotaPickedStore = useCuotaPickedStore();
    return { cuotaPickedStore };
  },
  props: {
    cuota: Object,
  },
  methods: {
    check(e) {
      this.$nextTick(() => {
        if (this.checkedCuotas) {
          this.cuotaPickedStore.addCuota(e.target.value);
        } else {
          this.cuotaPickedStore.removeCuota(e.target.value);
        }
      });
    },
  },
};
</script>

<style></style>
