<template>
  <div class="home-container flex flex-ac flex-col">
    <div class="home-header flex flex-row">
      <div class="header-text-1"> Welcome to </div> 
      <div class="header-text-2"> rent prize </div> 
      <div class="header-text-1"> tracker! </div> 
    </div>
    <div class="home-form-wrapper flex flex-row flex-jc flex-ac flex-gap-1">
      <Dropdown v-model="selected_city" optionLabel="name" optionValue="value" :options="cities" placeholder="Select a City" />
      <Dropdown v-model="selected_date" :options="dates" placeholder="Select date" />
      <Button label="Submit" icon="pi pi-check" @click="refreshChart()" iconPos="right" />
    </div>
    <district-chart v-if="show_chart" :city-name="selected_city" :scraping-date="selected_date"/>
    <rooms-chart v-if="show_chart" :city-name="selected_city" :scraping-date="selected_date"/>
    <history-chart v-if="show_chart" :city-name="selected_city" />
  </div>
</template>

<script>
import DistrictChart from '@/components/DistrictChart.vue'
import RoomsChart from '@/components/RoomsChart.vue'
import HistoryChart from '@/components/HistoryChart.vue';
import Dropdown from 'primevue/dropdown';

export default {
  components: {
    DistrictChart,
    RoomsChart,
    Dropdown,
    HistoryChart
  },
  data() {
    return {
      cities: [{name: 'Kraków', value: 'krakow'}, {name: 'Warszawa', value: 'warszawa'}, {name: 'Łódź', value: 'lodz'}, {name: 'Poznań', value: 'poznan'}, {name: 'Katowice', value: 'katowice'}, {name: 'Wrocław', value: 'wroclaw'}],
      dates: [],
      selected_city: null,
      selected_date: null,
      show_chart: false
    }
  },
  methods: {
    refreshChart() {
      this.show_chart = false
      setTimeout(() => {
        this.show_chart = true
      }, 250);
    },
    async getScrapingDates() {
      const response = await fetch('http://127.0.0.1:5000/getScrapingDates')
      const responseData = await response.json()
      this.dates = responseData

    }
  },
  mounted() {
    this.getScrapingDates()
  },
}
</script>

<style scoped>
.home-container {
  height: 100%;
  margin-top: 5rem;
  gap: 5rem;
}
.home-header {
  gap: 0.4rem;
}
.home-form-wrapper {
-webkit-box-shadow: 11px 17px 53px -30px rgba(66, 68, 90, 1);
-moz-box-shadow: 11px 17px 53px -30px rgba(66, 68, 90, 1);
box-shadow: 11px 17px 53px -30px rgba(66, 68, 90, 1);
  padding: 0.8rem;
}
</style>
