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
                }),
                myGeoObject = new ymaps.GeoObject({
                    // Описание геометрии.
                    geometry: {
                        type: "Point",
                        coordinates: [57.91685805, 60.11346185]
                    },
                    // Свойства.
                    properties: {
                        // Контент метки.
                        iconContent: 'Я тащусь',
                        hintContent: 'Ну давай уже тащи'
                    }
                }, {
                    // Опции.
                    // Иконка метки будет растягиваться под размер ее содержимого.
                    preset: 'islands#blackStretchyIcon',
                    // Метку можно перемещать.
                    draggable: true
                });
                my_map.geoObjects
                    .add(myGeoObject);


            });
        }
    },
    mounted() {
      this.startMap()
    }
}
</script>

