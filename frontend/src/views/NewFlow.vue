<template>
  <div class="flex-container">
    <div class="flex-child">
      <div
        class="vue-flow__node-input"
        :draggable="true"
        @dragstart="ondragstart($event, 'input')"
      >
        Input Node
      </div>
    </div>
    <div class="flex-child" @drop="onDrop">
      <VueFlow
        v-model="elements"
        :default-zoom="0.7"
        :min-zoom="0.2"
        :max-zoom="4"
        @connect="onConnect"
        @dragover="onDragOver"
      >
        <Background />
        <Controls />
      </VueFlow>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import type { Elements, FlowEvents, VueFlowStore } from "@braks/vue-flow";
import { Background, Controls, VueFlow, addEdge } from "@braks/vue-flow";

// Local Imports
import FlowSidebar from "@/components/FlowSidebar.vue";

import "@braks/vue-flow/dist/style.css";
import "@braks/vue-flow/dist/theme-default.css";

export default defineComponent({
  name: "NewFlow",
  components: { VueFlow, Background, Controls, FlowSidebar },
  data() {
    return {
      instance: null as VueFlowStore | null,
      elements: [
        {
          id: "1",
          type: "input",
          label: "Node 1",
          position: { x: 250, y: 5 },
          class: "light",
        },
        {
          id: "2",
          label: "Node 2",
          position: { x: 100, y: 100 },
          class: "light",
        },
        {
          id: "3",
          label: "Node 3",
          position: { x: 400, y: 100 },
          class: "light",
        },
        {
          id: "-4",
          label: "Node -4",
          position: { x: 400, y: 200 },
          class: "light",
        },
        { id: "e1-2", source: "1", target: "2", animated: true },
        { id: "e1-3", source: "1", target: "3", animated: true },
        { id: "e1-4", source: "1", target: "-4", animated: true },
      ] as Elements,
    };
  },
  methods: {
    onConnect(params: FlowEvents["connect"]) {
      addEdge(params, this.elements);
    },
    osDragStart(e, nodeType) {
      if (e.dataTransfer) {
        e.dataTransfer.setData("application/vueflow", nodeType);
        e.dataTransfer.effectAllowed = "move";
      }
    },
    onDrop(e) {
      const type = e.dataTransfer?.getData("application/vueflow");
      const position = { x: e.clientX - 40, y: e.clientY - 18 };
      const newNode = {
        id: "-1",
        type,
        position,
        label: "test",
      };
      this.elements.push(newNode);
    },
    onDragOver(e) {
      e.preventDefault();
      if (e.dataTransfer) {
        e.dataTransfer.dropEffect = "move";
      }
    },
  },
});
</script>

<style>
.flex-container {
  display: flex;
}

.flex-child {
  border: 2px solid yellow;
}

.flex-child:first-child {
  flex: 0.2;
  margin-right: 20px;
}
.flex-child:last-child {
  flex: 0.8;
}
.vue-flow {
  width: 50vw;
  height: 50vh;
}
.node-actions {
  position: absolute;
  right: 10px;
  top: 10px;
  z-index: 4;
}
.vue-flow__node {
  background-color: #3aa675;

  border: 0;
  border-radius: 0.5rem;

  font-weight: 500;
  font-size: 1rem;
  line-height: 1.75rem;
  color: white;

  padding: 0.5rem;
}
</style>
