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
            msg: ""
          }
        },
        methods: {
          getMessage() {
            const path = "http://127.0.0.1:8000/api/register";
            axios.get(path).then((res) => {
              this.msg = res.data;
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
