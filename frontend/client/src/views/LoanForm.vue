<template>
  <div
    class="d-flex flex-column loan-multistep-form"
    style="justify-content: space-between"
  >
    <b-row class="text-center mt-2 mb-4">
      <b-col>
        <img src="img/mayari-icon-cropped.png" style="height: 6rem" />
      </b-col>
    </b-row>
    <b-row>
      <b-col
        v-for="stepVal in totalSteps"
        :key="stepVal"
        lg="4"
        class="text-center d-flex align-items-center bg-secondary mt-3 mb-5"
        style="justify-content: center; height: 3px"
        :class="{ 'bg-step': stepVal <= step }"
      >
        <div class="d-flex align-items-center py-4 mb-5">
          <span class="text-left" style="font-size: 1.5rem">
            <strong class="step-title">{{ stepContent[stepVal - 1] }}</strong>
          </span>
        </div>
      </b-col>
    </b-row>
    <b-row class="loan-form-section text-center p-5">
      <b-col>
        <b-card class="text-left loan-form">
          <div>
            <div class="mt-4">
              <b-form @submit="onSubmitLoan">
                <div v-if="step == 1">
                  <div class="text-left">
                    <h2>01. Personal Information</h2>
                    <hr class="border-dark" style="border-width: 3px" />
                  </div>
                  <b-form>
                    <b-row>
                      <b-col>
                        <b-form-group label="Birthdate">
                          <b-form-datepicker
                            v-model="v$.form1.birthdate.$model"
                            type="date"
                            required
                            :state="validateState('birthdate', 1)"
                            placeholder="Enter your date of birth (MM/DD/YYYY)"
                          ></b-form-datepicker>
                        </b-form-group>
                      </b-col>
                      <b-col>
                        <b-form-group label="Street Address">
                          <b-form-input
                            v-model="v$.form1.street_address.$model"
                            :state="validateState('street_address', 1)"
                            required
                            placeholder="Enter your street address"
                          ></b-form-input>
                        </b-form-group>
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col>
                        <b-form-group label="City">
                          <b-form-input
                            v-model="v$.form1.city.$model"
                            :state="validateState('city', 1)"
                            required
                            placeholder="Enter your city"
                          ></b-form-input>
                        </b-form-group>
                      </b-col>
                      <b-col>
                        <b-form-group label="Zip Code">
                          <b-form-input
                            v-model="v$.form1.zip_code.$model"
                            :state="validateState('zip_code', 1)"
                            placeholder="Enter your zip code"
                            required
                          ></b-form-input>
                        </b-form-group>
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col>
                        <b-form-group label="Region">
                          <b-form-select
                            v-model="v$.form1.region.$model"
                            :options="regions"
                            :state="validateState('region', 1)"
                            placeholder="Select your region"
                          ></b-form-select>
                        </b-form-group>
                      </b-col>
                      <b-col>
                        <b-form-group label="Country">
                          <b-form-select
                            v-model="v$.form1.country.$model"
                            :state="validateState('country', 1)"
                            :options="countries"
                            required
                            placeholder="Select your country"
                          ></b-form-select>
                        </b-form-group>
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col>
                        <b-form-group label="Gender">
                          <b-form-select
                            v-model="v$.form1.gender.$model"
                            :state="validateState('gender', 1)"
                            :options="genders"
                            required
                            placeholder="Select your gender"
                          >
                          </b-form-select>
                        </b-form-group>
                      </b-col>
                      <b-col>
                        <b-form-group label="Marital Status">
                          <b-form-select
                            v-model="v$.form1.marital_status.$model"
                            :options="marital_statuses"
                            :state="validateState('marital_status', 1)"
                            placeholder="Select your marital status"
                          ></b-form-select>
                        </b-form-group>
                      </b-col>
                    </b-row>
                  </b-form>
                </div>
                <div v-if="step == 2">
                  <div class="text-left">
                    <h2>02. Business Information</h2>
                    <hr class="border-dark" style="border-width: 3px" />
                  </div>
                  <div class="custom-checkbox ml-4 mb-4">
                    <input
                      type="checkbox"
                      id="checkbox"
                      class="custom-control-input"
                      v-model="v$.form2.isHomeAddress.$model"
                      @change="onCheck"
                    />
                    <label class="custom-control-label" for="checkbox"
                      >&nbsp;Is your business address the same as your personal
                      address?</label
                    >
                  </div>
                  <b-row>
                    <b-col>
                      <b-form-group label="Company Name">
                        <b-form-input
                          v-model="v$.form2.name.$model"
                          :state="validateState('name', 2)"
                          required
                          placeholder="Enter your company name"
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col>
                      <b-form-group label="Street Address">
                        <b-form-input
                          v-model="v$.form2.street_address.$model"
                          :state="validateState('street_address', 2)"
                          required
                          placeholder="Enter your street address"
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      <b-form-group label="City">
                        <b-form-input
                          v-model="v$.form2.city.$model"
                          :state="validateState('city', 2)"
                          required
                          placeholder="Enter your city"
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col>
                      <b-form-group label="Zip Code">
                        <b-form-input
                          v-model="v$.form2.zip_code.$model"
                          :state="validateState('zip_code', 2)"
                          placeholder="Enter your zip code"
                          required
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      <b-form-group label="Industry">
                        <b-form-input
                          v-model="v$.form2.industry.$model"
                          :state="validateState('industry', 2)"
                          required
                          placeholder="Enter your industry"
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col>
                      <b-form-group label="Monthly Income">
                        <b-form-input
                          v-model="v$.form2.monthly_income.$model"
                          :state="validateState('monthly_income', 2)"
                          type="number"
                          required
                          placeholder="Enter your annual income"
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      <b-form-group label="Monthly Expenses">
                        <b-form-input
                          v-model="v$.form2.monthly_expenses.$model"
                          :state="validateState('monthly_expenses', 2)"
                          type="number"
                          required
                          placeholder="Enter your monthly expenses"
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col>
                      <b-form-group label="Year(s) of Business">
                        <b-form-input
                          v-model="v$.form2.years.$model"
                          :state="validateState('years', 2)"
                          type="number"
                          required
                          placeholder="Enter your year(s) of business"
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                  </b-row>
                </div>
                <div v-if="step == 3">
                  <div class="text-left">
                    <h2>03. Loan Details</h2>
                    <hr class="border-dark" style="border-width: 3px" />
                  </div>
                  <b-form>
                    <b-form-group label="Requested Amount">
                      <b-form-input
                        :state="validateState('requested_amount', 3)"
                        v-model="v$.form3.requested_amount.$model"
                        placeholder="Enter a requested loan amount"
                        required
                      ></b-form-input>
                    </b-form-group>
                    <b-form-group label="Payment Term">
                      <b-form-input
                        :state="validateState('payment_term', 3)"
                        v-model="v$.form3.payment_term.$model"
                        placeholder="Enter how long the loan will last in months"
                        required
                      >
                      </b-form-input>
                    </b-form-group>
                    <b-form-group label="Collateral Type">
                      <b-form-select
                        v-model="v$.form3.collateral_type.$model"
                        :state="validateState('collateral_type', 3)"
                        :options="collateral_types"
                        required
                      ></b-form-select>
                    </b-form-group>
                    <b-form-group label="Documents">
                      <p
                        class="text-secondary document-subtext mt-0"
                        style="font-size: 0.8rem"
                      >
                        *Only PDFs or JPGs with a maximum size of 10MB can be
                        uploaded
                      </p>
                      <p class="text-secondary mb-1">Primary Valid ID</p>
                      <b-form-file
                        v-model="v$.form3.primary_id.$model"
                        :state="Boolean(v$.form3.primary_id.$model)"
                        placeholder="Choose a file or drop it here..."
                        drop-placeholder="Drop file here..."
                      ></b-form-file>
                      <p class="text-secondary mt-3 mb-1">
                        Proof of Income (e.g. 1-Month Payslip, Tax Returns, or
                        Bank Statements)
                      </p>
                      <b-form-file
                        v-model="v$.form3.proof_of_income.$model"
                        :state="Boolean(v$.form3.proof_of_income.$model)"
                        placeholder="Choose a file or drop it here..."
                        drop-placeholder="Drop file here..."
                      ></b-form-file>
                    </b-form-group>
                  </b-form>
                </div>
                <div class="text-right">
                  <b-button
                    v-if="step > 1"
                    class="mx-2"
                    variant="outline-dark"
                    @click="onPrevious"
                    >Previous</b-button
                  >
                  <b-button
                    v-if="step < 3"
                    class="mx-2"
                    variant="dark"
                    @click="onNext"
                    >Next</b-button
                  >
                  <b-button
                    v-if="step === 3"
                    class="mx-2"
                    type="submit"
                    variant="dark"
                    :disabled="disableSubmit"
                    >Submit</b-button
                  >
                </div>
              </b-form>
            </div>
          </div>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>
