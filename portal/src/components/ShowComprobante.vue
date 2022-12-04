<template>
  <div class="container">
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <h1>Comprobante</h1>
    <img
      class="materialboxed main-image"
      :src="comprobante"
      alt="instruments"
    />
  </div>
</template>

<script>
import { apiService } from "../apiService";
import { useComprobanteStore } from "../stores/ComprobanteStore";
export default {
  name: "ShowComprobante",
  data() {
    return {
      comprobante: null,
      loading: true,
    };
  },
  setup() {
    const comprobanteStore = useComprobanteStore();
    return { comprobanteStore };
  },
  created() {
    this.getImage();
  },
  unmounted() {
    this.comprobanteStore.idComprobante = null;
  },
  methods: {
    async getImage() {
      let url = "me/comprobante";

      await apiService
        .get(url, {
          params: {
            id: this.comprobanteStore.idComprobante,
          },
          headers: {
            Authorization: `${localStorage.getItem("token")}`,
          },
          responseType: "blob",
        })
        .then((response) => {
          const urlCreator = window.URL || window.webkitURL;
          this.comprobante = urlCreator.createObjectURL(response.data);
          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
        });
    },
  },
};
</script>

<style>
.main-image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 40%;
}
</style>
