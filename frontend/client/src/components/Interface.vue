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
          <tr v-for="event in events" :key = "event">
            <th scope="row">{{ event.id }}</th>
            <td>{{ event.date }}</td>
            <td>{{ event.type }}</td>
            <td>{{ event.description }}</td>
          </tr>
        </tbody>
      </table>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Interface",
        data() {
          return {
            username : "",
            events : [
              {id : 1, date : '12.01.1997', type : 'Звонок', description : 'Позвонить в 911'},
              {id : 2, date : '12.01.1997', type : 'Встреча', description : 'Позвонить в 102'},
              {id : 3, date : '12.01.1997', type : 'Звонок', description : 'Позвонить в 103'},
              {id : 4, date : '12.01.1997', type : 'Встреча', description : 'Позвонить в 112'},
              {id : 5, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 6, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 7, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 8, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 9, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 10, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 11, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 12, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 13, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'},
              {id : 14, date : '12.01.1997', type : 'Конференция', description : 'Позвонить в 104'}
            ]
          };
        },
        methods: {
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
          this.get_username()
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
</style>
