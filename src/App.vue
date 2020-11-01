<template>
    <div id="app">
        <NavigationPanel @Shows="show"/>
        <Login v-show=show_login />
<!--        <Registration></Registration>-->
        <UserConfig v-show=show_userConfig />

  </div>
</template>

<script>
import NavigationPanel from "@/components/NavigationPanel";
import Login from "@/components/Login";
// import Registration from "@/components/Registration";
import UserConfig from "@/components/UserConfig";

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
    }
  },
    components: {
        NavigationPanel,
        Login,
    //     Registration,
        UserConfig,
  },
  methods: {
      show (data) {
          this.show_userConfig = data.show_userConfig
          this.show_tasks = data.show_tasks
          this.show_add_task = data.show_add_task
          this.show_settings = data.show_settings
          this.show_login = false
      }
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

.WorkSpace {
  padding: 1px 16px;
}
</style>
