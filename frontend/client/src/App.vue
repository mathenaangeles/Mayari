<template>
  <div id="app">
    <div id="nav">
    <b-navbar toggleable="lg">
    <b-navbar-brand href="#">MAYARI</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-navbar-nav> 
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item to="#">FAQ</b-nav-item>
        <b-nav-item to="#">Blog</b-nav-item>
        <b-nav-item to="/about">About Us</b-nav-item>
        <b-nav-item to="#">Contact Us</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    </div>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 1em;
  background-color: #F14F8C;
}

#nav a {
  font-weight: bold;
  color: #FFFFFF;
}

#nav a.router-link-exact-active {
  color: #000000;
}
</style>
