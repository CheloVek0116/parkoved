<template>
    <div class="row">
        <div v-for="cat in categories" class="col-6 p-0 die" v-bind:style="getCatBG(cat.category_photo)">
            <a :href="'/cat/' + cat.category_id">{{cat.category_name}}</a>
        </div>
    </div>
</template>

<script>
export default {
    name: 'main_page',
    data() {
        return {
            categories: []
        }
    },
    methods: {
        loadCategories() {
            axios.get("http://31.31.202.226:5002/get_categories?fiscal=0")
                .then(res => {
                    this.categories = res.data.response
                    console.log(this.categories)
                })
        },
        getCatBG(category_photo) {
          let default_url = 'https://parkoved1.joinposter.com';
          return 'background: url(https://parkoved1.joinposter.com' + category_photo + '?' + parseInt(new Date().getTime()/1000) + ') no-repeat center / cover';
        }
    },
    mounted() {
        this.loadCategories()
    }
}
</script>

