import axios from "axios";
import { useLoginStore } from ".//stores/LoginStore.js";

const apiService = axios.create({
  baseURL: "http://localhost:5000/api",
});

// Response interceptor for API calls
apiService.interceptors.response.use(
  (response) => {
    return response;
  },
  async function (error) {
    // const originalRequest = error.config;
    const loginStore = useLoginStore();
    if (error.response.status === 401) {
      loginStore.logOut();
      loginStore.setTokenExpired(true);
    }
    return Promise.reject(error);
  }
);
export { apiService };
