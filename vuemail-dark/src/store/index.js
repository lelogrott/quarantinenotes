import Vue from 'vue'
import Vuex from 'vuex'

// all modules import
import TablesModule from './modules/tables'
import NoteDataModule from './modules/notesdata'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    tables: TablesModule,
    notesData: NoteDataModule
  },
  state: {
    //
  },
  mutations: {
    //
  },
  actions: {
    //
  }
})

export default store
