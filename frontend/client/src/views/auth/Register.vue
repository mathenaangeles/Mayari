<template>
  <div class="register">
    <b-container fluid>
      <b-row>
        <b-col md="6" sm="12" class="px-0 custom-column">
          <AuthSideContainer :authContent="authContent"></AuthSideContainer>
        </b-col>
        <b-col md="6" sm="12">
          <div class="form-container">
            <b-form class="sign-up-form" @submit="onSubmit">
              <h1 class="my-2">Sign Up</h1>
              <b-form-group id="email" label="Email" label-for="email-input">
                <b-form-input
                  id="email-input"
                  v-model="v$.form.email.$model"
                  type="email"
                  placeholder="Enter your email"
                  :state="validateState('email')"
                  aria-describedby="email-feedback"
                ></b-form-input>
                <b-form-invalid-feedback id="email-feedback">
                  Invalid email.
                </b-form-invalid-feedback>
              </b-form-group>
              <b-form-group
                id="first-name"
                label="First Name"
                label-for="first-name-input"
              >
                <b-form-input
                  id="first-name-input"
                  v-model="v$.form.first_name.$model"
                  placeholder="Enter your first name"
                  :state="validateState('first_name')"
                  aria-describedby="first-name-feedback"
                ></b-form-input>
                <b-form-invalid-feedback id="first-name-feedback">
                  This is a required field.
                </b-form-invalid-feedback>
              </b-form-group>
              <b-form-group
                id="last-name"
                label="Last Name"
                label-for="last-name-input"
              >
                <b-form-input
                  id="last-name-input"
                  v-model="v$.form.last_name.$model"
                  placeholder="Enter your last name"
                  :state="validateState('last_name')"
                  aria-describedby="last-name-feedback"
                ></b-form-input>
                <b-form-invalid-feedback id="last-name-feedback">
                  This is a required field.
                </b-form-invalid-feedback>
              </b-form-group>
              <b-form-group
                id="mobile-number"
                label="Mobile Number"
                label-for="mobile-number-input"
              >
                <b-form-input
                  id="mobile-number-input"
                  v-model="v$.form.mobile_number.$model"
                  placeholder="Enter your mobile number"
                  :state="validateState('mobile_number')"
                  aria-describedby="mobile-number-feedback"
                  masked="false"
                  v-mask="'09##-###-####'"
                ></b-form-input>
                <b-form-invalid-feedback id="mobile-number-feedback">
                  This is a required field. Should contain 11 numbers.
                </b-form-invalid-feedback>
              </b-form-group>
              <b-form-group
                id="password"
                label="Password"
                label-for="password-input"
              >
                <b-form-input
                  id="password-input"
                  v-model="v$.form.password.$model"
                  type="password"
                  placeholder="Enter your password"
                  :state="validateState('password')"
                  aria-describedby="password-feedback"
                ></b-form-input>
                <b-form-invalid-feedback id="password-feedback">
                  This is a required field. Should have a minimum 5 characters.
                </b-form-invalid-feedback>
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
  min-height: 80vh;
}
</style>
<script>
import AuthSideContainer from "@/components/AuthSideContainer.vue";
import { EventBus } from "@/utils";
import { email, required, minLength } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
export default {
  name: "Register",
  data() {
    return {
      form: {
        email: this.$route.params.email ?? "",
        first_name: "",
        last_name: "",
        mobile_number: this.$route.params.mobile ?? "",
        password: "",
        error: "",
      },
      authContent: {
        linkRoute: "login",
        message: "Already have an account?",
        linkText: "Sign in",
      },
    };
  },
  setup: () => ({ v$: useVuelidate() }),
  validations() {
    return {
      form: {
        first_name: { required, minLength: minLength(2) },
        last_name: { required, minLength: minLength(2) },
        mobile_number: { required, minLength: minLength(13) },
        password: { required, minLength: minLength(5) },
        email: { required, email },
      },
    };
  },
  methods: {
    validateState(name) {
      const { $dirty, $error } = this.v$.form[name];
      return $dirty ? !$error : null;
    },
    onSubmit(event) {
      event.preventDefault();
      this.v$.form.$touch();
      if (this.v$.form.$invalid) {
        return;
      }
      // convert mobile_number to unmasked form
      const rawMobileNumber = this.form.mobile_number.replaceAll("-", "");
      this.$store
        .dispatch("register", {
          email: this.form.email,
          first_name: this.form.first_name,
          last_name: this.form.last_name,
          mobile_number: rawMobileNumber,
          password: this.form.password,
        })
        .then(() => window.location.reload());
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
  components: {
    AuthSideContainer,
  },
};
</script>
