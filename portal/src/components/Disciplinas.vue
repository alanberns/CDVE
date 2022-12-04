<template>
  <h1>Nuestras disciplinas</h1>
  <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
  <div>
    <table class="striped centered highlight">
      <thead>
        <tr>
          <th>NOMBRE</th>
          <th>CATEGORIA</th>
          <th>DIA</th>
          <th>HORA</th>
          <th>VALOR</th>
          <th>PROFESOR</th>
        </tr>
      </thead>
      <tbody>
          <tr v-for="disciplina in disciplinas" :key="disciplina.id">
            <td>{{ disciplina.name }}</td>
            <td>{{ disciplina.categoria }}</td>
            <td>{{disciplina.days}}</td>
            <td>{{disciplina.time}}</td>
            <td>{{disciplina.costo_mensual}}</td>
            <td>{{disciplina.teacher}}</td>
        </tr>
      </tbody>
    </table>
    <div class="container">
      <ul class="pagination">
        <li
          v-for="page in pages"
          v-bind:key="page"
          v-bind:class="{ active: page == current_page }"
          class="waves-effect"
        >
          <a @click="nextPage(page)" href="#">{{ page }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { apiService } from "../apiService";
export default {
  name: "Disciplinas",
  data() {
    return {
      disciplinas: [],
      current_page: 1,
      pages: 1,
      loading:true,
    };
  },
  async mounted() {
    await this.nextPage();
  },
  methods: {
    async nextPage(page) {
      let url = "club/disciplines";
      page = page || this.current_page;
      apiService
        .get(url, {
        params: {
            page: page,
          },
        })    
        .then((response) => {
          this.disciplinas = response.data.data
          this.pages = response.data.pages;
          this.current_page = response.data.current_page;
          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
        });
    },
  }
};
</script>

<style>
</style>
