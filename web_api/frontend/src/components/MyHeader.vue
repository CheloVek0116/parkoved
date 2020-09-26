<template>
    <header>
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
              <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Features</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Pricing</a>
              </li>
            </ul>
            <!-- Links -->

          </div>
          <div class="m-auto">
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
background-image: url('https://mdbootstrap.com/img/svg/hamburger6.svg?color=000');
}
.navbar .navbar-toggler {
    border: 0;
}
</style>
