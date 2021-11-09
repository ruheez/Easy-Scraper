<template>
    <div class="if-condition d-flex flex-row">
      <select class="form-select form-select-sm me-2"
              v-on:change="checkTypeSelect" v-model="type_select">
        <option value="HTML">HTML</option>
        <option value="XPATH">XPATH</option>
        <option value="ID">ID</option>
        <option value="CLASS">CLASS</option>
      </select>
      <input v-if="type_input_show" type="text" class="form-control me-2" v-model="type_input_text" v-on:change="dataChanged">
      <select class="form-select form-select-sm me-2"
              v-on:change="checkRuleSelect" v-model="rule_select">
        <option value="CONTAINS">CONTAINS</option>
        <option value="EXISTS">EXISTS</option>
      </select>
      <input v-if="rule_input_show" type="text" class="form-control me-2" v-model="rule_input_text" v-on:change="dataChanged">
      <button class="btn remove-rule-btn pb-0 pt-0 ps-2 pe-2" v-on:click="this.$emit('remove-rule')">-</button>
    </div>
</template>

<script>
export default {
  name: "rule",
  props: {
    data: {
      type: Object,
      required: true
    },
    index: {
      type: Number,
      required: true
    }
  },
  data: function () {
    return {
      id: null,
      type_select: 'HTML',
      type_input_text: '',
      rule_select: 'CONTAINS',
      rule_input_text: '',
      //
      type_input_show: false,
      rule_input_show: true,
    }
  },
  beforeMount() {
    this.id = this.data.id;
    if (this.data.type_select) {
      this.type_select = this.data.type_select
      this.checkTypeSelect()
    }
    if (this.data.type_input_text) {
      this.type_input_text = this.data.type_input_text
    }
    if (this.data.rule_select) {
      this.rule_select = this.data.rule_select
      this.checkRuleSelect()
    }
    if (this.data.rule_input_text) {
      this.rule_input_text = this.data.rule_input_text
    }
  },
  methods: {
    dataChanged() {
      const new_data = {
        index: this.index,
        id: this.id,
        type_select: this.type_select,
        type_input_text: this.type_input_text,
        rule_select: this.rule_select,
        rule_input_text: this.rule_input_text
      }
      this.$emit('data-changed', new_data)
    },
    checkTypeSelect() {
      const type_select = this.type_select;
      this.type_input_show = type_select !== 'HTML';
      this.dataChanged()
    },
    checkRuleSelect() {
      const rule_select = this.rule_select;
      this.rule_input_show = rule_select !== 'EXISTS';
      this.dataChanged()
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