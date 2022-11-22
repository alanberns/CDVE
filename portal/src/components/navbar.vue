<template>
    <div class="navbar-fixed">
      <nav>
        <div class="nav-wrapper blue-grey darken-4">
          <a href="#" class="brand-logo right"
            ><i class="material-icons right"
              ><i class="material-icons right">account_circle</i></i
            ></a
          >
          <ul id="nav-mobile" class="left hide-on-med-and-down">
            <li><router-link to="/disciplinas">Disciplinas</router-link></li>
            <li><router-link to="/user">User</router-link></li>
            <li><router-link to="/Login">Login</router-link></li>
            <li><router-link to="/pagos">Pagos</router-link></li>
            <li><router-link to="/">Home</router-link></li>
          </ul>
        </div>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: "navbarComponent",
  };
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .navbar-fixed {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
  }
  </style>
  