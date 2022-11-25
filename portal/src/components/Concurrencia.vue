<template>
  <br><br>
  <div>
      <Line
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
</div>
</template>

<script>
import { apiService } from "../apiService";
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale)

export default {
  name: "Concurrencia",
  components: {
      Line,
  },
  data() {
    return {
      loaded: false,
      chartData : {
          labels: [],
          datasets: [
              {
                  label: 'Cantidad de personas que concurren al club',
                  backgroundColor: '#f87979',
                  data: []
              }
          ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  mounted() {
    apiService
        .get("statistics/concurrencia", {
        headers: {
          Authorization: `${localStorage.getItem("token")}`,
        },
      })
        .then((response) => {
              this.chartData.labels = response.data.hora
              this.chartData.datasets[0].data = response.data.personas
            }
        )
        this.loaded = true;
  }

}
</script>