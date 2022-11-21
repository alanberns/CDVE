<template>
  <div id="app">
    <navbarComponent></navbarComponent>
    <router-view></router-view>
  </div>
</template>

<script>
import NavbarComponent from "./components/navbar.vue";
export default {
  name: "App",
  components: {
    NavbarComponent,
  },
};
</script>

<style>

</style>
