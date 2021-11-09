<template>
  <div class="mt-4">
      <div class="container">
          <div class="if-condition container-fluid d-flex flex-row ps-0">
              <span class="text-center me-2 condition rounded">IF</span>
              <select class="form-select form-select-sm me-2 if-select" v-model="if_condition">
                <option value="ALL">ALL</option>
                <option value="ANY">ANY</option>
                <option value="NONE">NONE</option>
              </select>
              <span>of these filters match</span>
          </div>
          <div class="mt-2 ps-3 pt-3 pb-3 border">
            <new-rule v-for="(item, index) in rules"
                      :key="JSON.stringify(item.id)" v-on:remove-rule="removeRule(index)"
                      :data="item" :index="index" v-on:data-changed="dataChanged"
                      class="mb-2"/>
            <div class="mt-2 add-rule-div">
              <button class="btn add-rule-btn" v-on:click="addRule">+</button>
            </div>
          </div>
      </div>
  </div>
</template>

<script>
import Rule from '@/components/rule'

export default {
    name: "NewTask",
    components: {
      'new-rule': Rule
    },
    data: function () {
      return {
        if_condition: 'ALL',
        rules: []
      }
    },
  methods: {
      dataChanged(data) {
        const rules = this.rules;
        const index = data.index;
        delete data['index'];
        rules.splice(index, 1, data)
        this.rules = rules;
      },
      removeRule(index) {
        const rules = this.rules;
        rules.splice(index, 1)
        this.rules = rules
      },
      addRule() {
        const default_id = this.rules[-1].id + 1;
        const new_rule = {
          id: default_id,
          type_input_text: null,
          type_input_show: null,
          rule_input_text: null,
          rule_input_show: null,
        }
        this.rules.push(new_rule)
      }
    }
  }
</script>

<!-- Global CSS -->
<style>
  .form-control {
    height: 27px;
  }
  .form-select-sm {
    padding-top: 0;
    padding-bottom: 0;
  }
</style>

<style scoped>
  .if-condition > .condition {
      width: 80px;
      background-color: #212121;
      color: white;
      padding-top: 1px;
  }
  .if-condition > .if-select {
    width: 90px;
  }
  .add-rule-div {
    text-align: initial;
  }
  .add-rule-div > .add-rule-btn {
    background: #212121;
    color: white;
    width: 80px;
  }
</style>