<template>
  <div>
    <v-navigation-drawer app permanent class="text-center">
      <h1 class="mt-3">Nodes</h1>
      <v-list class="nodes">
        <v-list-item>
          <DrawerNode name="Get Url" type="default" />
          <DrawerNode name="Get Element" type="default" />
          <DrawerNode name="If" type="default" />
          <DrawerNode name="Save" type="default" />
          <DrawerNode name="End" type="output" />
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-container class="pa-0">
      <div @drop="onDrop">
        <VueFlow
          v-model="elements"
          :default-zoom="1"
          :min-zoom="0.2"
          :max-zoom="4"
          @connect="onConnect"
          @dragover="onDragOver"
        >
          <Background />
          <Controls />
        </VueFlow>
      </div>
    </v-container>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import type { Elements, FlowEvents, VueFlowStore } from "@braks/vue-flow";
import { Background, Controls, VueFlow, addEdge } from "@braks/vue-flow";
import DrawerNode from "../components/DrawerNode.vue";

import "@braks/vue-flow/dist/style.css";
import "@braks/vue-flow/dist/theme-default.css";

export default defineComponent({
  name: "NewFlow",
  components: { VueFlow, Background, Controls, DrawerNode },
  data() {
    return {
      instance: null as VueFlowStore | null,
      elements: [] as Elements,
      // Nodes loaded from DB have positive id but ones generated on client side have negative ids
      last_node_id: 0,
    };
  },
  mounted() {
    this.setupNewFlow();
  },
  methods: {
    // Add edges on VueFlow load
    onConnect(params: FlowEvents["connect"]) {
      addEdge(params, this.elements);
    },
    // Creates a start node centered on the canvas
    setupNewFlow() {
      const drawer = document.getElementsByClassName("v-navigation-drawer")[0];
      const drawerWidth = drawer.style.width.replace("px", "");
      const windowWidth = document.documentElement.clientWidth;
      const position = { x: (windowWidth - drawerWidth) / 2 - 75, y: 50 };
      const startNode = {
        id: "0",
        type: "input",
        label: "Start",
        position,
      };
      this.elements.push(startNode);
    },
    //
    getID() {
      this.last_node_id -= 1;
      return JSON.stringify(this.last_node_id);
    },
    // Handle dragging from Node Menu to VueFlow
    onDrop(e) {
      const type = e.dataTransfer?.getData("application/vueflow/type");
      const label = e.dataTransfer?.getData("application/vueflow/label");
      const position = { x: e.clientX, y: e.clientY };
      const newNode = {
        id: this.getID(),
        type,
        position,
        label,
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

<style scoped>
.vue-flow {
  width: 100%;
  height: calc(100vh - 64px);
}
.node-actions {
  position: absolute;
  right: 10px;
  top: 10px;
  z-index: 4;
}
.nodes .node {
  position: relative;
  margin-bottom: 10px;
  cursor: grab;
  left: 50%;
  transform: translateX(-50%);
}
</style>
