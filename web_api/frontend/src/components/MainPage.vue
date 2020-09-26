<template>
    <div class="row text-success">
        <div v-for="cat in categories" class="col-6 die" v-bind:style="getCatBG(cat.category_photo)">
            <a :href="'cat/' + cat.category_id" style='display: block; width: 100%; height: 100%; text-decoration: none; color: #28a745;'></a>
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

<style>
.die {
    height: 30vh;
}
</style>
