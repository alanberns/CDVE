<template>
  <h1>Nuestras disciplinas</h1>
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
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Disciplinas",
  data() {
    return {
      disciplinas: [],
    };
  },
  created() {
    let url = "http://127.0.0.1:5000/api/club/disciplines";

    axios
      .get(url)
      .then((response) => (this.disciplinas = response.data))
      .catch((error) => console.log(error));
  },
};
</script>

<style>
</style>
