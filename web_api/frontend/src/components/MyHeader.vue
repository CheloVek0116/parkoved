<template>
    <header style="background: #00CCCC;">
        <nav class="navbar navbar-light light-blue lighten-4 p-0 m-0">
          <button class="navbar-toggler toggler-example" type="button" data-toggle="collapse" data-target="#navbarSupportedContent1"
            aria-controls="navbarSupportedContent1" aria-expanded="false" aria-label="Toggle navigation">
            <span class="dark-blue-text">
                <i class="navbar-toggler-icon fas fa-bars fa-1x"></i>
            </span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent1">
            <!-- Links -->
            <ul class="navbar-nav mr-auto">
              <li class="nav-item p-3 active">
                <a class="nav-link" href="/map">Карта</a>
              </li>
              <li class="nav-item p-3 active">
                <a class="nav-link" href="/">Покупки</a>
              </li>
            </ul>
            <!-- Links -->
          </div>
          <div class="title">
            {{ title }}
          </div>

        </nav>
    </header>
</template>


<script>
export default {
    name: 'myheader',
    data() {
        return {
            title: 'Нижний Тагил'
        }
    },
}
</script>
