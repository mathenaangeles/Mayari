<template>
  <div class="admin-dashboard">
    <b-container class="my-4">
      <h1 class="float-left mb-2">Loans</h1>
      <b-table striped bordered hover small :fields="fields" :items="loans">
        <template #cell(id)="data">
          {{ data.item.id }}
          <router-link
            :to="`loan/${data.item.id}`"
            v-b-tooltip.hover
            title="Edit Loan Info"
          >
            <Pencil />
          </router-link>
        </template>
      </b-table>
    </b-container>
  </div>
</template>
<style scoped>
.admin-dashboard {
  overflow: scroll;
}
</style>
<script>
import { mapState } from "vuex";
import Pencil from "vue-material-design-icons/Pencil.vue";
export default {
  name: "AdminDashboard",
  components: {
    Pencil,
  },
  computed: mapState({
    loans: (state) => state.loans,
  }),
  data() {
    return {
      fields: [
        "id",
        "borrower_id",
        "collateral",
        "collateral_type",
        "created_at",
        "installments",
        "interest_rate",
        "outstanding_balance",
        "overdue_balance",
        "payment_term",
        "principal",
        "requested_amount",
        "status",
        "total_amount",
      ],
    };
  },
  beforeMount() {
    this.$store.dispatch("fetchAllLoans");
  },
};
</script>
