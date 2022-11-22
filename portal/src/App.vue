<template>
  <div id="app">
    <navbarComponent></navbarComponent>
    <SociosPorDisciplina></SociosPorDisciplina>
    <router-view></router-view>
  </div>
</template>

<script>
import NavbarComponent from "./components/navbar.vue";
import SociosPorDisciplina from "./components/SociosPorDisciplina.vue";
export default {
  name: "App",
  components: {
    NavbarComponent,
    SociosPorDisciplina,
  },
};
</script>

<style>

</style>
