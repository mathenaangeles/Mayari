<template>
  <div class="admin-loan-form">
    <h1>Loan</h1>
    <h2>{{ loan.id }}</h2>
    <b-form @submit="onSubmitLoan">
      <b-form-group label="Status">
        <b-form-select
          v-model="form.status"
          :options="statuses"
          required
        ></b-form-select>
      </b-form-group>
      <b-form-group label="Principal">
        <b-form-input v-model="form.principal" type="number"></b-form-input>
      </b-form-group>
      <b-form-group label="Interest Rate">
        <b-form-input v-model="form.interest_rate" type="number"></b-form-input>
      </b-form-group>
      <b-form-group label="Payment Term">
        <b-form-input v-model="form.payment_term" type="number"></b-form-input>
      </b-form-group>
      <b-form-group label="Outstanding Balance">
        <b-form-input
          v-model="form.outstanding_balance"
          type="number"
        ></b-form-input>
      </b-form-group>
      <p>Total Amount {{ total_amount }} PHP</p>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>
<style scoped></style>
<script>
export default {
  name: "AdminLoanForm",
  components: {},
  data: () => {
    return {
      form: {
        status: "",
        interest_rate: 0,
        payment_term: 0,
        principal: 0,
        outstanding_balance: 0,
      },
      statuses: [
        { text: "Select a status", value: null },
        "pending",
        "approved",
        "rejected",
      ],
    };
  },
  beforeMount() {
    this.$store.dispatch("fetchLoan", {
      loanId: parseInt(this.$route.params.id),
    });
  },
  computed: {
    loan() {
      return this.$store.state.loan;
    },
    total_amount() {
      return (
        (this.form.principal *
          (this.form.interest_rate *
            Math.pow(1 + this.form.interest_rate, this.form.payment_term))) /
          (Math.pow(1 + this.form.interest_rate, this.form.payment_term) - 1) ||
        0
      );
    },
  },
  created: function () {
    let user = this.$store.state.user;
    if (user) {
      try {
        this.form.status = this.loan.status;
        this.form.payment_term = this.loan.payment_term ?? 0;
        this.form.interest_rate = this.loan.interest_rate ?? 0;
        this.form.principal = this.loan.principal ?? 0;
        if (this.loan.status == "approved" && this.loan.outstanding_balance) {
          this.form.outstanding_balance = this.loan.outstanding_balance;
        }
      } catch (error) {
        console.log("ERROR: User could not be found.", error);
      }
    }
  },
  methods: {
    onSubmitLoan(event) {
      event.preventDefault();
      this.$store
        .dispatch("updateLoan", {
          id: this.loan.id,
          interest_rate: this.form.interest_rate,
          payment_term: this.form.payment_term,
          principal: this.form.principal,
          total_amount: this.total_amount,
          status: this.form.status,
          outstanding_balance: this.form.outstanding_balance,
        })
        .then(() => this.$router.push("/admin/dashboard"))
        .catch((error) => {
          console.log("ERROR: Loan could not be updated.", error);
        });
    },
  },
};
</script>
