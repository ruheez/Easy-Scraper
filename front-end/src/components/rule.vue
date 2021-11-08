<template>
    <div class="if-condition d-flex flex-row">
      <select class="form-select form-select-sm me-2" v-on:change="checkTypeSelect" v-model="type_select">
        <option value="HTML">HTML</option>
        <option value="XPATH">XPATH</option>
        <option value="ID">ID</option>
        <option value="CLASS">CLASS</option>
      </select>
      <input v-if="type_input_show" type="text" class="form-control me-2" v-model="type_input_text">
      <select class="form-select form-select-sm me-2" v-on:change="checkRuleSelect" v-model="rule_select">
        <option value="CONTAINS">CONTAINS</option>
        <option value="EXISTS">EXISTS</option>
      </select>
      <input v-if="rule_input_show" type="text" class="form-control me-2" v-model="rule_input_text">
      <button class="btn remove-rule-btn pb-0 pt-0 ps-2 pe-2" v-on:click="this.$emit('remove-rule')">-</button>
    </div>
</template>

<script>
export default {
  name: "rule",
  data: function () {
    return {
      type_select: 'HTML',
      type_input_text: '',
      rule_select: 'CONTAINS',
      rule_input_text: '',
      //
      type_input_show: false,
      rule_input_show: true,
    }
  },
  methods: {
    checkTypeSelect() {
      const type_select = this.type_select;
      if (type_select === 'HTML') {
        this.type_input_show = false;
      } else {
        this.type_input_show = true;
      }
    },
    checkRuleSelect() {
      const rule_select = this.rule_select;
      if (rule_select === 'EXISTS') {
        this.rule_input_show = false;
      } else {
        this.rule_input_show = true;
      }
    }
  }
}
</script>

<style scoped>
  .form-select-sm,
  .form-control {
      width: 200px;
  }
  .remove-rule-btn {
    background: #212121;
    color: white;
    padding-bottom: 1px;
  }
</style>