<template>
  <div  class="delete-note-button">
    <v-layout row wrap justify="center">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on }">
          <v-btn color="red" dark v-on="on">Delete</v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">Delete Note</span>
          </v-card-title>
          <v-card-text>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-container>
                <v-layout row wrap>
                  <v-flex lg12 md12 sm12 xs12>
                    <v-text-field
                      v-model="password"
                      :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                      @click:append="show = !show"
                      :type="show ? 'text' : 'password'"
                      :rules="passwordRules"
                      required
                    ></v-text-field>
                  </v-flex>
                </v-layout row wrap>
              </v-container>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
            <v-btn color="blue darken-1" text @click="handleSubmit">Delete</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout row wrap>
  </div>
</template>

<script>
  import EventBus from './../../eventBus.js'
  import RepositoryFactory from './../../repositories'
  const NotesRepository = RepositoryFactory.get('notes')

  export default {
    props: {
      noteId: undefined
    },
    data () {
      return {
        valid: true,
        dialog: false,
        show: false,
        password: '',
        passwordRules: [
          v => (!!v) || 'Required.'
        ],
      }
    },
    methods: {
      async handleSubmit() {
        if (this.$refs.form.validate()) {
          var response = await NotesRepository.deleteNote(this.noteId, this.password);
          EventBus.$emit('note-deleted', response);
          this.dialog = false;
        }
      }
    }
  }
</script>
