import Vue from 'vue'
import App from './App.vue'
import VueRouter from "vue-router";
import MainPage from "./components/MainPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "",
    component: MainPage,
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
