<template>
    <div class="row text-success">
        <div v-for="product in products" class="col-6 die" v-bind:style="{'background': 'url(https://parkoved1.joinposter.com' + product.photo + ')' + 'no-repeat center / cover'}">
            {{ product.product_name }}
        </div>
    </div>
</template>

<script>
export default {
    name: 'attraction_list_page',
    data() {
        return {
            products: []
        }
    },
    methods: {
        loadProducts() {
            axios.get("http://192.168.0.5:5002/get_products/" + this.$route.params.id)
                .then(res => {
                    this.products = res.data.response
                    console.log(this.products)
                })
        },
        getRandomBackground() {
          var letters = '0123456789ABCDEF';
          var color = '#';
          for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
          }
          return color;
        }
    },
    mounted() {
        this.loadProducts()
    }
}
</script>

<style>
.die {
    height: 30vh;
}
</style>
