<template>
<div class="singl_task" @click="send">
    <div class="bt_singl_task bt_check"></div>
    <input class="in_singl_task" type="text" v-model="task[1]">
    <select class="sel_singl_task">
    </select>
    <button class="bt_singl_task">{{task[4]}}</button>
</div>
</template>

<script>
export default {
    name: "SingleTask",
    props: ['task'],
    methods: {
        send() {
            this.$emit('choose_task', {
                id: this.task[0],
                task: this.task[1],
                des: this.task[2],
                interval: this.task[3],
                count: this.task[4],
                timer: this.task[5]
            })
        }
    },

}
</script>

<style scoped>
    .singl_task {
        border: black dashed 2px;
        border-radius: 10px;

        display: flex;
        justify-content: space-around;
        align-items: center;

        margin: 1%;
        height: 5%;
    }

    .bt_singl_task {
        border-radius: 50%;
        width: 10%;
        height: 30px;

    }

    .bt_check {
        width: 5%;
        height: 25px;
        background: url('../img/check_mark.svg') no-repeat;
    }

    .in_singl_task {
        width: 50%;
        height: 20px;
        min-height: 5%;
        text-align: center;
    }

    .sel_singl_task {
        width: 20%;
        height: 25px;
        padding-left: 3%;
    }
</style>