<template>
  <div class="loan-form">
    <b-form @submit="onSubmit">
      <b-form-group label="Birthdate">
        <b-form-input
          v-model="form.birthdate"
          placeholder="Enter birthdate"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group label="Country">
        <b-form-input
          v-model="form.country"
          placeholder="Enter country"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group label="Region">
        <b-form-select
          v-model="form.region"
          :options="regions"
          required
        ></b-form-select>
      </b-form-group>
      <b-form-group>
        <b-form-checkbox-group v-model="form.business.isHomeAddress">
          <b-form-checkbox>Is your business address the same as your home address?</b-form-checkbox>
        </b-form-checkbox-group>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>
<style scoped></style>
<script>
export default {
  name: "LoanForm",
  components: {},
  data: () => {
    return {
      step: 0,
      form: {
        birthdate: new Date(),
        street_address: '',
        city: '',
        zip_code: '',
        region: null,
        country: '',
        gender: '',
        marital_status: '',
        business: {
          isHomeAddress: false,
          name: '',
          street_address: '',
          city: '',
          zip_code: '',
          industry: '',
          monthly_income: 0,
          monthly_expenses: 0,
          years: 0,
        },
        requested_amount: 0,
        payment_term: 0,
        collateral_type: '',
      },
      regions: [{ text: 'Select a region', value: null }, 'Region I', 'Region II'],
    };
  },
  methods: {
    onSubmit (event) {
      event.preventDefault();
      this.$store.dispatch('postLoan', {
        requested_amount: this.form.requested_amount,
        payment_term: this.form.payment_term,
        collateral_type: this.form.collateral_type,
        business: this.form.business,
      })
      .then(() => this.$router.push('/dashboard'))
      .catch((error) => {
        console.log('ERROR: Loan could not be created.', error)
      })
  },
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>
