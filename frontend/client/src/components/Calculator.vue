<template>
  <div class="calculator">
    <b-card title="Finance your future">
      <p>Get next-day funding of up to <b>50000 PHP</b> for up to <b>12 month</b> with flexible terms and low interest rates.*</p>
      <label for="loan-amount">Loan Amount</label><span class="float-right label-value">{{ loan_amount }} PHP</span>
      <b-form-input id="loan-amount"  v-model="loan_amount" type="range" min="5000" max="50000" step="1000"></b-form-input>
      <div class="range-limits mb-2">
        <b>5000PHP</b><b class="float-right">50000PHP</b>
      </div>
      <label for="loan-amount">Payment Term</label><span class="float-right label-value">{{ payment_term }} <span v-if="payment_term<=1">Month</span><span v-else-if="payment_term>1">Months</span></span>
      <b-form-input id="payment-terms" v-model="payment_term" type="range" min="1" max="12" step="1"></b-form-input>
      <div class="range-limits mb-2">
        <b>5000PHP</b><b class="float-right">50000PHP</b>
      </div>
      <b-button block variant="dark">Check Your Rate</b-button>
      <p class="subtext mt-2">* This is the maximum loan amount and repayment term. Your loan can be disbursed in as little as 1 business day.</p>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "Calculator",
  data() {
    return {
      loan_amount: '5000',
      payment_term: '1'
    }
  }
};
</script>

<style scoped>
.card {
  border-radius: 10px;
}
.calculator {
  text-align: start;
  
}
.btn-dark {
  background-color: #000000;
  font-weight: bold;
  font-size: 20px;
  border-radius: 10px;
}
.subtext {
  color: #707070;
  font-size: 15px;
}
label, .label-value {
  font-size: 18px;
  font-weight: bold;
}
.card-title {
  font-size: 25px;
  font-weight: bold;
}
input[type='range']::-webkit-slider-runnable-track {
  overflow: hidden;
  -webkit-appearance: none;
  background-color: #e5eef7;
}
input[type='range']::-webkit-slider-thumb {
      -webkit-appearance: none;
      cursor: ew-resize;
      background: #000000;
      box-shadow: -500px 0 0 500px #b456de;
}
.range-limits {
  color: #707070;
  font-size: 16px;
  margin-top: -10px;
}
</style>
