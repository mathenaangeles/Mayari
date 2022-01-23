<template>
  <div class="admin-loan-form">
    <h1>Loan</h1>
    <h2>{{ loan.id }}</h2>
    <p>{{ loan.status }}</p>
  </div>
</template>
<style scoped></style>
<script>
import { mapState } from "vuex";
export default {
  name: "AdminLoanForm",
  components: {},
  beforeMount() {
    this.$store.dispatch("fetchLoan", {
      loanId: parseInt(this.$route.params.id),
    });
  },
  computed: mapState({
    loan: (state) => state.loan,
  }),
};
</script>
