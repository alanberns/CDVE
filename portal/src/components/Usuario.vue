<template>
    <section id="mis datos">
      <h1>Mis datos</h1>  
      <div v-if="loading" class="progress">
        <div class="indeterminate"></div>
      </div>  
        <ul class="collection">
          <li class="collection-item"><strong>Numero de socio:</strong> {{ user_info.number }}</li>
          <li class="collection-item"><strong>Nombre:</strong> {{user_info.first_name}} {{ user_info.last_name }}</li>
          <li class="collection-item"><strong>Nombre de usuario:</strong> {{ user_info.user }}</li>
          <li class="collection-item"><strong>Email:</strong> {{ user_info.email }}</li>
          <li class="collection-item"><strong>Tipo de documento:</strong> {{ user_info.document_type }}</li>
          <li class="collection-item"><strong>Numero de documento:</strong> {{ user_info.document_number }}</li>
          <li class="collection-item"><strong>Género:</strong> {{ user_info.gender }}</li>
          <li class="collection-item"><strong>Teléfono:</strong> {{ user_info.phone }}</li>
          <li class="collection-item"><strong>Dirección:</strong> {{ user_info.address }}</li>
          <li class="collection-item"><strong>Estado:</strong> {{ estado }}</li>
        </ul>
    </section>
    <br>
</template>

<script>
import { apiService } from "../apiService";
export default {
  name: "Usuario",
  data() {
    return {
      user_info: [],
      loading: true,
    };
  },
  created() {
    let url = "me/license";

    apiService
      .get(url, {
        headers: {
          Authorization: `${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.user_info = response.data.profile;
        this.estado = response.data.description;
        this.loading = false;
      })
      .catch((error) => {
          console.log(error);
          this.loading = false;
        });
  },
};
</script>

<style></style>
