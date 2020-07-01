<template>
  <div id="app">
    <span v-if="pop_up_message">
      <message v-bind:text="pop_up_message.text" v-bind:type="pop_up_message.type"></message>
    </span>
    <register @form_submit="register_on_submit"></register>
  </div>
</template>

<script>

import Register from './components/Register.vue';
import Message from './components/Message';

export default {
  data() {
    return {
      pop_up_message: null
    }
  },
  methods: {
    register_on_submit(data) {
      this.pop_up_message = data;
    }
  },
  name: 'App',
  components: {
    'register': Register,
    'message' : Message
  }
};
</script>

<style>
</style>
