<template>
  <div class="admin-dashboard">
    <h1>Admin</h1>
    <div v-for="loan in loans" v-bind:key="loan.id">
      <p>{{ loan.id }}</p>
      <router-link :to="`loan/${loan.id}`">See Loan</router-link>
    </div>
  </div>
</template>
<style scoped></style>
<script>
import { mapState } from "vuex";
export default {
  name: "AdminDashboard",
  components: {},
  computed: mapState({
    loans: (state) => state.loans,
  }),
  beforeMount() {
    this.$store.dispatch("fetchAllLoans");
  },
};
</script>
