<template>
  <div class="app">
    <router-view/>
  </div>
</template>

<style>
.app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100vh;
}
body {
  margin: 0;
}
.flex {
  display: flex;
}
.flex-jc {
  justify-content: center;
}
.flex-ac {
  align-items: center;
}
.flex-col {
  flex-direction: column;
}
.flex-row {
  flex-direction: row;
}
.flex-sb {
  justify-content: space-between;
}
.flex-sa {
  justify-content: space-around;
}
.flex-gap-1 {
  gap: 1rem
}
.header-text-1 {
  font-size: 2.5rem;
  color: var(--secondary-color);
}
.header-text-2 {
  font-size: 2.5rem;
  color: var(--primary-color);
}
.chart-container {
  -webkit-box-shadow: 11px 17px 53px -30px rgba(66, 68, 90, 1);
  -moz-box-shadow: 11px 17px 53px -30px rgba(66, 68, 90, 1);
  box-shadow: 11px 17px 53px -30px rgba(66, 68, 90, 1);
  padding: 0.8rem;
  margin-bottom: 1rem;
}
</style>
