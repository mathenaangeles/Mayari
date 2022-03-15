<template>
  <div class="dashboard-container">
    <div id="sidebar" class="d-flex flex-column flex-shrink-0 p-4">
      <b-card class="user-card text-left">
        <b-row v-if="user.name" class="align-items-center ml-1">
          <img
            id="profile-photo"
            v-if="user.profile_photo"
            :src="user.profile_photo"
          />
          <b-col>
            <h4 class="bold mb-0" v-if="user.name.length < 16">
              {{ user.name }}
            </h4>
            <h4 class="bold mb-0" v-else>
              {{ user.name.substring(0, 16) + "..." }}
            </h4>
            <router-link :to="`/profile/${user.id}`"
              ><p class="mb-0 edit-profile-link">Edit Profile</p></router-link
            >
          </b-col>
        </b-row>
        <b-card-text class="mt-3">
          <div
            v-if="
              user.street_address || user.city || user.region || user.zip_code
            "
          >
            <MapMarker fillColor="#000000" />
            {{ user.street_address ? user.street_address + ", " : "" }}
            {{ user.city ? user.city + ", " : "" }}
            {{ user.region ? user.region + ", " : "" }} {{ user.zip_code }}
          </div>
          <div v-if="user.email" class="mt-1">
            <Email fillColor="#000000" />
            {{ user.email }}
          </div>
          <div v-if="user.mobile_number" class="mt-1">
            <Phone fillColor="#000000" />
            {{ user.mobile_number }}
          </div>
        </b-card-text>
      </b-card>
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
#sidebar {
  min-width: 25%;
  background-color: #e5e5e5;
}
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
  border-top: 10px solid #000000;
  border-radius: 10px;
  box-shadow: 2px 4px 6px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
#profile-photo {
  border-radius: 50%;
  width: 60px;
  height: 60px;
}
.edit-profile-link {
  color: #f14f8c;
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
