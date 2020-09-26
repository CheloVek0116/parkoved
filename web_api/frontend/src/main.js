import Vue from 'vue'
import ymaps from 'ymaps';
import App from './App.vue'
import VueRouter from "vue-router";
import MainPage from "./components/MainPage.vue";
import MapPage from "./components/MapPage.vue";

Vue.use(VueRouter);
Vue.use(ymaps);

const routes = [
  {
    path: "",
    component: MainPage,
  },
  {
    path: "/map",
    component: MapPage,
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
