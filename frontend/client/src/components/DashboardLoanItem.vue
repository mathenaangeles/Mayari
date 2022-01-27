<template>
  <b-card :title="loanInfo.payment_term">
    <div v-bind:class="getClass(loanInfo.status)">{{ loanInfo.status }}</div>
    <router-link :to="`loan/${loanInfo.id}`">See Loan</router-link>
  </b-card>
</template>
<script>
export default {
  name: "DashboardLoanItem",
  props: {
    loanInfo: {
      type: Object,
      required: true,
    },
  },
  methods: {
    getClass(status) {
      return {
        "text-warning": status === "pending",
      };
    },
  },
  setup() {},
};
</script>
