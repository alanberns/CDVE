<template>
  <div id="app" style="position: relative; min-height: 100vh;">
    <br />
    <NavbarComponent></NavbarComponent>
    <br />
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
import NavbarComponent from "./components/navbar.vue";
import Footer from "./components/Footer.vue";
export default {
  name: "App",
  components: {
    NavbarComponent,
    Footer,
  },
};
</script>

<style></style>
