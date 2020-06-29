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
            msg: "<no-data>"
          }
        },
        methods: {
          getMessage() {
            const path = "http://127.0.0.1:8000/api/register";
            axios.get(path).then((res) => {
              console.log(res.data);
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
