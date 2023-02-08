<template>
  <div>
    <select class="form-select mb-3" v-model="current_id" @change="changeRegion">
      <option v-for="region in regions" :key="region.id" v-bind:value="region.id">
        {{ region.name }}
      </option>
    </select>

    <select class="form-select mb-3" v-model="current_city_id" @change="changeCity" v-if="cities">
      <option v-for="city in cities" :key="city.id" v-bind:value="city.id">
        {{ city.city }}
      </option>
    </select>

    <select v-model="current_city_districts_id" @change="changeCityDistrict" v-if="cities_districts">
      <option v-for="district in cities_districts" :key="district.id" v-bind:value="district.id">
        {{ district.name }}
      </option>
    </select>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Regions",
  props: {
    regions: Array,
  },
  data() {
    return {
      current_id: null,
      current_city_id: null,
      cities: null,
      cities_districts: null,
    };
  },
  methods: {
    async changeRegion() {
      console.log('region_changed', this.current_id);
      const response = await axios.get(`http://localhost:8000/api/cities/region/${this.current_id}`);
      this.cities = response.data
      console.log('city_id', this.current_city_id)
      console.log('url', JSON.stringify(response))
      console.log('res', response.data)
    },

    async changeCity() {
      console.log("city_changed", this.current_city_id);
      try {
        const response = await axios.get(`http://localhost:8080/static/src/vue/dist/cities_districts.json?city_id={this.current_city_id}`);
        this.cities_districts = response.data;
        console.log("res", response.data);
      } catch (error) {
        console.log("Что-то пошло не так");
      }
    },
    changeCityDistrict() {},
  }
};
</script>
