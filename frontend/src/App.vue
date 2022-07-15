<template>
  <RouterView />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');

body {
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
  font-weight: normal;
}
#app {
  height: 100vh;
  width: 100vw;
  padding: 0 !important;
  margin: 0 !important;
}
</style>
