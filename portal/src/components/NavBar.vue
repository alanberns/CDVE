<template>
  <nav>
    <div class="nav-wrapper black">
      <router-link to="/">Home</router-link>
      <ul id="nav-mobile" class="right ">
        <li v-if="HayUser"><router-link to="/disciplinas">Disciplinas</router-link></li>
        <li v-if="HayUser"><router-link to="/user">User</router-link></li>
        <li v-if="!HayUser"><router-link to="/login">Login</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
    name: "NavBar",
    HayUser: false,
    }
</script>