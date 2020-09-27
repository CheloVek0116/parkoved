<template>
    <div class="row product-title">
        <div class="col d-flex align-items-end" v-bind:style="getProductBG(product.photo)">
            <p class="product_title__title">{{product.product_name}}</p>
            <p class="product_title__price">{{getPrice(product)}}</p>
            <div>
                <a v-if="product.price['1'] != 0" v-bind:href="getPayment(product.menu_category_id)" class="product_title__button">Купить</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'product_page',
    data() {
        return {
            product: {},
            payments: {
                6: 'https://oplata.qiwi.com/form?invoiceUid=1359a1c0-865a-48bf-ace3-2108a8ff8271',
                2: 'https://oplata.qiwi.com/form?invoiceUid=0a28446a-4d57-4a5b-9330-e4ee9205f2e3',
                5: 'https://oplata.qiwi.com/form?invoiceUid=10f5c25c-293d-442c-aab5-f4f0f0b3a829',
                7: 'https://oplata.qiwi.com/form?invoiceUid=65c4cd76-33ee-4568-a494-646cfbf956e0',
            }
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
        getPrice(product) {
            return product.price["1"] != 0 ? `${product.price["1"].slice(0, -2)}.${product.price["1"].slice(-2)} у.е.` : 'БЕСПЛАТНО'
        },
        getProductBG(product_photo) {
          let default_url = 'https://parkoved1.joinposter.com';
          return 'background: url(https://parkoved1.joinposter.com' + product_photo + '?' + parseInt(new Date().getTime()/1000) + ') no-repeat center / cover';
        },
        getPayment(cat_id) {
            return this.payments[cat_id]
        },
    },
    mounted() {
        this.loadProduct()
    }
}
</script>
