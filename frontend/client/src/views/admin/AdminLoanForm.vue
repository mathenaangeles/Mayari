<template>
  <b-container fluid class="admin-loan-form p-5">
    <b-card class="text-left p-4 edit-loan-card">
      <b-row align-v="center" align-h="space-between">
        <b-col md="8">
          <b-row align-v="center">
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
            <h1 class="ml-3 bold">Edit Loan #{{loan.id}}</h1>
          </b-row>
        </b-col>
        <b-col md="4" class="amount-text" >
          <b-badge class="amount-badge">
              {{ total_amount.toFixed(2) }} PHP
          </b-badge>
        </b-col>
      </b-row>
      <hr class="border-dark mb-4" style="border-width: 3px" />
      <div class="mt-4">
        <b-form @submit="onSubmitLoan">
          <b>Documents</b>
          <b-row align-h="between" class="my-1 mb-3">
            <b-col>
              <b class="text-secondary">Primary Valid ID</b><br/>
              <a :href="loan.primary_id" class="btn btn-outline-dark" download
                >Download File</a
              >
            </b-col>
            <b-col>
              <b class="text-secondary mb-2">Proof of Income</b><br/>
              <a :href="loan.proof_of_income" class="btn btn-outline-dark" download
                >Download File</a
              >
            </b-col>
          </b-row>
          <b-form-group class="bold" label="Status">
            <b-form-select
              v-model="form.status"
              :options="statuses"
              required
            ></b-form-select>
          </b-form-group>
          <b-form-group class="bold" label="Principal">
            <b-form-input v-model="form.principal" type="number"></b-form-input>
          </b-form-group>
          <b-form-group class="bold" label="Interest Rate">
            <b-form-input v-model="form.interest_rate" type="number"></b-form-input>
          </b-form-group>
          <b-form-group class="bold" label="Payment Term">
            <b-form-input v-model="form.payment_term" type="number"></b-form-input>
          </b-form-group>
          <b-form-group class="bold" label="Outstanding Balance">
            <b-form-input
              v-model="form.outstanding_balance"
              type="number"
            ></b-form-input>
          </b-form-group>
          <b-form-group class="bold" label="Overdue Balance">
            <b-form-input
              v-model="form.overdue_balance"
              type="number"
            ></b-form-input>
          </b-form-group>
          <b-form-group class="bold" label="Collateral">
            <b-form-input v-model="form.collateral"></b-form-input>
          </b-form-group>
          
          <b-button type="submit" variant="dark">Save</b-button>
        </b-form>
      </div>
    </b-card>
  </b-container>
</template>
<style scoped>
.edit-loan-card {
  border-radius: 10px;
  box-shadow: 2px 4px 6px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  height: 100%;
}
.amount-badge {
  font-size: 20px;
  background-color: #f14f8c;
}
.amount-text {
  text-align: right;
}
@media only screen and (max-width: 768px) {
  .amount-text {
    text-align: left !important;
  }
}
</style>
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
        overdue_balance: 0,
        collateral: null,
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
  watch: {
      loan: function () {
        this.initializeForm()
      }
  },
  // created: function () {
  //   let user = this.$store.state.user;
  //   if (user) {
  //     try {
  //       this.form.status = this.loan.status;
  //       this.form.payment_term = this.loan.payment_term ?? 0;
  //       this.form.interest_rate = this.loan.interest_rate ?? 0;
  //       this.form.principal = this.loan.principal ?? 0;
  //       if (this.loan.status == "approved" && this.loan.outstanding_balance) {
  //         this.form.outstanding_balance = this.loan.outstanding_balance;
  //       }
  //       if (this.loan.status == "approved" && this.loan.overdue_balance) {
  //         this.form.outstanding_balance = this.loan.overdue_balance;
  //       }
  //       if (this.loan.type == "with collateral" && this.loan.collateral) {
  //         this.form.collateral = this.loan.collateral;
  //       }
  //     } catch (error) {
  //       console.log("ERROR: User could not be found.", error);
  //     }
  //   }
  // },
  methods: {
    hasHistory() {
      return window.history.length > 2;
    },
    initializeForm(){
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
          if (this.loan.status == "approved" && this.loan.overdue_balance) {
            this.form.outstanding_balance = this.loan.overdue_balance;
          }
          if (this.loan.type == "with collateral" && this.loan.collateral) {
            this.form.collateral = this.loan.collateral;
          }
        } catch (error) {
          console.log("ERROR: User could not be found.", error);
        }
      }
    },
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
          overdue_balance: this.form.overdue_balance,
          collateral: this.form.collateral,
        })
        .then(() => this.$router.push("/admin/dashboard"))
        .catch((error) => {
          console.log("ERROR: Loan could not be updated.", error);
        });
    },
  },
};
</script>
