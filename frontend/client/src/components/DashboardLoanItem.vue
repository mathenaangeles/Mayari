<template>
  <b-col md="5" class="mx-1 mb-4">
    <b-card class="loan-card">
      <b class="loan-status-text">
        {{ loanInfo.status.charAt(0).toUpperCase() + loanInfo.status.slice(1) }}
      </b>
      <div class="amount-text">
        {{
          loanInfo.outstanding_balance
            ? "PHP " + loanInfo.outstanding_balance.toFixed(2)
            : loanInfo.requested_amount
            ? "PHP " + loanInfo.requested_amount.toFixed(2)
            : "NA"
        }}
      </div>
      <b-row>
        <b-col>
          <b>Monthly Installment</b><br />
          <b class="value-text">{{
            loanInfo.installment
              ? "PHP " + loanInfo.installment.toFixed(2)
              : "NA"
          }}</b>
        </b-col>
        <b-col>
          <b>Interest Rate</b><br />
          <b class="value-text">
            {{
              loanInfo.interest_rate
                ? loanInfo.interest_rate.toFixed(2) + "%"
                : "NA"
            }}
          </b>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b>Payment Term</b><br />
          <b class="value-text">
            {{
              loanInfo.payment_term
                ? loanInfo.payment_term +
                  " week" +
                  (loanInfo.payment_term > 1 ? "s" : "")
                : "NA"
            }}
          </b>
        </b-col>
        <b-col>
          <b>Total Paid</b><br />
          <b class="value-text">
            {{
              loanInfo.total_amount && loanInfo.outstanding_balance
                ? "PHP " +
                  (
                    loanInfo.total_amount - loanInfo.outstanding_balance
                  ).toFixed(2)
                : loanInfo.total_amount
                ? "PHP " + loanInfo.total_amount.toFixed(2)
                : "NA"
            }}
          </b>
        </b-col>
      </b-row>
      <b-button block variant="dark" class="mt-3">
        <router-link class="btn-bottom" :to="`loan/${loanInfo.id}`">
          View Loan
        </router-link>
      </b-button>
    </b-card>
  </b-col>
</template>
<style scoped>
.loan-card {
  border-radius: 10px;
  border: 0px;
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.2), 0 4px 16px 0 rgba(0, 0, 0, 0.19);
}
.loan-status-text {
  color: #fe6f8e;
}
.amount-text {
  font-size: 1.5rem;
  font-weight: 700;
}
.value-text {
  color: #ca4de5;
  font-size: 1.3rem;
}
.btn-bottom,
.btn-bottom:hover {
  text-decoration: none;
  color: white;
  padding: 1rem;
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
        "text-secondary": status === "pending",
        "custom-text-success": status === "approved",
        "text-danger": status === "denied",
      };
    },
  },
  setup() {},
};
</script>
