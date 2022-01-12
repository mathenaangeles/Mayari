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
              <h1 class="my-2">Sign In</h1>
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
                >Login to your account</b-button
              >
              <span>
                No account yet? <b-link href="/register">Register.</b-link>
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
.sign-in-form {
  text-align: left;
  margin: auto 2rem;
  min-width: 50%;
}
.custom-column {
  height: 80vh;
}
</style>
<script>
import AuthSideContainer from "@/components/AuthSideContainer.vue";
import { EventBus } from "@/utils";
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
        error: "",
      },
      authContent: {
        linkRoute: "register",
        message: "Don't have an account yet?",
        linkText: "Sign Up",
      },
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      this.$store
        .dispatch("login", {
          email: this.form.email,
          password: this.form.password,
        })
        .then(() => this.$router.push("/dashboard"));
    },
  },
  mounted() {
    EventBus.$on("failedLogin", (msg) => {
      this.form.error = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off("failedLogin");
  },
};
</script>
