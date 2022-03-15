<template>
  <b-container fluid class="edit-profile p-5">
    <b-card class="text-left p-4 edit-profile-card">
      <h1 class="bold">Edit Profile</h1>
      <div>
        <div class="mt-4">
          <b-form @submit="onSubmit">
            <b-form-group class="bold" label="Profile Photo">
              <b-form-file
                :placeholder="
                  form.profile_photo
                    ? getFilename(form.profile_photo)
                    : 'Choose a file or drop it here...'
                "
                drop-placeholder="Drop file here..."
                @change="onChangePhoto"
              ></b-form-file>
            </b-form-group>
            <b-form-group class="bold" label="Birthdate">
              <b-form-datepicker
                v-model="form.birthdate"
                type="date"
                required
              ></b-form-datepicker>
            </b-form-group>
            <b-form-group class="bold" label="Street Address">
              <b-form-input
                v-model="form.street_address"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-group class="bold" label="City">
              <b-form-input v-model="form.city" required></b-form-input>
            </b-form-group>
            <b-form-group class="bold" label="Zip Code">
              <b-form-input v-model="form.zip_code" required></b-form-input>
            </b-form-group>
            <b-form-group class="bold" label="Country">
              <b-form-select
                v-model="form.country"
                :options="countries"
                required
              ></b-form-select>
            </b-form-group>
            <b-form-group class="bold" label="Region">
              <b-form-select
                v-model="form.region"
                :options="regions"
                required
              ></b-form-select>
            </b-form-group>
            <b-form-group class="bold" label="Gender">
              <b-form-select v-model="form.gender" :options="genders" required>
              </b-form-select>
            </b-form-group>
            <b-form-group class="bold" label="Marital Status">
              <b-form-select
                v-model="form.marital_status"
                :options="marital_statuses"
                required
              ></b-form-select>
            </b-form-group>
            <b-button type="submit" variant="dark">Save</b-button>
          </b-form>
        </div>
      </div>
    </b-card>
  </b-container>
</template>
<style scoped>
.edit-profile-card {
  border-radius: 10px;
  box-shadow: 2px 4px 6px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  height: 100%;
}
.edit-profile {
  background-color: #e5e5e5;
  min-height: 100vh;
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
        profile_photo: null,
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
          profile_photo: this.form.profile_photo,
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
      this.form.profile_photo = event.target.files[0].filename;
    },
    getFilename(profileLink) {
      let splitString = profileLink.split("/");
      return splitString[splitString.length - 1];
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
        this.form.profile_photo = user.profile_photo;
      } catch (error) {
        console.log("ERROR: User could not be found.", error);
      }
    }
  },
};
</script>
