import Vue from 'vue'
import Vuex from 'vuex'

// all modules import
import TablesModule from './modules/tables'
import NoteDataModule from './modules/notesdata'
import CountryDataModule from './modules/countries'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    tables: TablesModule,
    notesData: NoteDataModule,
    countriesData: CountryDataModule
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
