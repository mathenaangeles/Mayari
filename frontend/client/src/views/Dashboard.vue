<template>
  <div class="dashboard-container">
    <b-row>
      <b-col id="sidebar" md="4" class="p-5">
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
      </b-col>
      <b-col md="8" class="text-left px-5 py-4">
        <h1 class="dashboard-header my-3">Business Loans</h1>
        <b-row>
          <b-col md="5" class="mx-1 mb-4">
            <b-card class="apply-card">
              <b-link href="/apply" class="apply-text pb-4"
                >Apply for a business loan now
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="22.099"
                  height="13.501"
                  viewBox="0 0 22.099 13.501"
                >
                  <path
                    id="Icon_ionic-ios-arrow-round-forward"
                    data-name="Icon ionic-ios-arrow-round-forward"
                    d="M21.968,11.51A.865.865,0,0,0,21.96,12.8l4.667,4.282H8.865a.917.917,0,1,0,0,1.828H26.619L21.952,23.2a.871.871,0,0,0,.008,1.294,1.059,1.059,0,0,0,1.4-.007l6.325-5.836h0a1.024,1.024,0,0,0,.207-.288.809.809,0,0,0,.077-.352.878.878,0,0,0-.284-.64l-6.325-5.836A1.042,1.042,0,0,0,21.968,11.51Z"
                    transform="translate(-7.875 -11.252)"
                    fill="#fff"
                  />
                </svg>
              </b-link>
            </b-card>
          </b-col>
          <DashboardLoanItem
            v-for="loan in loans"
            :key="loan.id"
            :loanInfo="loan"
          >
          </DashboardLoanItem>
        </b-row>
      </b-col>
    </b-row>
  </div>
</template>
<style scoped>
#sidebar {
  background-color: #e5e5e5;
  min-height: 100vh;
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
.edit-profile-link:hover {
  text-decoration: none !important;
}
.dashboard-header {
  font-weight: 700;
  font-size: 40px;
  text-align: left;
}
.apply-text,
.apply-text:hover {
  color: white;
  font-weight: 700;
  font-size: 24px;
  /* position: absolute;
  bottom: 0; */
}
.apply-card {
  /* position: relative; */
  height: 270px;
  border-radius: 10px;
  border: 0px;
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.2), 0 4px 16px 0 rgba(0, 0, 0, 0.19);
  background: rgb(175, 163, 240);
  background: linear-gradient(
    183deg,
    rgba(175, 163, 240, 1) 0%,
    rgba(180, 86, 222, 1) 100%
  );
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
