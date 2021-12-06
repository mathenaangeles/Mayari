<template>
  <div class="calculator">
    <b-card title="Loan Calculator" class="px-1 py-1">
      <b-row>
        <b-col md="8">
          <p class="my-0">
            Get next-day funding of up to <b>50000 PHP</b> for up to
            <b>12 month</b> with flexible terms and low interest rates.*
          </p>
          <p class="subtitle mt-0 mb-1"><i>
            The amounts listed are only an estimate and do not represent a formal offer from Mayari.**
          </i></p>
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
            <b>5000PHP</b><b class="float-right">50000PHP</b>
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
          <b-button block variant="dark" v-on:click="calculate">Check Your Rate</b-button>
          <p class="subtext mt-2 mb-0">
            * This is the maximum loan amount and repayment term. Your loan can be
            disbursed in as little as 1 business day.
          </p>
          <p class="subtext my-0">
            ** For example, a loan of PHP 10000 PHP over a period of 2 weeks will have an interest rate of 0.01% per day — 
            that is 100PHP per day. You will need to repay a total of  11400PHP.
          </p>
        </b-col>
        <b-col md="4">
          <h4><b>Loan Estimate</b></h4>
          <p class="pink-text mt-0 mb-1">
            Checking your rate will not affect your credit score or your final loan plan.
          </p>
          <h5><b>Monthly Installments</b></h5>
          <h5 class="purple-text"><b>{{result_weekly_installment}} PHP</b></h5>
          <hr/>
          <h5><b>Interest Rate</b></h5>
          <h5 class="purple-text"><b>{{result_interest_rate}}%</b></h5>
          <hr/>
          <h5><b>Payment Term</b></h5>
          <h5 class="purple-text"><b>{{result_payment_term}} Months</b></h5>
          <hr/>
          <h5><b>Loan Amount</b></h5>
          <h5 class="purple-text"><b>{{result_loan_amount}} PHP</b></h5>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "FAQCalculator",
  data() {
    return {
      loan_amount: 5000,
      payment_term: 1,
      result_weekly_installment: 0,
      result_interest_rate: 0,
      result_payment_term: 0,
      result_loan_amount: 0,
    };
  },
  methods: {
    installments: function(loan_amount,interest,payment_term){
      return loan_amount*((interest*Math.pow((1+interest),payment_term))/(Math.pow((1+interest),payment_term)-1));
    },
    calculate: function() {
      this.result_loan_amount = this.loan_amount
      this.result_payment_term = this.payment_term
      if (1<=this.payment_term && this.payment_term<=3){
        if (5000<=this.loan_amount && this.loan_amount<=30000) {
          this.result_interest_rate=3
        } else if (30001<=this.loan_amount && this.loan_amount<=50000) {
          this.result_interest_rate=4
        }
      } else if (4<=this.payment_term && this.payment_term<=6) {
        if (5000<=this.loan_amount && this.loan_amount<=20000) {
          this.result_interest_rate=3
        } else if (20001<=this.loan_amount && this.loan_amount<=40000) {
          this.result_interest_rate=4
        } else if (40001<=this.loan_amount && this.loan_amount<=50000) {
          this.result_interest_rate=5
        }
      } else if (7<=this.payment_term && this.payment_term<=9) {
        if (5000<=this.loan_amount && this.loan_amount<=15000) {
          this.result_interest_rate=3
        } else if (15001<=this.loan_amount && this.loan_amount<=30000) {
          this.result_interest_rate=4
        } else if (30001<=this.loan_amount && this.loan_amount<=45000) {
          this.result_interest_rate=5
        } else if (45001<=this.loan_amount && this.loan_amount<=50000) {
          this.result_interest_rate=6
        }
      } else if (10<=this.payment_term && this.payment_term<=12) {
        if (5000==this.loan_amount) {
          this.result_interest_rate=3
        } else if (5001<=this.loan_amount && this.loan_amount<=20000) {
          this.result_interest_rate=4
        } else if (20001<=this.loan_amount && this.loan_amount<=30000) {
          this.result_interest_rate=5
        } else if (30001<=this.loan_amount && this.loan_amount<=40000) {
          this.result_interest_rate=6
        } else if (40001<=this.loan_amount && this.loan_amount<=50000) {
          this.result_interest_rate=7
        }
      }
      this.result_weekly_installment = this.installments(this.result_loan_amount,this.result_interest_rate,this.result_payment_term).toFixed(2);
      console.log(this.result_weekly_installment);
    },
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
.subtitle, .subtext, .pink-text {
  font-size: 15px;
}
.subtext {
  color: #707070;
}
.pink-text {
  color: #F14F8C;
}
.purple-text{
  color: #CA4DE5;
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
