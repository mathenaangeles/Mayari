<template>
  <div class="about">
    <b-jumbotron class="m-0 pt-1 pb-4 about-hero">
      <div class="p-4">
        <h1>We are financing the Filipino future</h1>
        <p class="mt-2">
          Mayari is a solution devised by one of the winning teams of the Youth
          Power Hacks 2021 organized by Restless Development and Unilever. It
          was founded in 2021 by a group of female entrepreneurs from the
          Philippines. We provide online lending services to local businesses.
          Our goal is to make financial services more accessible to all
          borrowers regardless of their socio-economic background.
        </p>
        <b-link
          href="#"
          class="contact-link py-2"
          v-on:click="contact()"
        >
          <span class="contact-message">Send us a message </span>
          &nbsp;
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
        </b-link>
      </div>
    </b-jumbotron>
    <section id="our-values">
      <div class="px-5 mb-4">
        <h2 class="d-block">OUR VALUES</h2>
        <span class="d-block"
          >We redesigned the 3C’s of credit to work for underserved communities
          rather than against them.
        </span>
      </div>
      <b-row class="px-5">
        <b-col md="4">
          <div class="values-item">
            <b-row align-v="center">
              <b-col md="4" class="px-0">
                <ChartDonut size="70" />
              </b-col>
              <b-col md="8" class="px-0 values-item-text">
                <h2 class="d-block mb-1">CAPACITY</h2>
                <span class="d-block">
                  All our product decisions are informed by customer data and
                  analytics.
                </span>
              </b-col>
            </b-row>
          </div>
        </b-col>
        <b-col md="4">
          <div class="values-item">
            <b-row align-v="center">
              <b-col md="4" class="px-0">
                <Domain size="70" />
              </b-col>
              <b-col md="8" class="px-1 values-item-text">
                <h2 class="d-block mb-1">CAPITAL</h2>
                <span class="d-block">
                  We provide borrowers with the capital they need to grow their
                  business.
                </span>
              </b-col>
            </b-row>
          </div>
        </b-col>
        <b-col md="4">
          <div class="values-item">
            <b-row align-v="center">
              <b-col md="4" class="px-0">
                <TooltipAccount size="70" />
              </b-col>
              <b-col md="8" class="px-1 values-item-text">
                <h2 class="d-block mb-1">CHARACTER</h2>
                <span class="d-block">
                  We take a holistic approach to our assessments and look beyond
                  the credit score.
                </span>
              </b-col>
            </b-row>
          </div>
        </b-col>
      </b-row>
    </section>
    <section id="leadership" class="p-5 m-5">
      <h2 class="mb-1">LEADERSHIP</h2>
      <span class="leadership-main-text">
        We believe that financial inclusion is a human right.
      </span>
      <b-row class="mt-4">
        <b-col md="3">
          <div id="ceo-image" class="leaders-profile"></div>
          <div>
            <span class="d-block leader-name">Mathena Angeles</span>
            <span class="d-block">Chief Executive Officer</span>
          </div>
        </b-col>
        <b-col md="3">
          <div id="coo-image" class="leaders-profile"></div>
          <div>
            <span class="d-block leader-name">Annysia Dupaya</span>
            <span class="d-block">Chief Operations Officer</span>
          </div>
        </b-col>
        <b-col md="3">
          <div id="cco-image" class="leaders-profile"></div>
          <div>
            <span class="d-block leader-name">Jannah Abellanosa</span>
            <span class="d-block">Chief Compliance Officer</span>
          </div>
        </b-col>
        <b-col md="3">
          <div id="cfo-image" class="leaders-profile"></div>
          <div>
            <span class="d-block leader-name">Andrea Combate</span>
            <span class="d-block">Chief Finance Officer</span>
          </div>
        </b-col>
      </b-row>
    </section>
  </div>
</template>
<style scoped>
.about {
  text-align: left;
  font-size: 20px;
}
.about-hero {
  background-image: linear-gradient(#f14f8c, #ca4de5);
  border-radius: 0;
  text-align: left;
  color: white;
}
.about-hero h1 {
  font-weight: bolder;
}
.contact-message {
  border-bottom: 1px solid #fff;
  padding-bottom: 2px;
}
.contact-link {
  color: white;
}
.contact-link:hover {
  background-color: #7070701c;
  border-radius: 10px;
}
section#our-values {
  padding: 2.5em;
  background-image: url(~@/assets/our-values-bg.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: 50% 40%;
  color: white;
  box-shadow: inset 0 0 0 2000px rgba(0, 0, 0, 0.568);
}
.values-item-text {
  line-height: 100%;
}
section h2 {
  font-size: 1em;
  font-weight: bolder;
}
.leadership-main-text {
  font-size: 30pt;
}
.leader-name {
  font-weight: bolder;
}
.leaders-profile {
  background-image: url(~@/assets/leaders-sample-img.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  height: 15rem;
  width: 12rem;
  -webkit-filter: grayscale(100%); /* Safari 6.0 - 9.0 */
  filter: grayscale(100%);
}
</style>
<script>
import ChartDonut from "vue-material-design-icons/ChartDonut.vue";
import Domain from "vue-material-design-icons/Domain.vue";
import TooltipAccount from "vue-material-design-icons/TooltipAccount.vue";
export default {
  name: "About",
  components: {
    ChartDonut,
    Domain,
    TooltipAccount,
  },
  data() {
    return {
      contact() {
        window.location.href =
          "mailto:inquiries@mayari.io?subject=My%20Question&body=Place%20inquiries%20here";
      },
    };
  },
};
</script>
