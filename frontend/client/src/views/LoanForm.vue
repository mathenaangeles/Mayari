<template>
  <div class="loan-form"></div>
</template>
<style scoped></style>
<script>
export default {
  name: "LoanForm",
  components: {},
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>
