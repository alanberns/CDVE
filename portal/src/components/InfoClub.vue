<template>
    <section id="infoClub">
        <div class="row">
            <div class="col s12 m6">
            <div class="card grey darken-1">
                <div class="card-content white-text">
                <span class="card-title">Bienvenidos a la página del Club Deportivo Villa Elisa</span>
                </div>
                <div class="card-action grey">Contactanos
                <p><i class="material-icons left">email</i>{{club_info.email}}</p>
                <p><i class="material-icons left">phone</i>{{club_info.phone}}</p>
                </div>
            </div>
            </div>
        </div>
    </section>

    <section id="Disciplinas">
        <div class="row">
            <div class="col s12 m6">
            <div class="card grey darken-1">
                <div class="card-content white-text">
                <span class="card-title">Conoce nuestras disciplinas</span>
                </div>
                <div class="card-action grey">
                <router-link to="/disciplinas"><button>Ver más</button></router-link>
                </div>
            </div>
            </div>
        </div>
    </section>

    <section id="Estadisticas">
        <div class="row">
            <div class="col s12 m6">
            <div class="card grey darken-1">
                <div class="card-content white-text">
                <span class="card-title">Estadisticas de nuestro club</span>
                </div>
                <div class="card-action grey">
                <router-link to="/statistics/sociosPorDisciplina"><button>Inscriptos por disciplina</button></router-link>
                </div>
            </div>
            </div>
        </div>
    </section>

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
            .then(response => this.club_info = response.data.info);
    },
    };
</script>
