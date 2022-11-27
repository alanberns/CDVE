<template>
  <br />
  <div class="container">
    <SubirArchivo></SubirArchivo>
  </div>
</template>

<script>
import SubirArchivo from "./SubirArchivo.vue";
import { useComprobanteStore } from "../stores/ComprobanteStore";
export default {
  name: "SubirComprobante",
  data() {
    return {};
  },
  setup() {
    const comprobanteStore = useComprobanteStore();
    return { comprobanteStore };
  },
  beforeUnmount() {
    this.comprobanteStore.idComprobante = null;
  },
  components: {
    SubirArchivo,
  },
  methods: {},
};
</script>

<style></style>
