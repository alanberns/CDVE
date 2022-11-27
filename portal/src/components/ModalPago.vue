<!-- app -->
<template>
  <!-- button show -->
  <button class="btn waves-effect red accent-4" @click="showModal = true">
    Pagar <i class="material-icons right">attach_money</i>
  </button>

  <!-- overlay -->
  <div class="overlay" v-if="showModal" @click="showModal = false"></div>

  <!-- modal -->
  <div class="modal1" v-if="showModal">
    <h3 class="center-align">Confimación</h3>
    <div class="divider"></div>
    <p class="flow-text">Desea realizar un pago por el monto total de:</p>
    <div class="row valign-wrapper div-monto">
      <i class="material-icons">attach_money</i>
      <p class="flow-text center-align">{{ cuotaPickedStore.getMontoTotal }}</p>
    </div>

    <div class="row">
      <div class="col s1">
        <button
          class="btn waves-effect red accent-4 modal-button"
          @click="showModal = false"
        >
          <i class="material-icons">clear</i>
        </button>
      </div>
      <div class="col s1 offset-s9">
        <a
          href="javascript:;"
          v-on:click="confirmPago()"
          class="btn waves-effect green darken-3 modal-button"
        >
          <i class="material-icons">check</i>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { useCuotaPickedStore } from "../stores/CuotaPickedStore";
import { useLoginStore } from "../stores/LoginStore";
import { apiService } from "../apiService";
import router from "@/router";
export default {
  name: "ModalPago",
  data() {
    return { showModal: false };
  },
  setup() {
    const cuotaPickedStore = useCuotaPickedStore();
    const loginStore = useLoginStore();
    return { cuotaPickedStore, loginStore };
  },
  methods: {
    async confirmPago() {
      if (confirm("¿Deseas confirmar el pago?")) {
        let apiCuotas = [];
        this.cuotaPickedStore.getCuotas.forEach((cuota) =>
          apiCuotas.push({
            month: cuota.nro_cuota,
            amount: cuota.monto,
          })
        );
        apiService.defaults.headers[
          "Authorization"
        ] = `${this.loginStore.getToken}`;
        await apiService
          .post("/me/payments", {
            disciplina: this.cuotaPickedStore.disciplina,
            cuotas: apiCuotas,
          })
          .then((response) => {
            console.log(response);
            console.log("exito");
          })
          .catch((error) => console.log(error));
        this.cuotaPickedStore.pagoIsConfirmed = true;
        this.showModal = false;
        router.push("/pagos");
      }
    },
  },
};
</script>

<style>
.modal-vue .overlay {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-vue .modal1 {
  position: absolute;
  float: left;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  margin: 0 auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 10px 16px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.btn.modal-button {
  border-radius: 10px;
}

.div-monto {
  align-items: center;
  justify-content: center;
}
</style>
