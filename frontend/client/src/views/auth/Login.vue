<template>
  <div class="login">
    <b-container fluid>
      <b-row>
        <b-col md="6" sm="12" class="px-0 custom-column">
          <AuthSideContainer :authContent="authContent"></AuthSideContainer>
        </b-col>
        <b-col md="6" sm="12" class="custom-column">
          <div class="form-container">
            <b-form class="sign-in-form" @submit="onSubmit">
              <b-card v-if="error" class="mt-4 error-alert">
                {{ error }}
              </b-card>
              <h1 class="my-3"><b>Sign In</b></h1>
              <b-form-group
                class="bold"
                id="email"
                label="Email"
                label-for="email-input"
              >
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
                class="bold"
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
                  This is a required field.
                </b-form-invalid-feedback>
              </b-form-group>
              <b-button block type="submit" variant="dark" class="my-3"
                >Login to your account</b-button
              >
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
.sign-in-form {
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
import { email, required } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import router from "../../router";
export default {
  name: "Login",
  components: {
    AuthSideContainer,
  },
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      error: null,
      authContent: {
        linkRoute: "register",
        message: "Don't have an account yet?",
        linkText: "Sign Up",
      },
    };
  },
  setup: () => ({ v$: useVuelidate() }),
  validations() {
    return {
      form: {
        email: { required, email },
        password: { required },
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
      this.$store
        .dispatch("login", {
          email: this.form.email,
          password: this.form.password,
        })
        .then((response) => {
          console.log(response);
          router.go();
        });
    },
  },
  mounted() {
    EventBus.$on("failedLogin", () => {
      this.error =
        "Sorry, an unexpected error occurred. Please check the credentials you entered.";
    });
  },
  beforeDestroy() {
    EventBus.$off("failedLogin");
  },
};
</script>
