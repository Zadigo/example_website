<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12 col-md-8 offset-md-2">

        <v-card class="text-center">
          <v-card-text>
            <v-btn @click="allTodos" color="primary">
              Get all
            </v-btn>
          </v-card-text>
        </v-card>

        <v-toolbar class="my-4" color="orange accent-1">
          <v-toolbar-title class="text-h6 mr-6 hidden-sm-and-down">
            List of todos
          </v-toolbar-title>
          
          <v-text-field v-model="search" placeholder="Search" class="m-0" solo></v-text-field>              
        </v-toolbar>

        <v-expansion-panels class="my-4">
          <v-expansion-panel v-for="todo in searchedTodos" :key="todo.id">
            <v-expansion-panel-header>
              {{ todo.title }}
            </v-expansion-panel-header>
            
            <v-expansion-panel-content>
              <v-checkbox v-model="todo.completed" label="Completed"></v-checkbox> 
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>

      </div>
    </div>
  </div>
</template>

<script>
var _ = require('lodash')

export default {
  name: 'TestPage',
  data() {
    return {
      todos: [],
      search: null
    }
  },
  computed: {
    searchedTodos() {
      if (this.search == null | this.search === '') {
        return this.todos
      } else {
        return _.filter(this.todos, (todo) => {
          return todo.title.includes(this.search)
        })
      }
    }
  },
  methods: {
    allTodos() {
      this.$api.todos.getTodos()
      .then((response) => {
        this.todos = response.data
      })
      .catch((error) => {
        console.error(error)
      })
    }
  }
}
</script>
