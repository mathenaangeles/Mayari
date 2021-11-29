<template>
  <div class="home">
    <b-jumbotron class="m-0 home-hero">
      <div>
        <b-row class="m-0 p-0">
          <b-col md="8" sm="12" class="mt-2">
            <Calculator />
          </b-col>
          <b-col md="4" sm="12" class="mt-2">
            <b-card
              title="We offer the best online lending rates in the country. "
              class="transparent-card"
              text-variant="white"
            >
              <div>
                <b-form>
                  <b-form-group id="input-group-1">
                    <b-form-input
                      id="input-1"
                      v-model="form.email"
                      type="email"
                      placeholder="Enter your email"
                      required
                    ></b-form-input>
                  </b-form-group>
                  <b-form-group id="input-group-1">
                    <b-form-input
                      id="input-1"
                      v-model="form.mobile"
                      placeholder="Enter your mobile number"
                      required
                    ></b-form-input>
                  </b-form-group>
                  <b-button type="submit" class="form-submit-button">
                    Start your application now <ArrowRight />
                  </b-button>
                </b-form>
              </div>
            </b-card>
          </b-col>
        </b-row>
      </div>
    </b-jumbotron>
    <div class="faq-section mt-4">
      <b-container>
        <div>
          <h2 class="faq-header">Frequently Asked Questions</h2>
          <b-row>
            <b-col md="6">
              <h3>Requirements and Application Process</h3>
              <FAQListItem
                v-for="faqItem in faqOne"
                :key="faqItem.id"
                :faqItem="faqItem"
              >
              </FAQListItem>
              <b-row>
                <b-col cols="11">
                  <span v-b-toggle.faq-2>How do I apply for a loan?</span>
                </b-col>
                <b-col cols="1">
                  <ChevronDown />
                </b-col>
              </b-row>
              <b-collapse id="faq-2"> Here's the answer </b-collapse>
            </b-col>
            <b-col md="6">
              <h3>Disbursement and Repayment</h3>
            </b-col>
          </b-row>
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
.home-hero {
  background-image: linear-gradient(#f14f8c, #fe7171);
  border-radius: 0;
  background-position: right top, top left;
  background-repeat: no-repeat;
}
.transparent-card {
  text-align: start;
  background-color: rgba(255, 255, 255, 0);
  border: 0;
  border-radius: 10px;
}
.card-title {
  font-weight: bold;
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
.faq-header {
  font-weight: 700;
  font-size: 40px;
  text-align: left;
}
.faq-section {
  text-align: left;
}
.faq-section h3 {
  color: #f14f8c;
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
.form-submit-button {
  background: #00000000;
  border-style: none;
}
@supports (-moz-transform: translate(0, 0)) {
  .transparent-card {
    text-align: start;
    background-color: rgba(255, 255, 255, 0);
    border: 0;
    border-radius: 10px;
  }
}
</style>
<script>
import Calculator from "@/components/Calculator.vue";
import ArrowRight from "vue-material-design-icons/ArrowRight";
import ChevronDown from "vue-material-design-icons/ChevronDown.vue";
import FAQListItem from "../components/FAQListItem.vue";
export default {
  name: "FAQ",
  data() {
    return {
      form: {
        email: "",
        mobile: "",
      },
      faqOne: [
        {
          id: 'id1',
          question: "Question one",
          answer: 'Answer one'
        },
      ],
    };
  },
  components: {
    Calculator,
    FAQListItem,
    ArrowRight,
    ChevronDown,
  },
};
</script>
