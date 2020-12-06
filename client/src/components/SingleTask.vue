<template>
<div class="singl_task">
    <div class="bt_singl_task bt_check" @click="f_finish"></div>
    <input class="in_singl_task" type="text" v-model="task[1]">
    <button class="bt_singl_task" @click="send">{{task[4]}}</button>
    <div class="bt_singl_task bt_del" @click="f_delete"></div>
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
        },
        f_finish(){
            if (confirm("Вы уверены?")) {
                this.$emit('chage_status', {
                    id: this.task[0],
                    status: "1"
                })
            }
        },
        f_delete(){
            if (confirm("Вы уверены?")){
                this.$emit('chage_status', {
                    id: this.task[0],
                    status: "2"
                })
            }
        },
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

    .bt_del {
        width: 5%;
        height: 25px;
        background: url('../img/trash.svg') no-repeat;
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