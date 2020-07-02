<template>
  <div id="app">
    <span v-if="pop_up_message">
      <message v-bind:text="pop_up_message.text" v-bind:type="pop_up_message.type"></message>
    </span>

    <div v-if="!is_logged_in">
      <register @form_submit="register_on_submit" @logged_in="login_on_submit"></register>
    </div>
    <div v-else>
      <interface @logged_out="logout_on_submit"></interface>
    </div>
  </div>
</template>

<script>

import Register from './components/Register.vue';
import Message from './components/Message';
import Interface from "./components/Interface";
import axios from 'axios';

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

    login_on_submit() {
      this.is_authenticated();
    },

    logout_on_submit() {
      this.is_logged_in = false
    },

    is_authenticated() {
      const endpoint = 'http://127.0.0.1:8000/api/login/is_auth/';
      axios({
        url : endpoint,
        method : 'get',
        withCredentials: true
      }).then((response) => {
          this.is_logged_in = response.data.is_authenticated;
      }, (error) => console.log('Authentication error', error))
    }
  },
  name: 'App',
  components: {
    'register': Register,
    'message' : Message,
    'interface' : Interface
  },
  mounted() {
    this.is_authenticated()
  }
};
</script>

<style>
</style>
