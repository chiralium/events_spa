<template>
    <div>
      <p>{{ msg }}</p>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Register",
        data() {
          return {
            msg: "***"
          }
        },
        methods: {
          /* getting the main message */
          getMessage() {
            const path = "http://127.0.0.1:8000/api/register";
            axios.get(path).then((res) => {
              if (res.data.error) this.msg = "Something gonna wrong";
              else this.msg = res.data.message;
            })
          }
        },
        created() {
          this.getMessage()
        }
    }
</script>

<style scoped>

</style>
