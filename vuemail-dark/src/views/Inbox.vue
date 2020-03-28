<template>
  <div class="inbox">
    <v-container grid-list-md>

      <v-layout row wrap>
        <v-flex lg12 md12 sm12 xs12>
          <compose-note />
        </v-flex>
      </v-layout>

      <v-layout row wrap>

        <v-flex lg4 md6 sm12 xs12>
          <div class="card-left-side card-left-side-ui-design">

            <div v-on:click="activate(i, item.noteId)"
              v-bind:class="{active: item.noteId == selected}" class="card-index" v-for="(item,i) in notes" :key="i">
              <div class="card-info">
                <div class="card-head">
                  <h3><a>{{item.author}}</a></h3>
                  <div class="card-date">{{new Date(item.createdAt) | moment("MMM Do h:mmA") }}</div>
                </div>
                <a>{{item.country}}</a>
                <div class="card-para">
                  {{item.content}}
                </div>
              </div>
            </div>

          </div>

        </v-flex>

        <v-flex v-if="!isLoading" lg8 md6 sm12 xs12>
          <div class="card-right-side card-left-side-ui-design">
            <single-mail-details :noteDetailsData="notes[note]" />
          </div>
        </v-flex>

      </v-layout>
    </v-container>
  </div>


</template>

<script>
  import EventBus from './../eventBus.js'
  import RepositoryFactory from './../repositories'
  const NotesRepository = RepositoryFactory.get('notes')

  export default {
    name: 'inbox',
    data() {
      return {
        selected: undefined,
        note : '0',
        notes: [],
        isLoading: false
      }
    },
    created() {
      this.fetchNotes()
    },
    mounted() {
      var vm = this
      EventBus.$on('note-added', function (note) {
        vm.insertNote(note.data);
      })
    },
    methods: {
      insertNote(note) {
        this.notes.unshift(note);
        this.activate(0, note.noteId)
      },
      activate(index, elementId) {
        this.selected = elementId
        this.note = index
      },
      async fetchNotes() {
        this.isLoading = true;
        let response = await NotesRepository.get();
        this.notes = response.data.reverse();
        this.isLoading = false;
      }
    }
  }
</script>
