<template>
    <div>
      <header class="breadcrumb">
        <div class="container-fluid">
          <div class="row">
            <div class="col" style="text-align: left; font-style: italic">{{ username }}</div>
            <div id="signout" class="col" v-on:click="logout()">
              Выход
            </div>
          </div>
        </div>
      </header>

      <div v-if="show_add_row_window" id="add_new_row_window" class="card" style="width: 23rem;">
        <div class="card-body">
          <h5 class="card-title">{{ form_header }}</h5>
          <h6 class="card-subtitle mb-2 text-muted">Заполните следующие поля:</h6>
          <table>
            <tr>
              <td>Дата:</td>
              <td><input type="date" v-model="form_event_date" /></td>
            </tr>
            <tr>
              <td>Тип:</td>
              <td><input type="text" v-model="form_event_type" /></td>
            </tr>
            <tr>
              <td>Описание:</td>
              <td><input type="text" v-model="form_event_description" /></td>
            </tr>
            <tr><td><br></td></tr>
            <tr style="margin-top: 25px">
              <td><button type="button" class="btn btn-secondary btn-sm" v-on:click="hide_add_row_window()">Отмена</button></td>
              <td><button type="button" class="btn btn-success btn-sm" v-bind:disabled="is_valid" v-on:click="form_submit($event, form_handler_function)">Сохранить</button></td>
            </tr>
          </table>
        </div>
      </div>

      <div class="table-container">
        <table id="event-table" class="table table-bordered">
          <thead>
            <tr>
              <th scope="col">№</th>
              <th scope="col">Дата</th>
              <th scope="col">Тип</th>
              <th scope="col">Описание</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(event, index) in events">
              <td>
                <sup><span v-on:click="delete_event($event, event.id)" id="delete-button" class="badge badge-danger">удалить</span></sup>
                {{index + 1}}
                <sub><span v-on:click="update_event($event, event)"  id="update-button" class="badge badge-warning">ред.</span></sub>
              </td>
              <td>{{ event.event_date }}</td>
              <td>{{ event.event_type }}</td>
              <td>{{ event.event_description }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="container-fluid">
        <div class="row row justify-content-md-center">
          <div class="col-md-auto"><button type="button" class="btn btn-success" v-on:click="add_new_event">+</button></div>
        </div>
      </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Interface",
        data() {
          return {
            username : "",
            events : [],
            show_add_row_window : false,

            form_event_date : "",
            form_event_type : "",
            form_event_description : "",
            form_header : "",
            form_handler_function : null,

            update_event_id : null,
          };
        },
        methods: {
          form_submit(event, form_handler_function) {
            form_handler_function()
          },

          hide_add_row_window() {
            this.show_add_row_window = false
          },
          add_new_event() {
            this.form_header = "Новое событие";
            this.form_handler_function = this.create_new_event;
            this.show_add_row_window = true;

            /* Resetting the input fields */
            this.form_event_date = "";
            this.form_event_type = "";
            this.form_event_description = "";
          },

          update_event(event, event_data) {
            this.form_header = 'Редактировать событие `' + event_data.event_type + '`';
            this.form_handler_function = this.update_existed_event;
            this.update_event_id = event_data.id;

            /* Filling the inputs by existed data */
            this.form_event_date = event_data.event_date;
            this.form_event_type = event_data.event_type;
            this.form_event_description = event_data.event_description;

            this.show_add_row_window = true;
          },

          update_existed_event() {
            const endpoint = "http://127.0.0.1:8000/api/events/update/";
            const csrftoken = document.cookie.split('csrftoken=')[1];
            if (csrftoken === "") {
              console.log("CSRF-token is empty");
              return 0;
            }

            axios({
              url : endpoint,
              method : 'put',
              headers : { 'Content-Type' : 'application/json',
                          'X-CSRFToken'  : csrftoken },
              withCredentials : true,
              data : JSON.stringify({
                'event_id' : this.update_event_id,
                'event_type' : this.form_event_type,
                'event_date' : this.form_event_date,
                'event_description' : this.form_event_description
              }),
            }).then((response) => {
              if (response.data.error) {
                console.log(response.data.error);
                return;
              }
              this.get_user_events();
            }, (error) => {
              console.log(error);
            })
          },

          delete_event(event, id) {
            const endpoint = "http://127.0.0.1:8000/api/events/delete/";
            const csrftoken = document.cookie.split('csrftoken=')[1];
            if (csrftoken === "") {
              console.log("CSRF-token is empty");
              return 0;
            }
            axios({
              url : endpoint,
              method : 'delete',
              headers : { 'Content-Type' : 'application/json',
                          'X-CSRFToken'  : csrftoken },
              data : JSON.stringify({
                'id' : id
              }),
              withCredentials : true
            }).then((response) => {
              if (response.data.error) {
                console.log(response.data.error);
                return;
              }
              this.get_user_events();
            }, (error) => {
              console.log(error)
            })
          },

          create_new_event() {
            const endpoint = "http://127.0.0.1:8000/api/events/new/";
            const csrftoken = document.cookie.split('csrftoken=')[1];
            if (csrftoken === "") {
              console.log("CSRF-token is empty");
              return 0;
            }
            axios({
              url : endpoint,
              method : 'post',
              withCredentials : true,
              headers : { 'Content-Type' : 'application/json',
                          'X-CSRFToken'  : csrftoken },
              data : JSON.stringify({
                'event_date' : this.form_event_date,
                'event_type' : this.form_event_type,
                'event_description' : this.form_event_description
              })
            }).then((response) => {
              this.get_user_events();

              this.form_event_date = '';
              this.form_event_type = '';
              this.form_event_description = '';
            })
            this.show_add_row_window = false;
          },

          get_user_events() {
            const endpoint = "http://127.0.0.1:8000/api/events/all";
            axios({
              url : endpoint,
              method : 'get',
              withCredentials : true
            }).then((response) => {
              if (response.data.error) console.log(response.data.error);
              else {
                console.log(response.data.events)
                this.events = response.data.events;
              }
            })
          },
          get_username() {
            const endpoint = "http://127.0.0.1:8000/api/login/credentials";
              axios({
                url : endpoint,
                method : 'get',
                withCredentials : true
              }).then((response) => {
                if (response.data.username) this.username = response.data.username;
                else this.username = '<error>';
              }, (error) => {
                console.log(error)
              })
          },
          logout() {
            const endpoint = "http://127.0.0.1:8000/api/logout/";
            axios({
              url : endpoint,
              method : 'get',
              withCredentials : true
            }).then((response) => {
              this.$emit('logged_out', {is_logged_out : 1 })
            }, (error) => {
                console.log(error)
            })
          }
      },
      computed: {
          is_valid: function () {
            return !(this.form_event_date !== "" && this.form_event_type !== "" && this.form_event_description !== "");
          }
      },
      mounted() {
          this.get_username();
          this.get_user_events()
      }
    }
</script>

<style scoped>
  .breadcrumb {
    border-radius: 0;
    background-color: #5bb0ca;
    margin-bottom: 10px;
    height: 50px;
  }

  #signout {
    text-align: right;
    cursor: pointer
  }

  #signout:hover {
    color: red;
  }

  .table tbody th, tr {
    text-align: center;
  }

  .input-form {
    text-align: center;
    width: 160px;
    border-radius: 5px;
  }

  .table-container {
    max-height: 800px;
    min-height: 300px;
    overflow: auto;
  }

  #add_new_row_window {
    position: absolute;
    top: 25%;
    left: 43%;
    z-index: 9;
  }

  #delete-button:hover, #update-button:hover {
    cursor: pointer;
    box-shadow: 5px 2px 5px rgba(0, 0, 0, 0.5);
  }
</style>
