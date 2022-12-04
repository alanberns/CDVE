<template>
    <br><br>
    <Section> 
        <h2>Nuestros socios según su genero</h2>
        <span>
            Gráfico de dona que visibiliza la distribución de socios por genero
        </span>
    </Section>
    <br>
    <div>
        <Doughnut
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
  import { Doughnut } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)
  
  export default {
    name: "Genero",
    components: {
    Doughnut
},
    data() {
      return {
        loaded: false,
        chartData : {
            labels: [],
            datasets: [
                {
                    backgroundColor: ['blue', 'green', 'lightblue'],
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
          .get("statistics/genero", {
          headers: {
            Authorization: `${localStorage.getItem("token")}`,
          },
        })
          .then(response => {
                this.chartData.labels = response.data.genero;
                this.chartData.datasets[0].data = response.data.cantidad;
          })
          this.loaded = true;
    }
  
  }
  </script>