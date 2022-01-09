<template>
  <div class="register">
    <b-container fluid>
      <b-row>
        <b-col md="6" sm="12" class="px-0 custom-column">
          <div class="side">
            <div class="side-card">
              <div class="side-main">
                <img src="/img/icons/mayari-white-shadow.png" height="30px">
                <br />
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="2" viewBox="0 0 40 2">
                  <line id="Line_1" data-name="Line 1" x2="40" transform="translate(0 1)" fill="none" stroke="#fff" stroke-width="2"/>
                </svg>
                <p>MAYARI</p>
                <h2>We lend a helping hand.</h2>
                <p>We provide equitable access to capital and the financial support you need to succeed.</p>
              </div>
              <div class="link-container">
                Already have an account? <br/> <b-link class="custom-link" href="/login">Sign In</b-link>
              </div>
            </div>
          </div>
        </b-col>
        <b-col md="6" sm="12" class="custom-column">
          <div class="form-container">
            <b-form class="sign-up-form" @submit="onSubmit">
              <h1 class="my-2">Sign Up</h1>
              <b-form-group id="email" label="Email" label-for="email-input">
                <b-form-input
                  id="email-input"
                  v-model="form.email"
                  type="email"
                  placeholder="Enter your email"
                  required
                ></b-form-input>
              </b-form-group>
              <b-form-group
                id="first-name"
                label="First Name"
                label-for="first-name-input"
              >
                <b-form-input
                  id="first-name-input"
                  v-model="form.first_name"
                  placeholder="Enter your first name"
                  required
                ></b-form-input>
              </b-form-group>
              <b-form-group
                id="last-name"
                label="Last Name"
                label-for="last-name-input"
              >
                <b-form-input
                  id="last-name-input"
                  v-model="form.last_name"
                  placeholder="Enter your last name"
                  required
                ></b-form-input>
              </b-form-group>
              <b-form-group
                id="mobile-number"
                label="Mobile Number"
                label-for="mobile-number-input"
              >
                <b-form-input
                  id="mobile-number-input"
                  v-model="form.mobile_number"
                  placeholder="Enter your mobile number"
                  required
                ></b-form-input>
              </b-form-group>
              <b-form-group
                id="password"
                label="Password"
                label-for="password-input"
              >
                <b-form-input
                  id="password-input"
                  v-model="form.password"
                  type="password"
                  placeholder="Enter your password"
                  required
                ></b-form-input>
              </b-form-group>
              <b-button type="submit" variant="primary"
                >Create an account</b-button
              >
              <span>
                Already have an account? <b-link href="/login">Login.</b-link>
              </span>
            </b-form>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<style scoped>
  .form-container {
    min-height: 100%;
    display: flex;
    justify-content: center;
  }
  .sign-up-form {
    text-align: left;
    margin: auto 2rem;
    min-width: 50%;
  }
  .custom-column {
    height: 80vh;
  }
  .side {
    text-align: left;
    color: white;
    font-weight: bolder;
    background-image: url(~@/assets/auth-bg.png);
    background-repeat: no-repeat!important;
    background-size: cover;
    display: flex;
    flex-direction: column;
    min-height: 100%;
  }
  .side-card {
    margin: auto 4rem;
    padding: 3rem 2rem;
    background: rgba(0, 0, 0, 0.356);
    border-radius: 20px;
    height: 40vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }
  .link-container {
    margin-top: auto;
  }
  .custom-link {
    text-decoration: none;
    color: white;
    font-weight: bolder;
  }

  .custom-link:hover {
    color: #F14F8C;
  }
</style>
<script>
import { EventBus } from "@/utils";
export default {
  name: "Register",
  components: {},
  data() {
    return {
      form: {
        email: "",
        first_name: "",
        last_name: "",
        mobile_number: "",
        password: "",
        error: "",
      },
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      this.$store
        .dispatch("register", {
          email: this.form.email,
          first_name: this.form.first_name,
          last_name: this.form.last_name,
          mobile_number: this.form.mobile_number,
          password: this.form.password,
        })
        .then(() => this.$router.push("/dashboard"));
    },
  },
  mounted() {
    EventBus.$on("failedRegister", (msg) => {
      this.form.error = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off("failedRegister");
  },
};
</script>
