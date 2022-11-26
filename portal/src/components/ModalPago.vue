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
    <h3 class="center-align">Confimacion</h3>
    <div class="divider"></div>
    <p class="flow-text">Desea realizar un pago por el monto total de:</p>
    <div class="row valign-wrapper div-monto">
      <i class="material-icons">attach_money</i>
      <p class="flow-text center-align">1000</p>
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
        <button
          class="btn waves-effect green darken-3 modal-button"
          @click="showModal = false"
        >
          <i class="material-icons">check</i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalPago",
  data() {
    return { showModal: false };
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
