<template>
    <div class="row product-title">
        <div class="col d-flex align-items-end" v-bind:style="getProductBG(product.photo)">
            <p class="product_title__title">{{product.product_name}}</p>
            <p class="product_title__price">{{product.price["1"]}}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'product_page',
    data() {
        return {
            product: {}
        }
    },
    methods: {
        loadProduct() {
            axios.get("http://31.31.202.226:5002/get_product/" + this.$route.params.id)
                .then(res => {
                    this.product = res.data.response
                    console.log(this.product)
                })
        },
        getProductBG(product_photo) {
          let default_url = 'https://parkoved1.joinposter.com';
          return 'background: url(https://parkoved1.joinposter.com' + product_photo + '?' + parseInt(new Date().getTime()/1000) + ') no-repeat center / cover';
        }
    },
    mounted() {
        this.loadProduct()
    }
}
</script>
