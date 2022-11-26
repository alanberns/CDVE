import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "materialize-css/dist/css/materialize.min.css";
import "material-design-icons-iconfont";
import { pinia } from "./persistStore";
import Select2 from "vue3-select2-component";

createApp(App)
  .component("Select2", Select2)
  .use(router)
  .use(pinia)
  .mount("#app");
