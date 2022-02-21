<template>
  <b-container class="dashboard text-left">
    <router-link :to="`/profile/${user.id}`"><p>Edit Profile</p></router-link>
    <h1>Business Loans</h1>
    <b-row>
      <b-col md="4" sm="6" class="p-2 apply-container">
        <h4>You currently do not have any loans.</h4>
        <b-link href="/apply" class="text-light">Apply For a Business Loan now.</b-link>
      </b-col>
      <DashboardLoanItem v-for="loan in loans" :key="loan.id" :loanInfo="loan">
      </DashboardLoanItem>
    </b-row>
  </b-container>
</template>
<style scoped>
  .apply-container {
    height:100%;
    width: 1.5rem;
    background: rgb(175,163,240);
    background: linear-gradient(183deg, rgba(175,163,240,1) 0%, rgba(180,86,222,1) 100%);
  }
</style>
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
    user: (state) => state.user,
  }),
  beforeMount() {
    this.$store.dispatch("fetchLoans");
  },
};
</script>
