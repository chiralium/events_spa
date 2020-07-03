<template>
    <div>
      <header class="breadcrumb">
        <div class="container-fluid">
          <div class="row">
            <div class="col" style="text-align: left; font-style: italic">{{ username }}</div>
            <div id="signout" class="col" v-on:click="logout()">
              Sign Out
            </div>
          </div>
        </div>
      </header>
      <div class="table-container">
        <table class="table table-bordered">
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
              <th scope="row">
                {{ index + 1 }}
                <span v-if="event.__added__" class="badge badge-pill badge-danger">new</span>
              </th>
              <td><input class="input-form" type="date" v-bind:value="event.event_date" /></td>
              <td><input class="input-form" type="text" v-bind:value="event.event_type" /> </td>
              <td><textarea class="input-form" type="text" v-bind:value="event.event_description" /></td>
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
            events : []
          };
        },
        methods: {
          add_new_event() {
            this.events.push({id : "", event_date : "", event_type : "", event_description : "", __added__ : 1})
          },
          get_user_events() {
            const endpoint = "http://127.0.0.1:8000/api/events/all";
            axios({
              url : endpoint,
              method : 'get',
              withCredentials : true
            }).then((response) => {
              if (response.data.error) console.log(response.data.error);
              else this.events = response.data.events;
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

  .table tbody th:hover, tr:hover {
    background: #a7e8a7;
    cursor: pointer;
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
</style>
