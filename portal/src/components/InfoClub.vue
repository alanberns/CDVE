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
                            Somos un club con actividades deportivas, ubicado en Villa Elisa, Partido de La Plata.
                            Descubrí las actividades que se desarrollan en el club, conocé las estadísticas y 
                            gestioná tus pagos
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="elclub">
        <div class="row">
            <div class="col s12 m6">
                <div class="card grey darken-1">
                    <div class="card-content white-text">
                        <span class="card-title">El club</span>
                    </div>
                    <div class="card-action grey">
                        <router-link to="/disciplinas"><p class="white-text">Nuestras disciplinas</p></router-link>
                        <router-link to="/statistics/sociosPorDisciplina"><p class="white-text">Inscriptos por disciplina</p></router-link>
                        <router-link to="/statistics/concurrencia"><p class="white-text">Concurrencia por hora</p></router-link>
                        <router-link to="/statistics/genero"><p class="white-text">Socios por género</p></router-link>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="personal">
        <div class="row">
            <div class="col s12 m6">
                <div class="card grey darken-1">
                    <div class="card-content white-text">
                        <span class="card-title">Información personal </span>
                    </div>
                    <div class="card-action grey">
                        <router-link to="/pagos"><p class="white-text">Mis pagos</p></router-link>
                        <router-link to="/pagar"><p class="white-text">Subí tu comprobante de pago</p></router-link>
                        <router-link to="/user"><p class="white-text">Mis datos</p></router-link>
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
