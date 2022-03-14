<template>
  <div class="dashboard-container">
    <div
      class="d-flex flex-column flex-shrink-0 p-3 text-white"
      style="width: 300px; background-color: #e5e5e5"
    >
      <div class="user-card text-dark text-left">
        <div class="text-dark" v-if="user.name">
          <h3><strong>Hello, {{ user.name }}</strong></h3></div>
        <div v-if="user.street_address || user.city || user.region || user.zip_code">
          <MapMarker />
          {{ user.street_address ? user.street_address + ", " : "" }}
          {{ user.city ? user.city + ", " : "" }}
          {{ user.region ? user.region + ", " : "" }} {{ user.zip_code }}
        </div>
        <div v-if="user.email" class="mt-1">
          <Email />
          {{ user.email }}
        </div>
        <div v-if="user.mobile_number" class="mt-1">
          <Phone />
          {{ user.mobile_number }}
        </div>
        <div class="text-center">
          <router-link :to="`/profile/${user.id}`"><p>Edit Profile</p></router-link>
        </div>
      </div>
    </div>
    <b-container class="dashboard text-left">
      <h1>Business Loans</h1>
      <b-row>
        <b-col md="4" sm="6" class="p-2 apply-container">
          <h4 v-if="loans.length === 0">
            You currently do not have any loans.
          </h4>
          <b-link href="/apply" class="text-light apply-text"
            >Apply For a Business Loan now.</b-link
          >
        </b-col>
        <DashboardLoanItem
          v-for="loan in loans"
          :key="loan.id"
          :loanInfo="loan"
        >
        </DashboardLoanItem>
      </b-row>
    </b-container>
  </div>
</template>
<style scoped>
.apply-text {
  position: absolute;
  bottom: 10px;
}
.apply-container {
  position: relative;
  height: 200px;
  width: 1.5rem;
  border-radius: 10px;
  background: rgb(175, 163, 240);
  background: linear-gradient(
    183deg,
    rgba(175, 163, 240, 1) 0%,
    rgba(180, 86, 222, 1) 100%
  );
}
.dashboard-container {
  display: flex;
  flex-wrap: nowrap;
  height: 100vh;
  height: -webkit-fill-available;
  max-height: 100vh;
  overflow-x: auto;
  overflow-y: hidden;
}
.user-card {
  border-radius: 10px;
  background-color: white;
  border-top: solid black 3px;
  min-height: 3rem;
  padding: 0.5rem;
}
</style>
<script>
import { mapState } from "vuex";
import MapMarker from "vue-material-design-icons/MapMarker";
import Email from "vue-material-design-icons/Email";
import Phone from "vue-material-design-icons/Phone";
import DashboardLoanItem from "../components/DashboardLoanItem.vue";
export default {
  name: "Dashboard",
  components: {
    DashboardLoanItem,
    MapMarker,
    Email,
    Phone,
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
