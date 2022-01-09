<template>
  <div class="side">
    <div class="side-card">
      <div class="side-main">
        <img src="/img/icons/mayari-white-shadow.png" height="30px" />
        <br />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="40"
          height="2"
          viewBox="0 0 40 2"
        >
          <line
            id="Line_1"
            data-name="Line 1"
            x2="40"
            transform="translate(0 1)"
            fill="none"
            stroke="#fff"
            stroke-width="2"
          />
        </svg>
        <p>MAYARI</p>
        <h2>We lend a helping hand.</h2>
        <p>
          We provide equitable access to capital and the financial support you
          need to succeed.
        </p>
      </div>
      <div class="link-container">
        {{ authContent.message }} <br />
        <b-link class="custom-link" :to="authContent.linkRoute">{{ authContent.linkText }}</b-link>
      </div>
    </div>
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
  background-repeat: no-repeat !important;
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
  color: #f14f8c;
}
</style>
<script>
export default {
  name: "AuthSideContainer",
  props: {
    authContent: {
      type: Object,
      required: true,
    },
  },
  methods: {
      goTo(key) {
          this.$router.push({ name: key });
      }
  },
  components: {},
};
</script>
