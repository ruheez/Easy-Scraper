<template>
  <div class="if-condition d-flex flex-column text-left">
    <div class="input-group input-group-sm mb-3">
      <!-- Database profile selector -->
      <div class="input-group input-group-sm mb-3">
        <label class="input-group-text" for="database-profile-select">DB Profile</label>
        <!-- #TODO : Add a dropdown to select the database profile -->
        <select class="form-select form-select-sm then-select" id="database-profile-select" v-model="db_profile">
          <option value="PROFILE1">PROFILE1</option>
        </select>
      </div>
      <!-- END Database profile selector -->
      <!-- Data selector -->
      <label class="input-group-text" for="data-select">Data</label>
      <select class="form-select form-select-sm then-select" id="data-select" v-model="collector_type">
        <option value="CUSTOM">CUSTOM</option>
        <option value="XPATH">XPATH</option>
        <option value="CLASS">CLASS</option>
        <option value="ID">ID</option>
      </select>
      <select v-if="collector_type !== 'CUSTOM'" class="form-select form-select-sm then-select" id="data-select" v-model="data_type">
        <option value="TEXT">TEXT</option>
        <option value="HREF">HREF</option>
      </select>
    </div>
    <!-- END Data selector -->
    <!-- Input for chosen selector value -->
    <div v-if="collector_type === 'CUSTOM'" class="input-group input-group-sm mb-3">
      <span class="input-group-text">Value</span>
      <input type="text" class="form-control" aria-label="Some Random Value">
    </div>
    <div v-if="collector_type === 'XPATH'" class="input-group input-group-sm mb-3">
      <span class="input-group-text">XPath</span>
      <input type="text" class="form-control" aria-label="/body">
    </div>
    <div v-if="collector_type === 'CLASS'" class="input-group input-group-sm mb-3">
      <span class="input-group-text">Class</span>
      <input type="text" class="form-control" aria-label="my-favorite-class">
    </div>
    <div v-if="collector_type === 'ID'" class="input-group input-group-sm mb-3">
      <span class="input-group-text">ID</span>
      <input type="text" class="form-control" aria-label="this-cool-id">
    </div>
    <!-- END Input for chosen selector value -->
    <!--
    <div class="input-group input-group-sm mb-3">
      <label class="input-group-text" for="database-type-select">Type</label>
      <select class="form-select form-select-sm then-select" id="database-type-select" v-model="database_type">
        <option value="MYSQL">MYSQL</option>
        <option value="POSTGRESQL">POSTGRESQL</option>
      </select>
    </div>
    <div class="input-group input-group-sm mb-3">
      <span class="input-group-text">User</span>
      <input type="text" class="form-control" aria-label="root">
    </div>
    <div class="input-group input-group-sm mb-3">
      <span class="input-group-text">Password</span>
      <input type="password" class="form-control" aria-label="myUltraSecretPassword">
    </div>
    <div class="input-group input-group-sm mb-3">
      <span class="input-group-text">Host</span>
      <input type="text" class="form-control" aria-label="10.1.10.1">
    </div>
    <div class="input-group input-group-sm mb-3">
      <span class="input-group-text">Port</span>
      <input type="text" class="form-control" aria-label="3306">
    </div>
    <div class="input-group input-group-sm mb-3">
      <span class="input-group-text">Schema</span>
      <input type="text" class="form-control" aria-label="Schema1">
    </div>
    -->
  </div>
</template>

<script>
  export default {
    name: "save_to_database",
    data() {
      return {
        db_profiles: [],
        db_profile: "PROFILE1",
        collector_type: "CUSTOM",
        data_type: "TEXT",
      }
    },
  }
</script>

<style>
  .helper-button {
    text-decoration: none;
    color: white;
  }
  .helper-button:hover {
    text-decoration: none;
    color: white;
    cursor: pointer;
  }
  .bg-secondary {
    background-color: #212121 !important;
  }
</style>