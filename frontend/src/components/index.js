import Vue from 'vue'

// Components

// Importing Core layout component
import Drawer from './core/Drawer'
import View from './core/View'

// Importing Custom Components
import NoteDetails from './material/NoteDetails'
import ComposeNote from './material/ComposeNote'
import DeleteNoteButton from './material/deleteNoteButton'

// Registered  core Components
Vue.component('core-drawer', Drawer)
Vue.component('core-view', View)

// Registered Components
Vue.component('single-mail-details', NoteDetails)
Vue.component('compose-note', ComposeNote)
Vue.component('delete-note-button', DeleteNoteButton)

export {

  // core part
  Drawer,
  View,

  // others
  NoteDetails,
  ComposeNote,
  DeleteNoteButton
}
