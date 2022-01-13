<template>
  <div class="loan-form">
  </div>
</template>
<style scoped></style>
<script>
export default {
  name: "LoanForm",
  components: {},
  data: () => {
    return {
      step: 0,
      form: {

      },
    };
  },
  methods: {
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>
