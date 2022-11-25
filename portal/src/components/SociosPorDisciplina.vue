<template>
  <br><br>
  <Section> 
    <h2>Socios inscriptos por disciplina</h2>
    <span>
        Gráfico de barras en el que se refleja la cantidad de socios que hay inscriptos en cada una de nuestras disciplinas
    </span>
  </Section>
  <br>
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
import { apiService } from "../apiService";
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
                label: 'Numero de socios inscriptos',
                backgroundColor:['#ea80fc','#e040fb', '#d500f9', '#aa00ff', '#f8bbd0', '#f06292'],              
                data: [],                
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
    let data = []
    apiService
        .get("statistics/inscripcionesPorDisciplina", {
        headers: {
          Authorization: `${localStorage.getItem("token")}`,
        },
      })
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