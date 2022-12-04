<template>
  <h2>Subir un comprobante de pago</h2>
  <div class="container">
    <SubirArchivo></SubirArchivo>
  </div>
  <br>
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
