<template>
  <div class="register">
    <b-container fluid>
      <b-row>
        <b-col md="6"></b-col>
        <b-col md="6">
          <h1>Sign In</h1>
          <b-form @submit="onSubmit">
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
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<style scoped></style>
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
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name,
          mobile_number: this.mobile_number,
          password: this.password,
        })
        .then(() => this.$router.push("/dashboard"))
        .catch(() => console.log(this.error));
    },
  },
  mounted() {
    EventBus.$on("failedRegister", (msg) => {
      this.error = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off("failedRegister");
  },
};
</script>
