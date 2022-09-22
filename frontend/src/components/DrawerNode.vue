<template>
  <div
    :class="'align-center node vue-flow__node-' + type"
    :draggable="true"
    @dragstart="onDragStart"
    @drop="onDrop"
  >
    {{ name }}
  </div>
</template>

<script>
export default {
  name: "DrawerNode",
  props: {
    name: String,
    type: String,
    secondaryType: String,
  },
  methods: {
    // Handle dragging from Node Menu to VueFlow
    onDragStart(e) {
      if (e.dataTransfer) {
        e.dataTransfer.setData("application/flow/type", this.type);
        e.dataTransfer.setData(
          "application/flow/type/secondary",
          this.secondaryType
        );
        e.dataTransfer.setData("application/flow/label", this.name);
        e.dataTransfer.effectAllowed = "move";
      }
    },
  },
};
</script>

<style scoped></style>
