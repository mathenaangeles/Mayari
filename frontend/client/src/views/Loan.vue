<template>
  <b-container fluid class="loan-container p-5">
    <b-card class="loan-card p-4 text-left">
      <b-row>
        <b-col md="8">
          <b-row>
            <button
              @click="hasHistory() ? $router.go(-1) : $router.push('/')"
              class="btn btn-link text-dark"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32.709"
                height="23.069"
                viewBox="0 0 32.709 23.069"
              >
                <path
                  id="Icon_ionic-ios-arrow-round-forward"
                  data-name="Icon ionic-ios-arrow-round-forward"
                  d="M28.734,11.693a1.635,1.635,0,0,0-.011,2.211l6.908,7.317H9.341a1.565,1.565,0,0,0,0,3.124H35.619l-6.908,7.317a1.647,1.647,0,0,0,.011,2.211A1.415,1.415,0,0,0,30.8,33.86l9.362-9.972h0a1.766,1.766,0,0,0,.307-.493,1.565,1.565,0,0,0,.114-.6,1.614,1.614,0,0,0-.42-1.093L30.8,11.729A1.393,1.393,0,0,0,28.734,11.693Z"
                  transform="translate(40.584 34.321) rotate(180)"
                />
              </svg>
            </button>
            <h2 class="ml-3">Loan Information</h2>
          </b-row>
        </b-col>
        <b-col class="status-text" md="4">
          <h4 v-bind:class="getClass(loan.status)">
            {{ loan.status.toUpperCase() }}
          </h4>
        </b-col>
      </b-row>
      <hr class="border-dark mb-4" style="border-width: 3px" />
      <b-row class="my-4">
        <b-col>
          <div class="header-text">Outstanding Balance</div>
          <div class="header-value">
            {{
              !loan.outstanding_balance
                ? "NA"
                : "PHP " + loan.outstanding_balance.toFixed(2)
            }}
          </div>
        </b-col>
        <b-col>
          <div class="header-text">Overdue Balance</div>
          <div class="header-value">
            {{
              !loan.overdue_balance
                ? "NA"
                : "PHP " + loan.overdue_balance.toFixed(2)
            }}
          </div>
        </b-col>
      </b-row>
      <b-row class="my-2">
        <b-col md="4">
          <div class="more-info-text">Principal</div>
          <div class="more-info-value">
            {{ !loan.principal ? "NA" : "PHP " + loan.principal.toFixed(2) }}
          </div>
        </b-col>
        <b-col md="4">
          <div class="more-info-text">Total Paid</div>
          <div class="more-info-value">
            {{
              loan.total_amount && loan.outstanding_balance
                ? "PHP " +
                  (loan.total_amount - loan.outstanding_balance).toFixed(2)
                : loan.total_amount
                ? "PHP " + loan.total_amount.toFixed(2)
                : "NA"
            }}
          </div>
        </b-col>
        <b-col md="4">
          <div class="more-info-text">Monthly Installments</div>
          <div class="more-info-value">
            {{ loan.installment ? "PHP " + loan.installment.toFixed(2) : "NA" }}
          </div>
        </b-col>
      </b-row>
      <b-row class="my-2">
        <b-col md="4">
          <div class="more-info-text">Payment Term</div>
          <div class="more-info-value">
            {{ !loan.payment_term ? "NA" : loan.payment_term + " Months" }}
          </div>
        </b-col>
        <b-col md="4">
          <div class="more-info-text">Interest Rate</div>
          <div class="more-info-value">
            {{
              loan.interest_rate ? loan.interest_rate.toFixed(2) + "%" : "NA"
            }}
          </div>
        </b-col>
        <b-col md="4">
          <div class="more-info-text">Collateral</div>
          <div class="more-info-value">
            {{
              loan.collateral_type == "with collateral" && loan.collateral
                ? loan.collateral
                : "NA"
            }}
          </div>
        </b-col>
      </b-row>
      <hr />
      <div>
        <h3>Business Information</h3>
        <h5>
          {{
            business.name && business.industry
              ? business.name + " (" + business.industry + ")"
              : ""
          }}
        </h5>
        <p>
          {{
            business.street_address && business.city && business.zip_code
              ? business.street_address +
                ", " +
                business.city +
                ", " +
                business.zip_code
              : ""
          }}
        </p>
      </div>
      <hr />
      <h3>Documents</h3>
      <div class="my-3">
        <h5 class="text-secondary">Primary Valid ID</h5>
        <a :href="loan.primary_id" class="btn btn-outline-dark" download
          >Download File</a
        >
      </div>
      <div class="my-3">
        <h5 class="text-secondary mb-2">Proof of Income</h5>
        <a :href="loan.proof_of_income" class="btn btn-outline-dark" download
          >Download File</a
        >
      </div>
    </b-card>
  </b-container>
</template>
<style scoped>
.loan-card * {
  font-weight: 700;
}
p {
  font-weight: normal !important;
}
.loan-container {
  background-color: #e5e5e5;
  min-height: 100vh;
}
.loan-card {
  border: 0px;
  border-radius: 10px;
  box-shadow: 2px 4px 6px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.status-text {
  text-align: right;
}
@media only screen and (max-width: 768px) {
  .status-text {
    text-align: left !important;
  }
}
.custom-text-success {
  color: #f14f8c;
}
.header-text {
  font-weight: 700;
  font-size: 1.5rem;
}
.header-value {
  color: #f14f8c;
  font-size: 2rem;
}
.more-info-text {
  font-weight: 700;
  font-size: 1.2rem;
}
.more-info-value {
  color: #ca4de5;
  font-size: 1.8rem;
}
</style>
<script>
import { mapState } from "vuex";
export default {
  name: "Loan",
  components: {},
  methods: {
    hasHistory() {
      return window.history.length > 2;
    },
    getClass(status) {
      return {
        "text-secondary": status === "pending",
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
    business: (state) => state.business,
  }),
};
</script>
