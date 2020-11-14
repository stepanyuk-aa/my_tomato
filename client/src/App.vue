<template>
    <div id="app">
        <NavigationPanel @Shows="show"/>
        <Login @login_goto="login_goto" v-show=show_login />
<!--        <Registration></Registration>-->
        <UserConfig v-show=show_userConfig />
        <Registration @to_login="to_login" v-show=show_registration />
        <Settings v-show="show_settings"/>
        <Tasks v-show="show_tasks" @Tasks="Tasks" />
        <AddTask @Close_Add_Task="Close_Add_Task" class="modal" v-show="show_add_task" @close="showModal = false" ></AddTask>

        <button @click="local_storage('get', 'token')"></button>
    </div>

</template>

<script>

import axios from 'axios'

import NavigationPanel from "@/components/NavigationPanel";
import Login from "@/components/Login";
import Registration from "@/components/Registration";
import UserConfig from "@/components/UserConfig";
import Settings from "@/components/Settings";
import Tasks from "@/components/Tasks";
import AddTask from "@/components/AddTask";

export default {
  name: 'App',
  data() {
    return {
        title: "Hello!",
        show_userConfig: false,
        show_tasks: false,
        show_add_task: false,
        show_settings: false,
        show_login: true,
        show_registration: false,
    }
  },
    components: {
        NavigationPanel,
        Login,
        Registration,
        UserConfig,
        Settings,
        Tasks,
        AddTask,
  },
  methods: {
      show (data) {
          this.show_userConfig = data.show_userConfig
          this.show_tasks = data.show_tasks
          this.show_add_task = data.show_add_task
          this.show_settings = data.show_settings
          this.show_login = false
          this.show_registration = false
      },
      Close_Add_Task(){
          this.show_add_task = false;
      },
      login_goto(data){
          if (data.go === "tasks"){
              this.show_login = false
              this.show_tasks = true
          }
          else {
              this.show_login = false
              this.show_registration = true
          }
      },
      to_login(){
          this.show_login = true
          this.show_registration = false
      },
      server_get(data){
          console.log(data)
          axios
              .post("http://192.168.1.108:5000/registration", {'login':'admin', 'password':"test"})
              .then((response) => {
                  if(response.data.status === "success"){
                      this.local_storage('set', 'token', response.data.token)
                      console.log(response.data);
                  }
                  else {
                      console.log(response.data);
                  }
              })
              .catch((error) => {
                  console.log(error);
              });
      },
      local_storage(mode, key, value = ''){
          if (mode === 'set') {
              console.log("Set:" , key, "|", value)
              localStorage.setItem(key, value)
          }
          else {
              console.log(
                  localStorage.getItem(key)
              )
          }
      },
      Tasks(data){
              if (data.add_tasks === true) { this.show_add_task = true}
      },
  },
}


</script>

<style>

#app {
    background: #84909F;
    width: 100%;
    display: flex;
    align-items: stretch;
    flex-direction: row;
    position: absolute;
    left:0;
    right:0;
    top:0;
    bottom:0;
}

.modal {
    position: fixed;
    top: 25%;
    left: 25%;

    padding: 2%;
    border-radius: 10px;
    background-color: #B09F83;
    box-shadow: 0 0 17px 0 gray;

    width: 50%;
    height: 50%;
}
</style>
