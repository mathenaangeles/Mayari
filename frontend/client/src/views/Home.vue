<template>
  <div>
    <div class="home">
      <Calculator />
    </div>
    <div class="section-grey">
      <b-container class="eligibility">
        <b-row class="eligibility-reqs">
          <b-col cols="4">What are the eligibility requirements?</b-col>
          <b-col>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
            >
              <path
                id="Icon_material-person"
                data-name="Icon material-person"
                d="M18,18a6,6,0,1,0-6-6A6,6,0,0,0,18,18Zm0,3c-4.005,0-12,2.01-12,6v3H30V27C30,23.01,22.005,21,18,21Z"
                transform="translate(-6 -6)"
              />
            </svg>
            21-65 years old
          </b-col>
          <b-col>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="27"
              height="28.5"
              viewBox="0 0 27 28.5"
            >
              <path
                id="Icon_material-location-city"
                data-name="Icon material-location-city"
                d="M22.5,16.5v-9L18,3,13.5,7.5v3h-9v21h27v-15Zm-12,12h-3v-3h3Zm0-6h-3v-3h3Zm0-6h-3v-3h3Zm9,12h-3v-3h3Zm0-6h-3v-3h3Zm0-6h-3v-3h3Zm0-6h-3v-3h3Zm9,18h-3v-3h3Zm0-6h-3v-3h3Z"
                transform="translate(-4.5 -3)"
              />
            </svg>
            Filipino citizen
          </b-col>
          <b-col cols="4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="27"
              viewBox="0 0 30 27"
            >
              <path
                id="Icon_material-business-center"
                data-name="Icon material-business-center"
                d="M15,24V22.5H4.515l-.015,6a2.99,2.99,0,0,0,3,3h21a2.99,2.99,0,0,0,3-3v-6H21V24ZM30,10.5H23.985v-3l-3-3h-6l-3,3v3H6a3.009,3.009,0,0,0-3,3V18a2.99,2.99,0,0,0,3,3h9V18h6v3h9a3.009,3.009,0,0,0,3-3V13.5A3.009,3.009,0,0,0,30,10.5Zm-9,0H15v-3h6Z"
                transform="translate(-3 -4.5)"
              />
            </svg>
            Employed or self-employed
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>
<style scoped>
.section-grey {
  background-color: #e5e5e5;
}
.eligibility {
  padding: 1em;
  font-weight: bold;
}
.eligibility .eligibility-reqs {
  display: flex; 
  align-items:center;
}
</style>
<script>
import Calculator from "@/components/Calculator.vue";

export default {
  name: "Home",
  components: {
    Calculator,
  },
};
</script>
