<template>
  <div class="calculator">
    <b-card title="Finance your future" class="px-1 py-1">
      <p class="mt-0 mb-1">
        Get next-day funding of up to <b>50000 PHP</b> for up to
        <b>12 month</b> with flexible terms and low interest rates.
      </p>
      <label for="loan-amount">Loan Amount</label
      ><span class="float-right label-value">{{ loan_amount }} PHP</span>
      <b-form-input
        id="loan-amount"
        v-model="loan_amount"
        type="range"
        min="5000"
        max="50000"
        step="1000"
      ></b-form-input>
      <div class="range-limits mb-2">
        <b>5000 PHP</b><b class="float-right">50000 PHP</b>
      </div>
      <label for="loan-amount">Payment Term</label
      ><span class="float-right label-value"
        >{{ payment_term }} <span v-if="payment_term <= 1">Month</span
        ><span v-else-if="payment_term > 1">Months</span></span
      >
      <b-form-input
        id="payment-terms"
        v-model="payment_term"
        type="range"
        min="1"
        max="12"
        step="1"
      ></b-form-input>
      <div class="range-limits mb-2">
        <b>1 Month</b><b class="float-right">12 Months</b>
      </div>
      <b-button block variant="dark">Check Your Rate</b-button>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "HomeCalculator",
  data() {
    return {
      loan_amount: "5000",
      payment_term: "1",
    };
  },
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
label,
.label-value {
  font-size: 18px;
  font-weight: bold;
}
.card-title {
  font-size: 25px;
  font-weight: bold;
  margin-bottom: 1px;
}
input[type="range"]:focus {
  outline: none;
}
input[type="range"]::-webkit-slider-runnable-track {
  overflow: hidden;
  -webkit-appearance: none;
  background: -moz-linear-gradient(45deg, #afa3f0 0%, #b456de 100%);
  background: linear-gradient(45deg, #afa3f0 0%, #b456de 100%);
}
input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  cursor: grab;
  background: white;
  border: 2px rgba(61, 61, 61, 0.281) solid;
  border-radius: 50%;
  height: 15px;
  width: 15px;
  max-width: 15px;
  position: relative;
}
input[type="range"]::-moz-range-track {
  overflow: hidden;
  -moz-appearance: none;
  background: -moz-linear-gradient(45deg, #afa3f0 0%, #b456de 100%);
  height: 10px;
}
input[type="range"]::-moz-range-thumb {
  -moz-appearance: none;
  border: 2px rgba(61, 61, 61, 0.281) solid;
  border-radius: 50%;
  height: 20px;
  width: 20px;
  max-width: 20px;
  position: relative;
  bottom: 11px;
  background: white;
  cursor: -moz-grab;
  -moz-transition: border 1000ms ease;
  transition: border 1000ms ease;
}
.range-limits {
  color: #707070;
  font-size: 16px;
  margin-top: -10px;
}
</style>
