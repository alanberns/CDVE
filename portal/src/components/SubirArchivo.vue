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
          <input class="file-path validate" type="text" />
        </div>
      </div>
      <button>Upload!</button>
    </form>
  </div>
</template>

<script>
import { apiService } from "../apiService";
import { useLoginStore } from "../stores/LoginStore";
export default {
  name: "SubirArchivo",
  data() {
    return {};
  },
  setup() {
    const loginStore = useLoginStore();
    return { loginStore };
  },
  methods: {
    uploadFile() {
      this.Images = this.$refs.file.files[0];
    },
    submitFile() {
      apiService.defaults.headers[
        "Authorization"
      ] = `${this.loginStore.getToken}`;
      const formData = new FormData();
      formData.append("file", this.Images);
      const headers = {
        "Content-Type": "multipart/form-data",
      };
      console.log(formData);
      apiService
        .post("/me/comprobante", formData, {
          headers: headers,
        })
        .then((res) => {
          res.data.files; // binary representation of the file
          res.status; // HTTP status
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style></style>