<style scoped>
.loan-form *:not(input):not(.custom-select):not(.document-subtext) {
  font-weight: 700;
}
.loan-form {
  border: 0px;
  border-radius: 10px;
  box-shadow: 2px 4px 6px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.loan-form-section {
  background-color: #e5e5e5;
  min-height: 100vh;
  margin-top: -50px;
}
.bg-step {
  background-color: #b456de !important;
}
.step-container {
  height: 75px;
  width: 75px;
  border-radius: 50%;
  justify-content: center;
  padding: 10rem;
}
.custom-checkbox .custom-control-input:checked ~ .custom-control-label::before {
  background-color: black !important;
}
.custom-checkbox
  .custom-control-input:checked:focus
  ~ .custom-control-label::before {
  box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem #e5eef7;
}
.custom-checkbox .custom-control-input:focus ~ .custom-control-label::before {
  box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem #e5eef7;
}
.custom-checkbox .custom-control-input:active ~ .custom-control-label::before {
  background-color: black;
}
</style>
<script>
import {
  required,
  minLength,
  maxLength,
  integer,
  decimal,
  minValue,
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
export default {
  name: "LoanForm",
  components: {},
  data: () => {
    return {
      disableSubmit: false,
      totalSteps: 3,
      step: 1,
      stepContent: [
        "01. Personal Information",
        "02. Business Information",
        "03. Loan Information",
      ],
      form1: {
        birthdate: new Date(),
        street_address: "",
        city: "",
        zip_code: "",
        region: null,
        country: null,
        gender: null,
        marital_status: null,
      },
      form2: {
        isHomeAddress: false,
        name: "",
        street_address: "",
        city: "",
        zip_code: "",
        industry: "",
        monthly_income: 0,
        monthly_expenses: 0,
        years: 0,
      },
      form3: {
        requested_amount: 0,
        payment_term: 0,
        collateral_type: null,
        primary_id: null,
        proof_of_income: null,
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
  setup: () => ({ v$: useVuelidate() }),
  validations() {
    return {
      form1: {
        birthdate: {
          required,
          minValue(val) {
            return (
              this.calcDate(new Date(), new Date(val)) >= 21 &&
              this.calcDate(new Date(), new Date(val)) <= 65
            );
          },
        },
        street_address: { required, minLength: minLength(3) },
        city: { required },
        zip_code: {
          required,
          minLength: minLength(4),
          maxLength: maxLength(4),
          integer,
        },
        region: { required },
        country: { required },
        gender: { required },
        marital_status: { required },
      },
      form2: {
        isHomeAddress: {},
        name: { required, minLength: minLength(3) },
        street_address: { required, minLength: minLength(3) },
        city: { required },
        zip_code: {
          required,
          minLength: minLength(4),
          maxLength: maxLength(4),
          integer,
        },
        industry: { required },
        monthly_income: { required, decimal, minValue: minValue(1) },
        monthly_expenses: { required, decimal, minValue: minValue(1) },
        years: { required, integer, minValue: minValue(0) },
      },
      form3: {
        requested_amount: { required },
        payment_term: { required },
        collateral_type: { required },
        primary_id: { required },
        proof_of_income: { required },
      },
    };
  },
  methods: {
    calcDate(date1, date2) {
      var diff = Math.floor(date1.getTime() - date2.getTime());
      var day = 1000 * 60 * 60 * 24;
      var days = Math.floor(diff / day);
      var months = Math.floor(days / 31);
      var years = Math.floor(months / 12);
      return years;
    },
    validateState(name, step) {
      let form;
      switch (step) {
        case 1:
          form = this.v$.form1;
          break;
        case 2:
          form = this.v$.form2;
          break;
        case 3:
          form = this.v$.form3;
          break;
        default:
          form = null;
          break;
      }
      const { $dirty, $error } = form[name];
      return $dirty ? !$error : null;
    },
    onNext() {
      if (this.step === 1) {
        this.v$.form1.$touch();
        if (this.v$.form1.$invalid) {
          return;
        }
      } else if (this.step === 2) {
        this.v$.form2.$touch();
        if (this.v$.form2.$invalid) {
          console.log("FORM2", this.v$.form2);
          return;
        }
      }
      this.step++;
    },
    onPrevious() {
      this.step--;
    },
    onCheck() {
      if (this.form2.isHomeAddress) {
        this.form2.street_address = this.form1.street_address;
        this.form2.city = this.form1.city;
        this.form2.zip_code = this.form1.zip_code;
      }
    },
    onSubmitLoan(event) {
      event.preventDefault();
      this.disableSubmit = true;
      const promise1 = this.$store.dispatch("updateUser", {
        birthdate: this.form1.birthdate,
        street_address: this.form1.street_address,
        city: this.form1.city,
        zip_code: this.form1.zip_code,
        region: this.form1.region,
        country: this.form1.country,
        gender: this.form1.gender,
        marital_status: this.form1.marital_status,
      });
      let loan = new FormData();
      loan.append("primary_id", this.form3.primary_id);
      loan.append("proof_of_income", this.form3.proof_of_income);
      loan.append("name", this.form2.name);
      loan.append("street_address", this.form2.street_address);
      loan.append("city", this.form2.city);
      loan.append("zip_code", this.form2.zip_code);
      loan.append("industry", this.form2.industry);
      loan.append("monthly_income", this.form2.monthly_income);
      loan.append("monthly_expenses", this.form2.monthly_expenses);
      loan.append("years", this.form2.years);
      loan.append("requested_amount", this.form3.requested_amount);
      loan.append("payment_term", this.form3.payment_term);
      loan.append("collateral_type", this.form3.collateral_type);
      const promise2 = this.$store.dispatch("postLoan", loan);
      promise2
        .then(() => this.$router.push("/dashboard"))
        .catch((error) => {
          console.log("ERROR: Loan could not be created.", error);
        });
      Promise.all([promise1, promise2])
        .then(() => {
          this.$router.push("/dashboard");
          this.disableSubmit = false;
        })
        .catch((error) => {
          console.log("ERROR: Loan could not be created.", error);
          this.disableSubmit = false;
        });
    },
  },
  created: function () {
    let user = this.$store.state.user;
    if (user) {
      try {
        this.form1.birthdate = new Date(user.birthdate) ?? new Date();
        this.form1.street_address = user.street_address ?? "";
        this.form1.city = user.city ?? "";
        this.form1.zip_code = user.zip_code ?? "";
        this.form1.region = user.region;
        this.form1.country = user.country;
        this.form1.gender = user.gender;
        this.form1.marital_status = user.marital_status;
      } catch (error) {
        console.log("ERROR: User could not be found.", error);
      }
    }
  },
};
</script>
