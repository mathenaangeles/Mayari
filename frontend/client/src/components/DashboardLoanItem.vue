<template>
  <b-col class="p-2" md="4" sm="6">
    <div class="loan-card">
      <div class="loan-status-text">
        {{ loanInfo.status.charAt(0).toUpperCase() + loanInfo.status.slice(1) }}
      </div>
      <div class="amount-text">
        {{
          loanInfo.outstanding_balance
            ? "PHP " + loanInfo.outstanding_balance
            : loanInfo.requested_amount
            ? "PHP " + loanInfo.requested_amount
            : "NA"
        }}
      </div>
      <b-row>
        <b-col>
          <div>Weekly installment</div>
          <div class="value-text">NA</div>
        </b-col>
        <b-col>
          Interest rate
          <div class="value-text">
            {{ loanInfo.interest_rate ? loanInfo.interest_rate + "%" : "NA" }}
          </div>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <div>Payment Term</div>
          <div class="value-text">
            {{
              loanInfo.payment_term
                ? loanInfo.payment_term +
                  " week" +
                  (loanInfo.payment_term > 1 ? "s" : "")
                : "NA"
            }}
          </div>
        </b-col>
        <b-col>
          Total Paid
          <div class="value-text">
            {{ loanInfo.total_amount ? "PHP" + loanInfo.total_amount : "NA" }}
          </div>
        </b-col>
      </b-row>
      <div class="btn-bottom">
        <router-link :to="`loan/${loanInfo.id}`" class="p-2"
          ><strong>View Loan</strong></router-link
        >
      </div>
    </div>
  </b-col>
</template>
<style scoped>
.loan-card {
  border-radius: 10px;
  box-shadow: 10px 10px 12px grey;
  padding: 1rem;
}
.amount-text {
  font-size: 1.5rem;
  font-weight: 700;
}
.btn-bottom {
  color: white;
  background-color: black;
  width: 100%;
  border-radius: 5px;
  padding: 0.5rem;
  text-align: center;
}
.loan-status-text {
  color: #fe6f8e;
}
.btn-bottom * {
  text-decoration: none;
  color: white;
  padding: 1rem;
}
.value-text {
  color: #ca4de5;
  font-size: 1.3rem;
}
</style>
<script>
export default {
  name: "DashboardLoanItem",
  props: {
    loanInfo: {
      type: Object,
      required: true,
    },
  },
  methods: {
    getClass(status) {
      return {
        "text-warning": status === "pending",
        "custom-text-success": status === "approved",
        "text-danger": status === "denied",
      };
    },
  },
  setup() {},
};
</script>
