<template>
  <div>
    <div class="chart-container">
      <Chart v-if="data_loaded" type="bar" :width="1200" :height="600" :data="basicData" :options="basicOptions" />
    </div>
  </div>
</template>

<script>
import Chart from 'primevue/chart';
export default {
  props: {
    cityName: String,
    scrapingDate: String
  },
  components: {
    Chart
  },
  data() {
    return {
       basicData: {
            labels: ['One room', 'Two rooms', 'Three rooms', 'Four rooms+'],
            datasets: [
                {
                    label: 'Prize',
                    backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(255, 159, 64, 0.2)', 'rgba(255, 205, 86, 0.2)', 'rgba(75, 192, 192, 0.2)'].reverse(),
                    borderColor: ['rgb(255, 99, 132)', 'rgb(255, 159, 64)', 'rgb(255, 205, 86)', 'rgb(75, 192, 192)'].reverse(),
                    data: [],
                    borderWidth: 1
                }
            ]
        },
        basicOptions: {
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    padding: 15,
                    font: {weight: 'bold', size: '25'},
                    text: 'Average prize of flats by number of rooms'
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: '#495057'
                    },
                    grid: {
                        color: '#ebedef'
                    }
                },
                y: {
                    ticks: {
                        color: '#495057'
                    },
                    grid: {
                        color: '#ebedef'
                    }
                }
            }
        },
        data_loaded: false
    };
  },
  methods: {
    async getCityData(city, date) {
      const response = await fetch(`http://127.0.0.1:5000/getAveragePrizes?city=${city}&date=${date}`)
      const responseData = await response.json()
      this.basicData.datasets[0].data = responseData
      this.data_loaded = true
    }
  },
  mounted() {
    this.getCityData(this.cityName, this.scrapingDate)
  },
};
</script>

<style scoped>

</style>
