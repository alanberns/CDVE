<template>
  <div id="app">
    <NavBar>
      <li><router-link to="/user">User</router-link></li>
    </NavBar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
export default {
  name: "App",
  components: {
    NavBar,
  }
};
</script>

<style>

</style>
