<template>
    <div id="app">
        <NavigationPanel @Shows="show"/>
        <Login @login_goto="login_goto" v-show=show_login :ip=ip />
<!--        <Registration></Registration>-->
        <UserConfig v-show=show_userConfig />
        <Registration @to_login="to_login" v-show=show_registration :ip=ip />
        <Settings v-show="show_settings"/>
        <Tasks v-show="show_tasks" @Tasks="Tasks" @updateTasks="f_update_tasks" :tasks="tasks" :ip=ip />
        <AddTask ref="AddTask" @Close_Add_Task="Close_Add_Task" class="modal" v-show="show_add_task" @close="showModal = false" :ip=ip ></AddTask>

        <button @click="local_storage('get', 'token')"></button>
    </div>

</template>

<script>

import NavigationPanel from "@/components/NavigationPanel";
import Login from "@/components/Login";
import Registration from "@/components/Registration";
import UserConfig from "@/components/UserConfig";
import Settings from "@/components/Settings";
import Tasks from "@/components/Tasks";
import AddTask from "@/components/AddTask";
import axios from "axios";

export default {
  name: 'App',
  data() {
    return {
        title: "Hello!",
        ip: "192.168.1.106:5000",
        token: "",
        tasks: [],
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
          let tk = this.local_storage("get", "token")
          if ( tk === undefined || tk === null){
              this.show_login = data.show_userConfig
              this.show_userConfig = false
          }
          else {
              console.log(this.local_storage("get", "token"))


              this.show_userConfig = data.show_userConfig
              this.show_login = false
          }

          this.show_tasks = data.show_tasks
          if (this.show_tasks === true){
            this.get_tasks();
          }

          this.show_add_task = data.show_add_task

          if(this.show_add_task == true) {
              this.$refs.AddTask.get_groups()
          }

          this.show_settings = data.show_settings
          this.show_registration = false
      },
      Close_Add_Task(){
          this.show_add_task = false;
          this.get_tasks()
      },
      login_goto(data){
          if (data.go === "tasks"){
              this.show_login = false
              this.get_tasks()
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
      local_storage(mode, key, value = ''){
          if (mode === 'set') {
              if (key == "token") { this.token = value }

              console.log("Set:" , key, "|", value)
              localStorage.setItem(key, value)
          }
          else {
              return localStorage.getItem(key)
          }
      },
      Tasks(data){
              if (data.add_tasks === true) { this.show_add_task = true}
      },
      f_update_tasks(){
          this.get_tasks()
      },
      get_tasks(){
          console.log("get_tasks")
          let token = this.local_storage('get','token')
          if (token === null){
              alert("Вы не авторизованы!")
          }

          axios
              .post("http://" + this.ip + "/gettasks", {
                  "token": token,
              })
              .then((response) => {
                  if (response.data instanceof  Array) {
                      this.tasks = response.data;
                  } else {
                      console.log("ERROR DATA");
                  }
              })
              .catch((error) => {
                  console.log(error);
              });
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
