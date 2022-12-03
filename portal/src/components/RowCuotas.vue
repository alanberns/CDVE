<template>
  <tr>
    <td>{{ cuota.nro_cuota }}</td>
    <td>{{ formatDate(cuota.fecha) }}</td>
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
import moment from "moment";
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
    formatDate(value) {
      return moment(value).format("DD-MM-YYYY");
    },
    check() {
      this.$nextTick(() => {
        if (this.checkedCuotas) {
          this.cuotaPickedStore.addCuota(this.cuota);
        } else {
          this.cuotaPickedStore.removeCuota(this.cuota);
        }
      });
    },
  },
};
</script>

<style></style>
