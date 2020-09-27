<template>
    <div id="map" style="width: 100%; height: 95vh">
    </div>
</template>

<script>
export default {
    name: 'map_page',
    data() {
        return {}
    },
    methods: {
        startMap() {
            ymaps.ready(function(){
                var my_map = new ymaps.Map("map", {
                    center: [57.91740616, 60.11397683],
                    zoom: 10
                }, {
                    restrictMapArea: [
                        [57.91242725, 60.10835492],
                        [57.91987252, 60.12101495]
                    ]
                }, {
                    searchControlProvider: 'yandex#search'
                });

            });
        }
    },
    mounted() {
      this.startMap()
    }
}
</script>

