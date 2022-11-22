<template>
  <br><br>
  <div>
      <Bar
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
import axios from 'axios';
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: "SociosPorDisciplina",
  components: {
    Bar,
  },
  data() {
    return {
      loaded: false,
      chartData: {
        labels: [],
        datasets: [
            {
                label: 'Numero de socios',
                backgroundColor:['#ea80fc','#e040fb', '#d500f9', '#aa00ff', '#f8bbd0', '#f06292'],              
                data: [],                
            }
        ]
      },
      chartOptions: {
        responsive: true
      }
    }
  },
  mounted() {
    let data = []
    axios
        .get("http://localhost:5000/api/statistics/inscripcionesPorDisciplina")
        .then(response => response.data.forEach(element => {
            this.chartData.labels.push(element.nombre);
            data.push(element.num_socios);
            })
        )
        this.chartData.datasets[0].data=data;
        this.loaded = true;
  }

}
</script>