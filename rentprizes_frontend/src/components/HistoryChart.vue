<template>
  <div>
    <div class="chart-container">
      <Chart v-if="data_loaded" type="line" :width="1200" :height="600" :data="basicData" :options="basicOptions" />
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
            labels: [],
            datasets: [
                {
                    label: 'One room',
                    data: [],
                    fill: false,
                    borderColor: "#42A5F5",
                    tension: .4
                },
                {
                    label: 'Two rooms',
                    data: [],
                    fill: false,
                    borderColor: "#66BB6A",
                    tension: .4
                },
                {
                    label: 'Three rooms',
                    data: [],
                    fill: false,
                    borderColor: "#FFA726",
                    tension: .4
                },
                {
                    label: 'Four rooms',
                    data: [],
                    fill: false,
                    borderColor: "rgb(75, 192, 192)",
                    tension: .4
                }
            ]
        },
        basicOptions: {
            plugins: {
                legend: {
                    labels: {
                        color: '#495057'
                    }
                },
                title: {
                    display: true,
                    padding: 15,
                    font: {weight: 'bold', size: '25'},
                    text: 'History of average prizes by rooms'
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
    async getPrizesHistory(city) {
        const response = await fetch(`http://127.0.0.1:5000/getPrizesHistory?city=${city}`)
        const responseData = await response.json()
        
        for (const elem of responseData) {
            this.basicData.labels.push(elem.date)
            for (let index = 0; index < 4; index++) {
            this.basicData.datasets[index].data.push(elem.values[index])
            }
        }

        
        const arr_len = this.basicData.labels.length
        for (let index = arr_len; index < 12; index++) {
            this.basicData.labels.push(`${index < 10 ? '0' + index : index}/23`)
        }

        this.data_loaded = true

    }
  },
  mounted() {
    this.getPrizesHistory(this.cityName)
  },
};
</script>

<style scoped>

</style>
