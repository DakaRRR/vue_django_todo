<template>

    <table class="table">
      <thead>
        <th>Что нужно сделать?</th>
        <th>Сделано</th>
      </thead>
      <tbody>
          <tr v-for="todo in todos" :key="todo.id" @dblclick="$data.todo=todo">
            <td>{{ todo.title }}</td>
            <td>{{ todo.is_done }}</td>
            <td>
              <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteTodo(todo)">x</button>
            </td>
          </tr>
      </tbody>
    </table>
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" v-model="todo.title">
        <button class="btn btn-success">Создать</button>
      </div>
    </form>
</template>
<script>
  export default {

    data(){
      return {
        todo: {},
        todos: []
      }
    },

    async created() {
      await this.getTodos();
    },
    methods: {

      submitForm(){
        if (this.todo.id === undefined){
          this.createTodo();
        } else {
          this.editTodo();
        }
      },
      async getTodos(){
        var response = await fetch('http://127.0.0.1:8000/api/todos/')
        this.todos = await response.json();
      },
      async createTodo(){
        await this.getTodos()

        await fetch('http://127.0.0.1:8000/api/todos/',{
          method:'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.todo)
        });

        await this.getTodos()
      },
      async editTodo(){
        await this.getTodos()

        await fetch(`http://127.0.0.1:8000/api/todos/${this.todo.id}/`,{
          method:'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.todo)
        });

        await this.getTodos()
        this.todo = {}
      },
      async deleteTodo(todo){
        await this.getTodos()

        await fetch(`http://127.0.0.1:8000/api/todos/${todo.id}/`,{
          method:'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.todo)
        });

        await this.getTodos()
      }
    }
  };
</script>