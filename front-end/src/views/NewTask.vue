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
            <new-rule v-for="(item, index) in rule_count" v-bind:key="index" v-on:remove-rule="removeRule(index)" class="mb-2"/>
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
        rule_count: []
      }
    },
    methods: {
      removeRule(index) {
        console.log(this.rule_count)
        console.log(index)
        this.rule_count.splice(index - 1, 1)
      },
      addRule() {
        const rule_count = this.rule_count
        if (rule_count.length === 0) {
          this.rule_count.push(0)
        } else {
          this.rule_count.push(rule_count[rule_count.length - 1] + 1)
        }
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