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
          <b-form-input
            v-model="form.principal"
            type="number"
            required
          ></b-form-input>
      </b-form-group>
      <b-form-group label="Interest Rate">
          <b-form-input
            v-model="form.interest_rate"
            type="number"
            required
          ></b-form-input>
      </b-form-group>
      <b-form-group label="Payment Term">
          <b-form-input
            v-model="form.payment_term"
            type="number"
            required
          ></b-form-input>
      </b-form-group>
      <b-form-group label="Total Amount">
          <b-form-input
            v-model="form.total_amount"
            type="number"
            required
          ></b-form-input>
      </b-form-group>
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
        total_amount: 0,
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
    loan () {
      console.log(this.$store.state.loan)
      return this.$store.state.loan
    }
  },
  created: function () {
    let user = this.$store.state.user;
    if (user) {
      try {
        this.form.status = this.loan.status;
        this.form.payment_term = this.loan.payment_term;
      } catch (error) {
        console.log("ERROR: User could not be found.", error);
      }
    }
  },
  methods : {
    onSubmitLoan(event) {
      event.preventDefault();
      this.$store
        .dispatch("updateLoan", {
          interest_rate: this.form.interest_rate,
          payment_term: this.form.payment_term,
          principal: this.form.principal,
          total_amount: this.form.total_amount,
          status: this.form.status,
        })
        .then(() => this.$router.push("/dashboard"))
        .catch((error) => {
          console.log("ERROR: Loan could not be updated.", error);
        });
    },
  }
};
</script>
