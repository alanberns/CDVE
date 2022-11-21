import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "materialize-css/dist/css/materialize.min.css";
import "material-design-icons-iconfont";
import { createPinia } from "pinia";

createApp(App).use(router).use(createPinia()).mount("#app");
