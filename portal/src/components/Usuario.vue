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
    import axios from "axios";
    export default {
    name: "Usuario",
    data() {
        return {
        user_info: [],
        };
    },
    created() {
        let url = "http://127.0.0.1:5000/api/me/profile";

        axios
        .get(url)
        .then((response => (this.user_info = response.data)))
        .catch((error) => console.log(error));
    },
    };
</script>

<style></style>