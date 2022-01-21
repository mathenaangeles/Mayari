<template>
  <div class="dashboard">
    <div v-for="loan in loans" v-bind:key="loan.id">
      <p>{{loan.status}}</p>
      <router-link :to="`loan/${loan.id}`">See Loan</router-link>
    </div>
  </div>
</template>
<style scoped></style>
<script>
import { mapState } from 'vuex'
export default {
  name: "Dashboard",
  components: {},
  computed: mapState({
    loans: state => state.loans
  }),
  beforeMount () {
    this.$store.dispatch('fetchLoans')
  },
};
</script>
