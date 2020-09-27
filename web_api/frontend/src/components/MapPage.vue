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
                    center: [57.91605197, 60.11301396],
                    zoom: 10
                }, {
                    restrictMapArea: [
                        [57.91242725, 60.10835492],
                        [57.91987252, 60.12101495]
                    ]
                }, {
                    searchControlProvider: 'yandex#search'
                });
                let myPlacemark = new ymaps.Placemark([57.91605197, 60.11301396], {
                    hintContent: 'Собственный значок метки',
                    balloonContent: 'Это красивая метка'
                }, {
                    // Опции.
                    // Необходимо указать данный тип макета.
                    iconLayout: 'default#image',
                    // Своё изображение иконки метки.
                    iconImageHref: '../assets/carousel.png',
                    // Размеры метки.
                    iconImageSize: [30, 42],
                    // Смещение левого верхнего угла иконки относительно
                    // её "ножки" (точки привязки).
                    iconImageOffset: [-5, -38]
                });
                my_map.geoObjects.add(myPlacemark);

            });
        }
    },
    mounted() {
      this.startMap()
    }
}
</script>

