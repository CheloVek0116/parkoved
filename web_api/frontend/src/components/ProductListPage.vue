<template>
    <div class="row">
        <div v-for="product in products" class="col-6 p-0 die" v-bind:style="getProductBG(product.photo)">
            <a :href="'/product/' + product.product_id">{{product.product_name}}</a>
        </div>
    </div>
</template>

<script>
export default {
    name: 'product_list_page',
    data() {
        return {
            products: []
        }
    },
    methods: {
        loadProducts() {
            axios.get("http://31.31.202.226:5002/get_products/" + this.$route.params.id)
                .then(res => {
                    this.products = res.data.response
                    console.log(this.products)
                })
        },
        getProductBG(product_photo) {
          let default_url = 'https://parkoved1.joinposter.com';
          return 'background: url(https://parkoved1.joinposter.com' + product_photo + '?' + parseInt(new Date().getTime()/1000) + ') no-repeat center / cover';
        }
    },
    mounted() {
        this.loadProducts()
    }
}
</script>
