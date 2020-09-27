<template>
  <div id="app">
    <MyHeader></MyHeader>
    <router-view />
  </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'
export default {
    name: 'app',
    data() {
        return {}
    },
    components: {MyHeader, }
}
</script>

<style lang='scss'>
@import "./assets/css/custom.scss";
</style>

