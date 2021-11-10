<template>
  <div class="home">
    <b-jumbotron class="m-0 home-hero">
      <div class="home-circles">
        <b-row class="m=0 p-0">
          <b-col md="8" class="mt-2">
            <b-card title="Change your life one loan at a time" class="transparent-card" text-variant="white">
              <b-card-text class="home-card-text">
                We are here to support your dreams no matter your credit score.  You can get business loans as low as 2% APR.
              </b-card-text>
              <a href=#>
                <span class="home-card-subtext mr-2">Start your application now</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="22.099" height="13.501" viewBox="0 0 22.099 13.501">
                  <path id="Icon_ionic-ios-arrow-round-forward" data-name="Icon ionic-ios-arrow-round-forward" d="M21.968,11.51A.865.865,0,0,0,21.96,12.8l4.667,4.282H8.865a.917.917,0,1,0,0,1.828H26.619L21.952,23.2a.871.871,0,0,0,.008,1.294,1.059,1.059,0,0,0,1.4-.007l6.325-5.836h0a1.024,1.024,0,0,0,.207-.288.809.809,0,0,0,.077-.352.878.878,0,0,0-.284-.64l-6.325-5.836A1.042,1.042,0,0,0,21.968,11.51Z" transform="translate(-7.875 -11.252)" fill="#fff"/>
                </svg>
              </a>
            </b-card>
          </b-col>
          <b-col md="4" class="mt-2">
            <Calculator />
          </b-col>
        </b-row>
      </div>
    </b-jumbotron>
    <div class="section section-grey">
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
    <div class="section">
      <b-container>
        <div>
          <h2>How it works</h2>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="84"
            height="3"
            viewBox="0 0 84 3"
          >
            <line
              id="Line_3"
              data-name="Line 3"
              x2="84"
              transform="translate(0 1.5)"
              fill="none"
              stroke="#000"
              stroke-width="3"
              opacity="0.709"
            />
          </svg>
          <p>
            Secure your loan in just three easy steps. Start and scale your
            business today in the most convenient and cost-effective way
            possible.
          </p>
        </div>
        <div class="card-container">
          <b-card-group deck> 
            <b-card
              title="01. Complete the form"
              style="max-width: 20 rem;"
              class="custom-card mb-2">
            <b-card-text>
              Register for an account and answer a few questions. 
              Choose the loan amount and repayment terms according to your needs.
            </b-card-text>
            </b-card>
            <b-card
              title="02. Get approved"
              style="max-width: 20 rem;"
              class="custom-card mb-2">
            <b-card-text>
              Our team will verify and process your application. We will notify you 
              via SMS and email once we have matched you to an appropriate loan plan.
            </b-card-text>
            </b-card>
            <b-card
              title="03. Receive your money"
              style="max-width: 20 rem;"
              class="custom-card mb-2">
            <b-card-text>
              Your loan will be disbursed within 24 hours of being approved. 
              You can make easy monthly payment through your chosen method.
            </b-card-text>
            </b-card>
          </b-card-group>
        </div>
      </b-container>
    </div>
  </div>
</template>
<style scoped>
a, a:hover {
  text-decoration: none;
  color: white;
}
.home-hero {
  background-image: url(~@/assets/hero_circle_3.png), url(~@/assets/hero_circle_2.png), linear-gradient(#F14F8C, #FE7171);
  border-radius: 0;
  background-position: right top, top left;
  background-repeat: no-repeat;
}
.transparent-card {
  text-align:start;
  background-color: rgba(255, 255, 255, 0.01);
  backdrop-filter: blur(17px) brightness(75%);
  border: 0;
  border-radius: 10px;
}
.card-title {
  font-size: 40px;
  font-weight: bold;
}
.home-card-text {
  font-size: 20px;
  font-weight: 500;
}
.home-card-subtext {
  border-bottom: 1px solid #fff;
  padding-bottom: 2px;
  font-size: 20px;
  font-weight: 500;
}
.section-grey {
  background-color: #e5e5e5;
}
.eligibility {
  padding: 1em;
  font-weight: bold;
}
.eligibility .eligibility-reqs {
  display: flex;
  align-items: center;
}

.card-container {
  text-align: left;
}
.card-container .custom-card {
  border-top: 10px solid #000000;
  padding-top: 1em;
  font-weight: bold;
  border-radius: 10px;
  height: 250px;
  box-shadow: 2px 4px 6px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
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