<template>
  <div>
    <div class="chart-container">
      <Chart v-if="data_loaded" type="bar" :width="1200" :height="600" :data="stackedData" :options="stackedOptions" />
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
      stackedData: {
        labels: [],
        datasets: [
          {
            type: "bar",
            label: "1 room",
            backgroundColor: "#42A5F5",
            data: [],
            stack: 'Stack 0',
          },
          {
            type: "bar",
            label: "2 rooms",
            backgroundColor: "#66BB6A",
            data: [],
            stack: 'Stack 1',
          },
          {
            type: "bar",
            label: "3 rooms",
            backgroundColor: "#FFA726",
            data: [],
            stack: 'Stack 2',
          },
          {
            type: "bar",
            label: "4 rooms",
            backgroundColor: "rgb(75, 192, 192)",
            data: [],
            stack: 'Stack 3',
          },
        ],
      },
      stackedOptions: {
        plugins: {
          tooltip: {
            mode: "index",
            intersect: false,
          },
          legend: {
            labels: {
              color: "#495057",
            },
          },
          title: {
            display: true,
            padding: 15,
            font: {weight: 'bold', size: '25'},
            text: 'Average prize of flats by district'
          }
        },
        scales: {
          x: {
            stacked: true,
            ticks: {
              color: "#495057",
            },
            grid: {
              color: "#ebedef",
            },
          },
          y: {
            stacked: true,
            ticks: {
              color: "#495057",
            },
            grid: {
              color: "#ebedef",
            },
          },
        },
      },
      data_loaded: false
    };
  },
  methods: {
    async getCityData(city, date) {
      const response = await fetch(`http://127.0.0.1:5000//getDataByDistrict?city=${city}&date=${date}`)
      const responseData = await response.json()
      for (const elem of responseData) {
      this.stackedData.labels.push(elem.district_name)
      for (let index = 0; index < 4; index++) {
        this.stackedData.datasets[index].data.push(elem.district_prizes[index])
      }
      this.data_loaded = true
    }
    }
  },
  mounted() {
    this.getCityData(this.cityName, this.scrapingDate)
  },
};
</script>

<style scoped>

</style>
