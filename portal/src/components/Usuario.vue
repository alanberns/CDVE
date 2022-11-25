<template>
    <div>
        <br><br>
        <table class="responsive-table centered highlight ">
            <thead>
                <tr>
                    <th>N° SOCIO</th>
                    <th>NOMBRE DE USUARIO</th>
                    <th>NOMBRE</th>
                    <th>APELLIDO</th>
                    <th>EMAIL</th>
                    <th>TIPO DOCUMENTO</th>
                    <th>N° DOCUMENTO</th>
                    <th>GENERO</th>
                    <th>TELEFONO</th>
                    <th>DIRECCIÓN</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{user_info.number}}</td>
                    <td>{{usern_info.first_name}}</td>
                    <td>{{user_info.last_name}}</td>
                    <td>{{ user_info.user }}</td>
                    <td>{{ user_info.email }}</td>
                    <td>{{user_info.document_type}}</td>
                    <td>{{user_info.document_number}}</td>
                    <td>{{user_info.gender}}</td>
                    <td>{{user_info.phone}}</td>
                    <td>{{user_info.address}}</td>
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