<template>
  <div class="faq">
    <b-jumbotron class="m-0 pt-1 faq-hero">
      <div>
        <transition name="fade" appear>
          <b-row class="m-0 p-0">
            <b-col md="9" sm="12" class="my-2">
              <FAQCalculator />
            </b-col>
            <b-col
              md="3"
              sm="12"
              class="my-2"
              align="start"
              align-self="center"
            >
              <h2 class="ctv-header">
                We offer the best online lending rates in the country.
              </h2>
              <b-form>
                <b-input-group class="mt-3 mb-2">
                  <b-input-group-prepend>
                    <span class="icon-prepend mt-1"><Email /></span>
                  </b-input-group-prepend>
                  <b-form-input
                    id="ctv-email"
                    v-model="form.email"
                    type="email"
                    placeholder="Enter your email"
                    required
                  ></b-form-input>
                </b-input-group>
                <b-input-group class="mt-2 mb-3">
                  <b-input-group-prepend>
                    <span class="icon-prepend mt-1"><Phone /></span>
                  </b-input-group-prepend>
                  <b-form-input
                    id="ctv-mobile"
                    v-model="form.mobile"
                    placeholder="Enter your mobile number"
                    required
                  ></b-form-input>
                </b-input-group>
                <b-link @click="applyNow" type="submit" class="ctv-button">
                  Start your application now &nbsp;
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
              </b-form>
            </b-col>
          </b-row>
        </transition>
      </div>
    </b-jumbotron>
    <div class="faq-section mt-4">
      <b-container fluid class="px-5">
        <h2 class="faq-header">Frequently Asked Questions</h2>
        <div class="my-3">
          <b-row align-h="around">
            <b-col md="6" data-aos="fade">
              <h3>General</h3>
              <transition-group name="fade" tag="div" appear>
                <FAQListItem
                  v-for="faqItem in faqGeneral"
                  :key="faqItem.id"
                  :faqItem="faqItem"
                >
                </FAQListItem>
              </transition-group>
            </b-col>
            <b-col md="6" data-aos="fade">
              <h3>Legal</h3>
              <transition-group name="fade" tag="div" appear>
                <FAQListItem
                  v-for="faqItem in faqLegal"
                  :key="faqItem.id"
                  :faqItem="faqItem"
                >
                </FAQListItem>
              </transition-group>
            </b-col>
          </b-row>
          <b-row align-h="around">
            <b-col md="6" data-aos="fade">
              <h3>Application</h3>
              <transition-group name="fade" tag="div" appear>
                <FAQListItem
                  v-for="faqItem in faqApplication"
                  :key="faqItem.id"
                  :faqItem="faqItem"
                >
                </FAQListItem>
              </transition-group>
            </b-col>
            <b-col md="6" data-aos="fade">
              <h3>Repayment</h3>
              <transition-group name="fade" tag="div" appear>
                <FAQListItem
                  v-for="faqItem in faqRepayment"
                  :key="faqItem.id"
                  :faqItem="faqItem"
                >
                </FAQListItem>
              </transition-group>
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
  background-image: linear-gradient(#f14f8c, #ca4de5);
  border-radius: 0;
}
.ctv-header,
.ctv-button {
  font-weight: bold;
  color: white;
}
.ctv-button {
  font-size: 20px;
  background: transparent;
  border: 0px;
}
input::placeholder,
input {
  color: white;
}
#ctv-email,
#ctv-mobile {
  background-color: rgba(0, 0, 0, 0);
  border-top-style: hidden;
  border-right-style: hidden;
  border-left-style: hidden;
  border-radius: 0px;
  border-bottom: 2px solid white;
  color: white;
  outline: none !important;
}
input,
input:focus {
  outline: none;
  -webkit-appearance: none;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.icon-prepend {
  color: white;
  border-bottom: 2px solid white;
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
  font-weight: bold;
}
</style>
<script>
import FAQCalculator from "@/components/FAQCalculator.vue";
import FAQListItem from "../components/FAQListItem.vue";
import Email from "vue-material-design-icons/Email.vue";
import Phone from "vue-material-design-icons/Phone.vue";
export default {
  name: "FAQ",
  data() {
    return {
      form: {
        email: "",
        mobile: "",
      },
      show: true,
      faqGeneral: [
        {
          id: "id13",
          question: "What is Mayari?",
          answer:
            "Mayari is an online lending company that enables local businesses to achieve financial success. We make it possible for borrowers to secure low-interest loans from the comfort of their own homes.",
        },
        {
          id: "id14",
          question: "Is Mayari a government institution or a bank?",
          answer:
            "We are neither a government institution nor a bank. Mayari is a private lending company registered with the Philippine Securities and Exchange Commission. ",
        },
      ],
      faqApplication: [
        {
          id: "id1",
          question: "How will I know if my application is approved?",
          answer:
            "A confirmation message will be sent to your registered email address within 24 to 48 hours after submitting your application.",
        },
        {
          id: "id2",
          question: "What are examples of a valid proof of income?",
          answer:
            "Examples of a valid proof of income are salary slips, bank statements, and Annual Income Tax Returns.",
        },
        {
          id: "id3",
          question: "What are examples of a valid personal identification?",
          answer:
            "Any government-issued ID counts as valid personal identification. Examples are passports, driver's licenses, or national IDs.",
        },
        {
          id: "id4",
          question:
            "What are the eligibility requirements to apply for a loan?",
          answer:
            "The applicant must be 21-65 years of age, a Filipino citizen, and either employed or self-employed.",
        },
        {
          id: "id5",
          question: "Can I get a new loan if I have an ongoing one?",
          answer: "No, applicants may only have one active loan at a time.",
        },
        {
          id: "id6",
          question: "Can I get a loan if I have a bad credit history?",
          answer:
            "Mayari extends loans to eligible applicants irrespective of their credit history.",
        },
        {
          id: "id7",
          question: "Is this available anywhere in the Philippines?",
          answer:
            "Yes, Mayari can be accessed anywhere within the Philippines.",
        },
      ],
      faqLegal: [
        {
          id: "id8",
          question: "Is there a penalty for late payments?",
          answer:
            "Yes, late payments will be subject to penalties charged in the next billing statement.",
        },
      ],
      faqRepayment: [
        {
          id: "id9",
          question: "How will I be billed?",
          answer:
            "Loan billing statements will be sent every 10th of the following month and must be settled before the 25th.",
        },
        {
          id: "id10",
          question: "How will I send my monthly payment?",
          answer:
            "Principal and interest payments may be sent through any accredited bank and other e-wallet.",
        },
        {
          id: "id11",
          question: "How much interest will I pay?",
          answer:
            "The interest rate will be based on the loan amount and the repayment term.",
        },
        {
          id: "id12",
          question: "How long will I have to pay the borrowed amount?",
          answer:
            "Mayari offers flexible payment terms within a minimum of 1 month up to 12 months.",
        },
      ],
    };
  },
  methods: {
    applyNow: function () {
      if (!this.$store.getters.isAuthenticated) {
        this.$router.push({
          name: "register",
          params: { email: this.form.email, term: this.form.mobile },
        });
      } else {
        this.$router.push({
          name: "apply",
        });
      }
    },
  },
  components: {
    FAQCalculator,
    FAQListItem,
    Email,
    Phone,
  },
};
</script>
