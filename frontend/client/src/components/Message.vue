<template>
  <div
    v-bind:class="{'alert alert-danger'  : type === 'error',
                   'alert alert-success' : type === 'success',
                   'alert alert-info'    : type === 'info'}">
    {{ text }}
  </div>
</template>

<script>
    export default {
        props: ['text', 'type'],
        name: "Message.vue"
    }
</script>

<style scoped></style>
