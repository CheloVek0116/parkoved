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
        placemark(coords, name, link, productLink='', productName='') {
            return new ymaps.Placemark(coords, {
                balloonContent:  productLink ? `<a href="${productLink}" target="_blank">${productName}</a>` : null,
                hintContent: name,
            }, {
                // Опции.
                // Необходимо указать данный тип макета.
                iconLayout: 'default#image',
                // Своё изображение иконки метки.
                iconImageHref: link,
                // Размеры метки.
                iconImageSize: [25, 30],
                // Смещение левого верхнего угла иконки относительно
                // её "ножки" (точки привязки).
                iconImageOffset: [-15, -20]
            });
        },
        startMap() {
            ymaps.ready(() => {
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
                let toilet = this.placemark([57.91799071, 60.11453981], 'Туалет!', 'https://img.icons8.com/doodle/2x/toilet-paper.png');
                let carousel = this.placemark(
                    [57.91639024, 60.11259783],
                    'Лошадки!',
                    'https://img.icons8.com/doodle/2x/carousel--v1.png',
                    'http://31.31.202.226:8080/product/9',
                    'Лошадки!',
                );
                let carousel1 = this.placemark(
                    [57.91600770, 60.11237252],
                    'Машинки!',
                    'https://img.icons8.com/doodle/2x/carousel--v1.png',
                    'http://31.31.202.226:8080/product/7',
                    'Машинки!',
                );
                let carousel2 = this.placemark(
                    [57.91678419, 60.11350171],
                    'Колесо обозрения!',
                    'https://img.icons8.com/doodle/2x/theme-park.png',
                    'http://31.31.202.226:8080/product/8',
                    'Колесо обозрения!',
                );
                let cafe = this.placemark(
                    [57.91767200, 60.11373238],
                    'Кафе!',
                    'https://img.icons8.com/doodle/2x/cafe--v1.png'
                );
                let cafe1 = this.placemark(
                    [57.91864542, 60.11439756],
                    'Кафе!',
                    'https://img.icons8.com/doodle/2x/cafe--v1.png'
                );
                my_map.geoObjects.add(toilet);
                my_map.geoObjects.add(carousel);
                my_map.geoObjects.add(carousel1);
                my_map.geoObjects.add(carousel2);
                my_map.geoObjects.add(cafe);
                my_map.geoObjects.add(cafe1);

            });
        }
    },
    mounted() {
      this.startMap()
    }
}
</script>

