<template>
    <h1>{{club_info.info.email}}</h1>
    <h2>{{club_info.info.phone}}</h2>
</template>

<script>
import axios from "axios";
    export default {
    name: "InfoClub",
    data() {
        return {
        club_info: [],
        };
    },
    created() {
        let url = "http://127.0.0.1:5000/api/club/info";

        axios
        .get(url)
        .then((response => (this.club_info = response.data)))
        .catch((error) => console.log(error));
    },
    };
</script>