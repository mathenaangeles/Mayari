<template>
  <div class="home">
    <b-jumbotron class="m-0 home-hero">
      <b-row class="m-0 p-0">
        <b-col md="6" class="mt-2">
          <transition name="fade" appear>
            <b-card
              title="Change your life one loan at a time"
              class="transparent-card"
              text-variant="white"
              id="main-card"
            >
              <b-card-text class="home-card-text">
                We are here to support your dreams no matter your credit score.
                You can get business loans as low as 2% APR disbursed in as little
                as 1 business day.
              </b-card-text>
              <a href="/register">
                <span class="home-card-subtext mr-2"
                  >Start your application now</span
                >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="22.099"
                  height="13.501"
                  viewBox="0 0 22.099 13.501"
                >
                  <path
                    id="Icon_ionic-ios-arrow-round-forward"
                    data-name="Icon ionic-ios-arrow-round-forward"
                    d="M21.968,11.51A.865.865,0,0,0,21.96,12.8l4.667,4.282H8.865a.917.917,0,1,0,0,1.828H26.619L21.952,23.2a.871.871,0,0,0,.008,1.294,1.059,1.059,0,0,0,1.4-.007l6.325-5.836h0a1.024,1.024,0,0,0,.207-.288.809.809,0,0,0,.077-.352.878.878,0,0,0-.284-.64l-6.325-5.836A1.042,1.042,0,0,0,21.968,11.51Z"
                    transform="translate(-7.875 -11.252)"
                    fill="#fff"
                  />
                </svg>
              </a>
            </b-card>
          </transition>
        </b-col>
        <b-col md="6" class="mt-2">
          <transition name="fade" appear>
            <HomeCalculator />
          </transition>
        </b-col>
      </b-row>
    </b-jumbotron>
    <div class="section section-grey">
      <transition name="fade" appear>
        <b-container fluid class="eligibility">
          <b-row class="mx-2 eligibility-requirements"
          style="animation-duration: 2s">
            <b-col md="3" class="my-1"
              >What are the eligibility requirements?</b-col
            >
            <b-col md="3" class="my-1">
              <account />
              21-65 years old
            </b-col>
            <b-col md="3" class="my-1">
              <home-city />
              Filipino citizen
            </b-col>
            <b-col md="3" class="my-1">
              <briefcase-variant />
              Employed or self-employed
            </b-col>
          </b-row>
        </b-container>
      </transition>
    </div>
    <div class="section mt-4">
      <b-container>
        <div>
          <h2 class="how-to-header">How it works</h2>
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
          <p class="how-to-subtitle">
            Secure your loan in just three easy steps. Start and scale your
            business today in the most convenient and cost-effective way
            possible.
          </p>
        </div>
        <div class="card-container my-4" data-aos="fade">
          <b-card-group deck>
            <b-card
              title="01. Complete the form"
              style="max-width: 20 rem"
              class="custom-card mb-2 mt-1"
            >
              <b-card-text>
                Register for an account and answer a few questions. Choose a
                loan amount and a repayment term according to your needs.
              </b-card-text>
            </b-card>
            <b-card
              title="02. Get approved"
              style="max-width: 20 rem"
              class="custom-card mb-2 mt-1"
            >
              <b-card-text>
                Our team will verify and process your application. We will
                notify you via SMS and email once we have matched you to an
                appropriate loan plan.
              </b-card-text>
            </b-card>
            <b-card
              title="03. Receive your money"
              style="max-width: 20 rem"
              class="custom-card mb-2 mt-1"
            >
              <b-card-text>
                Your loan will be disbursed within 24 hours of being approved.
                You can make easy monthly payments through your chosen method.
              </b-card-text>
            </b-card>
          </b-card-group>
        </div>
      </b-container>
    </div>
  </div>
</template>
<style scoped>
a,
a:hover {
  text-decoration: none;
  color: white;
}
@media (min-width: 800px) {
  .home-hero {
    background-image: url(~@/assets/hero_circle_3.png),
      url(~@/assets/hero_circle_2.png), url(~@/assets/hero_circle_1.png),
      linear-gradient(#f14f8c, #fe7171);
    border-radius: 0;
    background-position: 120% -50%, 50% 0%, -20% 500%;
    background-repeat: no-repeat;
  }
}
@media (max-width: 799px) {
  .home-hero {
    background-image: linear-gradient(#f14f8c, #fe7171);
    border-radius: 0;
    background-position: 50% 0%;
    background-repeat: no-repeat;
  }
}

.transparent-card {
  text-align: start;
  background-color: rgba(255, 255, 255, 0.01);
  backdrop-filter: blur(17px) brightness(75%);
  border: 0;
  border-radius: 10px;
}
.card-title {
  font-weight: bold;
  font-size: 35px;
}
.home-hero > .card-title {
  font-size: 40px;
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
  font-size: 18px;
}
.eligibility .eligibility-requirements {
  display: flex;
  align-items: center;
}
.how-to-header {
  font-weight: 700;
  font-size: 40px;
}
.how-to-subtitle {
  font-size: 20px;
}
.card-container {
  text-align: left;
}
.card-container .custom-card {
  border-top: 10px solid #000000;
  padding-top: 1em;
  border-radius: 10px;
  min-height: 250px;
  font-size: 18px;
  box-shadow: 2px 4px 6px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
@supports (-moz-transform: translate(0, 0)) {
  .transparent-card {
    text-align: start;
    background-color: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(17px) brightness(75%);
    border: 0;
    border-radius: 10px;
  }
}
</style>
<script>
import HomeCalculator from "@/components/HomeCalculator.vue";
import HomeCity from "vue-material-design-icons/HomeCity.vue";
import Account from "vue-material-design-icons/Account.vue";
import BriefcaseVariant from "vue-material-design-icons/BriefcaseVariant.vue";
export default {
  name: "Home",
  components: {
    HomeCalculator,
    HomeCity,
    Account,
    BriefcaseVariant,
  },
};
</script>
