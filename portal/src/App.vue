<template>
  <div id="app">
    <navbarComponent></navbarComponent>
    <router-view></router-view>
  </div>
</template>

<script>
import navbarComponent from "./components/navbar.vue";
export default {
  name: "App",
  components: {
    navbarComponent,
  },
};
</script>

<style>

</style>
