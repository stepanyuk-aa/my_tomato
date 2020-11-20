<template>
    <div class="root_select">
        <select
            v-model="select_group" class="input_new_group"
            v-on:input="$emit('input', $event.target.value)"
        >
            <option
                v-for="group in groups"
                v-bind:key="group"
            >{{group}}</option>
        </select>
    </div>
</template>

<script>
export default {
    name: "SelectGroup",
    props: ['value', 'groups'],
    data() {
        return {
            select_group: '',
        }
    },
    components: {
    },
    methods: {
    },
}
</script>
import axios from "axios";

<style scoped>
    .root_select {
        width: 35%;
        height: 65%;
    }
    .input_new_group {
        text-align: center;
        width: 100%;
        height: 100%;
        margin-left: 10%;
        border-radius: 10px;
    }
</style>