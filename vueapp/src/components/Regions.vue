<template>
  <div>
    <select class="form-select mb-3" v-model="current_id" @change="changeRegion">
      <option v-for="region in items" :key="region.id" v-bind:value="region.id">
        {{ region.name }}
      </option>
    </select>

    <select class="form-select mb-3" v-model="current_city_id" @change="changeRegion" v-if="cities">
      <option v-for="city in cities" :key="city.id" v-bind:value="city.id">
        {{ city.name }}
      </option>
    </select>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Regions",
  props: {
    items: Array,
  },
  data() {
    return {
      current_id: null,
      current_city_id: null,
      cities: null,
    };
  },
  methods: {
    async changeRegion() {
      console.log('region_change', this.current_id);
      const response = await axios.get(`http://localhost:8080/static/src/vue/dist/cities.json`);
      this.cities = response.data
      console.log('res', response.data)
    },
  }
};

</script>