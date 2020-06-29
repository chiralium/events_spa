<template>
    <div class="d-flex justify-content-center">
    <div class="card" style="width: 18rem">
      <div class="card-body">
        <h5 class="card-title">Регистрация</h5>
        <h6 class="card-subtitle mb-2 text-muted">Введите e-mail и пароль для регистрации</h6>
        <p class="card-text">
          <form>
            <div class="form-group">
              <label for="exampleInputEmail1">Email</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="example@mail.com">
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Пароль</label>
              <input type="password" class="form-control" id="exampleInputPassword1">
            </div>
            <button type="submit" class="btn btn-primary">Регистрация</button>
          </form>
        </p>
      </div>
    </div>
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
