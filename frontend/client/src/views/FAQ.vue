<template>
  <div class="faq">
    <b-jumbotron class="m-0 pt-1 faq-hero">
      <div>
        <b-row class="m-0 p-0">
          <b-col md="9" sm="12" class="mt-2">
            <FAQCalculator />
          </b-col>
          <b-col md="3" sm="12" class="mt-2">
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
              <h3>General</h3>
            </b-col>
            <b-col md="6">
              <h3>Repayment</h3>
              <FAQListItem
                v-for="faqItem in faqRepayment"
                :key="faqItem.id"
                :faqItem="faqItem"
              >
              </FAQListItem>
            </b-col>
          </b-row>
          <b-row>
            <b-col md="6">
              <h3>Application</h3>
              <FAQListItem
                v-for="faqItem in faqApplication"
                :key="faqItem.id"
                :faqItem="faqItem"
              >
              </FAQListItem>
            </b-col>
            <b-col md="6">
              <h3>Legal</h3>
              <FAQListItem
                v-for="faqItem in faqLegal"
                :key="faqItem.id"
                :faqItem="faqItem"
              >
              </FAQListItem>
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
.faq-hero {
  background-image: linear-gradient(#F14F8C, #CA4DE5);
  border-radius: 0;
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
import FAQCalculator from "@/components/FAQCalculator.vue";
import ArrowRight from "vue-material-design-icons/ArrowRight";
import FAQListItem from "../components/FAQListItem.vue";
export default {
  name: "FAQ",
  data() {
    return {
      form: {
        email: "",
        mobile: "",
      },
      faqApplication: [
        {
          id: 'id1',
          question: "How will I know if my application is approved?",
          answer: 'A confirmation message will be sent to the applicant’s registered email address within 24 to 48 hours after submitting their application.'
        },
        {
          id: 'id2',
          question: "Can I get a new loan if I have an ongoing one?",
          answer: 'No. Applicants may only have one active loan at a time.'
        },
        {
          id: 'id3',
          question: "Can I get a loan if I have a bad credit history?",
          answer: 'Mayari extends loans to eligible MSMEs irrespective of their credit history.'
        },
        {
          id: 'id4',
          question: "Is this available anywhere in the Philippines?",
          answer: 'Yes. Mayari may be accessed anywhere within the Philippines.'
        },
      ],
      faqLegal: [
        {
          id: 'id5',
          question: "Is there a penalty for late payment of monthly interest?",
          answer: 'Yes. Late payment will be subject to penalties charged on the next billing statement.'
        }
      ],
      faqRepayment: [
        {
          id: 'id6',
          question: "How will I be billed?",
          answer: 'Loan billing statements will be sent every 10th of the following month and must be settled before the 25th.'
        },
        {
          id: 'id7',
          question: "How will I send my monthly payment?",
          answer: 'Principal payment and interest may be sent through accredited banks and other e-wallets.'
        },
        {
          id: 'id8',
          question: "How much interest will I pay?",
          answer: 'Interest will be based on the loan amount and repayment terms.'
        },
        {
          id: 'id9',
          question: "How long will I have to pay the borrowed amount?",
          answer: 'Mayari offers payment terms from a minimum of 3 months up to 12 months.'
        },
      ],
    };
  },
  components: {
    FAQCalculator,
    FAQListItem,
    ArrowRight
  },
};
</script>
