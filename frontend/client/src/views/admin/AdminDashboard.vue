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
            title="Edit Loan"
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
svg {
  color: #f14f8c;
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
        { key: "id", label: "ID"},
        { key: "borrower_id", label: "Borrower ID"},
        { key: "collateral", label: "Collateral"},
        { key: "created_at", label: "Created At"},
        { key: "total_amount", label: "Total Amount", formatter: (value) => {return Number((value)?.toFixed(2))}},
        { key: "installments", label: "Installments", formatter: (value) => {return Number((value)?.toFixed(2))}},
        { key: "interest_rate", label: "Interest Rate"},
        { key: "outstanding_balance", label: "Outstanding Balance", formatter: (value) => {return Number((value)?.toFixed(2))}},
        { key: "overdue_balance", label: "Overdue Balance", formatter: (value) => {return Number((value)?.toFixed(2))}},
        { key: "payment_term", label: "Payment Term"},
        { key: "principal", label: "Principal", formatter: (value) => {return Number((value)?.toFixed(2))}},
        { key: "status", label: "Status"},
      ],
    };
  },
  beforeMount() {
    this.$store.dispatch("fetchAllLoans");
  },
};
</script>
