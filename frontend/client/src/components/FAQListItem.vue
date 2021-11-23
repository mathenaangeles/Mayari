<template>
  <b-row>
    <b-col cols="11">
      <span v-b-toggle=faqItem.id>{{ faqItem.question }}</span>
    </b-col>
    <b-col cols="1">
      <ChevronDown />
    </b-col>
    <b-col cols="12">
        <b-collapse id=faqItem.id> {{ faqItem.answer }} </b-collapse>
    </b-col>
  </b-row>
</template>
<script>
import ChevronDown from "vue-material-design-icons/ChevronDown.vue";
export default {
  name: "FAQListItem",
  props: {
      faqItem: {
          type: Object,
          required: true
      }
  },
  components: {
    ChevronDown,
  },
};
</script>
