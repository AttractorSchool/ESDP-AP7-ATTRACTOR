<template>
  <div id="app">
    <Regions />
  </div>
</template>


<script>
import Regions from "./components/Regions";
export default {
  delimiters: ['[[', ']]'],
  name: "App",
  components: {
    Regions,
  },
};
// window.regions = [
//   { id: 1, name: "Алматинская область" },
//   { id: 2, name: "Акмолинская область" },
//   { id: 3, name: "Карагандинская область" },
// ];
</script>