<template>
  <b-container class="loan-info mt-4 py-2 px-5 text-left">
    <b-row>
      <b-col md="8">
        <button
          @click="hasHistory() ? $router.go(-1) : $router.push('/')"
          class="btn btn-link text-dark"
        >
          <h2><ArrowLeft /> Loan Information </h2>
        </button>
      </b-col>
      <b-col md="4">
        <h2 v-bind:class="getClass(loan.status)">{{ loan.status.charAt(0).toUpperCase() + loan.status.slice(1) }}</h2>
      </b-col>
    </b-row>
    <hr />
    <b-row>
      <b-col>
        <div class="header-text">Outstanding Balance</div>
        <div class="header-value">{{!loan.outstanding_balance ? "NA" : "Php"+loan.outstanding_balance}}</div>
      </b-col>
      <b-col>
        <div class="header-text">Overdue Balance</div>
        <div class="header-value">{{!loan.overdue_balance ? "NA" : "Php"+loan.overdue_balance}}</div>
      </b-col>
    </b-row>
    <p class="custom-text-success">Your loan application is pending approval.</p>
    <b-row>
      <b-col>
        <div class="more-info-text">Principal</div>
        <div class="more-info-value">{{!loan.principal ? "NA" : "Php"+loan.principal}}</div>
      </b-col>
      <b-col>
        <div class="more-info-text">Total Paid</div>
        <div class="more-info-value">{{!loan.principal ? "NA" : "Php"+loan.principal}}</div>
      </b-col>
      <b-col>
        <div class="more-info-text">Weekly Installments</div>
        <div class="more-info-value">{{!loan.principal ? "NA" : "Php"+loan.principal}}</div>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <div class="more-info-text">Payment Term</div>
        <div class="more-info-value">{{!loan.payment_term ? "NA" : loan.payment_term + " Weeks"}}</div>
      </b-col>
      <b-col>
        <div class="more-info-text">Interest Rate</div>
        <div class="more-info-value">{{!loan.interest_rate ? "NA" : (loan.interest_rate * 100) + "%"}}</div>
      </b-col>
      <b-col>
        <div class="more-info-text">Collateral</div>
        <div class="more-info-value">{{loan.collateral_type}}</div>
      </b-col>
    </b-row>
    <hr />
    <h3> Business Information </h3>
    <!-- TO DO: Business Information not yet available -->
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum cor</p>
    <hr />
    <h3>Documents</h3>
    <div>
      <h5 class="photo-text">Primary Valid ID</h5>
      <a :href="loan.primary_id" class="btn btn-outline-secondary" download>Download File</a>
    </div>
    <div>
      <h5 class="photo-text">Proof of Income</h5>
      <a :href="loan.proof_of_income" class="btn btn-outline-secondary" download>Download File</a>
    </div>
  </b-container>
</template>
<style scoped>
.loan-info * {
  font-weight: 700;
}
.loan-info {
  border-radius: 10px;
  box-shadow: 10px 10px 12px rgb(182, 182, 182);
  height: 100%;
  border: 1px solid #535353;
}
.custom-text-success {
  color: #F14F8C;
}
.header-text {
  font-weight: 700;
  font-size: 1.5rem;
}
.header-value {
  color:#F14F8C;
  font-size: 2rem;
}
.more-info-text {
  font-weight: 700;
  font-size: 1.2rem;
}
.more-info-value {
  color:#CA4DE5;
  font-size: 1.8rem;
}
.photo-text {
  color: #707070;
}
</style>
<script>
import { mapState } from "vuex";
import ArrowLeft from "vue-material-design-icons/ArrowLeft.vue";
export default {
  name: "Loan",
  components: {
    ArrowLeft,
  },
  methods: {
    hasHistory() {
      return window.history.length > 2;
    },
    getClass(status) {
      return {
        "text-warning": status === "pending",
        "custom-text-success": status === "approved",
        "text-danger": status === "denied",
      };
    },
  },
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
