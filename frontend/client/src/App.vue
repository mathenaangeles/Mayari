<template>
	<div id="app">
		<div id="nav">
		<b-navbar toggleable="lg">
		<b-navbar-brand href="#"><img src="img/icons/mayari-white.png" style="width:50; height:50px"/></b-navbar-brand>

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
		<!-- FOOTER -->
		<div class="section-footer">
			<b-container>
				<b-row>
					<b-col>
						<h3>MAYARI</h3>
						<span>Quezon City, Metro Manila</span> <br/>
						<span>Philippines, 1126</span> <br/>
						<span>support@mayari.com</span> <br/>
						<span>+63 (917) 000 0000</span>
					</b-col>
					<b-col>
						<h4>BORROW</h4>
						<b-link class="footer-link" to="#">Business Loans</b-link>
						<b-link class="footer-link" to="#">Personal Loans (Coming Soon)</b-link>
						<b-link class="footer-link" to="#">Finance Loans (Coming Soon)</b-link>
					</b-col> 
					<b-col>
						<h4>LEARN</h4>
						<b-link class="footer-link" to="#">Home</b-link>
						<b-link class="footer-link" to="#">Blog</b-link>
						<b-link class="footer-link" to="#">FAQ</b-link>
					</b-col> 
					<b-col>
						<h4>CONNECT</h4>
						<b-link class="footer-link" to="#">About Us</b-link>
						<b-link class="footer-link" to="#">Contact Us</b-link>
					</b-col> 
				</b-row>
			</b-container>
		</div>
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
/* FOOTER */
div.section-footer {
	padding: 1em 1em ;
	color: white;
	text-align: left;
	background-color: #000000;
}

.footer-link {
	display: block;
	color: white;
	font-weight: bold;
}
.footer-link:hover {
	color: #f14f8c;
	text-decoration: none;
}
</style>
