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
            <b-button type="submit" variant="primary"
              >Login to your account</b-button
            >
          </b-form>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<style scoped></style>
<script>
export default {
  name: "Login",
  components: {},
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
    },
  },
};
</script>
