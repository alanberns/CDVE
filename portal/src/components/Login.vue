<template>
  <div class="container center-align">
    <div class="row">
      <form @submit.prevent="login" class="col s12 center-align">
        <div class="row center-align">
          <div class="input-field col s6 center-align">
            <input
              placeholder="Placeholder"
              id="first_name"
              type="text"
              class="validate center-align"
              v-model="user"
            />
            <label for="first_name">Email</label>
          </div>
        </div>
        <div class="row center-align">
          <div class="input-field col s6 center-align">
            <input
              id="password"
              type="password"
              class="validate center-align"
              v-model="password"
            />
            <label for="password">Password</label>
          </div>
        </div>
        <button
          class="btn waves-effect waves-light"
          type="submit"
          name="action"
        >
          Submit
          <i class="material-icons right">send</i>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      info: null,
      user: "",
      password: "",
    };
  },
  methods: {
    async login() {
      await axios
        .post(
          "http://127.0.0.1:5000/api/login",
          {},
          {
            auth: {
              username: this.user,
              password: this.password,
            },
          }
        )
        .then(
          (response) => ((this.info = response.data), console.log(this.info))
        )
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style></style>
