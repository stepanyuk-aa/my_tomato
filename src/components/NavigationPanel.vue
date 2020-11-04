<template>
    <div class="sidebar">
        <div @click='fun_userConfig' class="user_conf icon">.</div>
        <div @click='fun_tasks' class="tasks icon"></div>
        <div @click='fun_add_task' class="add_task icon"></div>
        <div @click='fun_settings' class="settings icon"></div>
    </div>
</template>

<script>
export default {
    name: "NavigationPanel",
    data() {
        return {
            title: "Hello!",
            show_userConfig: false,
            show_tasks: false,
            show_add_task: false,
            show_settings: false,
        }
    },
    methods: {
        fun_userConfig() {
            this.show_userConfig = !this.show_userConfig
            if(this.show_userConfig){
                this.show_tasks = false
                this.show_add_task = false
                this.show_settings =false
            }

            this.send()
        },
        fun_tasks() {
            this.show_tasks = !this.show_tasks
            if(this.show_tasks){
                this.show_userConfig = false
                this.show_add_task = false
                this.show_settings =false
            }

            this.send()
        },
        fun_add_task(){
            this.show_add_task = !this.show_add_task

            this.send()
        },
        fun_settings(){
            this.show_settings = !this.show_settings
            if(this.show_settings){
                this.show_tasks = false
                this.show_add_task = false
                this.show_userConfig =false
            }

            this.send()
        },
        send() {
            this.$emit('Shows', {
                show_userConfig: this.show_userConfig,
                show_tasks: this.show_tasks,
                show_add_task: this.show_add_task,
                show_settings: this.show_settings,
            })
        }
    }
}
</script>

<style scoped>
    .sidebar {
        background: #7A8A9F;
        width: 5%;
        display: flex;
        flex-wrap: wrap;
        align-content: space-around;
        justify-content: center;
        /*border: */
        border-right: black solid 2px;
    }

    .icon {
        margin: 10%;
        width: 80%;
        height: 10%;
    }
    .user_conf {
        background: url('../img/user_logo.svg') no-repeat ;
    }
    .tasks {
        background: url('../img/tasks.svg') no-repeat ;
    }
    .settings {
        background: url('../img/settings.svg') no-repeat ;
    }
    .add_task {
        background: url('../img/add_task.svg') no-repeat ;
    }
</style>