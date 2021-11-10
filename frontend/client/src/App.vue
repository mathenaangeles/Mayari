<template>
	<div id="app" class="d-flex flex-column min-vh-100">
		<div id="nav">
		<b-navbar toggleable="lg">
		<b-navbar-brand href="/404"><img src="img/icons/mayari-white-shadow.png" style="height:40px"/></b-navbar-brand>

		<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
		<b-collapse id="nav-collapse" is-nav>
			<b-navbar-nav> 
				<b-nav-item class="nav-style" to="/">Home</b-nav-item>
				<b-nav-item class="nav-style" to="/404">FAQ</b-nav-item>
				<b-nav-item class="nav-style" to="/404">Blog</b-nav-item>
				<b-nav-item class="nav-style" to="/about">About Us</b-nav-item>
				<b-nav-item class="nav-style" to="/404">Contact Us</b-nav-item>
			</b-navbar-nav>
		</b-collapse>
		</b-navbar>
		</div>
		<router-view />
		<!-- FOOTER -->
		<footer class="section-footer mt-auto">
			<b-container>
				<b-row>
					<b-col xs="6">
						<span class="mayari-footer">
							<img src="/img/icons/mayari-white-shadow.png" height="30px"/> <h3 style="display: inline-block;">ayari</h3>
						</span>
						<span>Quezon City, Metro Manila</span> <br/>
						<span>Philippines, 1126</span> <br/>
						<span>support@mayari.com</span> <br/>
						<span>+63 (917) 000 0000</span>
					</b-col>
					<b-col xs="6">
						<h4>BORROW</h4>
						<b-link class="footer-link" to="/404">Business Loans</b-link>
						<b-link class="footer-link" to="/404">Personal Loans (Coming Soon)</b-link>
						<b-link class="footer-link" to="/404">Finance Loans (Coming Soon)</b-link>
					</b-col> 
					<b-col xs="6">
						<h4>LEARN</h4>
						<b-link class="footer-link" to="/404">Home</b-link>
						<b-link class="footer-link" to="/404">Blog</b-link>
						<b-link class="footer-link" to="/404">FAQ</b-link>
					</b-col> 
					<b-col xs="6">
						<h4>CONNECT</h4>
						<b-link class="footer-link" to="/404">About Us</b-link>
						<b-link class="footer-link" to="/404">Contact Us</b-link>
					</b-col> 
				</b-row>
			</b-container>
		</footer>
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
#nav a.nav-link:hover {
	background-color: #7070701c;
	border-radius: 10px;
}
#nav a.router-link-exact-active {
	color: #000000;
}
/* FOOTER */
footer.section-footer {
	padding: 1em 1em ;
	color: white;
	text-align: left;
	background-color: #000000;
}

.mayari-footer {
	display: flex;
 	align-items: center;
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
