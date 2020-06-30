<template>
    <div>
    <!-- Register form -->
    <div v-if="is_register">
      <div v-if="!form_is_valid" class="alert alert-danger" style="position: absolute; z-index: 10; top: 10%; left: 41%" role="alert">Ошибка валидации формы регистрации!</div>
        <div class="d-flex justify-content-center">
          <div class="card" style="width: 18rem">
            <div class="card-body">
              <h5 class="card-title">Регистрация</h5>
              <h6 class="card-subtitle mb-2 text-muted">Введите e-mail и пароль для регистрации</h6>
              <p class="card-text">
                  <div class="form-group">
                    <label for="exampleInputEmail1">Email</label>
                    <input v-model="email_address"
                           v-bind:class="{'form-control border border-success' : email_is_valid,
                                          'form-control border border-danger'  : !email_is_valid}"

                           type="email" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="example@mail.com">
                  </div>
                  <div class="form-group">
                    <label for="password_field">Пароль</label>
                    <input v-model="original_password" type="password" class="form-control" id="password_field">
                  </div>

                  <div class="form-group">
                    <label for="confirm_password">Подтвердите пароль</label>
                    <input v-model="confirmed_password" type="password" id="confirm_password"
                           v-bind:class="{'form-control border border-success' : is_compared,
                                          'form-control border border-danger' : !is_compared}">
                  </div>
                  <button v-on:click="form_submit()" type="submit" class="btn btn-primary">Регистрация</button>
              </p>
              <h6 class="card-subtitle mb-3 text-muted" v-on:click="change_form()"><a href="#" >Уже есть аккаунт?</a></h6>
            </div>
          </div>
        </div>
    </div>

    <!-- Login form -->
    <div v-else>
      <div v-if="!form_is_valid" class="alert alert-danger" style="position: absolute; z-index: 10; top: 10%; left: 41%" role="alert">Ошибка валидации формы регистрации!</div>
        <div class="d-flex justify-content-center">
          <div class="card" style="width: 18rem">
            <div class="card-body">
              <h5 class="card-title">Войти</h5>
              <h6 class="card-subtitle mb-2 text-muted">Введите e-mail и пароль для того чтобы войти в учетную запись</h6>
              <p class="card-text">
                  <div class="form-group">
                    <label for="exampleInputEmail1">Email</label>
                    <input v-model="email_address"
                           v-bind:class="{'form-control border border-success' : email_is_valid,
                                          'form-control border border-danger'  : !email_is_valid}"

                           type="email" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="example@mail.com">
                  </div>
                  <div class="form-group">
                    <label for="password_field">Пароль</label>
                    <input v-model="original_password" type="password" class="form-control" id="password_field">
                  </div>
                  <button v-on:click="form_submit()" type="submit" class="btn btn-primary">Войти</button>
              </p>
              <h6 class="card-subtitle mb-3 text-muted" v-on:click="change_form()"><a href="#" >Нет аккаунта?</a></h6>
            </div>
          </div>
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
            msg: "***",
            original_password: '',
            confirmed_password: '',
            email_address: '',
            form_is_valid: true,
            is_register: true
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
          },

          /* check the form fields */
          form_submit() {
            if ( (this.form_is_valid = this.is_compared && this.email_is_valid) ) this.registration();
          },

          /* change the form */
          change_form() {
            this.is_register = !this.is_register;
          },

          /* send post-request to endpoint */
          registration() {
            const endpoint = "http://127.0.0.1:8000/api/register";
            axios({
              method: 'post',
              url: endpoint,
              headers: {'Content-Type': 'multipart/form-data' },
              data: {
                email: this.register_email,
                password: this.register_password
              }
            }).then((response) => {
              if (response.data.user_exists) this.message = "Пользователь уже существует!";
              else this.message = "Регистрация прошла успешно!";
            }, (error) => console.log(error))
          }

        },

        computed: {
          /* comparing the a passwords */
          is_compared: function() {
            if (this.original_password === '') return false;
            else return this.original_password === this.confirmed_password;
          },

          /* comparing the an email */
          email_is_valid: function() {
            var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(this.email_address);
          }
        },

        created() {
          this.getMessage()
        }
    }
</script>

<style scoped>

</style>
