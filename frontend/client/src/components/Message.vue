<template>
  <div  id="fade_out_message"
        v-bind:class="{'alert alert-danger'  : type === 'error',
                       'alert alert-success' : type === 'success',
                       'alert alert-info'    : type === 'info'}">
    {{ text }}
  </div>
</template>

<script>

    export default {
        props: ['text', 'type'],
        name: "Message.vue",
        mounted() {
          setTimeout( () => {fade_out_message.style.display = 'none'}, 2000)
        }
    }
</script>

<style scoped></style>
