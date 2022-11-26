<template>
    <section id="bienvenidos">
        <div class="row">
            <div class="col s12 m6">
                <div class="card grey darken-1">
                    <div class="card-content white-text">
                    <span class="card-title"> Bienvenidos ¿Quiénes somos?</span>
                </div>
                    <div class="card-action grey">
                        <span>
                            Somos un club con actividades deportivas, ubicado en Villa Elisa, Partido de La Plata
                        </span>
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
                        <span class="card-title">Conocé nuestras disciplinas</span>
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
                        <router-link to="/statistics/concurrencia"><button>Concurrencia</button></router-link>
                        <router-link to="/statistics/genero"><button>Genero</button></router-link>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="Contactanos">
        <div class="row">
            <div class="col s12 m6">
                <div class="card grey darken-1">
                    <div class="card-content white-text">
                        <span class="card-title">Contactanos</span>
                    </div>
                    <div class="card-action grey">
                        <p><i class="material-icons left">email</i>{{club_info.email}}</p>
                        <p><i class="material-icons left">phone</i>{{club_info.phone}}</p>
                        <p>
                            <i class="material-icons">location_on</i>
                            Camino Parque Centenario y 48, Villa Elisa, Argentina
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

</template>

<script>
import { apiService } from "../apiService";
    export default {
    name: "InfoClub",
    data() {
        return {
        club_info: [],
        };
    },
    created() {
        let url = "club/info";

        apiService
            .get(url)
            .then(response => this.club_info = response.data.info);
    },
    };
</script>
