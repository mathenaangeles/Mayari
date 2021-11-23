<template>
	<div id="app" class="d-flex flex-column min-vh-100">
		<div id="nav">
		<b-navbar toggleable="lg">
		<b-navbar-brand to="/"><img src="img/icons/mayari-white-shadow.png" style="height:40px"/></b-navbar-brand>
		<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
		<b-collapse id="nav-collapse" is-nav>
			<b-navbar-nav> 
				<b-nav-item class="nav-style" to="/">Home</b-nav-item>
				<b-nav-item class="nav-style" to="/faq">FAQ</b-nav-item>
				<b-nav-item class="nav-style" to="/blog">Blog</b-nav-item>
				<b-nav-item class="nav-style" to="/about">About Us</b-nav-item>
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
						<span>inquiries@mayari.io</span> <br/>
						<span>+63 (917) 828 9919</span>
					</b-col>
					<b-col xs="6">
						<h5><b>BORROW</b></h5>
						<b-link class="footer-link" to="/404">Business Loans</b-link>
						<b-link class="footer-link" to="/404">Personal Loans (Coming Soon)</b-link>
						<b-link class="footer-link" to="/404">Finance Loans (Coming Soon)</b-link>
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
						<b-link href='#' class="footer-link" v-on:click="contact()">Contact Us</b-link>
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
				window.location.href = "mailto:inquiries@mayari.io?subject=My%20Question&body=Place%20inquiries%20here";
			}
		}		
	},
}
</script>

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
	font-weight: 400s;
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
	font-weight: 400;
}
.footer-link:hover {
	color: #f14f8c;
	text-decoration: none;
}
</style>
