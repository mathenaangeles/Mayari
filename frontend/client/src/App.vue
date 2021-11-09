<template>
  <div id="app">
    <div id="nav">
    <b-navbar toggleable="lg">
    <b-navbar-brand href="#">MAYARI</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-navbar-nav> 
        <b-nav-item class="nav-style" to="/">Home</b-nav-item>
        <b-nav-item class="nav-style" to="#">FAQ</b-nav-item>
        <b-nav-item class="nav-style" to="#">Blog</b-nav-item>
        <b-nav-item class="nav-style" to="/about">About Us</b-nav-item>
        <b-nav-item class="nav-style" to="#">Contact Us</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    </div>
    <router-view />
  </div>
</template>

<style>
@import url('http://fonts.cdnfonts.com/css/adobe-clean');
#app {
  font-family: 'Adobe Clean', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 1em;
  background-color: #f14f8c;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #000000;
}
</style>
