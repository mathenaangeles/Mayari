<template>
  <div class="container text-left mt-5 loan-form">
    <b-row>
      <b-col
        v-for="stepVal in totalSteps"
        :key="stepVal"
        class="text-center d-flex align-items-center"
        style="justify-content: center"
      >
        <div
          class="bg-secondary d-flex align-items-center step-container"
          :class="{ 'bg-info': stepVal <= step }"
        >
          <span class="text-white" style="font-size: 25px">
            <strong>{{ stepVal }}</strong>
          </span>
        </div>
      </b-col>
    </b-row>
    <div class="mt-4 border p-3 rounded"
      style="border-width: 3px">
      <div v-if="step == 1">
        <b-form @submit="onSubmitUser">
          <b-form-group label="Birthdate">
            <b-form-datepicker
              v-model="form.birthdate"
              type="date"
              required
            ></b-form-datepicker>
          </b-form-group>
          <b-form-group label="Street Address">
            <b-form-input v-model="form.street_address" required></b-form-input>
          </b-form-group>
          <b-form-group label="City">
            <b-form-input v-model="form.city" required></b-form-input>
          </b-form-group>
          <b-form-group label="Zip Code">
            <b-form-input v-model="form.zip_code" required></b-form-input>
          </b-form-group>
          <b-form-group label="Country">
            <b-form-select
              v-model="form.country"
              :options="countries"
              required
            ></b-form-select>
          </b-form-group>
          <b-form-group label="Region">
            <b-form-select
              v-model="form.region"
              :options="regions"
              required
            ></b-form-select>
          </b-form-group>
          <b-form-group label="Gender">
            <b-form-select v-model="form.gender" :options="genders" required>
            </b-form-select>
          </b-form-group>
          <b-form-group label="Marital Status">
            <b-form-select
              v-model="form.marital_status"
              :options="marital_statuses"
              required
            ></b-form-select>
          </b-form-group>
        </b-form>
      </div>
      <div v-if="step == 2">
        <b-form>
          <b-form-group>
            <b-form-checkbox v-model="form.isHomeAddress" @change="onCheck">
              Is your business address the same as your home address?
            </b-form-checkbox>
          </b-form-group>
          <b-form-group label="Name">
            <b-form-input v-model="form.business.name" required></b-form-input>
          </b-form-group>
          <b-form-group label="Street Address">
            <b-form-input
              v-model="form.business.street_address"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group label="City">
            <b-form-input v-model="form.business.city" required></b-form-input>
          </b-form-group>
          <b-form-group label="Zip Code">
            <b-form-input
              v-model="form.business.zip_code"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group label="Industry">
            <b-form-input
              v-model="form.business.industry"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group label="Monthly Income">
            <b-form-input
              v-model="form.business.monthly_income"
              type="number"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group label="Monthly Expenses">
            <b-form-input
              v-model="form.business.monthly_expenses"
              type="number"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group label="Years in Business">
            <b-form-input
              v-model="form.business.years"
              type="number"
              required
            ></b-form-input>
          </b-form-group>
        </b-form>
      </div>
      <div v-if="step == 3">
        <b-form @submit="onSubmitLoan">
          <b-form-group label="Requested Amount">
            <b-form-input v-model="form.requested_amount" required></b-form-input>
          </b-form-group>
          <b-form-group label="Payment Term">
            <b-form-input v-model="form.payment_term" required></b-form-input>
          </b-form-group>
          <b-form-group label="Collateral Type">
            <b-form-select
              v-model="form.collateral_type"
              :options="collateral_types"
              required
            ></b-form-select>
          </b-form-group>
        </b-form>
      </div>
      <div class="text-center">
        <b-button v-if="step > 1" class="mx-2" variant="secondary" @click="onPrevious">Previous</b-button>
        <b-button v-if="step < 3" class="mx-2" variant="primary" @click="onNext">Next</b-button>
        <b-button v-if="step === 3" class="mx-2" type="submit" variant="primary">Submit</b-button>
      </div>
    </div>
  </div>
</template>
<style scoped>
.step-container {
  height: 75px;
  width: 75px;
  border-radius: 50%;
  justify-content: center;
}
</style>
<script>
export default {
  name: "LoanForm",
  components: {},
  data: () => {
    return {
      totalSteps: 3,
      step: 1,
      form: {
        birthdate: new Date(),
        street_address: "",
        city: "",
        zip_code: "",
        region: null,
        country: null,
        gender: null,
        marital_status: null,
        isHomeAddress: false,
        business: {
          name: "",
          street_address: "",
          city: "",
          zip_code: "",
          industry: "",
          monthly_income: 0,
          monthly_expenses: 0,
          years: 0,
        },
        requested_amount: 0,
        payment_term: 0,
        collateral_type: "",
      },
      regions: [
        { text: "Select a region", value: null },
        "NCR",
        "CAR",
        "Region I",
        "Region II",
        "Region III",
        "Region IV-A",
        "Mimaropa",
        "Region V",
        "Region VI",
        "Region VII",
        "Region VIII",
        "Region IX",
        "Region X",
        "Region XI",
        "Region XII",
        "Region XIII",
        "BARMM",
      ],
      countries: [{ text: "Select a country", value: null }, "Philippines"],
      genders: [
        { text: "Select a gender", value: null },
        "Male",
        "Female",
        "Prefer not to say",
      ],
      marital_statuses: [
        { text: "Select a marital status", value: null },
        "Single",
        "Married",
      ],
      collateral_types: [
        { text: "Select a collateral type", value: null },
        "with collateral",
        "no collateral",
      ],
    };
  },
  methods: {
    onNext() {
      console.log(this.step);
      this.step++;
    },
    onPrevious() {
      this.step--;
    },
    onSubmitUser(event) {
      event.preventDefault();
      this.$store
        .dispatch("updateUser", {
          birthdate: this.form.birthdate,
          street_address: this.form.street_address,
          city: this.form.city,
          zip_code: this.form.zip_code,
          region: this.form.region,
          country: this.form.country,
          gender: this.form.gender,
          marital_status: this.form.marital_status,
        })
        .then(() => {
          this.onNext();
        })
        .catch((error) => {
          console.log("ERROR: User could not be updated.", error);
        });
    },
    onCheck() {
      if (this.form.isHomeAddress) {
        this.form.business.street_address = this.form.street_address;
        this.form.business.city = this.form.city;
        this.form.business.zip_code = this.form.zip_code;
      }
    },
    onSubmitLoan(event) {
      event.preventDefault();
      this.$store
        .dispatch("postLoan", {
          requested_amount: this.form.requested_amount,
          payment_term: this.form.payment_term,
          collateral_type: this.form.collateral_type,
          business: this.form.business,
        })
        .then(() => this.$router.push("/dashboard"))
        .catch((error) => {
          console.log("ERROR: Loan could not be created.", error);
        });
    },
  },
  created: function () {
    let user = this.$store.state.user;
    if (user) {
      try {
        this.form.birthdate = new Date(user.birthdate) ?? new Date();
        this.form.street_address = user.street_address ?? "";
        this.form.city = user.city ?? "";
        this.form.zip_code = user.zip_code ?? "";
        this.form.region = user.region;
        this.form.country = user.country;
        this.form.gender = user.gender;
        this.form.marital_status = user.marital_status;
      } catch (error) {
        console.log("ERROR: User could not be found.", error);
      }
    }
  },
};
</script>
