<template>
  <div id="app">
    <span v-if="pop_up_message">
      <message v-bind:text="pop_up_message.text" v-bind:type="pop_up_message.type"></message>
    </span>

    <div v-if="!is_logged_in">
      <register @form_submit="register_on_submit" @logged_in="login_on_submit"></register>
    </div>

    <div v-else>
      <interface></interface>
    </div>
  </div>
</template>

<script>

import Register from './components/Register.vue';
import Message from './components/Message';
import Interface from "./components/Interface";

export default {
  data() {
    return {
      pop_up_message: null,
      is_logged_in: false
    }
  },
  methods: {
    register_on_submit(data) {
      this.pop_up_message = data;
    },

    login_on_submit(data) {
      this.is_logged_in = true;
    }
  },
  name: 'App',
  components: {
    'register': Register,
    'message' : Message,
    'interface' : Interface
  }
};
</script>

<style>
</style>
