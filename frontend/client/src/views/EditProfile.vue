<template>
  <div class="edit-profile">
    <b-form @submit="onSubmit">
      <b-form-file
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
        @change="onChangePhoto"
      ></b-form-file>
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
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
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
  name: "EditProfile",
  components: {},
  data: () => {
    return {
      form: {
        birthdate: new Date(),
        street_address: "",
        city: "",
        zip_code: "",
        region: null,
        country: null,
        gender: null,
        marital_status: null,
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
    onSubmit(event) {
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
        .catch((error) => {
          console.log("ERROR: User could not be updated.", error);
        });
    },
    onChangePhoto(event) {
      const image = new FormData();
      image.append("profile_photo", event.target.files[0]);
      this.$store.dispatch("uploadProfilePhoto", image).catch((error) => {
        console.log("ERROR: Profile photo could not be updated.", error);
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
