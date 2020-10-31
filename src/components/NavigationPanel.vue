<template>
    <div class="sidebar">
        <div class="user_conf icon">.</div>

        <div class="tasks icon"></div>
        <div class="add_task icon"></div>
        <div class="settings icon"></div>
    </div>
</template>

<script>
export default {
    name: "NavigationPanel"
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