<template>
    <div>
        <table>
            <thead>
                <tr>
                    <th>NOMBRE</th>
                    <th>EMAIL</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{ user_info.user }}</td>
                    <td>{{ user_info.email }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { apiService } from "../apiService";
export default {
    name: "Usuario",
    data() {
        return {
        user_info: [],
        };
    },
    created() {
        let url = "me/profile";

        apiService
        .get(url, {
        headers: {
          Authorization: `${localStorage.getItem("token")}`,
        },
      })
        .then((response => (this.user_info = response.data)))
        .catch((error) => console.log(error));
    },
    };
</script>

<style></style>