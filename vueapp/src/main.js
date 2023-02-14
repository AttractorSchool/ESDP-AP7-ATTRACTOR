import Vue from 'vue'
import Regions from "@/components/Regions.vue";
import VueTheMask from 'vue-the-mask'

Vue.config.productionTip = false


Vue.component("regions-component", Regions);
Vue.use(VueTheMask)
new Vue({
    el: "#app"
});
