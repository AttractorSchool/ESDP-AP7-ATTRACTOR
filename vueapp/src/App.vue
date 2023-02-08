<template>
  <div id="app">
    <Regions v-bind:regions="regions_items"/>
  </div>
</template>


<script>
import Regions from "./components/Regions";
export default {
  name: "App",
  components: {
    Regions,
  },
  data() {
    return {
      regions_items: window.regions
    };
  },
};
window.regions = [
  { id: 1, name: "Алматинская область" },
  { id: 2, name: "Акмолинская область" },
  { id: 3, name: "Карагандинская область" },
];
</script>