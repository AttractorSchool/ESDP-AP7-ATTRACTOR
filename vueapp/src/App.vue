<template>
  <div id="app">
    <Regions v-bind:items="regions_items"/>
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
  { id: 2, name: "Джамбульская область" },
  { id: 3, name: "Акмолинская область" },
];

</script>