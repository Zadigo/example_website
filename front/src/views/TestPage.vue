<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12 col-md-8 offset-md-2">

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
    
      <div class="col-12 text-center">
        <v-btn @click="getPrevious" class="mr-2">Previous</v-btn>
        <v-btn @click="getNext">Next</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
var _ = require('lodash')
import { parsePaginationUrl } from '../utils'

export default {
  name: 'TestPage',
  data() {
    return {
      todos: [],
      search: null,
      nextDetails: {},
      previousDetails: {}
    }
  },
  beforeMount() {
    this._getAll()
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
    _getAll(limit, offset) {
      this.$api.todos.getTodos(limit, offset)
      .then((response) => {
        this.todos = response.data['results']
        this.nextDetails = parsePaginationUrl(response.data.next)
        this.previousDetails = parsePaginationUrl(response.data.previous)
      })
      .catch((error) => {
        console.error(error)
      })
    },
    getNext() {
      this._getAll(this.nextDetails.limit, this.nextDetails.offset)
    },
    getPrevious() {
      this._getAll(this.previousDetails.limit, this.previousDetails.offset)
    }
  }
}
</script>
