<template>
  <div>
    <form @submit.prevent="submitFile">
      <div class="file-field input-field">
        <div class="btn">
          <span><i class="material-icons">attach_file</i></span>
          <input
            placeholder="Subir Comprobante"
            id="attach_input"
            type="file"
            @change="uploadFile"
            ref="file"
          />
        </div>
        <div class="file-path-wrapper">
          <input :value="fileName" class="file-path validate" type="text" />
        </div>
      </div>
      <button>Upload!</button>
    </form>
  </div>
</template>

<script>
import { apiService } from "../apiService";
import { useLoginStore } from "../stores/LoginStore";
import { useComprobanteStore } from "../stores/ComprobanteStore";
import router from "@/router";
export default {
  name: "SubirArchivo",
  data() {
    return {
      images: null,
      fileName: null,
    };
  },
  setup() {
    const comprobanteStore = useComprobanteStore();
    const loginStore = useLoginStore();
    return { loginStore, comprobanteStore };
  },
  methods: {
    uploadFile(e) {
      console.log(e);
      this.images = this.$refs.file.files[0];
      this.fileName = e.target.files[0].name;
    },
    async submitFile() {
      apiService.defaults.headers[
        "Authorization"
      ] = `${this.loginStore.getToken}`;
      const formData = new FormData();
      formData.append("file", this.images);
      formData.append("id", this.comprobanteStore.idComprobante);
      const headers = {
        "Content-Type": "multipart/form-data",
      };
      console.log(formData);
      await apiService
        .post("/me/comprobante", formData, {
          headers: headers,
        })
        .then((res) => {
          res.data.files; // binary representation of the file
          res.status; // HTTP status
          this.comprobanteStore.message = "Hemos recibido su comprobante";
        })
        .catch((error) => {
          console.log(error);
          this.comprobanteStore.message =
            "No pudimos recibir su comprobante, asegure que el formato sea jpg,png o pdf";
        });
      router.push("/pagos");
    },
  },
};
</script>

<style></style>
