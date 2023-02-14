<template>
  <div>
    <p class="mb-1">Область</p>
    <select class="form-select mb-3" v-model="current_id" @change="changeRegion">
      <option v-for="region in regions" :key="region.id" v-bind:value="region.id">
        {{ region.region }}
      </option>
    </select>

    <p class="mb-1">Город</p>
    <select class="form-select mb-3" v-model="current_city_id" @change="changeCity" v-if="cities">
      <option v-for="city in cities" :key="city.id" v-bind:value="city.id">
        {{ city.city }}
      </option>
    </select>

    <p class="mb-1">Район</p>
    <select class="form-select mb-3" v-model="current_district_id" @change="changeCity" v-if="districts">
      <option v-for="district in districts" :key="district.id" v-bind:value="district.id">
        {{ district.district }}
      </option>
    </select>
  </div>
</template>

<script>
import axios from "axios";


export default {
  name: "Regions",
  props: {
    test: Array,
    region_id: Number
  },
  mounted() {
    this.displayRegions()
    this.current_id = this.region_id
    this.changeRegion()
    this.changeCity()
  },
  data() {
    return {
      regions: null,
      current_id: null,
      current_city_id: null,
      cities: null,
      cities_districts: null,
      city_id: null,
      districts: null,
      current_district_id: null,
    };
  },
  methods: {
    async displayRegions() {
      const response = await axios.get(`http://127.0.0.1:8000/api/regions/`)
      this.regions = response.data
    },

    async changeRegion() {
      const response = await axios.get(`http://localhost:8000/api/cities/region/${this.current_id}`);
      this.cities = response.data
    },

    async changeCity() {
      const response = await axios.get(`http://localhost:8000/api/districts/cities/${this.current_city_id}`);
      this.districts = response.data
      console.log('url', JSON.stringify(response))
      console.log('res', response.data)
    },
  }
};
</script>
