<template>
  <div class="home">
    <h1 class="title">Task App</h1>
    <hr>
    <!-- Column #1 -->
    <div class="columns">
      <!-- Sub Column  #1 -->
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="createTodo">
          <h2 class="subtitle">Add Task</h2>
          <!-- Field #1 -->
          <div class="field">
            <label class="label">Что хотите сделать?</label>
            <div class="control">
              <input type="text" class="input" v-model="title">
            </div>
          </div>
          <!-- Field #2 -->
          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="todo">To Do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>
          <!-- Field #3 -->
          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
    <!-- Column #2 -->
    <div class="columns">
      <!-- Sub Column #1 -->
      <div class="column is-6">
        <h2 class="subtitle">To Do</h2>
        <div class="todo">
          <div class="card" v-for="todo in todos"  v-bind:key="todo.id" >
            {% if todo.status == 'todo' %}
            <div class="card-content">{{ todo.title }}</div>
            <footer class="card-footer">
              <a class="card-footer-item" v-on:click="setStatus(todo.id, 'done')">Done</a>
            </footer>
            {% endif %}
          </div>
        </div>
      </div>
      <!-- Sub Column #2 -->
      <div class="column is-6">
        <h2 class="subtitle">Done</h2>
        <div class="done">
          <div class="card" v-for="todo in todos" v-bind:key="todo.id" >
            {% if todo.status == 'done' %}
            <div class="card-content">{{ todo.title }}</div>
            <footer class="card-content">
              <a class="card-footer-item" v-on:click="setStatus(todo.id, 'todo')" >To do</a>
            </footer>
            {% endif %}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {

  data () {
    return {
      todos: [],
      title: '',
      status: 'todo'
    }
  },
  mounted () {
    this.getTodos()
  },
  methods: {
    // GET
    getTodos() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/todos/',

      }).then(response => this.todos = response.data)
    },
    // POST
    createTodo() {
      if (this.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/todos',
          data: {
            title: this.title,
            status: this.status,
          },

        })
        .then(response => {
          let newTodo = {
            'id': response.data.id,
            'title': this.title,
            'status': this.status
          }
          this.todos.push(newTodo),
          this.title = '',
          this.status = 'todo'
        })
        .catch(error => {
          console.log(error);
        })
      }
    },
    // PUT
    setStatus(todo_id, status) {
      const todo = this.todos.filter(todo => todo.id === todo_id)[0]
      const title = todo.title
      axios({
        method: 'put',
        url: 'http://127.0.0.1:8000/api/todos/' + todo_id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          title: title,
          status: status,
        },

      })
      .then(() => {
        todo.status = status
      })
    }
  }
}
</script>
<style lang="scss">
.select, select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  opacity: 0.3;
}
</style>