<template>
    <div>
    <!-- Register form -->
    <div v-if="is_register">
        <div class="d-flex justify-content-center">
          <div class="card" style="width: 25rem; margin-top: 5%">
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
          <div class="card" style="width: 25rem; margin-top: 5%">
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
                  <button v-on:click="login_form_submit()" type="submit" class="btn btn-primary">Войти</button>
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
            original_password: '',
            confirmed_password: '',
            email_address: '',

            form_is_valid: true,
            is_register: true
          }
        },

        methods: {
          /* check the login form fields */
          login_form_submit() {
            if ( (this.form_is_valid = this.email_is_valid && this.original_password !== '') ) this.login();
            else {
              this.$emit('form_submit',
                          {text : 'Ошибка валидации формы ввода!', type : 'error'})
            }
          },

          /* check the register form fields */
          form_submit() {
            if ( (this.form_is_valid = this.is_compared && this.email_is_valid) ) this.registration();
            else {
              this.$emit('form_submit',
                          {text : 'Ошибка валидации формы ввода!', type : 'error'})
            }
          },

          /* change the form */
          change_form() {
            this.is_register = !this.is_register;
          },

          /* send post-request to login endpoint */
          login() {
            const endpoint = "http://127.0.0.1:8000/api/login/";
            axios({
              method : 'post',
              url : endpoint,
              headers : { 'Content-Type': 'application/json' },
              data: JSON.stringify({
                "email" : this.email_address,
                "password" : this.original_password
              })
            }).then((response) => {
              if (response.data.logged_in) {
                this.$emit('form_submit', {text : 'Вы авторизованы!', type : 'success'})
                this.$emit('logged_in',   {data : 'logged in'});
              }
              else this.$emit('form_submit', {text : 'Ошибка авторизации', type : 'error'})
            }, (error) => console.log(error))
          },

          /* send post-request to endpoint */
          registration() {
            const endpoint = "http://127.0.0.1:8000/api/register/";
            axios({
              method: 'post',
              url: endpoint,
              headers: { 'Content-Type': 'application/json' },
              data: JSON.stringify({
                "email" : this.email_address,
                "password" : this.original_password
              })
            }).then((response) => {
              if (response.data.is_user_exists) this.$emit('form_submit', {text : 'Пользователь с таким E-mail уже существует!', type : 'error'})
              else {
                this.$emit('form_submit', {text : 'Регистрация прошла успешно!', type : 'success'});
                this.change_form()
              }
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
        }
    }
</script>

<style scoped>

</style>
