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
            <ul class="navbar-nav mr-auto" style="">
              <li class="nav-item p-3 active">
                <a class="nav-link" href="/map">Карта</a>
              </li>
              <li class="nav-item p-3 active">
                <a class="nav-link" href="/">Главная</a>
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


<style>
.navbar .navbar-toggler-icon {
    width: 3em;
    height: 3em;
}
.navbar .navbar-toggler {
    border: 0;
}
.navbar .navbar-collapse {
    position: absolute;
    z-index: 2;
    background: #33CCCC;
    width: 100vw;
    opacity: 0.85;
    top: 4em;
    margin-top: 4px;
}
.navbar .navbar-collapse ul {
    border-bottom: .1em solid #00FFFF;
}
.navbar .navbar-collapse li {
    border: .1em solid #CCFFFF;
}
.navbar .navbar-collapse li:hover {
    border: .1em solid #000;
    background: #00FFFF;
}
.title {
    top: 1.5em;
    left: 50%;
    transform: translateX(-50%);
    position: absolute;
}
</style>
