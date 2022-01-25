<template>
  <div class="dashboard">
    <div v-if="!loans || loans.length === 0">
      <h1>You currently do not have any loans.</h1>
      <b-button href="/apply" class="ctv-button">Apply Now</b-button>
    </div>
    <DashboardLoanItem v-for="loan in loans" :key="loan.id" :loanInfo="loan">
    </DashboardLoanItem>
    <!-- <div v-for="loan in loans" v-bind:key="loan.id">
      <p>{{ loan.status }}</p>
      <router-link :to="`loan/${loan.id}`">See Loan</router-link>
    </div> -->
  </div>
</template>
<style scoped></style>
<script>
import { mapState } from "vuex";
import DashboardLoanItem from "../components/DashboardLoanItem.vue";
export default {
  name: "Dashboard",
  components: {
    DashboardLoanItem,
  },
  computed: mapState({
    loans: (state) => state.loans,
  }),
  beforeMount() {
    this.$store.dispatch("fetchLoans");
  },
};
</script>
