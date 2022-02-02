<template>
  <div class="dashboard">
    <div>
      <!-- <div v-if="!loans || loans.length === 0"> -->
      <h1>You currently do not have any loans.</h1>
      <b-button href="/apply" class="ctv-button">Apply Now</b-button>
    </div>
    <router-link :to="`/profile/${user.id}`"><p>Edit Profile</p></router-link>
    <DashboardLoanItem v-for="loan in loans" :key="loan.id" :loanInfo="loan">
    </DashboardLoanItem>
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
    user: (state) => state.user,
  }),
  beforeMount() {
    this.$store.dispatch("fetchLoans");
  },
};
</script>
