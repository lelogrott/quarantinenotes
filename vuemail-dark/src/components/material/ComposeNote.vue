<template>
  <div  class="compose-note">
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-container grid-list-md pb-2>

        <v-layout row wrap>
          <v-flex lg4 md6 sm12 xs12>
            <v-text-field
              v-model="note.author"
              :counter="20"
              :rules="nameRules"
              label="Name"
              dark
            ></v-text-field>
          </v-flex>
          <v-flex lg4 md6 sm12 xs12>
            <v-select
              v-model="note.country"
              item-text="friendly_name"
              item-value="id"
              :items="countries"
              label="Country"
              dark
            ></v-select>
          </v-flex>
        </v-layout>

        <v-layout row wrap>
          <v-flex lg12 md12 sm12 xs12>
            <div class="comment">
              <v-textarea
                v-model="note.content"
                :rules="noteRules"
                required
                id="mail-comment"
                :placeholder="options.placeholder"
              ></v-textarea>
              <button
                :disabled="!valid"
                @click="handleSubmit"
                class="scroll-top" type="submit">
                <i class="flaticon-sent-mail"></i>
              </button>
            </div>
          </v-flex>
        </v-layout>
      </v-container>
      <br>
    </v-form>
  </div>
</template>

<script>
  import EventBus from './../../eventBus.js'
  import RepositoryFactory from './../../repositories'
  const NotesRepository = RepositoryFactory.get('notes')

  export default {
    data () {
      return {
        note: {
          author: '',
          country: '',
          content: ''
        },
        valid: true,
        nameRules: [
          v => (v.length <= 20) || 'Name must be less than 20 characters'
        ],
        noteRules: [
          v => (v.length > 0) || "Ain't you gonna write something?"
        ],
        countries: this.$store.state.countriesData.countriesInfo
      }
    },
    props: {
      options: {
        type: Object,
        default: () => {
          return {
            placeholder: "How's the quarantine so far?",
            noteId: undefined
          }
        }
      },
      messageType: {
        type: String,
        default: () => { return "Note" }
      }
    },
    methods: {
      isReply() {
        return this.messageType === "NoteReply";
      },
      async handleSubmit() {
        if (this.$refs.form.validate()) {
          if (this.isReply()) {
            var response = await NotesRepository.addNoteReply(this.options.noteId, this.note);
            EventBus.$emit('reply-added', response);
          } else {
            var response = await NotesRepository.createNote(this.note);
            EventBus.$emit('note-added', response)
          }
        }
      }
    }
  }
</script>
