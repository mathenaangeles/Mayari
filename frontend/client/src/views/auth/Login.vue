<template>
  <div class="login">
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
            <b-button @click="onSubmit()" type="submit" variant="primary"
              >Login to your account</b-button
            >
            <span>
              No account yet? <b-link href="/register">Register.</b-link>
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
  name: "Login",
  components: {},
  data() {
    return {
      form: {
        email: "",
        password: "",
        error: "",
      },
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      this.$store
        .dispatch("login", { email: this.email, password: this.password })
        .then(() => this.$router.push("/dashboard"));
    },
  },
  mounted() {
    EventBus.$on("failedLogin", (msg) => {
      this.error = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off("failedLogin");
  },
};
</script>
