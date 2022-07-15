<template>
  <div>
    <VueFlow
      v-model="elements"
      :default-zoom="1"
      :min-zoom="0.2"
      :max-zoom="4"
      @connect="onConnect"
      @pane-ready="onPaneReady"
      @node-drag-stop="onNodeDragStop"
    >
      <Background />
      <Controls />
    </VueFlow>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import type { Elements, FlowEvents, VueFlowStore } from "@braks/vue-flow";
import {
  Background,
  Controls,
  MiniMap,
  VueFlow,
  addEdge,
  isNode,
} from "@braks/vue-flow";

import "@braks/vue-flow/dist/style.css";
import "@braks/vue-flow/dist/theme-default.css";

export default defineComponent({
  name: "NewFlow",
  components: { VueFlow, Background, MiniMap, Controls },
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
          id: "4",
          label: "Node 4",
          position: { x: 400, y: 200 },
          class: "light",
        },
        { id: "e1-2", source: "1", target: "2", animated: true },
        { id: "e1-3", source: "1", target: "3", animated: true },
        { id: "e1-4", source: "1", target: "4", animated: true },
      ] as Elements,
    };
  },
  methods: {
    logToObject() {
      console.log(this.instance?.toObject());
    },
    resetTransform() {
      this.instance?.setTransform({ x: 0, y: 0, zoom: 1 });
    },
    toggleclass() {
      this.elements.forEach(
        (el) => (el.class = el.class === "light" ? "dark" : "light")
      );
    },
    updatePos() {
      this.elements.forEach((el) => {
        if (isNode(el)) {
          el.position = {
            x: Math.random() * 400,
            y: Math.random() * 400,
          };
        }
      });
    },
    onNodeDragStop(e: FlowEvents["nodeDragStop"]) {
      console.log("drag stop", e);
    },
    onPaneReady(instance: FlowEvents["paneReady"]) {
      instance.fitView();
      this.instance = instance;
    },
    onConnect(params: FlowEvents["connect"]) {
      addEdge(params, this.elements);
    },
  },
});
</script>

<style>
.vue-flow {
  width: 100vw;
  height: 100vh;
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
