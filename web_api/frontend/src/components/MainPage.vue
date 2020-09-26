<template>
    <div class="row text-success">
        <div v-for="cat in categories" class="col-6 die" v-bind:style="{'background': 'url(https://parkoved1.joinposter.com' + cat.category_photo + ')' + 'no-repeat center / cover'}">
            <a :href="'cat/' + cat.category_id" style='display: block; width: 100%; height: 100%; text-decoration: none; color: #28a745;'>{{ cat.category_name }}</a>
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
            axios.get("http://192.168.0.5:5002/get_categories?fiscal=0")
                .then(res => {
                    this.categories = res.data.response
                    console.log(this.categories)
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
        this.loadCategories()
    }
}
</script>

<style>
.die {
    height: 30vh;
}
</style>
