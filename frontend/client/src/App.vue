<template>
  <div id="app" class="d-flex flex-column">
    <div id="nav">
      <b-navbar toggleable="lg">
        <b-navbar-brand to="/"
          ><img src="img/icons/mayari-white-shadow.png" style="height: 40px"
        /></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item class="nav-style" to="/">Home</b-nav-item>
            <b-nav-item class="nav-style" to="/faq">FAQ</b-nav-item>
            <b-nav-item class="nav-style" to="/blog">Blog</b-nav-item>
            <b-nav-item class="nav-style" to="/about">About</b-nav-item>
          </b-navbar-nav>
          <b-navbar-nav v-if="isAuthenticated" class="ml-auto">
            <b-button class="white-outline-button mt-1" @click="logout">Logout</b-button>
          </b-navbar-nav>
          <b-navbar-nav v-if="!isAuthenticated" class="ml-auto">
            <router-link to="/register">
              <b-button class="white-outline-button mt-1 mr-2"
                >Register</b-button
              >
            </router-link>
            <router-link to="/login">
              <b-button class="white-outline-button mt-1">Login</b-button>
            </router-link>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <!-- <vue-page-transition name="fade" style="animation-duration: 0.5s"> -->
    <router-view />
    <!-- </vue-page-transition> -->
    <!-- FOOTER -->
    <footer class="section-footer mt-auto">
      <b-container>
        <b-row>
          <b-col xs="6">
            <span class="mayari-footer">
              <img src="/img/icons/mayari-white-shadow.png" height="30px" />
              <h3 style="display: inline-block">AYARI</h3>
            </span>
            <span>Quezon City, Metro Manila</span> <br />
            <span>Philippines, 1126</span> <br />
            <span>inquiries@mayari.io</span> <br />
            <span>+63 (917) 828 9919</span>
          </b-col>
          <b-col xs="6">
            <h5><b>BORROW</b></h5>
            <b-link class="footer-link" to="/404">Business Loans</b-link>
            <b-link class="footer-link" to="/404"
              >Personal Loans (Coming Soon)</b-link
            >
            <b-link class="footer-link" to="/404"
              >Finance Loans (Coming Soon)</b-link
            >
          </b-col>
          <b-col xs="6">
            <h5><b>LEARN</b></h5>
            <b-link class="footer-link" to="/">Home</b-link>
            <b-link class="footer-link" to="/blog">Blog</b-link>
            <b-link class="footer-link" to="/faq">FAQ</b-link>
          </b-col>
          <b-col xs="6">
            <h5><b>CONNECT</b></h5>
            <b-link class="footer-link" to="/about">About Us</b-link>
            <b-link href="#" class="footer-link" v-on:click="contact()"
              >Contact Us</b-link
            >
          </b-col>
        </b-row>
      </b-container>
    </footer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      contact() {
        window.location.href =
          "mailto:inquiries@mayari.io?subject=My%20Question&body=Place%20inquiries%20here";
      },
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    logout: function () {
      this.$store.dispatch("logout")
      .then(() => {this.$router.push('/login')});
    }
  },
};
</script>

<style>
@import url("http://fonts.cdnfonts.com/css/adobe-clean");
#app {
  font-family: "Adobe Clean", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  margin: 0;
  display: flex;
  flex-direction: column;
}
#nav {
  padding: 1em;
  background-color: #f14f8c;
}
#nav a {
  font-weight: 500;
  color: #ffffff;
}
#nav a.nav-link:hover {
  background-color: #7070701c;
  border-radius: 10px;
}
#nav a.router-link-exact-active {
  font-weight: 700;
}
footer.section-footer {
  padding: 1em 1em;
  color: white;
  text-align: left;
  background-color: #000000;
  margin-top: auto;
}
.mayari-footer {
  display: flex;
  align-items: center;
}
.footer-link {
  display: block;
  color: white;
  font-weight: 400;
}
.footer-link:hover {
  color: #f14f8c;
  text-decoration: none;
}
.navbar-toggler-icon {
  background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'><path stroke='rgba(255, 255, 255, 1)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/></svg>") !important;
}
.navbar-toggler {
  border: 0px !important;
}
.white-outline-button {
  background: transparent !important;
  border: 1px solid white !important;
  border-radius: 10px;
}
</style>
