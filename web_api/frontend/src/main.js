import Vue from 'vue'
import App from './App.vue'
import VueRouter from "vue-router";
import MainPage from "./components/MainPage.vue";
import MapPage from "./components/MapPage.vue";
import ProductListPage from "./components/ProductListPage.vue";
import ProductPage from "./components/ProductPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "",
    component: MainPage,
  },
  {
    path: "/cat/:id",
    component: ProductListPage,
  },
  {
    path: "/product/:id",
    component: ProductPage,
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
