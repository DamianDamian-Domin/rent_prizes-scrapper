import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import PrimeVue from 'primevue/config';
import router from './router'
import store from './store'
import 'primevue/resources/themes/lara-light-teal/theme.css'
import 'primeicons/primeicons.css';
import Button from 'primevue/button';

createApp(App).use(store).use(router).use(PrimeVue).component('Button', Button).mount('#app')
